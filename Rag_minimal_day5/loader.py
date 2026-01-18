from models import Document

def load_documents():
    with open("data/docs.txt", "r", encoding="utf-8") as f:
        text = f.read()
    return [Document(id=1, text=text)]
