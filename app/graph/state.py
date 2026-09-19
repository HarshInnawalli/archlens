from typing import TypedDict


class ArchLensState(TypedDict, total=False):
    # ---------------------------------------------------------
    # Input
    # ---------------------------------------------------------
    architecture: str

    # ---------------------------------------------------------
    # Extracted architecture information
    # ---------------------------------------------------------
    claims: list[dict]
    requirements: list[dict]

    # ---------------------------------------------------------
    # Claim processing
    # ---------------------------------------------------------
    current_claim_index: int

    # ---------------------------------------------------------
    # Retrieval queries
    # ---------------------------------------------------------
    support_query: str
    challenge_query: str

    # ---------------------------------------------------------
    # Retrieved evidence
    # ---------------------------------------------------------
    support_evidence: list[dict]
    challenge_evidence: list[dict]

    # ---------------------------------------------------------
    # Evidence refinement
    # ---------------------------------------------------------
    refinement_iteration: int
    max_refinement_iterations: int

    evidence_sufficient: bool
    evidence_sufficiency_reasoning: str
    missing_evidence_aspects: list[str]

    # ---------------------------------------------------------
    # Claim assessments
    # ---------------------------------------------------------
    claim_assessments: list[dict]

    # ---------------------------------------------------------
    # Final output
    # ---------------------------------------------------------
    final_report: str