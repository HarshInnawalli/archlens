from dataclasses import dataclass
from typing import Optional

from langchain_text_splitters import RecursiveCharacterTextSplitter


@dataclass
class Chunk:
    text: str
    chunk_id: str
    section: Optional[str] = None
    chunk_index: int = 0


# Designed to keep technical explanations together while preventing
# excessively large chunks.
_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1800,
    chunk_overlap=250,
    separators=[
        "\n## ",
        "\n### ",
        "\n#### ",
        "\n\n",
        "\n",
        ". ",
        "; ",
        ", ",
        " ",
    ],
    keep_separator=True,
)


def _extract_section(text: str) -> Optional[str]:
    """
    Find the most recent Markdown heading in the chunk.
    """

    lines = text.splitlines()

    current_section = None

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#"):
            current_section = stripped.lstrip("#").strip()

    return current_section


def chunk_document(text: str, document_id: str) -> list[Chunk]:
    """
    Split a document into retrieval-friendly chunks.

    Each chunk receives a deterministic ID:
        document_id_0000
        document_id_0001
        ...
    """

    if not text or not text.strip():
        return []

    text = text.strip()

    raw_chunks = _splitter.split_text(text)

    chunks = []

    for index, raw_chunk in enumerate(raw_chunks):

        chunk_text = raw_chunk.strip()

        if not chunk_text:
            continue

        section = _extract_section(chunk_text)

        chunk_id = f"{document_id}_{index:04d}"

        chunks.append(
            Chunk(
                text=chunk_text,
                chunk_id=chunk_id,
                section=section,
                chunk_index=index,
            )
        )

    return chunks