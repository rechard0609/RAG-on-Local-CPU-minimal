from models import Document

def load_documents():
    """
    문서 로딩 (Day 3 기준)
    - 현재: 파일 기반
    - 이후: DB / Vector DB / API로 확장
    """
    with open("data/docs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    return [
        Document(
            id=1,
            text=text
        )
    ]
