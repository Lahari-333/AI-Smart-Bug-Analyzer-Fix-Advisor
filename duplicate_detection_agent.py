from similarity_search import retrieve_similar_bugs


def duplicate_detection_agent(
    bug_title,
    bug_description,
    stack_trace
):

    query = f"""
Bug Title:
{bug_title}

Bug Description:
{bug_description}

Stack Trace:
{stack_trace}
"""

    similar_bugs = retrieve_similar_bugs(query, k=1)

    if not similar_bugs:
        return {
            "duplicate": False,
            "similarity_percentage": 0,
            "matched_bug": ""
        }

    top_bug = similar_bugs[0]

    # FAISS IndexFlatL2 returns DISTANCE
    distance = float(top_bug["similarity_score"])

    # Smaller distance = more similar
    #
    # For our current knowledge base:
    # distance <= 0.5 is treated as a strong match.
    is_duplicate = distance <= 0.5

    # Convert distance to an easy-to-read similarity value.
    similarity_percentage = max(
        0,
        min(100, (1 - distance) * 100)
    )

    return {
        "duplicate": is_duplicate,
        "similarity_percentage": round(
            similarity_percentage, 2
        ),
        "matched_bug": top_bug["bug_report"][:800]
    }