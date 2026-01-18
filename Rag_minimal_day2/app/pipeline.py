# app/pipeline.py
from loader import load_documents

def pipeline(query: str, config: dict):
    doc_path = config["data"]["document_path"]
    max_docs = config["pipeline"]["max_docs"]

    documents = load_documents(doc_path)

    return {
        "query": query,
        "documents": documents[:max_docs]
    }
