# loader.py
from models import Document

def load_documents(path):
    docs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                docs.append(Document(text=line))
    return docs
