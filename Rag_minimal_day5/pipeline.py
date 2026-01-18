from embedding import embed
from ingest import build_vectorstore
from llm import generate
from config import TOP_K

_store = None

def get_store():
    global _store
    if _store is None:
        _store = build_vectorstore()
    return _store

def pipeline(query: str) -> str:
    store = get_store()

    query_vector = embed([query])[0]
    contexts = store.search(query_vector, top_k=TOP_K)

    context_text = "\n".join(contexts)

    prompt = f"""
아래 문서를 참고해 질문에 답하세요.

문서:
{context_text}

질문:
{query}
"""

    return generate(prompt)
