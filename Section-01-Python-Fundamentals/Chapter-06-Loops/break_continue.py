"""Learning file for break and continue."""

# Topic Name: break and continue
# Level: Beginner
# break exits a loop early; continue skips the current iteration and moves to the next one.
# Read the theory first, then run this file and modify examples.

# Theory
# break exits a loop early; continue skips the current iteration and moves to the next one.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# break
# continue
# for item in items: ...

# Practice Programs
# 1. Print multiplication tables.
# 2. Find the sum of digits of a number.
# 3. Print triangle and square patterns.

# Mini Project
# Build a tiny program that uses break and continue
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When do you use for instead of while?
# A1. Use for when iterating over a known iterable; use while when repeating until a condition changes.
# Q2. What does continue do?
# A2. It skips the rest of the current loop iteration.

# Examples and practice implementations start below.
def example_break():
    for number in range(1, 10):
        if number == 4:
            break
        print("Before break:", number)


def example_continue():
    for number in range(1, 6):
        if number % 2 == 0:
            continue
        print("Odd:", number)


def practice_first_negative(numbers):
    for number in numbers:
        if number < 0:
            return number
    return None


def main():
    print("--- break and continue ---")
    example_break()
    example_continue()
    print("First negative:", practice_first_negative([5, 3, -2, 8]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- break and continue ---
# Before break: 1
# Before break: 2
# Before break: 3
# Odd: 1
# Odd: 3
# Odd: 5
# First negative: -2
# End Expected Output
