"""Learning file for List Comprehension."""

# Topic Name: List Comprehension
# Level: Intermediate
# List comprehensions build new lists from iterables in a compact, readable expression.
# Read the theory first, then run this file and modify examples.

# Theory
# List comprehensions build new lists from iterables in a compact, readable expression.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# [expression for item in iterable]
# [x for x in values if condition]

# Practice Programs
# 1. Create a marks list and calculate average marks.
# 2. Remove duplicates while preserving order.
# 3. Build a 3x3 matrix and print row totals.

# Mini Project
# Build a tiny program that uses list comprehension
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are lists mutable?
# A1. Yes. You can add, remove, and modify list items in place.
# Q2. What is a list comprehension?
# A2. A compact expression for building a new list from an iterable.

# Examples and practice implementations start below.
def example_squares():
    squares = [number ** 2 for number in range(1, 6)]
    print("Squares:", squares)


def example_filtering():
    even_numbers = [number for number in range(1, 11) if number % 2 == 0]
    print("Even:", even_numbers)


def practice_clean_names(names):
    return [name.strip().title() for name in names if name.strip()]


def main():
    print("--- List Comprehension ---")
    example_squares()
    example_filtering()
    print("Names:", practice_clean_names([" asha ", "", "ravi"]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- List Comprehension ---
# Squares: [1, 4, 9, 16, 25]
# Even: [2, 4, 6, 8, 10]
# Names: ['Asha', 'Ravi']
# End Expected Output
