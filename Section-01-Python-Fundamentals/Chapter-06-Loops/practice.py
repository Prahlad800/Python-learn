"""Learning file for Loop Practice Programs."""

# Topic Name: Loop Practice Programs
# Level: Beginner
# Loop Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Loop Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Print multiplication tables.
# 2. Find the sum of digits of a number.
# 3. Print triangle and square patterns.

# Mini Project
# Build a tiny program that uses loop practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When do you use for instead of while?
# A1. Use for when iterating over a known iterable; use while when repeating until a condition changes.
# Q2. What does continue do?
# A2. It skips the rest of the current loop iteration.

# Examples and practice implementations start below.
def multiplication_table(number, limit):
    return [number * value for value in range(1, limit + 1)]


def count_vowels(text):
    total = 0
    for char in text.lower():
        if char in "aeiou":
            total += 1
    return total


def practice_factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main():
    print("--- Loop Practice Programs ---")
    print("Table:", multiplication_table(5, 5))
    print("Vowels:", count_vowels("Python is readable"))
    print("Factorial:", practice_factorial(5))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Loop Practice Programs ---
# Table: [5, 10, 15, 20, 25]
# Vowels: 6
# Factorial: 120
# End Expected Output
