"""Learning file for Functions."""

# Topic Name: Functions
# Level: Beginner
# Functions package reusable logic, reduce duplication, and make programs easier to test.
# Read the theory first, then run this file and modify examples.

# Theory
# Functions package reusable logic, reduce duplication, and make programs easier to test.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# def name(parameters):
#     return value
# result = name(arguments)

# Practice Programs
# 1. Create functions for add, subtract, multiply, and divide.
# 2. Refactor repeated code into reusable functions.
# 3. Write recursive and non-recursive solutions for factorial.

# Mini Project
# Build a tiny program that uses functions
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why are functions important?
# A1. They make code reusable, testable, readable, and easier to change.
# Q2. What is recursion?
# A2. A function calling itself with a smaller problem until a base case is reached.

# Examples and practice implementations start below.
def greet(name):
    return f"Hello, {name}!"


def calculate_area(length, width):
    return length * width


def practice_is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def main():
    print("--- Functions ---")
    print(greet("Asha"))
    print("Area:", calculate_area(5, 4))
    print("11 is prime:", practice_is_prime(11))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Functions ---
# Hello, Asha!
# Area: 20
# 11 is prime: True
# End Expected Output
