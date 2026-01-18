from pipeline import pipeline

def main():
    query = "RAG가 뭐야?"
    result = pipeline(query)

    print("=== QUERY ===")
    print(result["query"])

    print("\n=== DOCUMENTS ===")
    for doc in result["documents"]:
        print(f"- ({doc['id']}) {doc['title']}: {doc['text']}")

if __name__ == "__main__":
    main()
