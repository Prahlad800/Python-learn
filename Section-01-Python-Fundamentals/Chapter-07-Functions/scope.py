"""Learning file for Variable Scope."""

# Topic Name: Variable Scope
# Level: Intermediate
# Scope controls where names can be read or assigned; Python follows the LEGB lookup rule.
# Read the theory first, then run this file and modify examples.

# Theory
# Scope controls where names can be read or assigned; Python follows the LEGB lookup rule.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# local_name = value
# global name
# nonlocal name

# Practice Programs
# 1. Create functions for add, subtract, multiply, and divide.
# 2. Refactor repeated code into reusable functions.
# 3. Write recursive and non-recursive solutions for factorial.

# Mini Project
# Build a tiny program that uses variable scope
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why are functions important?
# A1. They make code reusable, testable, readable, and easier to change.
# Q2. What is recursion?
# A2. A function calling itself with a smaller problem until a base case is reached.

# Examples and practice implementations start below.
course = "Python"


def example_local_scope():
    course = "Data Science"
    print("Local:", course)


def example_global_scope():
    print("Global:", course)


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


def main():
    print("--- Variable Scope ---")
    example_local_scope()
    example_global_scope()
    counter = make_counter()
    print("Counter:", counter(), counter())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Variable Scope ---
# Local: Data Science
# Global: Python
# Counter: 1 2
# End Expected Output
