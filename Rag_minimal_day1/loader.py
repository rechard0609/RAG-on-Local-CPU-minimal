def load_documents():
    """
    RAG용 최소 문서 로더 (Day 1)
    - 실제 환경에서는 DB / 파일 / API로 확장됨
    - Day 1에서는 '문서를 가져온다'는 개념만 전달
    """
    documents = [
        {
            "id": 1,
            "title": "RAG 개요",
            "text": "RAG는 Retrieval Augmented Generation의 약자이다."
        },
        {
            "id": 2,
            "title": "LLM 개요",
            "text": "LLM은 대규모 언어 모델로 문맥을 기반으로 답변한다."
        },
        {
            "id": 3,
            "title": "Pipeline",
            "text": "AI 시스템은 단계적 파이프라인으로 구성된다."
        }
    ]
    return documents
