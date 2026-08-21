import re

# ==========================================
# LOG ANALYSIS AGENT
# ==========================================

def log_analysis_agent(stack_trace):

    exception_type = "Unknown"

    failure_point = "Unknown"

    code_path = []

    # ----------------------------
    # Exception Detection
    # ----------------------------

    exception_pattern = r'([A-Za-z]+Exception|Error)'

    match = re.search(exception_pattern, stack_trace)

    if match:
        exception_type = match.group()

    # ----------------------------
    # Failure Point
    # ----------------------------

    lines = stack_trace.splitlines()

    for line in lines:

        line = line.strip()

        if line.startswith("at"):

            failure_point = line

            break

    # ----------------------------
    # Code Path
    # ----------------------------

    for line in lines:

        line = line.strip()

        if line.startswith("at"):

            code_path.append(line)

    return {

        "exception_type": exception_type,

        "failure_point": failure_point,

        "code_path": code_path

    }