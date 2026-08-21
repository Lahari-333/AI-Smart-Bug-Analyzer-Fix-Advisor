import re

# Read cleaned dataset
with open("clean_bug_reports.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split into bug reports using "Created by"
chunks = re.split(r'(?=Created by)', text)

# Remove empty chunks
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

print("Total Chunks:", len(chunks))

# Save chunks
with open("chunks.txt", "w", encoding="utf-8") as file:
    for i, chunk in enumerate(chunks, start=1):
        file.write(f"========== Bug Report {i} ==========\n")
        file.write(chunk)
        file.write("\n\n")

print("Chunking completed successfully!")