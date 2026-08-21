from sentence_transformers import SentenceTransformer
import numpy as np

print("Loading embedding model...")

# Load the Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")

# Read the chunked bug reports
with open("chunks.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split into chunks
chunks = text.split("========== Bug Report")

# Remove empty chunks
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

print(f"Total Chunks: {len(chunks)}")

print("Generating embeddings...")

# Generate embeddings
embeddings = model.encode(chunks)

print("Embeddings generated successfully!")

# Save embeddings
np.save("embeddings.npy", embeddings)

print("Embeddings saved as embeddings.npy")

print("Embedding Shape:", embeddings.shape)