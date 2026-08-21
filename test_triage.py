from triage_agent import triage_agent

result = triage_agent(
    "Application crashes during login",
    "NullPointerException while clicking Login button",
    "java.lang.NullPointerException at LoginService.java:45"
)

print(result)