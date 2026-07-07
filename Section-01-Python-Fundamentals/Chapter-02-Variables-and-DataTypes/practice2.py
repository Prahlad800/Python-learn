"""Learning file for Data Type Practice."""

# Topic Name: Data Type Practice
# Level: Beginner
# Data Type Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Data Type Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses data type practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def describe_values(values):
    return [type(value).__name__ for value in values]


def split_profile():
    return {
        "name": "Asha",
        "skills": ["Python", "Git"],
        "active": True,
    }


def practice_mutable_copy(values):
    copied = values.copy()
    copied.append("new")
    return values, copied


def main():
    print("--- Data Type Practice ---")
    print(describe_values([1, 2.5, "py", True]))
    print(split_profile())
    print("Copy:", practice_mutable_copy(["old"]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Data Type Practice ---
# ['int', 'float', 'str', 'bool']
# {'name': 'Asha', 'skills': ['Python', 'Git'], 'active': True}
# Copy: (['old'], ['old', 'new'])
# End Expected Output
