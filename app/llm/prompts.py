# =========================================================
# CLAIM EXTRACTION
# =========================================================

CLAIM_EXTRACTION_PROMPT = """
You are an architecture analysis system.

Analyze the architecture description below.

Extract two things:

1. Architecture claims:
   Statements about whether a technology, design choice, or architecture
   capability is true, suitable, scalable, reliable, performant, etc.

2. Requirements:
   Explicit goals, constraints, workload assumptions, or priorities.

IMPORTANT:
- Do NOT invent technologies that are not mentioned.
- Do NOT create claims from requirements alone.
- "Expect 100,000 concurrent users" is a requirement, not a claim.
- "Prioritize low latency over consistency" is a requirement/trade-off.
- Only include claims that are actually stated or clearly implied by the architecture.
- Do not add explanations.
- Do not use Markdown.
- Return ONLY valid JSON.

Required JSON format:

{{
  "claims": [
    {{
      "claim": "string",
      "category": "string",
      "importance": "High|Medium|Low"
    }}
  ],
  "requirements": [
    {{
      "requirement": "string",
      "category": "string",
      "importance": "High|Medium|Low"
    }}
  ]
}}

Architecture description:

{architecture}
"""


# =========================================================
# SUPPORT QUERY
# =========================================================

SUPPORT_QUERY_PROMPT = """
Generate one concise technical search query that can find evidence supporting this architecture claim.

Claim:
{claim}

Return ONLY valid JSON in exactly this format:

{{
  "query": "your search query"
}}
"""


# =========================================================
# CHALLENGE QUERY
# =========================================================

CHALLENGE_QUERY_PROMPT = """
Generate one concise technical search query that can find evidence challenging or identifying limitations of this architecture claim.

Claim:
{claim}

Return ONLY valid JSON in exactly this format:

{{
  "query": "your search query"
}}
"""


# =========================================================
# EVIDENCE SUFFICIENCY
# =========================================================

EVIDENCE_SUFFICIENCY_PROMPT = """
You are evaluating whether the retrieved evidence is sufficient to assess an
architecture claim.

Claim:
{claim}

Supporting evidence:
{support_evidence}

Challenging evidence:
{challenge_evidence}

Determine whether the evidence is sufficient to make a meaningful assessment
of the claim.

Return ONLY valid JSON.
Do not use Markdown.
Do not include any text before or after the JSON.

Required format:

{{
  "sufficient": true,
  "reasoning": "Brief explanation of why the evidence is or is not sufficient.",
  "missing_aspects": [
    "Specific missing evidence aspect"
  ]
}}

Rules:
- "sufficient" must be either true or false.
- "reasoning" must explain the decision.
- "missing_aspects" must be an array of strings.
- If the evidence is sufficient, return an empty missing_aspects array.
"""


# =========================================================
# QUERY REFINEMENT
# =========================================================

QUERY_REFINEMENT_PROMPT = """
You are a technical search-query generation engine.

Your task is to improve TWO search queries for ONE architecture claim.

Claim:
{claim}

Current support query:
{support_query}

Current challenge query:
{challenge_query}

Missing evidence aspects:
{missing_aspects}

STRICT OUTPUT RULES:

- Return EXACTLY ONE JSON object.
- Return ONLY the JSON object.
- Do NOT explain your answer.
- Do NOT summarize anything.
- Do NOT use Markdown.
- Do NOT use code fences.
- Do NOT number the queries.
- Do NOT include text before or after the JSON.
- Do NOT return a JSON array.

The JSON MUST contain exactly these two fields:

{{
  "support_query": "improved query for finding evidence supporting the claim",
  "challenge_query": "improved query for finding evidence challenging or identifying limitations of the claim"
}}

Rules:
- Queries must be concise technical search queries.
- The queries must directly address the claim.
- Incorporate the missing evidence aspects where relevant.
- Do not introduce unrelated technologies or concepts.
- Do not answer the claim.
- Only generate search queries.

OUTPUT ONLY THE JSON OBJECT.
"""


# =========================================================
# CLAIM ASSESSMENT
# =========================================================

CLAIM_ASSESSMENT_PROMPT = """
You are a JSON-producing architecture evidence analysis engine.

Your task is to assess ONE SINGLE CLAIM.

========================
CLAIM
========================
{claim}

========================
SUPPORTING EVIDENCE
========================
{support_evidence}

========================
CHALLENGING EVIDENCE
========================
{challenge_evidence}

========================
EVIDENCE SUFFICIENCY
========================
{sufficiency}

Missing evidence aspects:
{missing_aspects}

========================
STRICT OUTPUT RULES
========================

You MUST output exactly ONE JSON object.

Your entire response MUST be valid JSON.

DO NOT:
- summarize the evidence
- explain your task
- discuss distributed systems generally
- discuss other claims
- write Markdown
- use ``` code fences
- write text before the JSON
- write text after the JSON
- output multiple JSON objects
- output a JSON array

The JSON object MUST have exactly these fields:

{{
  "claim": "original claim",
  "verdict": "Supported",
  "reasoning": "concise evidence-based reasoning",
  "supporting_evidence_ids": [],
  "challenging_evidence_ids": [],
  "missing_information": []
}}

Allowed verdict values:

"Supported"
"Partially Supported"
"Challenged"
"Insufficient Evidence"

IMPORTANT:
- Assess ONLY the claim given above.
- Use ONLY the supplied evidence.
- Do not use outside knowledge.
- supporting_evidence_ids may contain ONLY chunk IDs appearing in Supporting Evidence.
- challenging_evidence_ids may contain ONLY chunk IDs appearing in Challenging Evidence.
- If evidence does not establish the claim, use "Insufficient Evidence".
- If evidence supports some aspects but not the entire claim, use "Partially Supported".
- missing_information must contain specific information needed to assess the claim further.
- If nothing is missing, use [].

OUTPUT ONLY THE JSON OBJECT.
"""


# =========================================================
# FINAL REPORT
# =========================================================

FINAL_REPORT_PROMPT = """
You are generating the final architecture evidence review.

Architecture:
{architecture}

Requirements:
{requirements}

Claim assessments:
{assessments}

Produce a concise but technically useful report.

Structure:

# Architecture Evidence Review

## Summary

Briefly describe the overall evidence picture.

## Requirements

List the extracted requirements and constraints.

## Claim-by-Claim Analysis

For every claim include:

### Claim
The claim itself.

### Category
The claim category.

### Importance
Its importance.

### Verdict
Supported / Challenged / Mixed / Insufficient Evidence

### Reasoning
Explain what the retrieved evidence establishes and what it does
not establish.

### Supporting Evidence
For each selected source include:
- source
- technology
- document type
- section
- URL if available
- chunk ID

### Challenging Evidence
Use the same metadata format.

### Missing Information
List important unresolved issues.

## Overall Findings

Summarize the major evidence-backed findings, limitations,
assumptions, and unresolved questions.

## Important Questions

List questions that should be answered before treating uncertain
architecture claims as established.

Rules:

- Use ONLY the supplied evidence.
- Never invent a source.
- Never invent a URL.
- Preserve source metadata exactly.
- Do not treat topical similarity as proof.
- Clearly distinguish requirements from externally testable claims.
"""