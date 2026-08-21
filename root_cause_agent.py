import os
from dotenv import load_dotenv
from google import genai

from similarity_search import retrieve_similar_bugs

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def root_cause_analysis(bug_title, bug_description, stack_trace):

    # Combine user input
    query = f"""
    Bug Title:
    {bug_title}

    Bug Description:
    {bug_description}

    Stack Trace:
    {stack_trace}
    """

    # Retrieve historical bugs
    similar_bugs = retrieve_similar_bugs(query)

    evidence = ""

    for bug in similar_bugs:
        evidence += f"""
Rank: {bug['rank']}
Similarity Score: {bug['similarity_score']}

Historical Bug:
{bug['bug_report']}

----------------------------------------
"""

    prompt = f"""
You are a senior software engineer.

Analyze the following bug.

Current Bug:

{query}

Historical Similar Bugs:

{evidence}

Based on the retrieved historical bugs,

return ONLY in the following format.

Root Cause:
...

Confidence Score:
...

Supporting Evidence:
...

Do not include any extra explanation.
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text