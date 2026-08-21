from knowledge_base_growth import add_resolved_bug


bug = """
Application crashes during login because the User object
is returned as null from the repository.
"""

resolution = """
Added validation for the repository response and handled
the missing User object using Optional<User>.
"""


result = add_resolved_bug(bug, resolution)

print(result)