# ==========================================
# AI SMART BUG ANALYZER
# TRIAGE AGENT
# ==========================================

def triage_agent(title, description, stack_trace):

    # ----------------------------------
    # STEP 1 : Combine User Input
    # ----------------------------------

    text = (
        title +
        " " +
        description +
        " " +
        stack_trace
    ).lower()

    # ----------------------------------
    # STEP 2 : Keyword Dictionaries
    # ----------------------------------

    critical_keywords = [
        "crash",
        "fatal",
        "nullpointerexception",
        "outofmemory",
        "segmentation fault",
        "stack overflow",
        "exception"
    ]

    high_keywords = [
        "database",
        "timeout",
        "connection refused",
        "failed",
        "unable",
        "deadlock",
        "sql exception"
    ]

    medium_keywords = [
        "slow",
        "performance",
        "warning",
        "delay",
        "memory leak",
        "latency"
    ]

    low_keywords = [
        "button",
        "alignment",
        "font",
        "spacing",
        "color",
        "label"
    ]

    # ----------------------------------
    # STEP 3 : Severity Score
    # ----------------------------------

    score = 0

    matched_keywords = []

    for word in critical_keywords:

        if word in text:

            score += 5

            matched_keywords.append(word)

    for word in high_keywords:

        if word in text:

            score += 4

            matched_keywords.append(word)

    for word in medium_keywords:

        if word in text:

            score += 2

            matched_keywords.append(word)

    for word in low_keywords:

        if word in text:

            score += 1

            matched_keywords.append(word)

    # ----------------------------------
    # STEP 4 : Predict Severity
    # ----------------------------------

    if score >= 15:

        severity = "Critical"

    elif score >= 8:

        severity = "High"

    elif score >= 3:

        severity = "Medium"

    else:

        severity = "Low"

    # ----------------------------------
    # STEP 5 : Priority Mapping
    # ----------------------------------

    priority_map = {

        "Critical": "P1",

        "High": "P2",

        "Medium": "P3",

        "Low": "P4"

    }

    priority = priority_map[severity]
        # ----------------------------------
    # STEP 6 : Component Prediction
    # ----------------------------------

    component = "General"

    component_keywords = {

        "Authentication": [
            "login",
            "logout",
            "signup",
            "password",
            "authentication",
            "user",
            "credential"
        ],

        "Database": [
            "database",
            "mysql",
            "oracle",
            "sql",
            "query",
            "connection"
        ],

        "Backend": [
            "backend",
            "server",
            "api",
            "service",
            "endpoint"
        ],

        "Frontend": [
            "button",
            "page",
            "screen",
            "ui",
            "frontend",
            "layout"
        ],

        "Performance": [
            "performance",
            "slow",
            "cpu",
            "memory",
            "latency"
        ],

        "Security": [
            "security",
            "token",
            "jwt",
            "encryption",
            "unauthorized",
            "authentication failed"
        ],

        "Networking": [
            "network",
            "socket",
            "dns",
            "proxy",
            "http",
            "https"
        ],

        "Payment": [
            "payment",
            "transaction",
            "invoice",
            "billing",
            "upi"
        ]
    }

    max_matches = 0

    for comp, words in component_keywords.items():

        matches = 0

        for word in words:

            if word in text:
                matches += 1

        if matches > max_matches:

            max_matches = matches

            component = comp

    # ----------------------------------
    # STEP 7 : Dynamic Confidence
    # ----------------------------------

    confidence = min(60 + score * 2, 99)

    # ----------------------------------
    # STEP 8 : Reasoning
    # ----------------------------------

    if matched_keywords:

        reasoning = (
            "Prediction based on detected keywords: "
            + ", ".join(matched_keywords)
        )

    else:

        reasoning = (
            "No major severity keywords were detected. "
            "Bug classified as Low severity."
        )

    # ----------------------------------
    # STEP 9 : Structured Output
    # ----------------------------------

    return {

        "severity": severity,

        "priority": priority,

        "component": component,

        "confidence": confidence,

        "matched_keywords": matched_keywords,

        "reasoning": reasoning

    }