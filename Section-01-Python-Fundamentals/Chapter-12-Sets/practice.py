"""Learning file for Set Practice Programs."""

# Topic Name: Set Practice Programs
# Level: Beginner
# Set Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Set Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Find common students between two clubs.
# 2. Remove duplicate emails from a list.
# 3. Compare required and submitted documents.

# Mini Project
# Build a tiny program that uses set practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What are sets optimized for?
# A1. Uniqueness and fast membership tests.
# Q2. Do sets preserve order?
# A2. Do not rely on set ordering; use a list when order matters.

# Examples and practice implementations start below.
def remove_duplicates(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def common_skills(team_a, team_b):
    return sorted(set(team_a) & set(team_b))


def practice_all_documents_submitted(required, submitted):
    return set(required).issubset(submitted)


def main():
    print("--- Set Practice Programs ---")
    print("Deduped:", remove_duplicates([1, 2, 1, 3]))
    print("Common:", common_skills(["Python", "Git"], ["Git", "SQL"]))
    print("Complete:", practice_all_documents_submitted({"id"}, {"id", "photo"}))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Set Practice Programs ---
# Deduped: [1, 2, 3]
# Common: ['Git']
# Complete: True
# End Expected Output
