# llm.py
def generate_answer(query: str, contexts: list[str]) -> str:
    if not contexts:
        return "관련 문서를 찾지 못했습니다."

    joined = "\n".join(contexts)

    return (
        f"질문:\n{query}\n\n"
        f"참고 문서:\n{joined}\n\n"
        f"답변:\n"
        f"Embedding은 텍스트를 숫자 벡터로 변환하여 "
        f"질문과 문서 간 의미적 유사도를 계산하기 위해 필요합니다."
    )
