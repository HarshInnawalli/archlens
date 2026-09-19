def should_refine_evidence(state):
    """
    Decide whether another retrieval/refinement iteration
    is necessary.
    """

    sufficient = state.get(
        "evidence_sufficient",
        False,
    )

    iteration = state.get(
        "refinement_iteration",
        0,
    )

    max_iterations = state.get(
        "max_refinement_iterations",
        2,
    )

    # Evidence is already sufficient.
    if sufficient:
        return "assess_claim"

    # Evidence is insufficient but refinement remains.
    if iteration < max_iterations:
        return "refine_queries"

    # Maximum refinement attempts exhausted.
    return "assess_claim"


def should_process_next_claim(state):
    """
    Decide whether another claim should be processed.
    """

    next_index = state["current_claim_index"]

    if next_index < len(state["claims"]):
        return "process_claim"

    return "final_report"