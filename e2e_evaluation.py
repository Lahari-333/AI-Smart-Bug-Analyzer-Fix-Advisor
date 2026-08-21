tests = [
    {
        "id": 1,
        "bug_type": "Authentication",
        "expected_exception": "NullPointerException",
        "expected_component": "Authentication"
    },
    {
        "id": 2,
        "bug_type": "Database",
        "expected_exception": "SQLException",
        "expected_component": "Database"
    },
    {
        "id": 3,
        "bug_type": "Network",
        "expected_exception": "SocketTimeoutException",
        "expected_component": "Backend"
    },
    {
        "id": 4,
        "bug_type": "Security",
        "expected_exception": "SecurityException",
        "expected_component": "Authentication"
    },
    {
        "id": 5,
        "bug_type": "Concurrency",
        "expected_exception": "RuntimeException",
        "expected_component": "Backend"
    }
]

print("END-TO-END TEST CASES")
print("=" * 50)

for test in tests:
    print(f"\nTest Case {test['id']}")
    print(f"Bug Type           : {test['bug_type']}")
    print(f"Expected Exception : {test['expected_exception']}")
    print(f"Expected Component : {test['expected_component']}")

print("\nTotal Test Cases:", len(tests))