file_path = "bugzilla bug reports/corpus (fixsev).txt"

with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
    data = file.read()

# Remove unnecessary spaces
clean_data = data.strip()

# Split into lines
lines = clean_data.splitlines()

# Remove empty lines
clean_lines = []

for line in lines:
    if line.strip() != "":
        clean_lines.append(line.strip())

# Join cleaned lines
final_text = "\n".join(clean_lines)

# Save cleaned file
with open("clean_bug_reports.txt", "w", encoding="utf-8") as file:
    file.write(final_text)

print("Dataset cleaned successfully!")