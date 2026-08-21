from triage_agent import triage_agent
from log_analysis_agent import log_analysis_agent
from root_cause_agent import root_cause_analysis
from duplicate_detection_agent import duplicate_detection_agent
from remediation_agent import remediation_agent
# ==========================================
# MULTI-AGENT ORCHESTRATOR
# ==========================================

def orchestrate_bug_analysis(title, description, stack_trace):

    # ----------------------------
    # Run Triage Agent
    # ----------------------------
    triage_output = triage_agent(
        title,
        description,
        stack_trace
    )

    # ----------------------------
    # Run Log Analysis Agent
    # ----------------------------
    log_output = log_analysis_agent(
        stack_trace
    )

    # ----------------------------
    # Run Root Cause Agent
    # ----------------------------
    root_cause_output = root_cause_analysis(
        title,
        description,
        stack_trace
    )
    duplicate_output = duplicate_detection_agent(
    title,
    description,
    stack_trace
    )
    remediation_output = remediation_agent(
    title,
    description,
    stack_trace
    )
    # ----------------------------
    # Combine Results
    # ----------------------------
    final_output = {
    "triage": triage_output,
    "log_analysis": log_output,
    "root_cause": root_cause_output,
    "duplicate_detection": duplicate_output,
    "remediation": remediation_output
     }

    return final_output