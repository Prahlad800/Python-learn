"""Learning file for Set Operations."""

# Topic Name: Set Operations
# Level: Intermediate
# Set operations compare groups using union, intersection, difference, and symmetric difference.
# Read the theory first, then run this file and modify examples.

# Theory
# Set operations compare groups using union, intersection, difference, and symmetric difference.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# a | b
# a & b
# a - b
# a ^ b

# Practice Programs
# 1. Find common students between two clubs.
# 2. Remove duplicate emails from a list.
# 3. Compare required and submitted documents.

# Mini Project
# Build a tiny program that uses set operations
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What are sets optimized for?
# A1. Uniqueness and fast membership tests.
# Q2. Do sets preserve order?
# A2. Do not rely on set ordering; use a list when order matters.

# Examples and practice implementations start below.
def example_operations():
    python_students = {"Asha", "Ravi", "Meera"}
    sql_students = {"Ravi", "Kiran"}
    print("Union:", python_students | sql_students)
    print("Intersection:", python_students & sql_students)
    print("Only Python:", python_students - sql_students)
    print("Symmetric difference:", python_students ^ sql_students)


def practice_jaccard(left, right):
    left_set = set(left)
    right_set = set(right)
    return len(left_set & right_set) / len(left_set | right_set)


def main():
    print("--- Set Operations ---")
    example_operations()
    print("Similarity:", round(practice_jaccard([1, 2, 3], [2, 3, 4]), 2))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Set Operations ---
# Union: {'Asha', 'Meera', 'Ravi', 'Kiran'}
# Intersection: {'Ravi'}
# Only Python: {'Asha', 'Meera'}
# Symmetric difference: {'Kiran', 'Asha', 'Meera'}
# Similarity: 0.5
# End Expected Output
