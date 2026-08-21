from root_cause_agent import root_cause_analysis

bug_title = "Application crashes on login"

bug_description = """
The application crashes immediately after entering valid credentials.
"""

stack_trace = """
java.lang.NullPointerException
at LoginService.authenticate(LoginService.java:45)
"""

result = root_cause_analysis(
    bug_title,
    bug_description,
    stack_trace
)

print(result)