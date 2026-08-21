from defect_pattern_analytics import get_defect_patterns

patterns = get_defect_patterns()

print("\nDEFECT PATTERN ANALYTICS")
print("========================")

print("\nSeverity:")
print(patterns["severity"])

print("\nPriority:")
print(patterns["priority"])

print("\nComponents:")
print(patterns["component"])

print("\nExceptions:")
print(patterns["exception"])

print("\nRoot Cause Themes:")
print(patterns["root_cause"])