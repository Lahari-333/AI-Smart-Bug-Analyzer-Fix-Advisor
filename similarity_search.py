from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("bug_index.faiss")

# Read all bug report chunks
with open("chunks.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = text.split("========== Bug Report")
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

# User input
query = input("Enter Bug Description:\n")

# Convert query to embedding
query_embedding = model.encode([query]).astype("float32")

# Search Top 5 similar bugs
k = 5
distances, indices = index.search(query_embedding, k)

print("\nTop Similar Bug Reports:\n")

for i, idx in enumerate(indices[0]):
    print("=" * 60)
    print(f"Rank {i+1}")
    print(f"Distance : {distances[0][i]:.4f}")
    print(chunks[idx][:700])   # Show first 700 characters
    print()