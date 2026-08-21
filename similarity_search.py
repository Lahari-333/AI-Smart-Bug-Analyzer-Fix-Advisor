from sentence_transformers import SentenceTransformer
import faiss


# ==========================================
# LOAD EMBEDDING MODEL
# ==========================================

model = SentenceTransformer("all-MiniLM-L6-v2")


# ==========================================
# LOAD FAISS INDEX
# ==========================================

index = faiss.read_index("bug_index.faiss")


# ==========================================
# READ BUG REPORTS
# ==========================================

with open("chunks.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = text.split("========== Bug Report")
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]


# ==========================================
# SIMILARITY SEARCH FUNCTION
# ==========================================

def retrieve_similar_bugs(query, k=5):

    query_embedding = model.encode(
        [query]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for i, idx in enumerate(indices[0]):

        if idx < 0 or idx >= len(chunks):
            continue

        results.append({
            "rank": i + 1,
            "similarity_score": float(distances[0][i]),
            "bug_report": chunks[idx]
        })

    return results


# ==========================================
# TEST THE SEARCH
# ==========================================

if __name__ == "__main__":

    query = input("Enter Bug Description:\n")

    results = retrieve_similar_bugs(query)

    print("\nTop Similar Bug Reports:\n")

    for result in results:

        print("=" * 60)
        print(f"Rank: {result['rank']}")
        print(f"Similarity Score: {result['similarity_score']:.4f}")
        print(result["bug_report"][:700])
        print()