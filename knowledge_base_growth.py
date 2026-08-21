import faiss
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = "chunks.txt"
INDEX_FILE = "bug_index.faiss"

model = SentenceTransformer("all-MiniLM-L6-v2")


def add_resolved_bug(bug_text, resolution):

    knowledge = f"""
Bug Report:
{bug_text}

Confirmed Resolution:
{resolution}
"""

    # Add using the same separator used by the existing knowledge base
    with open(CHUNKS_FILE, "a", encoding="utf-8") as file:
        file.write("\n========== Bug Report\n")
        file.write(knowledge)
        file.write("\n")

    # Create embedding
    embedding = model.encode(
        [knowledge],
        convert_to_numpy=True
    ).astype("float32")

    # Load FAISS index
    index = faiss.read_index(INDEX_FILE)

    # Add embedding
    index.add(embedding)

    # Save updated index
    faiss.write_index(index, INDEX_FILE)

    return {
        "status": "success",
        "message": "Resolved bug added to knowledge base",
        "total_vectors": index.ntotal
    }