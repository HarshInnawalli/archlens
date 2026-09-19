from collections import Counter

from app.retrieval.qdrant import get_qdrant_client
from app.ingestion.indexer import COLLECTION_NAME


def main():

    client = get_qdrant_client()

    info = client.get_collection(
        COLLECTION_NAME
    )

    print(f"Collection: {COLLECTION_NAME}")
    print(f"Total chunks: {info.points_count}")

    points, _ = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=10000,
        with_payload=True,
        with_vectors=False,
    )

    technologies = Counter()
    document_types = Counter()
    documents = Counter()

    for point in points:

        payload = point.payload or {}

        technologies[
            payload.get("technology", "unknown")
        ] += 1

        document_types[
            payload.get("document_type", "unknown")
        ] += 1

        documents[
            payload.get("document_id", "unknown")
        ] += 1

    print("\n===== TECHNOLOGIES =====")

    for name, count in technologies.most_common():
        print(f"{name}: {count}")

    print("\n===== DOCUMENT TYPES =====")

    for name, count in document_types.most_common():
        print(f"{name}: {count}")

    print("\n===== DOCUMENTS =====")

    for name, count in documents.most_common():
        print(f"{name}: {count}")


if __name__ == "__main__":
    main()