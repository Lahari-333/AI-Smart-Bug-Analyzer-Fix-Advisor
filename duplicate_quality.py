import json

with open("analysis_history.json", "r", encoding="utf-8") as f:
    history = json.load(f)

tests = [
    {
        "id": 1,
        "expected_duplicate": True,
        "expected_exception": "NullPointerException"
    },
    {
        "id": 2,
        "expected_duplicate": False,
        "expected_exception": "SQLException"
    },
    {
        "id": 3,
        "expected_duplicate": False,
        "expected_exception": "SocketTimeoutException"
    },
    {
        "id": 4,
        "expected_duplicate": False,
        "expected_exception": "SecurityException"
    },
    {
        "id": 5,
        "expected_duplicate": False,
        "expected_exception": "RuntimeException"
    }
]


def find_result(expected_exception):

    for item in history:

        analysis = item.get("analysis", {})
        log = analysis.get("log_analysis", {})

        exception = str(
            log.get("exception_type", "")
        )

        if exception.lower() == expected_exception.lower():
            return analysis

    return None


print("=" * 60)
print("DUPLICATE DETECTION QUALITY")
print("=" * 60)

correct = 0
total = len(tests)

for test in tests:

    analysis = find_result(test["expected_exception"])

    print("\nTest Case:", test["id"])

    if analysis is None:
        print("❌ Actual result not found")
        continue

    duplicate = analysis.get("duplicate", False)
    similarity = analysis.get("similarity_percentage", 0)

    expected = test["expected_duplicate"]

    print("Expected Duplicate :", expected)
    print("Actual Duplicate   :", duplicate)
    print("Similarity         :", similarity, "%")

    if duplicate == expected:
        correct += 1
        print("Result             : ✅ CORRECT")
    else:
        print("Result             : ❌ INCORRECT")


accuracy = (correct / total) * 100

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

print("Correct:", correct, "/", total)
print("Duplicate Detection Accuracy:", f"{accuracy:.2f}%")
print("=" * 60)