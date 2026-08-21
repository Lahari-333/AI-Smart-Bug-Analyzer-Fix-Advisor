from log_analysis_agent import log_analysis_agent

stack_trace = """
java.lang.NullPointerException

at LoginService.java:45

at LoginController.java:18

at Main.java:10
"""

result = log_analysis_agent(stack_trace)

print(result)