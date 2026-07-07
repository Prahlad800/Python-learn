"""Learning file for for Loop."""

# Topic Name: for Loop
# Level: Beginner
# for loops iterate over ranges, strings, lists, dictionaries, files, and any iterable object.
# Read the theory first, then run this file and modify examples.

# Theory
# for loops iterate over ranges, strings, lists, dictionaries, files, and any iterable object.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# for item in iterable:
# for index, value in enumerate(items):
# for number in range(5):

# Practice Programs
# 1. Print multiplication tables.
# 2. Find the sum of digits of a number.
# 3. Print triangle and square patterns.

# Mini Project
# Build a tiny program that uses for loop
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When do you use for instead of while?
# A1. Use for when iterating over a known iterable; use while when repeating until a condition changes.
# Q2. What does continue do?
# A2. It skips the rest of the current loop iteration.

# Examples and practice implementations start below.
def example_range_loop():
    for number in range(1, 4):
        print("Number:", number)


def example_enumerate():
    skills = ["Python", "Git", "SQL"]
    for index, skill in enumerate(skills, start=1):
        print(f"{index}. {skill}")


def practice_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def main():
    print("--- for Loop ---")
    example_range_loop()
    example_enumerate()
    print("Total:", practice_total([10, 20, 30]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- for Loop ---
# Number: 1
# Number: 2
# Number: 3
# 1. Python
# 2. Git
# 3. SQL
# Total: 60
# End Expected Output
