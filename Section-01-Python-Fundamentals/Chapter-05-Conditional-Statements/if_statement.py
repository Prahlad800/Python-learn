"""Learning file for if Statement."""

# Topic Name: if Statement
# Level: Beginner
# An if statement runs a block only when its condition is true.
# Read the theory first, then run this file and modify examples.

# Theory
# An if statement runs a block only when its condition is true.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# if condition:
#     statement

# Practice Programs
# 1. Write a grade calculator.
# 2. Check eligibility for a discount.
# 3. Build a menu using match-case.

# Mini Project
# Build a tiny program that uses if statement
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When should you use elif?
# A1. Use elif when only one branch from several ordered choices should run.
# Q2. What is a truthy value?
# A2. A value that behaves like True in a boolean context.

# Examples and practice implementations start below.
def example_if():
    temperature = 39
    if temperature > 37:
        print("Fever alert")


def example_truthy():
    username = "asha"
    if username:
        print("Username provided")


def practice_is_even(number):
    if number % 2 == 0:
        return True
    return False


def main():
    print("--- if Statement ---")
    example_if()
    example_truthy()
    print("12 is even:", practice_is_even(12))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- if Statement ---
# Fever alert
# Username provided
# 12 is even: True
# End Expected Output
