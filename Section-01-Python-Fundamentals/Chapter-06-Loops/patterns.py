"""Learning file for Pattern Programs."""

# Topic Name: Pattern Programs
# Level: Beginner
# Pattern programs strengthen loop logic by printing structured shapes from repeated characters.
# Read the theory first, then run this file and modify examples.

# Theory
# Pattern programs strengthen loop logic by printing structured shapes from repeated characters.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# for row in range(1, n + 1):
#     print('*' * row)

# Practice Programs
# 1. Print multiplication tables.
# 2. Find the sum of digits of a number.
# 3. Print triangle and square patterns.

# Mini Project
# Build a tiny program that uses pattern programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When do you use for instead of while?
# A1. Use for when iterating over a known iterable; use while when repeating until a condition changes.
# Q2. What does continue do?
# A2. It skips the rest of the current loop iteration.

# Examples and practice implementations start below.
def right_triangle(rows):
    for row in range(1, rows + 1):
        print("*" * row)


def number_pattern(rows):
    for row in range(1, rows + 1):
        line = ""
        for number in range(1, row + 1):
            line += str(number)
        print(line)


def practice_square(size):
    return ["#" * size for _ in range(size)]


def main():
    print("--- Pattern Programs ---")
    right_triangle(3)
    number_pattern(3)
    print("Square:", practice_square(2))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Pattern Programs ---
# *
# **
# ***
# 1
# 12
# 123
# Square: ['##', '##']
# End Expected Output
