"""Learning file for Packing and Unpacking."""

# Topic Name: Packing and Unpacking
# Level: Intermediate
# Packing groups values into tuples; unpacking assigns iterable values to multiple names.
# Read the theory first, then run this file and modify examples.

# Theory
# Packing groups values into tuples; unpacking assigns iterable values to multiple names.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# packed = 10, 20, 30
# x, y, z = packed
# first, *middle, last = values

# Practice Programs
# 1. Return multiple values from a function using a tuple.
# 2. Unpack coordinates into x and y variables.
# 3. Count repeated values in a tuple.

# Mini Project
# Build a tiny program that uses packing and unpacking
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use tuples?
# A1. Use tuples for fixed-size records, immutable data, and multiple return values.
# Q2. Can a tuple contain mutable objects?
# A2. Yes. The tuple binding is immutable, but a contained mutable object can change.

# Examples and practice implementations start below.
def example_packing():
    student = "Asha", 21, "Python"
    print("Packed:", student)


def example_unpacking():
    name, age, course = ("Asha", 21, "Python")
    print(f"{name} | {age} | {course}")


def practice_star_unpack(values):
    first, *middle, last = values
    return first, middle, last


def main():
    print("--- Packing and Unpacking ---")
    example_packing()
    example_unpacking()
    print("Star unpack:", practice_star_unpack([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Packing and Unpacking ---
# Packed: ('Asha', 21, 'Python')
# Asha | 21 | Python
# Star unpack: (1, [2, 3, 4], 5)
# End Expected Output
