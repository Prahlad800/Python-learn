"""Learning file for Tuple Practice Programs."""

# Topic Name: Tuple Practice Programs
# Level: Beginner
# Tuple Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Tuple Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Return multiple values from a function using a tuple.
# 2. Unpack coordinates into x and y variables.
# 3. Count repeated values in a tuple.

# Mini Project
# Build a tiny program that uses tuple practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use tuples?
# A1. Use tuples for fixed-size records, immutable data, and multiple return values.
# Q2. Can a tuple contain mutable objects?
# A2. Yes. The tuple binding is immutable, but a contained mutable object can change.

# Examples and practice implementations start below.
def coordinate_distance(point):
    x, y = point
    return (x ** 2 + y ** 2) ** 0.5


def swap_pair(pair):
    left, right = pair
    return right, left


def practice_student_tuple(name, marks):
    return name, marks, "Pass" if marks >= 40 else "Fail"


def main():
    print("--- Tuple Practice Programs ---")
    print("Distance:", round(coordinate_distance((3, 4)), 2))
    print("Swap:", swap_pair(("left", "right")))
    print("Student:", practice_student_tuple("Asha", 88))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Tuple Practice Programs ---
# Distance: 5.0
# Swap: ('right', 'left')
# Student: ('Asha', 88, 'Pass')
# End Expected Output
