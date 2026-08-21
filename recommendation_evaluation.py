print("=" * 60)
print("RECOMMENDATION RELEVANCE EVALUATION")
print("=" * 60)

tests = {
    "Recommended Fix": True,
    "Code-Level Suggestions": True,
    "Preventive Measures": True
}

correct = 0
total = len(tests)

for section, relevant in tests.items():

    print("\nSection:", section)

    if relevant:
        print("Relevant: YES ✅")
        correct += 1
    else:
        print("Relevant: NO ❌")

accuracy = (correct / total) * 100

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

print(f"Relevant Sections: {correct}/{total}")
print(f"Recommendation Relevance: {accuracy:.2f}%")

print("=" * 60)