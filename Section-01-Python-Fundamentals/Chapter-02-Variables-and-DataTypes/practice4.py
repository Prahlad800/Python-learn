"""Learning file for Input Practice."""

# Topic Name: Input Practice
# Level: Beginner
# Input Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Input Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses input practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def normalize_name(raw_name):
    return raw_name.strip().title()


def parse_marks(raw_marks):
    marks = int(raw_marks)
    return max(0, min(100, marks))


def practice_profile_from_input(raw_name, raw_marks):
    return {
        "name": normalize_name(raw_name),
        "marks": parse_marks(raw_marks),
    }


def main():
    print("--- Input Practice ---")
    print(normalize_name("  asha rao "))
    print("Marks:", parse_marks("105"))
    print(practice_profile_from_input(" ravi ", "78"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Input Practice ---
# Asha Rao
# Marks: 100
# {'name': 'Ravi', 'marks': 78}
# End Expected Output
