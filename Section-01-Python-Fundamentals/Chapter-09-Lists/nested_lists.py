"""Learning file for Nested Lists."""

# Topic Name: Nested Lists
# Level: Intermediate
# Nested lists represent tables, matrices, grids, and grouped records.
# Read the theory first, then run this file and modify examples.

# Theory
# Nested lists represent tables, matrices, grids, and grouped records.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# matrix[row][column]
# [[0 for col in range(3)] for row in range(2)]

# Practice Programs
# 1. Create a marks list and calculate average marks.
# 2. Remove duplicates while preserving order.
# 3. Build a 3x3 matrix and print row totals.

# Mini Project
# Build a tiny program that uses nested lists
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are lists mutable?
# A1. Yes. You can add, remove, and modify list items in place.
# Q2. What is a list comprehension?
# A2. A compact expression for building a new list from an iterable.

# Examples and practice implementations start below.
def example_matrix():
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("Element row 2 col 3:", matrix[1][2])
    for row in matrix:
        print("Row total:", sum(row))


def example_grid_creation():
    grid = [[0 for _ in range(3)] for _ in range(2)]
    print("Grid:", grid)


def practice_transpose(matrix):
    return [[row[index] for row in matrix] for index in range(len(matrix[0]))]


def main():
    print("--- Nested Lists ---")
    example_matrix()
    example_grid_creation()
    print("Transpose:", practice_transpose([[1, 2], [3, 4]]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Nested Lists ---
# Element row 2 col 3: 6
# Row total: 6
# Row total: 15
# Grid: [[0, 0, 0], [0, 0, 0]]
# Transpose: [[1, 3], [2, 4]]
# End Expected Output
