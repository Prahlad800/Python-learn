"""Learning file for Arithmetic Operators."""

# Topic Name: Arithmetic Operators
# Level: Beginner
# Arithmetic operators calculate numeric results and are the foundation for formulas and algorithms.
# Read the theory first, then run this file and modify examples.

# Theory
# Arithmetic operators calculate numeric results and are the foundation for formulas and algorithms.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# a + b
# a - b
# a * b
# a / b
# a // b
# a % b
# a ** b

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses arithmetic operators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
def example_operations():
    a = 10
    b = 3
    print("addition:", a + b)
    print("subtraction:", a - b)
    print("multiplication:", a * b)
    print("division:", a / b)
    print("floor_division:", a // b)
    print("modulus:", a % b)
    print("power:", a ** b)


def practice_average(first, second, third):
    return (first + second + third) / 3


def main():
    print("--- Arithmetic Operators ---")
    example_operations()
    print("Average:", practice_average(80, 90, 100))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Arithmetic Operators ---
# addition: 13
# subtraction: 7
# multiplication: 30
# division: 3.3333333333333335
# floor_division: 3
# modulus: 1
# power: 1000
# Average: 90.0
# End Expected Output
