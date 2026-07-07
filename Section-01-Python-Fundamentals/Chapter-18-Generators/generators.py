"""Learning file for Generators."""

# Topic Name: Generators
# Level: Advanced
# Generators produce values lazily, saving memory for large or infinite sequences.
# Read the theory first, then run this file and modify examples.

# Theory
# Generators produce values lazily, saving memory for large or infinite sequences.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# def numbers():
#     yield value

# Practice Programs
# 1. Generate even numbers lazily.
# 2. Read a large file line by line using a generator.
# 3. Compare a list comprehension with a generator expression.

# Mini Project
# Build a tiny program that uses generators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why use generators?
# A1. They produce values lazily and can save memory.
# Q2. What does yield do?
# A2. It returns a value and pauses the function state until the next iteration.

# Examples and practice implementations start below.
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1


def example_generator():
    print("Numbers:", list(count_up_to(5)))


def practice_even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


def main():
    print("--- Generators ---")
    example_generator()
    print("Even:", list(practice_even_numbers(10)))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Generators ---
# Numbers: [1, 2, 3, 4, 5]
# Even: [2, 4, 6, 8, 10]
# End Expected Output
