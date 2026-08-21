import os
from dotenv import load_dotenv
from google import genai

from similarity_search import retrieve_similar_bugs

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def remediation_agent(bug_title, bug_description, stack_trace):

    query = f"""
Bug Title:
{bug_title}

Bug Description:
{bug_description}

Stack Trace:
{stack_trace}
"""

    similar_bugs = retrieve_similar_bugs(query)

    historical_bugs = ""

    for bug in similar_bugs:
        historical_bugs += bug["bug_report"] + "\n\n"

    prompt = f"""
You are a senior software engineer.

Analyze the following bug.

Current Bug:
{query}

Historical Bugs:
{historical_bugs}

Suggest:

1. Recommended Fix
2. Code-Level Suggestions
3. Preventive Measures

Return only these three headings.
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text