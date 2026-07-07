"""Learning file for Comparison Operators."""

# Topic Name: Comparison Operators
# Level: Beginner
# Comparison operators return booleans and drive filtering, validation, loops, and conditional logic.
# Read the theory first, then run this file and modify examples.

# Theory
# Comparison operators return booleans and drive filtering, validation, loops, and conditional logic.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# a == b
# a != b
# a > b
# a <= b

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses comparison operators
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
    print("equal:", a == b)
    print("not_equal:", a != b)
    print("greater:", a > b)
    print("less_or_equal:", a <= b)

def practice_in_range(value, low, high):
    return low <= value <= high


def main():
    print("--- Comparison Operators ---")
    example_operations()
    print("85 in range 0..100:", practice_in_range(85, 0, 100))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Comparison Operators ---
# equal: False
# not_equal: True
# greater: True
# less_or_equal: False
# 85 in range 0..100: True
# End Expected Output
