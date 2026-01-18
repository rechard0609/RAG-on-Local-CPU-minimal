# loader.py
from typing import List

class Document:
    def __init__(self, text: str):
        self.text = text

def load_documents(path: str) -> List[Document]:
    docs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                docs.append(Document(line))
    return docs
