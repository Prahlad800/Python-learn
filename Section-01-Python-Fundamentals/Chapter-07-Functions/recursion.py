"""Learning file for Recursion."""

# Topic Name: Recursion
# Level: Intermediate
# Recursion solves a problem by reducing it into smaller versions of itself with a clear base case.
# Read the theory first, then run this file and modify examples.

# Theory
# Recursion solves a problem by reducing it into smaller versions of itself with a clear base case.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# def solve(n):
#     if base_case: return value
#     return solve(smaller_n)

# Practice Programs
# 1. Create functions for add, subtract, multiply, and divide.
# 2. Refactor repeated code into reusable functions.
# 3. Write recursive and non-recursive solutions for factorial.

# Mini Project
# Build a tiny program that uses recursion
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why are functions important?
# A1. They make code reusable, testable, readable, and easier to change.
# Q2. What is recursion?
# A2. A function calling itself with a smaller problem until a base case is reached.

# Examples and practice implementations start below.
def factorial(number):
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def countdown(number):
    if number == 0:
        return ["Go"]
    return [str(number)] + countdown(number - 1)


def practice_sum_numbers(number):
    if number == 0:
        return 0
    return number + practice_sum_numbers(number - 1)


def main():
    print("--- Recursion ---")
    print("5!:", factorial(5))
    print("Countdown:", countdown(3))
    print("Sum 1..5:", practice_sum_numbers(5))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Recursion ---
# 5!: 120
# Countdown: ['3', '2', '1', 'Go']
# Sum 1..5: 15
# End Expected Output
