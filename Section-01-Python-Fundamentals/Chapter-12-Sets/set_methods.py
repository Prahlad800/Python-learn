"""Learning file for Set Methods."""

# Topic Name: Set Methods
# Level: Beginner
# Set methods add, remove, compare, and copy unique collections.
# Read the theory first, then run this file and modify examples.

# Theory
# Set methods add, remove, compare, and copy unique collections.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# values.add(x)
# values.discard(x)
# values.copy()

# Practice Programs
# 1. Find common students between two clubs.
# 2. Remove duplicate emails from a list.
# 3. Compare required and submitted documents.

# Mini Project
# Build a tiny program that uses set methods
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What are sets optimized for?
# A1. Uniqueness and fast membership tests.
# Q2. Do sets preserve order?
# A2. Do not rely on set ordering; use a list when order matters.

# Examples and practice implementations start below.
def example_add_remove():
    skills = {"Python", "Git"}
    skills.add("SQL")
    skills.discard("Java")
    print("Skills:", skills)


def example_copy_clear():
    values = {1, 2, 3}
    copied = values.copy()
    copied.clear()
    print("Original:", values)
    print("Cleared copy:", copied)


def practice_missing_items(required, submitted):
    return set(required) - set(submitted)


def main():
    print("--- Set Methods ---")
    example_add_remove()
    example_copy_clear()
    print("Missing:", practice_missing_items(["id", "photo"], ["id"]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Set Methods ---
# Skills: {'Python', 'SQL', 'Git'}
# Original: {1, 2, 3}
# Cleared copy: set()
# Missing: {'photo'}
# End Expected Output
