from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from app.graph.state import ArchLensState

from app.graph.nodes import (
    extract_claims,
    generate_support_query,
    generate_challenge_query,
    retrieve_support_evidence,
    retrieve_challenge_evidence,
    check_evidence_sufficiency,
    refine_queries,
    assess_claim,
    move_to_next_claim,
    generate_final_report,
)

from app.graph.edges import (
    should_refine_evidence,
    should_process_next_claim,
)


def build_graph():

    graph = StateGraph(
        ArchLensState
    )

    # ---------------------------------------------------------
    # Nodes
    # ---------------------------------------------------------

    graph.add_node(
        "extract_claims",
        extract_claims,
    )

    graph.add_node(
        "generate_support_query",
        generate_support_query,
    )

    graph.add_node(
        "generate_challenge_query",
        generate_challenge_query,
    )

    graph.add_node(
        "retrieve_support_evidence",
        retrieve_support_evidence,
    )

    graph.add_node(
        "retrieve_challenge_evidence",
        retrieve_challenge_evidence,
    )

    graph.add_node(
        "check_evidence_sufficiency",
        check_evidence_sufficiency,
    )

    graph.add_node(
        "refine_queries",
        refine_queries,
    )

    graph.add_node(
        "assess_claim",
        assess_claim,
    )

    graph.add_node(
        "move_to_next_claim",
        move_to_next_claim,
    )

    graph.add_node(
        "generate_final_report",
        generate_final_report,
    )

    # ---------------------------------------------------------
    # Initial flow
    # ---------------------------------------------------------

    graph.add_edge(
        START,
        "extract_claims",
    )

    graph.add_edge(
        "extract_claims",
        "generate_support_query",
    )

    graph.add_edge(
        "generate_support_query",
        "generate_challenge_query",
    )

    graph.add_edge(
        "generate_challenge_query",
        "retrieve_support_evidence",
    )

    graph.add_edge(
        "retrieve_support_evidence",
        "retrieve_challenge_evidence",
    )

    graph.add_edge(
        "retrieve_challenge_evidence",
        "check_evidence_sufficiency",
    )

    # ---------------------------------------------------------
    # Evidence refinement loop
    # ---------------------------------------------------------

    graph.add_conditional_edges(
        "check_evidence_sufficiency",
        should_refine_evidence,
        {
            "refine_queries": "refine_queries",
            "assess_claim": "assess_claim",
        },
    )

    graph.add_edge(
        "refine_queries",
        "retrieve_support_evidence",
    )

    # ---------------------------------------------------------
    # Assessment
    # ---------------------------------------------------------

    graph.add_edge(
        "assess_claim",
        "move_to_next_claim",
    )

    # ---------------------------------------------------------
    # Next claim / final report
    # ---------------------------------------------------------

    graph.add_conditional_edges(
        "move_to_next_claim",
        should_process_next_claim,
        {
            "process_claim": "generate_support_query",
            "final_report": "generate_final_report",
        },
    )

    graph.add_edge(
        "generate_final_report",
        END,
    )

    return graph.compile()