"""Learning file for Tuples."""

# Topic Name: Tuples
# Level: Beginner
# Tuples store ordered, immutable collections and are useful for fixed records and safe returns.
# Read the theory first, then run this file and modify examples.

# Theory
# Tuples store ordered, immutable collections and are useful for fixed records and safe returns.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# point = (10, 20)
# single = ('Python',)
# point[0]

# Practice Programs
# 1. Return multiple values from a function using a tuple.
# 2. Unpack coordinates into x and y variables.
# 3. Count repeated values in a tuple.

# Mini Project
# Build a tiny program that uses tuples
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use tuples?
# A1. Use tuples for fixed-size records, immutable data, and multiple return values.
# Q2. Can a tuple contain mutable objects?
# A2. Yes. The tuple binding is immutable, but a contained mutable object can change.

# Examples and practice implementations start below.
def example_tuple_record():
    point = (10, 20)
    print("x:", point[0])
    print("y:", point[1])


def example_immutable():
    roles = ("admin", "editor", "viewer")
    print("Roles:", roles)


def practice_min_max(values):
    return min(values), max(values)


def main():
    print("--- Tuples ---")
    example_tuple_record()
    example_immutable()
    print("Min/Max:", practice_min_max((5, 9, 1, 3)))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Tuples ---
# x: 10
# y: 20
# Roles: ('admin', 'editor', 'viewer')
# Min/Max: (1, 9)
# End Expected Output
