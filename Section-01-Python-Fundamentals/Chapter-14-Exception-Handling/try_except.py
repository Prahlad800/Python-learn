"""Learning file for try-except."""

# Topic Name: try-except
# Level: Beginner
# try-except handles errors gracefully so the program can recover or show a helpful message.
# Read the theory first, then run this file and modify examples.

# Theory
# try-except handles errors gracefully so the program can recover or show a helpful message.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# try:
#     risky_code()
# except ValueError as error:
#     handle(error)

# Practice Programs
# 1. Handle invalid integer input.
# 2. Raise an error for negative age.
# 3. Create a custom exception for low account balance.

# Mini Project
# Build a tiny program that uses try-except
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Should you catch bare Exception everywhere?
# A1. No. Catch specific exceptions so unrelated bugs are not hidden.
# Q2. When should you raise exceptions?
# A2. Raise when a function cannot complete its contract with the given data.

# Examples and practice implementations start below.
def parse_int(raw_text):
    try:
        return int(raw_text)
    except ValueError:
        return None


def example_try_except():
    for raw in ["42", "oops"]:
        print(raw, "->", parse_int(raw))


def practice_divide(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return "Cannot divide by zero"


def main():
    print("--- try-except ---")
    example_try_except()
    print("Divide:", practice_divide(10, 0))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- try-except ---
# 42 -> 42
# oops -> None
# Divide: Cannot divide by zero
# End Expected Output
