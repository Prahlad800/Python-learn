"""Learning file for List Practice Programs."""

# Topic Name: List Practice Programs
# Level: Beginner
# List Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# List Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Create a marks list and calculate average marks.
# 2. Remove duplicates while preserving order.
# 3. Build a 3x3 matrix and print row totals.

# Mini Project
# Build a tiny program that uses list practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are lists mutable?
# A1. Yes. You can add, remove, and modify list items in place.
# Q2. What is a list comprehension?
# A2. A compact expression for building a new list from an iterable.

# Examples and practice implementations start below.
def second_largest(values):
    unique_values = sorted(set(values))
    return unique_values[-2]


def rotate_left(values):
    return values[1:] + values[:1]


def practice_flatten(matrix):
    return [value for row in matrix for value in row]


def main():
    print("--- List Practice Programs ---")
    print("Second largest:", second_largest([10, 5, 20, 20, 8]))
    print("Rotated:", rotate_left([1, 2, 3, 4]))
    print("Flatten:", practice_flatten([[1, 2], [3, 4]]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- List Practice Programs ---
# Second largest: 10
# Rotated: [2, 3, 4, 1]
# Flatten: [1, 2, 3, 4]
# End Expected Output
