import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


CHUNKS_FILE = "chunks.txt"
EMBEDDINGS_FILE = "embeddings.npy"
INDEX_FILE = "bug_index.faiss"


print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")


# ==========================================
# 1. Fix the separator of the resolved bug
# ==========================================

with open(CHUNKS_FILE, "r", encoding="utf-8") as file:
    text = file.read()

text = text.replace(
    "========== Resolved Bug ==========",
    "========== Bug Report"
)

with open(CHUNKS_FILE, "w", encoding="utf-8") as file:
    file.write(text)

print("Chunk separator fixed.")


# ==========================================
# 2. Read all chunks
# ==========================================

chunks = text.split("========== Bug Report")
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

print("Total text chunks:", len(chunks))


# ==========================================
# 3. Load ORIGINAL 267 embeddings
# ==========================================

embeddings = np.load(EMBEDDINGS_FILE)

embeddings = embeddings.astype("float32")

print("Original embeddings:", len(embeddings))


# ==========================================
# 4. Create a fresh FAISS index
# ==========================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("FAISS vectors after original data:", index.ntotal)


# ==========================================
# 5. Get the newly added resolved bug
# ==========================================

new_bug = chunks[-1]

print("\nNew resolved bug found:")
print(new_bug[:500])


# ==========================================
# 6. Create embedding for new resolved bug
# ==========================================

new_embedding = model.encode(
    [new_bug],
    convert_to_numpy=True
).astype("float32")


# ==========================================
# 7. Add new resolved bug to FAISS
# ==========================================

index.add(new_embedding)

print("\nFAISS vectors after adding resolved bug:", index.ntotal)


# ==========================================
# 8. Save repaired FAISS index
# ==========================================

faiss.write_index(index, INDEX_FILE)

print("\nKnowledge base repaired successfully!")
print("Text chunks:", len(chunks))
print("FAISS vectors:", index.ntotal)