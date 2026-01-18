# app/loader.py
from pathlib import Path
 
BASE_DIR = Path(__file__).resolve().parent.parent

def load_documents(path: str):
    documents = []
    doc_path = BASE_DIR / path   # 🔥 핵심

    with open(doc_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            documents.append({
                "id": idx,
                "text": line.strip()
            })

    return documents
