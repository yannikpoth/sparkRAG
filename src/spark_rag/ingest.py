import os
import hashlib
import json

def make_doc_id(text: str) -> str:
    text_bytes = text.encode("utf-8")
    digest = hashlib.sha1(text_bytes).hexdigest()
    return f"doc_{digest[:12]}"

def ingest_file(path: str) -> str:
    
    if not isinstance(path, str):
        raise TypeError(f"path must be a string, got {type(path).__name__}")

    if path.strip() == "":
        raise ValueError("path must not be empty")
    
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")


    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    doc_id = make_doc_id(text)

    document = {
        "doc_id": doc_id,
        "source_path": path,
        "char_count": len(text),
        "text": text,
    }

    os.makedirs("outputs/docs", exist_ok=True)

    output_path = f"outputs/docs/{doc_id}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(document, f, ensure_ascii=False, indent=2)
    
    print(f"Read {len(text)} characters from {path}")
    print(f"Created doc_id: {doc_id}")
    print(f"Wrote JSON to {output_path}")

    return doc_id