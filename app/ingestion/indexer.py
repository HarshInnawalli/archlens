from pathlib import Path
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from .loader import load_document
from .cleaner import prepare_text
from .chunker import chunk_document
from .metadata import DocumentMetadata
from .metadata_registry import (
    DocumentRecord,
    get_registry,
)
from .metadata import build_chunk_payload
from .embeddings import (
    embed_texts,
    EMBEDDING_DIMENSION,
)


COLLECTION_NAME = "archlens"

DATA_DIR = Path("data")

SUPPORTED_EXTENSIONS = {
    ".md",
    ".txt",
    ".html",
    ".htm",
    ".pdf",
}


def get_qdrant_client(
    url: str = "http://localhost:6333",
) -> QdrantClient:
    """
    Create a Qdrant client.
    """

    return QdrantClient(url=url)


def create_collection(
    client: QdrantClient,
    collection_name: str = COLLECTION_NAME,
    recreate: bool = False,
) -> None:
    """
    Create the Qdrant collection.

    If recreate=True, delete the existing collection first.
    """

    existing_collections = client.get_collections()

    collection_names = {
        collection.name
        for collection in existing_collections.collections
    }

    if collection_name in collection_names:

        if not recreate:
            return

        print(
            f"Deleting existing collection: "
            f"{collection_name}"
        )

        client.delete_collection(
            collection_name=collection_name
        )

    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=EMBEDDING_DIMENSION,
            distance=Distance.COSINE,
        ),
    )

    print(
        f"Created collection: {collection_name}"
    )


def discover_files(
    data_dir: Path = DATA_DIR,
) -> list[Path]:
    """
    Recursively discover all supported files under data/.
    """

    if not data_dir.exists():
        raise FileNotFoundError(
            f"Data directory not found: {data_dir}"
        )

    files = sorted(
        path
        for path in data_dir.rglob("*")
        if (
            path.is_file()
            and path.suffix.lower()
            in SUPPORTED_EXTENSIONS
        )
    )

    return files


def get_registered_documents(
    data_dir: Path = DATA_DIR,
) -> list[tuple[str, DocumentMetadata]]:
    """
    Discover files and match them against the metadata registry.

    Unregistered files are reported and skipped.
    """

    registry = get_registry()

    files = discover_files(data_dir)

    documents = []

    unregistered = []

    for file_path in files:

        relative_path = file_path.as_posix()

        record = registry.get(relative_path)

        if record is None:
            unregistered.append(relative_path)
            continue

        metadata = DocumentMetadata(
            document_id=record.document_id,
            source=record.source,
            technology=record.technology,
            topic=record.topic,
            document_type=record.document_type,
            url=record.url,
            file_path=record.file_path,
        )

        documents.append(
            (
                relative_path,
                metadata,
            )
        )

    # --------------------------------------------------------------
    # Report unregistered files
    # --------------------------------------------------------------

    if unregistered:

        print(
            "\nWARNING: The following files are not "
            "present in metadata_registry.py:"
        )

        for path in unregistered:
            print(f"  - {path}")

        print(
            "\nThese files will NOT be indexed."
        )

    # --------------------------------------------------------------
    # Report registry entries whose files don't exist
    # --------------------------------------------------------------

    discovered_paths = {
        path.as_posix()
        for path in files
    }

    missing_files = []

    for registry_path in registry:

        if registry_path not in discovered_paths:
            missing_files.append(registry_path)

    if missing_files:

        print(
            "\nWARNING: The following registry entries "
            "do not correspond to existing files:"
        )

        for path in missing_files:
            print(f"  - {path}")

    return documents


def index_documents(
    client: QdrantClient,
    documents: list[tuple[str, DocumentMetadata]],
    collection_name: str = COLLECTION_NAME,
) -> int:
    """
    Ingest and index multiple documents.
    """

    create_collection(
        client,
        collection_name,
    )

    total_chunks = 0

    for file_path, metadata in documents:

        print(
            f"\nProcessing: {file_path}"
        )

        # ----------------------------------------------------------
        # 1. Load
        # ----------------------------------------------------------

        raw_text = load_document(file_path)

        # ----------------------------------------------------------
        # 2. Clean
        # ----------------------------------------------------------

        cleaned_text = prepare_text(raw_text)

        if not cleaned_text:
            print(
                "Skipping empty document."
            )
            continue

        # ----------------------------------------------------------
        # 3. Chunk
        # ----------------------------------------------------------

        chunks = chunk_document(
            cleaned_text,
            metadata.document_id,
        )

        if not chunks:
            print(
                "No chunks generated."
            )
            continue

        print(
            f"Generated {len(chunks)} chunks."
        )

        # ----------------------------------------------------------
        # 4. Embed
        # ----------------------------------------------------------

        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = embed_texts(texts)

        # ----------------------------------------------------------
        # 5. Create Qdrant points
        # ----------------------------------------------------------

        points = []

        for chunk, embedding in zip(
            chunks,
            embeddings,
        ):

            payload = build_chunk_payload(
                chunk,
                metadata,
            )

            # Deterministic UUID based on chunk ID.
            #
            # Re-running ingestion therefore updates
            # the same Qdrant point instead of creating
            # duplicates.

            point_id = str(
                uuid.uuid5(
                    uuid.NAMESPACE_URL,
                    chunk.chunk_id,
                )
            )

            points.append(
                PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload=payload,
                )
            )

        # ----------------------------------------------------------
        # 6. Upsert
        # ----------------------------------------------------------

        client.upsert(
            collection_name=collection_name,
            points=points,
        )

        total_chunks += len(points)

        print(
            f"Indexed {len(points)} chunks "
            f"from {metadata.source}"
        )

    print(
        f"\nFinished. Indexed "
        f"{total_chunks} chunks total."
    )

    return total_chunks


def main():

    client = get_qdrant_client()

    print(
        "===== DISCOVERING DATA ====="
    )

    documents = get_registered_documents()

    print(
        f"\nRegistered files ready for indexing: "
        f"{len(documents)}"
    )

    if not documents:
        raise RuntimeError(
            "No registered documents found."
        )

    print(
        "\n===== DOCUMENTS TO INDEX ====="
    )

    for file_path, metadata in documents:

        print(
            f"\n{file_path}"
        )

        print(
            f"  Source:      {metadata.source}"
        )

        print(
            f"  Technology:  {metadata.technology}"
        )

        print(
            f"  Topic:       {metadata.topic}"
        )

        print(
            f"  Type:        {metadata.document_type}"
        )

        print(
            f"  URL:         {metadata.url}"
        )

    # --------------------------------------------------------------
    # Rebuild collection
    # --------------------------------------------------------------

    print(
        "\n===== REBUILDING QDRANT COLLECTION ====="
    )

    create_collection(
        client,
        COLLECTION_NAME,
        recreate=True,
    )

    # --------------------------------------------------------------
    # Index
    # --------------------------------------------------------------

    index_documents(
        client=client,
        documents=documents,
        collection_name=COLLECTION_NAME,
    )


if __name__ == "__main__":
    main()