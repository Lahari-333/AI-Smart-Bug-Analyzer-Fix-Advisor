import json
from collections import Counter


HISTORY_FILE = "analysis_history.json"


def load_analysis_history():
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_defect_patterns():
    history = load_analysis_history()

    severity_count = Counter()
    priority_count = Counter()
    component_count = Counter()
    exception_count = Counter()
    root_cause_themes = Counter()

    for record in history:

        analysis = record.get("analysis", {})
        triage = analysis.get("triage", {})
        log_analysis = analysis.get("log_analysis", {})

        # Severity
        severity = triage.get("severity")
        if severity:
            severity_count[severity] += 1

        # Priority
        priority = triage.get("priority")
        if priority:
            priority_count[priority] += 1

        # Component
        component = triage.get("component")
        if component:
            component_count[component] += 1

        # Exception type
        exception_type = log_analysis.get("exception_type")
        if exception_type and exception_type != "Unknown":
            exception_count[exception_type] += 1

        # Root cause themes
        root_cause = analysis.get("root_cause", "")

        text = root_cause.lower()

        if "nullpointerexception" in text or "null object" in text:
            root_cause_themes["Null / Initialization Issue"] += 1

        if "database" in text or "repository" in text:
            root_cause_themes["Database / Data Access"] += 1

        if "concurrency" in text or "race condition" in text:
            root_cause_themes["Concurrency / Race Condition"] += 1

        if "authentication" in text or "login" in text:
            root_cause_themes["Authentication"] += 1

        if "timeout" in text:
            root_cause_themes["Timeout / Connectivity"] += 1

    return {
        "severity": dict(severity_count),
        "priority": dict(priority_count),
        "component": dict(component_count),
        "exception": dict(exception_count),
        "root_cause": dict(root_cause_themes)
    }