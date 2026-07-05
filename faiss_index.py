import numpy as np
import faiss

# Load embeddings
embeddings = np.load("embeddings.npy")

print("Embeddings Loaded Successfully!")

# Convert to float32
embeddings = embeddings.astype("float32")

# Get embedding dimension
dimension = embeddings.shape[1]

# Create FAISS Index
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

print("Total Embeddings:", index.ntotal)

# Save index
faiss.write_index(index, "bug_index.faiss")

print("FAISS Index Created Successfully!")