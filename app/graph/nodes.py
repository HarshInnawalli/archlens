from app.llm.providers import get_llm
from app.llm.prompts import (
    CLAIM_EXTRACTION_PROMPT,
    SUPPORT_QUERY_PROMPT,
    CHALLENGE_QUERY_PROMPT,
    EVIDENCE_SUFFICIENCY_PROMPT,
    QUERY_REFINEMENT_PROMPT,
    CLAIM_ASSESSMENT_PROMPT,
    FINAL_REPORT_PROMPT,
)
from app.llm.structured import (
    ClaimExtractionResult,
    SearchQuery,
    RefinedQueries,
    EvidenceSufficiency,
    ClaimAssessment,
    structured_llm,
    invoke_structured,
)

from app.llm.providers import invoke_with_fallback
from app.retrieval.search import search
from app.retrieval.reranker import rerank


# =========================================================
# Helpers
# =========================================================

def _current_claim(state):
    index = state["current_claim_index"]
    return state["claims"][index]


def _search_and_rerank(query: str, top_k: int = 5):
    """
    Retrieve candidate evidence and rerank it.

    Returns the top_k reranked evidence chunks with
    complete provenance metadata.
    """

    results = search(
        query=query,
        top_k=10,  # retrieve more candidates before reranking
    )

    if not results:
        return []

    reranked = rerank(
        query=query,
        results=results,
        top_k=top_k,
    )

    evidence = []

    for item in reranked:
        evidence.append({
            "text": item.text,
            "score": item.score,
            "rerank_score": item.rerank_score,

            "chunk_id": item.chunk_id,
            "document_id": item.document_id,

            "source": item.source,
            "technology": item.technology,
            "topic": item.topic,
            "document_type": item.document_type,

            "section": item.section,
            "url": item.url,
            "file_path": item.file_path,
        })

    return evidence


def format_evidence(evidence):
    """
    Convert evidence objects into text suitable for LLM prompts.
    """

    if not evidence:
        return "No evidence was retrieved."

    formatted = []

    for i, item in enumerate(evidence, start=1):
        formatted.append(
            f"""
Evidence {i}

Chunk ID: {item.get("chunk_id")}
Document ID: {item.get("document_id")}
Source: {item.get("source")}
Technology: {item.get("technology")}
Topic: {item.get("topic")}
Document type: {item.get("document_type")}
Section: {item.get("section")}
URL: {item.get("url")}

Text:
{item.get("text")}
"""
        )

    return "\n".join(formatted)


def _model_dump_items(items):
    return [
        item.model_dump() if hasattr(item, "model_dump") else item
        for item in items
    ]


# =========================================================
# CLAIM EXTRACTION
# =========================================================

def extract_claims(state):
    llm = get_llm()

    prompt = CLAIM_EXTRACTION_PROMPT.format(
        architecture=state["architecture"]
    )

    result = invoke_structured(
        llm=llm,
        prompt=prompt,
        schema=ClaimExtractionResult,
    )

    claims = [
        item.model_dump()
        for item in result.claims
    ]

    requirements = [
        item.model_dump()
        for item in result.requirements
    ]

    print("\n===== EXTRACTED CLAIMS =====")

    for claim in claims:
        print(claim)

    print("\n===== EXTRACTED REQUIREMENTS =====")

    for requirement in requirements:
        print(requirement)

    return {
        "claims": claims,
        "requirements": requirements,
        "current_claim_index": 0,
        "refinement_iteration": 0,
        "max_refinement_iterations": 2,
        "claim_assessments": [],
    }


# =========================================================
# SUPPORT QUERY
# =========================================================

def generate_support_query(state):
    claim = _current_claim(state)

    llm = get_llm()

    structured = structured_llm(
        llm,
        SearchQuery,
    )

    result = structured.invoke(
        SUPPORT_QUERY_PROMPT.format(
            claim=claim["claim"],
            category=claim["category"],
        )
    )

    print(
        f"\n[Support Query] {result.query}"
    )

    return {
        "support_query": result.query
    }


# =========================================================
# CHALLENGE QUERY
# =========================================================

def generate_challenge_query(state):
    claim = _current_claim(state)

    llm = get_llm()

    structured = structured_llm(
        llm,
        SearchQuery,
    )

    result = structured.invoke(
        CHALLENGE_QUERY_PROMPT.format(
            claim=claim["claim"],
            category=claim["category"],
        )
    )

    print(
        f"[Challenge Query] {result.query}"
    )

    return {
        "challenge_query": result.query
    }


# =========================================================
# SUPPORT RETRIEVAL
# =========================================================

def retrieve_support_evidence(state):
    query = state["support_query"]

    evidence = _search_and_rerank(
        query,
        top_k=8,
    )

    print(
        f"\n[Support Retrieval] "
        f"{len(evidence)} evidence chunks"
    )

    return {
        "support_evidence": evidence
    }


# =========================================================
# CHALLENGE RETRIEVAL
# =========================================================

def retrieve_challenge_evidence(state):
    query = state["challenge_query"]

    evidence = _search_and_rerank(
        query,
        top_k=8,
    )

    print(
        f"[Challenge Retrieval] "
        f"{len(evidence)} evidence chunks"
    )

    return {
        "challenge_evidence": evidence
    }


# =========================================================
# EVIDENCE SUFFICIENCY
# =========================================================

def check_evidence_sufficiency(state):
    claim = _current_claim(state)

    llm = get_llm()

    structured = structured_llm(
        llm,
        EvidenceSufficiency,
    )

    result = structured.invoke(
        EVIDENCE_SUFFICIENCY_PROMPT.format(
            claim=claim["claim"],
            support_evidence=format_evidence(
                state.get("support_evidence", [])
            ),
            challenge_evidence=format_evidence(
                state.get("challenge_evidence", [])
            ),
        )
    )

    print(
        f"\n[Evidence Sufficiency] "
        f"{result.sufficient}"
    )

    print(
        f"[Reasoning] {result.reasoning}"
    )

    if result.missing_aspects:
        print(
            "[Missing Aspects] "
            + "; ".join(result.missing_aspects)
        )

    return {
        "evidence_sufficient": result.sufficient,
        "evidence_sufficiency_reasoning": result.reasoning,
        "missing_evidence_aspects": result.missing_aspects,
    }


# =========================================================
# QUERY REFINEMENT
# =========================================================

def refine_queries(state):
    claim = _current_claim(state)

    iteration = state.get(
        "refinement_iteration",
        0,
    )

    llm = get_llm()

    structured = structured_llm(
        llm,
        RefinedQueries,
    )

    result = structured.invoke(
        QUERY_REFINEMENT_PROMPT.format(
            claim=claim["claim"],
            support_query=state.get(
                "support_query",
                "",
            ),
            challenge_query=state.get(
                "challenge_query",
                "",
            ),
            missing_aspects=", ".join(
                state.get(
                    "missing_evidence_aspects",
                    [],
                )
            ),
        )
    )

    new_iteration = iteration + 1

    print(
        f"\n[Query Refinement] "
        f"Iteration {new_iteration}"
    )

    print(
        f"[Refined Support Query] "
        f"{result.support_query}"
    )

    print(
        f"[Refined Challenge Query] "
        f"{result.challenge_query}"
    )

    return {
        "support_query": result.support_query,
        "challenge_query": result.challenge_query,

        "refinement_iteration": new_iteration,

        # Clear old evidence so the next retrieval is explicit.
        "support_evidence": [],
        "challenge_evidence": [],
    }


# =========================================================
# CLAIM ASSESSMENT
# =========================================================

def assess_claim(state):
    claim = _current_claim(state)

    support_evidence = state.get(
        "support_evidence",
        [],
    )

    challenge_evidence = state.get(
        "challenge_evidence",
        [],
    )

    llm = get_llm()

    structured = structured_llm(
        llm,
        ClaimAssessment,
    )

    result = structured.invoke(
        CLAIM_ASSESSMENT_PROMPT.format(
            claim=claim["claim"],
            support_evidence=format_evidence(
                support_evidence
            ),
            challenge_evidence=format_evidence(
                challenge_evidence
            ),
            sufficiency=state.get(
                "evidence_sufficiency_reasoning",
                "",
            ),
            missing_aspects=", ".join(
                state.get(
                    "missing_evidence_aspects",
                    [],
                )
            ),
        )
    )

    # ---------------------------------------------------------
    # Preserve the complete evidence objects.
    # ---------------------------------------------------------

    supporting_ids = set(
        result.supporting_evidence_ids
    )

    challenging_ids = set(
        result.challenging_evidence_ids
    )

    selected_support = [
        item
        for item in support_evidence
        if item["chunk_id"] in supporting_ids
    ]

    selected_challenge = [
        item
        for item in challenge_evidence
        if item["chunk_id"] in challenging_ids
    ]

    assessment = {
        "claim": result.claim,
        "category": claim.get("category"),
        "importance": claim.get("importance"),

        "verdict": result.verdict,
        "reasoning": result.reasoning,

        "supporting_evidence": selected_support,
        "challenging_evidence": selected_challenge,

        "missing_information": (
            result.missing_information
        ),

        "refinement_iterations": state.get(
            "refinement_iteration",
            0,
        ),

        "evidence_sufficient": state.get(
            "evidence_sufficient",
            False,
        ),

        "evidence_sufficiency_reasoning": state.get(
            "evidence_sufficiency_reasoning",
            "",
        ),

        "missing_evidence_aspects": state.get(
            "missing_evidence_aspects",
            [],
        ),
    }

    print(
        f"\n[Assessment] {result.verdict}"
    )

    print(
        f"[Claim] {result.claim}"
    )

    print(
        f"[Reasoning] {result.reasoning}"
    )

    assessments = list(
        state.get(
            "claim_assessments",
            [],
        )
    )

    assessments.append(assessment)

    return {
        "claim_assessments": assessments
    }


# =========================================================
# NEXT CLAIM
# =========================================================

def move_to_next_claim(state):
    next_index = (
        state["current_claim_index"] + 1
    )

    return {
        "current_claim_index": next_index,

        # Reset per-claim state.
        "support_query": "",
        "challenge_query": "",

        "support_evidence": [],
        "challenge_evidence": [],

        "refinement_iteration": 0,

        "evidence_sufficient": False,
        "evidence_sufficiency_reasoning": "",
        "missing_evidence_aspects": [],
    }


# =========================================================
# FINAL REPORT HELPERS
# =========================================================

def format_requirements(requirements):
    if not requirements:
        return "No explicit requirements were extracted."

    output = []

    for i, requirement in enumerate(
        requirements,
        start=1,
    ):
        output.append(
            f"""
Requirement {i}
Requirement: {requirement.get("requirement")}
Category: {requirement.get("category")}
Importance: {requirement.get("importance")}
"""
        )

    return "\n".join(output)


def format_assessments(assessments):
    if not assessments:
        return "No claim assessments available."

    output = []

    for i, assessment in enumerate(
        assessments,
        start=1,
    ):
        output.append(
            f"""
==================================================
Claim {i}
==================================================

Claim:
{assessment.get("claim")}

Category:
{assessment.get("category")}

Importance:
{assessment.get("importance")}

Verdict:
{assessment.get("verdict")}

Reasoning:
{assessment.get("reasoning")}

Evidence sufficient:
{assessment.get("evidence_sufficient")}

Evidence sufficiency reasoning:
{assessment.get("evidence_sufficiency_reasoning")}

Refinement iterations:
{assessment.get("refinement_iterations")}

Missing evidence aspects:
{assessment.get("missing_evidence_aspects")}

Supporting Evidence:
{format_evidence(
    assessment.get(
        "supporting_evidence",
        [],
    )
)}

Challenging Evidence:
{format_evidence(
    assessment.get(
        "challenging_evidence",
        [],
    )
)}

Missing Information:
{assessment.get("missing_information")}
"""
        )

    return "\n".join(output)


# =========================================================
# FINAL REPORT
# =========================================================

def generate_final_report(state):
    prompt = FINAL_REPORT_PROMPT.format(
        architecture=state["architecture"],

        requirements=format_requirements(
            state.get(
                "requirements",
                [],
            )
        ),

        assessments=format_assessments(
            state.get(
                "claim_assessments",
                [],
            )
        ),
    )

    response = invoke_with_fallback(prompt)

    # ChatOllama / Gemini / ChatOpenAI all normally expose `.content`.
    report = (
        response.content
        if hasattr(response, "content")
        else str(response)
    )

    print("\n===== FINAL REPORT =====")
    print(report)

    return {
        "final_report": report
    }