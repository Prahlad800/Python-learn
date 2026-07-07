"""Learning file for while Loop."""

# Topic Name: while Loop
# Level: Beginner
# while loops continue until a condition becomes false and are useful when the number of repeats is unknown.
# Read the theory first, then run this file and modify examples.

# Theory
# while loops continue until a condition becomes false and are useful when the number of repeats is unknown.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# while condition:
#     update_condition

# Practice Programs
# 1. Print multiplication tables.
# 2. Find the sum of digits of a number.
# 3. Print triangle and square patterns.

# Mini Project
# Build a tiny program that uses while loop
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When do you use for instead of while?
# A1. Use for when iterating over a known iterable; use while when repeating until a condition changes.
# Q2. What does continue do?
# A2. It skips the rest of the current loop iteration.

# Examples and practice implementations start below.
def example_countdown():
    count = 3
    while count > 0:
        print("Count:", count)
        count -= 1


def example_find_power(limit):
    value = 1
    while value < limit:
        value *= 2
    print("First power of two >= limit:", value)


def practice_sum_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def main():
    print("--- while Loop ---")
    example_countdown()
    example_find_power(20)
    print("Digit sum:", practice_sum_digits(1234))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- while Loop ---
# Count: 3
# Count: 2
# Count: 1
# First power of two >= limit: 32
# Digit sum: 10
# End Expected Output
