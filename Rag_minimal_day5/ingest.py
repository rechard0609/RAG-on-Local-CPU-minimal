from loader import load_documents
from embedding import embed
from vectorstore import VectorStore

def build_vectorstore():
    docs = load_documents()
    texts = [d.text for d in docs]

    vectors = embed(texts)
    store = VectorStore(dim=len(vectors[0]))
    store.add(vectors, texts)

    return store
