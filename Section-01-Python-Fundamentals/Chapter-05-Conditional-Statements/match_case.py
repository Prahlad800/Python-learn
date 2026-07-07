"""Learning file for match-case Statement."""

# Topic Name: match-case Statement
# Level: Intermediate
# match-case provides structural pattern matching for clean branching over values and shapes.
# Read the theory first, then run this file and modify examples.

# Theory
# match-case provides structural pattern matching for clean branching over values and shapes.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# match value:
#     case 'add':
#         ...
#     case _:
#         ...

# Practice Programs
# 1. Write a grade calculator.
# 2. Check eligibility for a discount.
# 3. Build a menu using match-case.

# Mini Project
# Build a tiny program that uses match-case statement
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When should you use elif?
# A1. Use elif when only one branch from several ordered choices should run.
# Q2. What is a truthy value?
# A2. A value that behaves like True in a boolean context.

# Examples and practice implementations start below.
def calculator(command, left, right):
    match command:
        case "add":
            return left + right
        case "subtract":
            return left - right
        case "multiply":
            return left * right
        case "divide" if right != 0:
            return left / right
        case "divide":
            return "Cannot divide by zero"
        case _:
            return "Unknown command"


def example_match_case():
    for command in ["add", "multiply", "divide"]:
        print(command, "->", calculator(command, 10, 2))


def practice_http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Other"


def main():
    print("--- match-case Statement ---")
    example_match_case()
    print("HTTP 404:", practice_http_status(404))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- match-case Statement ---
# add -> 12
# multiply -> 20
# divide -> 5.0
# HTTP 404: Not Found
# End Expected Output
