"""Learning file for Lambda Functions."""

# Topic Name: Lambda Functions
# Level: Intermediate
# Lambda functions are small anonymous functions commonly used with sorting, map, filter, and callbacks.
# Read the theory first, then run this file and modify examples.

# Theory
# Lambda functions are small anonymous functions commonly used with sorting, map, filter, and callbacks.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# lambda x: x * 2
# sorted(items, key=lambda item: item[1])

# Practice Programs
# 1. Create functions for add, subtract, multiply, and divide.
# 2. Refactor repeated code into reusable functions.
# 3. Write recursive and non-recursive solutions for factorial.

# Mini Project
# Build a tiny program that uses lambda functions
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why are functions important?
# A1. They make code reusable, testable, readable, and easier to change.
# Q2. What is recursion?
# A2. A function calling itself with a smaller problem until a base case is reached.

# Examples and practice implementations start below.
def example_lambda_map():
    numbers = [1, 2, 3]
    doubled = list(map(lambda value: value * 2, numbers))
    print("Doubled:", doubled)


def example_lambda_sort():
    students = [("Asha", 91), ("Ravi", 85), ("Meera", 98)]
    ranked = sorted(students, key=lambda item: item[1], reverse=True)
    print("Top student:", ranked[0])


def practice_filter_even(numbers):
    return list(filter(lambda value: value % 2 == 0, numbers))


def main():
    print("--- Lambda Functions ---")
    example_lambda_map()
    example_lambda_sort()
    print("Even:", practice_filter_even([1, 2, 3, 4, 5, 6]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Lambda Functions ---
# Doubled: [2, 4, 6]
# Top student: ('Meera', 98)
# Even: [2, 4, 6]
# End Expected Output
