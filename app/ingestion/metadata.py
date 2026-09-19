from dataclasses import asdict, dataclass
from typing import Optional

from .chunker import Chunk


@dataclass(frozen=True)
class DocumentMetadata:
    """
    Metadata associated with a source document.
    """

    document_id: str
    source: str
    technology: str
    topic: str
    document_type: str

    url: Optional[str] = None
    file_path: Optional[str] = None


def build_chunk_payload(
    chunk: Chunk,
    metadata: DocumentMetadata,
) -> dict:
    """
    Build the payload stored alongside a Qdrant vector.
    """

    return {
        # ----------------------------------------------------------
        # Chunk information
        # ----------------------------------------------------------

        "text": chunk.text,
        "chunk_id": chunk.chunk_id,
        "chunk_index": chunk.chunk_index,
        "section": chunk.section,

        # ----------------------------------------------------------
        # Document information
        # ----------------------------------------------------------

        "document_id": metadata.document_id,
        "source": metadata.source,
        "technology": metadata.technology,
        "topic": metadata.topic,
        "document_type": metadata.document_type,

        # ----------------------------------------------------------
        # Citation information
        # ----------------------------------------------------------

        "url": metadata.url,
        "file_path": metadata.file_path,
    }


def metadata_to_dict(
    metadata: DocumentMetadata,
) -> dict:
    """
    Convert metadata into a normal dictionary.
    """

    return asdict(metadata)