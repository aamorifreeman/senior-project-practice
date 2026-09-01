"""Senior Project — student developer profile.

Prints a short profile card describing who I am, what I study,
the area of technology I'm most interested in, and the skill I
want to strengthen during Senior Project.
"""

NAME = "Aamori Freeman"
MAJOR = "Computer Science (Mathematics minor)"
TECHNOLOGY_INTEREST = "DevOps and Cloud Infrastructure"
SKILL_GOAL = "End-to-End System Design and Deployment"


def build_profile() -> str:
    """Return the formatted developer profile as a single string."""
    lines = [
        "Senior Project Developer Profile",
        "-" * 32,
        f"Name: {NAME}",
        f"Major: {MAJOR}",
        f"Technology Interest: {TECHNOLOGY_INTEREST}",
        f"Skill Goal: {SKILL_GOAL}",
    ]
    return "\n".join(lines)


def main() -> None:
    print(build_profile())


if __name__ == "__main__":
    main()
