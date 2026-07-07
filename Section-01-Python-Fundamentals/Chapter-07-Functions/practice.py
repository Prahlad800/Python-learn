"""Learning file for Function Practice Programs."""

# Topic Name: Function Practice Programs
# Level: Beginner
# Function Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Function Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Create functions for add, subtract, multiply, and divide.
# 2. Refactor repeated code into reusable functions.
# 3. Write recursive and non-recursive solutions for factorial.

# Mini Project
# Build a tiny program that uses function practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why are functions important?
# A1. They make code reusable, testable, readable, and easier to change.
# Q2. What is recursion?
# A2. A function calling itself with a smaller problem until a base case is reached.

# Examples and practice implementations start below.
def add(left, right):
    return left + right


def divide(left, right):
    if right == 0:
        return "Cannot divide by zero"
    return left / right


def create_slug(title):
    return title.strip().lower().replace(" ", "-")


def practice_calculator(left, right, operator):
    if operator == "+":
        return add(left, right)
    if operator == "/":
        return divide(left, right)
    return "Unsupported operator"


def main():
    print("--- Function Practice Programs ---")
    print("Add:", add(10, 5))
    print("Slug:", create_slug(" Python Functions "))
    print("Calculator:", practice_calculator(10, 2, "/"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Function Practice Programs ---
# Add: 15
# Slug: python-functions
# Calculator: 5.0
# End Expected Output
