# ingest.py
from loader import load_documents
from vectorstore import build_store
from keyword_index import KeywordIndex
from reranker import build_reranker
from config import DATA_PATH

def build_assets():
    docs = load_documents(DATA_PATH)
    print("LOADED DOCS:", len(docs))

    store = build_store(docs)
    keyword = KeywordIndex(docs)
    reranker = build_reranker(docs)

    return store, keyword, reranker
