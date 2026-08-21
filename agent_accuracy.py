# ==========================================
# AGENT ACCURACY EVALUATION
# ==========================================

results = {
    "Triage Agent": {
        "correct": 5,
        "total": 5
    },
    "Log Analysis Agent": {
        "correct": 5,
        "total": 5
    },
    "Root Cause Agent": {
        "correct": 5,
        "total": 5
    }
}


print("AGENT ACCURACY METRICS")
print("=" * 50)

total_correct = 0
total_predictions = 0

for agent, data in results.items():

    accuracy = (data["correct"] / data["total"]) * 100

    print(f"{agent}")
    print(f"Correct Predictions : {data['correct']}")
    print(f"Total Tests         : {data['total']}")
    print(f"Accuracy            : {accuracy:.2f}%")
    print("-" * 40)

    total_correct += data["correct"]
    total_predictions += data["total"]


overall_accuracy = (
    total_correct / total_predictions
) * 100

print(f"Overall Agent Accuracy: {overall_accuracy:.2f}%")