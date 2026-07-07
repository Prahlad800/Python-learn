"""Learning file for Logical Operators."""

# Topic Name: Logical Operators
# Level: Beginner
# Logical operators combine boolean expressions and short-circuit when the result is already known.
# Read the theory first, then run this file and modify examples.

# Theory
# Logical operators combine boolean expressions and short-circuit when the result is already known.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# condition_a and condition_b
# condition_a or condition_b
# not condition

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses logical operators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
def example_boolean_logic():
    age = 22
    has_id = True
    print("Can enter:", age >= 18 and has_id)
    print("Needs help:", age < 18 or not has_id)
    print("Not blocked:", not False)


def example_short_circuit():
    username = ""
    display_name = username or "Guest"
    print("Display name:", display_name)


def practice_discount(is_member, cart_total):
    return is_member and cart_total >= 1000


def main():
    print("--- Logical Operators ---")
    example_boolean_logic()
    example_short_circuit()
    print("Discount eligible:", practice_discount(True, 1200))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Logical Operators ---
# Can enter: True
# Needs help: False
# Not blocked: True
# Display name: Guest
# Discount eligible: True
# End Expected Output
