"""Learning file for Operators Practice."""

# Topic Name: Operators Practice
# Level: Beginner
# Operators Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Operators Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses operators practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
def calculator(left, right):
    return {
        "add": left + right,
        "subtract": left - right,
        "multiply": left * right,
        "divide": left / right,
    }


def eligibility(age, has_id):
    return age >= 18 and has_id


def practice_even_and_positive(number):
    return number > 0 and number % 2 == 0


def main():
    print("--- Operators Practice ---")
    print(calculator(10, 2))
    print("Eligible:", eligibility(20, True))
    print("Even positive:", practice_even_and_positive(12))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Operators Practice ---
# {'add': 12, 'subtract': 8, 'multiply': 20, 'divide': 5.0}
# Eligible: True
# Even positive: True
# End Expected Output
