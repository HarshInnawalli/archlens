from qdrant_client import QdrantClient

from app.ingestion.indexer import COLLECTION_NAME


QDRANT_URL = "http://localhost:6333"


def get_qdrant_client(
    url: str = QDRANT_URL,
) -> QdrantClient:
    """
    Create and return a Qdrant client.
    """

    return QdrantClient(url=url)


def collection_exists(
    client: QdrantClient,
    collection_name: str = COLLECTION_NAME,
) -> bool:
    """
    Check whether a Qdrant collection exists.
    """

    collections = client.get_collections()

    return any(
        collection.name == collection_name
        for collection in collections.collections
    )


def get_collection_info(
    client: QdrantClient,
    collection_name: str = COLLECTION_NAME,
):
    """
    Return information about the ArchLens Qdrant collection.
    """

    if not collection_exists(client, collection_name):
        raise ValueError(
            f"Collection '{collection_name}' does not exist."
        )

    return client.get_collection(
        collection_name=collection_name
    )