"""Learning file for String Formatting Techniques."""

# Topic Name: String Formatting Techniques
# Level: Beginner
# String formatting controls alignment, precision, padding, and readable reports.
# Read the theory first, then run this file and modify examples.

# Theory
# String formatting controls alignment, precision, padding, and readable reports.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# f'{amount:,.2f}'
# '{:>10}'.format(text)
# f'{ratio:.1%}'

# Practice Programs
# 1. Clean and normalize user names.
# 2. Check whether a sentence is a palindrome after removing spaces.
# 3. Count words and characters in text.

# Mini Project
# Build a tiny program that uses string formatting techniques
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are strings mutable?
# A1. No. String methods return new strings instead of changing the original.
# Q2. What does slicing exclude?
# A2. The stop index is excluded from the result.

# Examples and practice implementations start below.
def example_alignment():
    print(f"{'Item':<10}{'Price':>8}")
    print(f"{'Book':<10}{249.5:>8.2f}")


def example_precision():
    pi = 3.14159265
    print(f"Pi: {pi:.3f}")
    print(f"Percent: {0.875:.1%}")


def practice_invoice_line(item, qty, price):
    return f"{item:<12}{qty:>3} x Rs.{price:>7.2f}"


def main():
    print("--- String Formatting Techniques ---")
    example_alignment()
    example_precision()
    print(practice_invoice_line("Pen", 3, 12.5))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- String Formatting Techniques ---
# Item         Price
# Book        249.50
# Pi: 3.142
# Percent: 87.5%
# Pen           3 x Rs.  12.50
# End Expected Output
