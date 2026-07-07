"""Learning file for I/O Practice: Bill Calculator."""

# Topic Name: I/O Practice: Bill Calculator
# Level: Beginner
# I/O Practice: Bill Calculator reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# I/O Practice: Bill Calculator reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Read name and marks, then print a formatted report.
# 2. Format a bill with currency and tax.
# 3. Handle empty input with a default value.

# Mini Project
# Build a tiny program that uses i/o practice: bill calculator
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does input() return?
# A1. It always returns a string.
# Q2. Why use formatted output?
# A2. Formatting makes reports predictable, readable, and easier to maintain.

# Examples and practice implementations start below.
def calculate_bill(price, quantity, tax_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax


def example_bill():
    total = calculate_bill(250, 2, 0.18)
    print(f"Bill total: Rs.{total:.2f}")


def practice_discounted_bill(price, quantity, discount):
    return price * quantity * (1 - discount)


def main():
    print("--- I/O Practice: Bill Calculator ---")
    example_bill()
    print(f"After discount: Rs.{practice_discounted_bill(100, 5, 0.10):.2f}")


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- I/O Practice: Bill Calculator ---
# Bill total: Rs.590.00
# After discount: Rs.450.00
# End Expected Output
