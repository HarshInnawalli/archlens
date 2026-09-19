from functools import lru_cache

from sentence_transformers import SentenceTransformer


MODEL_NAME = "BAAI/bge-small-en-v1.5"

EMBEDDING_DIMENSION = 384


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    """
    Load the embedding model once and reuse it.
    """

    return SentenceTransformer(MODEL_NAME)


def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Generate normalized embeddings for a list of texts.
    """

    if not texts:
        return []

    model = get_embedding_model()

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    return embeddings.tolist()


def embed_query(query: str) -> list[float]:
    """
    Generate an embedding for a single retrieval query.
    """

    if not query.strip():
        raise ValueError("Query cannot be empty.")

    model = get_embedding_model()

    embedding = model.encode(
        query,
        normalize_embeddings=True,
    )

    return embedding.tolist()