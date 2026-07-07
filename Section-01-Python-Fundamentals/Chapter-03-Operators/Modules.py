"""Learning file for Operator Module Practice."""

# Topic Name: Operator Module Practice
# Level: Intermediate
# Operator Module Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Operator Module Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses operator module practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
import operator


def example_operator_functions():
    print("Add:", operator.add(10, 5))
    print("Multiply:", operator.mul(10, 5))
    print("Greater:", operator.gt(10, 5))


def example_sort_with_itemgetter():
    students = [("Asha", 92), ("Ravi", 85), ("Meera", 98)]
    ranked = sorted(students, key=operator.itemgetter(1), reverse=True)
    print("Top:", ranked[0])


def practice_apply(operation, left, right):
    operations = {"add": operator.add, "sub": operator.sub}
    return operations[operation](left, right)


def main():
    print("--- Operator Module Practice ---")
    example_operator_functions()
    example_sort_with_itemgetter()
    print("Apply:", practice_apply("sub", 10, 3))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Operator Module Practice ---
# Add: 15
# Multiply: 50
# Greater: True
# Top: ('Meera', 98)
# Apply: 7
# End Expected Output
