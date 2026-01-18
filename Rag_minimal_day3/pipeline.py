from loader import load_documents

def pipeline(query: str) -> str:
    """
    RAG Pipeline (Day 3)
    - Retrieve: load_documents
    - Generate: (Day 4 이후)
    """
    documents = load_documents()

    # 아직 LLM 없음
    # 구조/흐름 고정이 목적
    return f"입력 질문: {query}, 문서 수: {len(documents)}"
