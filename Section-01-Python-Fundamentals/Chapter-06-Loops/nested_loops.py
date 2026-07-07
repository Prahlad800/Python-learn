"""Learning file for Nested Loops."""

# Topic Name: Nested Loops
# Level: Beginner
# Nested loops solve grid, table, matrix, and pair-comparison problems.
# Read the theory first, then run this file and modify examples.

# Theory
# Nested loops solve grid, table, matrix, and pair-comparison problems.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# for row in rows:
#     for column in columns:
#         ...

# Practice Programs
# 1. Print multiplication tables.
# 2. Find the sum of digits of a number.
# 3. Print triangle and square patterns.

# Mini Project
# Build a tiny program that uses nested loops
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When do you use for instead of while?
# A1. Use for when iterating over a known iterable; use while when repeating until a condition changes.
# Q2. What does continue do?
# A2. It skips the rest of the current loop iteration.

# Examples and practice implementations start below.
def example_multiplication_table(size):
    for row in range(1, size + 1):
        values = []
        for column in range(1, size + 1):
            values.append(row * column)
        print(values)


def example_pairs():
    colors = ["red", "blue"]
    sizes = ["S", "M"]
    for color in colors:
        for size in sizes:
            print(f"{color}-{size}")


def practice_matrix_total(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total


def main():
    print("--- Nested Loops ---")
    example_multiplication_table(3)
    example_pairs()
    print("Matrix total:", practice_matrix_total([[1, 2], [3, 4]]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Nested Loops ---
# [1, 2, 3]
# [2, 4, 6]
# [3, 6, 9]
# red-S
# red-M
# blue-S
# blue-M
# Matrix total: 10
# End Expected Output
