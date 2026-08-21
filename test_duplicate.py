from duplicate_detection_agent import duplicate_detection_agent

result = duplicate_detection_agent(
    "Application crashes on login",
    "Application crashes after entering credentials",
    "java.lang.NullPointerException at LoginService.java:45"
)

print(result)