"""Learning file for Function Arguments."""

# Topic Name: Function Arguments
# Level: Intermediate
# Arguments let callers pass data into functions using positional, keyword, default, variadic, and unpacked forms.
# Read the theory first, then run this file and modify examples.

# Theory
# Arguments let callers pass data into functions using positional, keyword, default, variadic, and unpacked forms.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# def greet(name='Learner'):
# def total(*numbers):
# def build(**options):

# Practice Programs
# 1. Create functions for add, subtract, multiply, and divide.
# 2. Refactor repeated code into reusable functions.
# 3. Write recursive and non-recursive solutions for factorial.

# Mini Project
# Build a tiny program that uses function arguments
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why are functions important?
# A1. They make code reusable, testable, readable, and easier to change.
# Q2. What is recursion?
# A2. A function calling itself with a smaller problem until a base case is reached.

# Examples and practice implementations start below.
def describe_student(name, course="Python", *, active=True):
    return f"{name} studies {course}; active={active}"


def total_marks(*marks):
    return sum(marks)


def build_profile(**details):
    return ", ".join(f"{key}={value}" for key, value in details.items())


def practice_average(*numbers):
    return sum(numbers) / len(numbers)


def main():
    print("--- Function Arguments ---")
    print(describe_student("Asha"))
    print("Total:", total_marks(80, 90, 95))
    print(build_profile(name="Prahlad", role="Learner"))
    print("Average:", practice_average(10, 20, 30))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Function Arguments ---
# Asha studies Python; active=True
# Total: 265
# name=Prahlad, role=Learner
# Average: 20.0
# End Expected Output
