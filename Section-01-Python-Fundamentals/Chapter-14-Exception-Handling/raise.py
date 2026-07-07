"""Learning file for raise Statement."""

# Topic Name: raise Statement
# Level: Intermediate
# raise deliberately creates an exception when invalid data or impossible state is detected.
# Read the theory first, then run this file and modify examples.

# Theory
# raise deliberately creates an exception when invalid data or impossible state is detected.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# raise ValueError('message')
# raise TypeError('message')

# Practice Programs
# 1. Handle invalid integer input.
# 2. Raise an error for negative age.
# 3. Create a custom exception for low account balance.

# Mini Project
# Build a tiny program that uses raise statement
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Should you catch bare Exception everywhere?
# A1. No. Catch specific exceptions so unrelated bugs are not hidden.
# Q2. When should you raise exceptions?
# A2. Raise when a function cannot complete its contract with the given data.

# Examples and practice implementations start below.
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age


def example_raise():
    try:
        set_age(-1)
    except ValueError as error:
        print("Error:", error)


def practice_withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


def main():
    print("--- raise Statement ---")
    example_raise()
    print("Balance:", practice_withdraw(1000, 250))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- raise Statement ---
# Error: Age cannot be negative.
# Balance: 750
# End Expected Output
