# ingest.py
from loader import load_documents
from config import DATA_PATH
from vectorstore import build_store
from reranker import build_reranker

def build_assets():
    docs = load_documents(DATA_PATH)
    print("LOADED DOCS:", len(docs))

    texts = [d.text for d in docs]
    print("TEXT SAMPLE:", texts[:1])

    store = build_store(docs)
    reranker = build_reranker(docs)

    return store, reranker
