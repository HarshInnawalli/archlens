from dataclasses import replace
from typing import Optional

from sentence_transformers import CrossEncoder

from app.retrieval.search import SearchResult


MODEL_NAME = "BAAI/bge-reranker-base"

_model: Optional[CrossEncoder] = None


def get_reranker() -> CrossEncoder:

    global _model

    if _model is None:
        _model = CrossEncoder(MODEL_NAME)

    return _model


def rerank(
    query: str,
    results: list[SearchResult],
    top_k: int = 5,
) -> list[SearchResult]:

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    if not results:
        return []

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0.")

    model = get_reranker()

    pairs = [
        (query, result.text)
        for result in results
    ]

    scores = model.predict(pairs)

    reranked = [
        replace(
            result,
            rerank_score=float(score),
        )
        for result, score in zip(results, scores)
    ]

    reranked.sort(
        key=lambda result: result.rerank_score,
        reverse=True,
    )

    return reranked[:top_k]