"""Learning file for Identity Operators."""

# Topic Name: Identity Operators
# Level: Beginner
# Identity operators compare whether two names refer to the exact same object in memory.
# Read the theory first, then run this file and modify examples.

# Theory
# Identity operators compare whether two names refer to the exact same object in memory.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# a is b
# a is not b
# value is None

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses identity operators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
def example_identity():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print("a is b:", a is b)
    print("a is c:", a is c)
    print("a == c:", a == c)


def example_none_check():
    value = None
    print("Missing value:", value is None)


def practice_alias_check(left, right):
    return left is right


def main():
    print("--- Identity Operators ---")
    example_identity()
    example_none_check()
    shared = {"course": "Python"}
    print("Same object:", practice_alias_check(shared, shared))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Identity Operators ---
# a is b: True
# a is c: False
# a == c: True
# Missing value: True
# Same object: True
# End Expected Output
