from loader import load_documents

def pipeline(query: str):
    """
    RAG 파이프라인의 최소 형태 (Day 1)

    Retrieve  : 문서 로딩
    Generate  : (Day 2 이후)
    """
    documents = load_documents()

    result = {
        "query": query,
        "documents": documents
    }
    return result
