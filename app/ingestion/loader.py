from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".md",
    ".txt",
    ".html",
    ".htm",
    ".pdf",
}


def load_document(path: str) -> str:
    """
    Load a document and return its raw text.

    Supported:
        .md
        .txt
        .html
        .htm
        .pdf
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = file_path.suffix.lower()

    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {suffix}. "
            f"Supported types: {SUPPORTED_EXTENSIONS}"
        )

    if suffix in {".md", ".txt"}:
        return file_path.read_text(encoding="utf-8")

    if suffix in {".html", ".htm"}:
        return _load_html(file_path)

    if suffix == ".pdf":
        return _load_pdf(file_path)

    raise ValueError(f"Unsupported file type: {suffix}")


def _load_html(file_path: Path) -> str:
    """
    Extract readable text from an HTML document.
    """

    from bs4 import BeautifulSoup

    html = file_path.read_text(encoding="utf-8")

    soup = BeautifulSoup(html, "html.parser")

    # Remove elements that normally contain non-content noise.
    for element in soup(
        ["script", "style", "noscript", "nav", "footer", "header"]
    ):
        element.decompose()

    return soup.get_text("\n")


def _load_pdf(file_path: Path) -> str:
    """
    Extract text from a PDF using PyMuPDF.
    """

    import fitz

    document = fitz.open(file_path)

    pages = []

    try:
        for page in document:
            text = page.get_text("text")
            pages.append(text)
    finally:
        document.close()

    return "\n".join(pages)