"""Learning file for Variables."""

# Topic Name: Variables
# Level: Beginner
# Variables are names bound to objects; Python uses dynamic typing, so the object carries the type.
# Read the theory first, then run this file and modify examples.

# Theory
# Variables are names bound to objects; Python uses dynamic typing, so the object carries the type.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# name = value
# x, y = 10, 20
# name = new_value

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses variables
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def example_assignment():
    name = "Asha"
    age = 21
    print(f"{name} is {age} years old.")


def example_reassignment():
    score = 10
    score = score + 5
    print("Updated score:", score)


def practice_swap_values(left, right):
    left, right = right, left
    return left, right


def main():
    print("--- Variables ---")
    example_assignment()
    example_reassignment()
    print("Swapped:", practice_swap_values("first", "second"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Variables ---
# Asha is 21 years old.
# Updated score: 15
# Swapped: ('second', 'first')
# End Expected Output
