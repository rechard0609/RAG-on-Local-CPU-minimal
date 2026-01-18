# app/main.py
from pipeline import pipeline
from config import load_config

def main():
    config = load_config()
    query = "RAG가 뭐야?"

    result = pipeline(query, config)

    print("=== QUERY ===")
    print(result["query"])

    print("\n=== DOCUMENTS ===")
    for doc in result["documents"]:
        print(f"- ({doc['id']}) {doc['text']}")

if __name__ == "__main__":
    main()
