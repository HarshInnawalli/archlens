from dataclasses import dataclass
from typing import Optional

from app.ingestion.embeddings import embed_query
from app.ingestion.indexer import COLLECTION_NAME
from app.retrieval.qdrant import get_qdrant_client


@dataclass
class SearchResult:
    text: str
    score: float
    rerank_score: Optional[float] = None

    chunk_id: Optional[str] = None
    document_id: Optional[str] = None
    source: Optional[str] = None
    technology: Optional[str] = None
    topic: Optional[str] = None
    document_type: Optional[str] = None
    section: Optional[str] = None
    url: Optional[str] = None
    file_path: Optional[str] = None


def search(
    query: str,
    client=None,
    top_k: int = 10,
    collection_name: str = COLLECTION_NAME,
) -> list[SearchResult]:

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0.")

    if client is None:
        client = get_qdrant_client()

    query_vector = embed_query(query)

    response = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=top_k,
        with_payload=True,
    )

    results = []

    for point in response.points:

        payload = point.payload or {}

        results.append(
            SearchResult(
                text=payload.get("text", ""),
                score=float(point.score),

                chunk_id=payload.get("chunk_id"),
                document_id=payload.get("document_id"),
                source=payload.get("source"),
                technology=payload.get("technology"),
                topic=payload.get("topic"),
                document_type=payload.get("document_type"),
                section=payload.get("section"),
                url=payload.get("url"),
                file_path=payload.get("file_path"),
            )
        )

    return results


def print_results(results: list[SearchResult]):

    for i, result in enumerate(results, 1):

        print(f"\nRESULT {i}")

        print(f"Semantic Score: {result.score:.4f}")

        if result.rerank_score is not None:
            print(f"Rerank Score:   {result.rerank_score:.4f}")

        print(f"Source:         {result.source}")
        print(f"Technology:     {result.technology}")
        print(f"Topic:          {result.topic}")
        print(f"Section:        {result.section}")
        print(f"Chunk ID:        {result.chunk_id}")

        if result.url:
            print(f"URL:            {result.url}")

        print("\nText:")
        print(result.text)


if __name__ == "__main__":

    query = "Is Redis Pub/Sub suitable for reliable event processing?"

    results = search(
        query=query,
        top_k=10,
    )

    print_results(results)