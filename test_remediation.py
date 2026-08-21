from remediation_agent import remediation_agent

result = remediation_agent(
    "Application crashes on login",
    "Application crashes after entering credentials",
    "java.lang.NullPointerException at LoginService.java:45"
)

print(result)