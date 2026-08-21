import time
import faiss
import numpy as np

print("=" * 60)
print("HISTORICAL DATASET SIZE TEST")
print("=" * 60)

# -------------------------------------------------
# 1. Load embeddings
# -------------------------------------------------

embeddings = np.load("embeddings.npy").astype("float32")

print("\nTotal available embeddings:", len(embeddings))

# -------------------------------------------------
# 2. Dataset sizes to test
# -------------------------------------------------

dataset_sizes = [
    50,
    150,
    len(embeddings)
]

# -------------------------------------------------
# 3. Use first embedding as test query
# -------------------------------------------------

query_vector = embeddings[0].reshape(1, -1)

print("\n")
print("=" * 60)
print("DATASET SIZE COMPARISON")
print("=" * 60)

for size in dataset_sizes:

    # Make sure size doesn't exceed dataset
    size = min(size, len(embeddings))

    # Take only this many historical embeddings
    subset = embeddings[:size]

    # Create temporary FAISS index in memory
    index = faiss.IndexFlatL2(
        subset.shape[1]
    )

    index.add(subset)

    # Measure search time
    start = time.perf_counter()

    distances, indices = index.search(
        query_vector,
        min(5, size)
    )

    end = time.perf_counter()

    search_time = (
        end - start
    ) * 1000

    print("\nDataset Size:", size)

    print(
        "FAISS Vectors:",
        index.ntotal
    )

    print(
        "Top Results:",
        len(indices[0])
    )

    print(
        "Search Time:",
        round(search_time, 4),
        "ms"
    )

# -------------------------------------------------
# 4. Final consistency check
# -------------------------------------------------

print("\n")
print("=" * 60)
print("CURRENT KNOWLEDGE BASE CONSISTENCY")
print("=" * 60)

with open(
    "chunks.txt",
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

chunks = text.split(
    "========== Bug Report"
)

chunks = [
    c.strip()
    for c in chunks
    if c.strip()
]

# Load actual saved FAISS index
saved_index = faiss.read_index(
    "bug_index.faiss"
)

print(
    "Text chunks     :",
    len(chunks)
)

print(
    "Embeddings      :",
    len(embeddings)
)

print(
    "FAISS vectors   :",
    saved_index.ntotal
)

print(
    "Vector dimension:",
    saved_index.d
)

if len(embeddings) == saved_index.ntotal:
    print(
        "Embeddings / FAISS : MATCH ✅"
    )
else:
    print(
        "Embeddings / FAISS : MISMATCH ❌"
    )

if len(chunks) == saved_index.ntotal:
    print(
        "Chunks / FAISS     : MATCH ✅"
    )
else:
    print(
        "Chunks / FAISS     : MISMATCH ❌"
    )

print("\n" + "=" * 60)
print("DATASET SIZE TEST COMPLETED")
print("=" * 60)