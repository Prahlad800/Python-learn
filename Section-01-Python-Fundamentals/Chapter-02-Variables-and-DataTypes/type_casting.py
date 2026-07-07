"""Learning file for Type Casting."""

# Topic Name: Type Casting
# Level: Beginner
# Type casting converts values between compatible types such as strings, integers, floats, lists, and tuples.
# Read the theory first, then run this file and modify examples.

# Theory
# Type casting converts values between compatible types such as strings, integers, floats, lists, and tuples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# int('42')
# float('3.14')
# str(100)
# list(('a', 'b'))

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses type casting
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def example_numeric_casting():
    quantity = int("5")
    price = float("19.99")
    print("Total:", quantity * price)


def example_collection_casting():
    letters = tuple("abc")
    numbers = list((1, 2, 3))
    print("Tuple:", letters)
    print("List:", numbers)


def practice_safe_int(text, default=0):
    return int(text) if text.strip().isdigit() else default


def main():
    print("--- Type Casting ---")
    example_numeric_casting()
    example_collection_casting()
    print("Safe int:", practice_safe_int("42"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Type Casting ---
# Total: 99.94999999999999
# Tuple: ('a', 'b', 'c')
# List: [1, 2, 3]
# Safe int: 42
# End Expected Output
