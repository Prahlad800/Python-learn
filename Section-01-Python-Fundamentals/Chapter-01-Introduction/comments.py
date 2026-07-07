"""Learning file for Comments and Docstrings."""

# Topic Name: Comments and Docstrings
# Level: Beginner
# Comments explain why code exists; docstrings document modules, classes, and functions for tools and teammates.
# Read the theory first, then run this file and modify examples.

# Theory
# Comments explain why code exists; docstrings document modules, classes, and functions for tools and teammates.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # Single-line comment
# """Multi-line docstring"""
# def function(): ...

# Practice Programs
# 1. Print your name, city, and learning goal.
# 2. Create a short script with a main() function.
# 3. Add comments that explain the purpose of each line.

# Mini Project
# Build a tiny program that uses comments and docstrings
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why is Python popular?
# A1. It is readable, versatile, has a huge ecosystem, and supports many programming styles.
# Q2. What does the main guard do?
# A2. It lets code run only when the file is executed directly, not when imported.

# Examples and practice implementations start below.
def calculate_area(length, width):
    """Return the area of a rectangle."""
    # Multiplication is used because rectangle area is length times width.
    return length * width


def example_inline_comment():
    tax_rate = 0.18  # GST-like example rate used for demonstration.
    print("Tax rate:", tax_rate)


def practice_documented_function(number):
    """Return True when number is even."""
    return number % 2 == 0


def main():
    print("--- Comments and Docstrings ---")
    print("Area:", calculate_area(5, 4))
    example_inline_comment()
    print("10 is even:", practice_documented_function(10))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Comments and Docstrings ---
# Area: 20
# Tax rate: 0.18
# 10 is even: True
# End Expected Output
