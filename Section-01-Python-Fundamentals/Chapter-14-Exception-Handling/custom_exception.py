"""Learning file for Custom Exceptions."""

# Topic Name: Custom Exceptions
# Level: Intermediate
# Custom exceptions name domain-specific problems and make error handling clearer.
# Read the theory first, then run this file and modify examples.

# Theory
# Custom exceptions name domain-specific problems and make error handling clearer.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# class AppError(Exception): pass
# raise AppError('message')

# Practice Programs
# 1. Handle invalid integer input.
# 2. Raise an error for negative age.
# 3. Create a custom exception for low account balance.

# Mini Project
# Build a tiny program that uses custom exceptions
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Should you catch bare Exception everywhere?
# A1. No. Catch specific exceptions so unrelated bugs are not hidden.
# Q2. When should you raise exceptions?
# A2. Raise when a function cannot complete its contract with the given data.

# Examples and practice implementations start below.
class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds available balance."""


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough money.")
    return balance - amount


def example_custom_exception():
    try:
        withdraw(500, 900)
    except InsufficientBalanceError as error:
        print("Custom error:", error)


def practice_validate_percentage(value):
    if not 0 <= value <= 100:
        raise ValueError("Percentage must be between 0 and 100.")
    return value


def main():
    print("--- Custom Exceptions ---")
    example_custom_exception()
    print("Percentage:", practice_validate_percentage(88))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Custom Exceptions ---
# Custom error: Not enough money.
# Percentage: 88
# End Expected Output
