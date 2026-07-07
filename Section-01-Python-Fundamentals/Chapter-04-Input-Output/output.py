"""Learning file for Output Handling."""

# Topic Name: Output Handling
# Level: Beginner
# Output handling includes printing clean messages, controlling separators, endings, and redirecting output.
# Read the theory first, then run this file and modify examples.

# Theory
# Output handling includes printing clean messages, controlling separators, endings, and redirecting output.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# print('Saved')
# print('A', 'B', sep=' | ')
# print('Loading', end='...')

# Practice Programs
# 1. Read name and marks, then print a formatted report.
# 2. Format a bill with currency and tax.
# 3. Handle empty input with a default value.

# Mini Project
# Build a tiny program that uses output handling
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does input() return?
# A1. It always returns a string.
# Q2. Why use formatted output?
# A2. Formatting makes reports predictable, readable, and easier to maintain.

# Examples and practice implementations start below.
from io import StringIO


def example_separators():
    print("Asha", "Python", "95", sep=" | ")


def example_output_stream():
    stream = StringIO()
    print("line written to stream", file=stream)
    print("Stream value:", stream.getvalue().strip())


def practice_receipt(item, price):
    return f"{item:<10} Rs.{price:>7.2f}"


def main():
    print("--- Output Handling ---")
    example_separators()
    example_output_stream()
    print(practice_receipt("Book", 249.5))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Output Handling ---
# Asha | Python | 95
# Stream value: line written to stream
# Book       Rs. 249.50
# End Expected Output
