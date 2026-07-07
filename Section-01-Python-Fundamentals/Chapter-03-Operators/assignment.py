"""Learning file for Assignment Operators."""

# Topic Name: Assignment Operators
# Level: Beginner
# Assignment operators bind or update variables, often combining an operation with reassignment.
# Read the theory first, then run this file and modify examples.

# Theory
# Assignment operators bind or update variables, often combining an operation with reassignment.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# x = 10
# x += 5
# x *= 2
# x //= 3

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses assignment operators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
def example_assignment_updates():
    score = 10
    print("Initial:", score)
    score += 5
    print("After += 5:", score)
    score *= 2
    print("After *= 2:", score)
    score //= 3
    print("After //= 3:", score)


def example_multiple_assignment():
    name, age, active = "Asha", 21, True
    print(f"{name} | {age} | active={active}")


def practice_wallet(balance, deposit, withdrawal):
    balance += deposit
    balance -= withdrawal
    return balance


def main():
    print("--- Assignment Operators ---")
    example_assignment_updates()
    example_multiple_assignment()
    print("Wallet balance:", practice_wallet(1000, 250, 400))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Assignment Operators ---
# Initial: 10
# After += 5: 15
# After *= 2: 30
# After //= 3: 10
# Asha | 21 | active=True
# Wallet balance: 850
# End Expected Output
