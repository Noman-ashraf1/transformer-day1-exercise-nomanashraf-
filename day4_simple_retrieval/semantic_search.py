import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# File paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCUMENT_FILE = os.path.join(SCRIPT_DIR, "documents.txt")
QUERY_FILE = os.path.join(SCRIPT_DIR, "queries.txt")
RESULT_FILE = os.path.join(SCRIPT_DIR, "results.txt")

def load_documents():
    with open(DOCUMENT_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_query(query):
    with open(QUERY_FILE, "a", encoding="utf-8") as f:
        f.write(query + "\n")

def save_results(output):
    with open(RESULT_FILE, "a", encoding="utf-8") as f:
        f.write(output + "\n")  # adds newline between queries

def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    documents = load_documents()
    document_embeddings = model.encode(documents)

    print("\nSemantic Search Ready")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Enter Query: ")
        if query.lower() == "exit":
            break

        query_embedding = model.encode([query])
        similarities = cosine_similarity(query_embedding, document_embeddings)[0]

        top_indices = np.argsort(similarities)[::-1][:3]

        output = f"Query: {query}\nTop 3 Results:\n"
        for rank, idx in enumerate(top_indices, start=1):
            document = documents[idx]
            score = similarities[idx]
            print(f"{rank}. {document} ({score:.2f})")
            output += f"{rank}. {document} ({score:.2f})\n"
        output += "---------------------------------\n"

        # Save query and results
        save_query(query)
        save_results(output)

        print("\n---------------------------------\n")

if __name__ == "__main__":
    main()