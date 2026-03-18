import os
import hashlib
import json
from spark_rag.chunking import chunk_text

def make_id(text: str) -> str:
    text_bytes = text.encode("utf-8")
    digest = hashlib.sha1(text_bytes).hexdigest()
    return digest[:12]

def build_chunks(doc_id: str, chunks_list: list) -> list:
    chunks = []

    for index in range(len(chunks_list)):
        chunk = {
            "chunk_id": f"{doc_id}_{make_id(chunks_list[index])}_{index}",
            "chunk_index": index,
            "text": chunks_list[index],
        }
        chunks.append(chunk)

    return chunks

def ingest_file(path: str) -> str:
    
    if not isinstance(path, str):
        raise TypeError(f"path must be a string, got {type(path).__name__}")

    if path.strip() == "":
        raise ValueError("path must not be empty")
    
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")


    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    doc_id = f"doc_{make_id(text)}"
    chunks_list = chunk_text(text, max_chars=2000)

    document = {
        "doc_id": doc_id,
        "source_path": path,
        "char_count": len(text),
        "chunk_count": len(chunks_list),
        "chunks_path": f"outputs/chunks/{doc_id}.json",
    }

    chunks = build_chunks(doc_id, chunks_list)

    os.makedirs("outputs/docs", exist_ok=True)
    os.makedirs("outputs/chunks", exist_ok=True)

    doc_output_path = f"outputs/docs/{doc_id}.json"
    chunks_output_path = f"outputs/chunks/{doc_id}.json"

    with open(doc_output_path, "w", encoding="utf-8") as f:
        json.dump(document, f, ensure_ascii=False, indent=2)

    with open(chunks_output_path, "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks}, f, ensure_ascii=False, indent=2)
    
    print(f"Read {len(text)} characters from {path}")
    print(f"Created doc_id: {doc_id}")
    print(f"Wrote Document JSON to {doc_output_path}")
    print(f"Wrote Chunks JSON to {chunks_output_path}")

    return doc_id