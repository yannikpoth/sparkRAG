def split_into_paragraphs(text: str) -> list[str]:
    pieces = text.split("\n\n")
    chunks = []

    for piece in pieces:
        cleaned = piece.strip()
        if cleaned != "":
            chunks.append(cleaned)
    return chunks


def chunk_text(text: str, max_chars: int = 500) -> list[str]:
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, got {type(text).__name__}")
    if text.strip() == "":
        raise ValueError("text must not be empty")

    pieces = text.split("\n\n")

    chunks = []

    for piece in pieces:
        cleaned = piece.strip()
        if cleaned != "":
            chunks.append(cleaned)

    return chunks
    
