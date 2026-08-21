tests = [
    {
        "id": 1,
        "bug": "Application crashes during login because User object is null",
        "expected_duplicate": True
    },
    {
        "id": 2,
        "bug": "Database connection refused during checkout",
        "expected_duplicate": False
    },
    {
        "id": 3,
        "bug": "Payment API request times out",
        "expected_duplicate": False
    },
    {
        "id": 4,
        "bug": "Unauthorized user can access admin page",
        "expected_duplicate": False
    },
    {
        "id": 5,
        "bug": "Application freezes during concurrent requests",
        "expected_duplicate": False
    }
]

print("=" * 60)
print("DUPLICATE DETECTION EVALUATION")
print("=" * 60)

for test in tests:
    print()
    print("Test Case:", test["id"])
    print("Bug:", test["bug"])
    print("Expected Duplicate:", test["expected_duplicate"])

print()
print("=" * 60)
print("Total Tests:", len(tests))
print("=" * 60)