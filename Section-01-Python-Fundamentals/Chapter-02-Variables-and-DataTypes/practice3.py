"""Learning file for Casting Practice."""

# Topic Name: Casting Practice
# Level: Beginner
# Casting Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Casting Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses casting practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def parse_prices(raw_prices):
    return [float(price) for price in raw_prices]


def join_numbers(numbers):
    return ", ".join(str(number) for number in numbers)


def practice_bool_cast(values):
    return [bool(value) for value in values]


def main():
    print("--- Casting Practice ---")
    print("Prices:", parse_prices(["10.5", "20"]))
    print("Joined:", join_numbers([1, 2, 3]))
    print("Booleans:", practice_bool_cast(["", "Python", 0, 7]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Casting Practice ---
# Prices: [10.5, 20.0]
# Joined: 1, 2, 3
# Booleans: [False, True, False, True]
# End Expected Output
