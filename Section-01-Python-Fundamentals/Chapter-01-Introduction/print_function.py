"""Learning file for The print() Function."""

# Topic Name: The print() Function
# Level: Beginner
# print() writes text representations of objects to standard output and is the first debugging tool beginners use.
# Read the theory first, then run this file and modify examples.

# Theory
# print() writes text representations of objects to standard output and is the first debugging tool beginners use.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# print(object)
# print(a, b, sep='-', end='!\n')
# print(value, file=stream)

# Practice Programs
# 1. Print your name, city, and learning goal.
# 2. Create a short script with a main() function.
# 3. Add comments that explain the purpose of each line.

# Mini Project
# Build a tiny program that uses the print() function
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why is Python popular?
# A1. It is readable, versatile, has a huge ecosystem, and supports many programming styles.
# Q2. What does the main guard do?
# A2. It lets code run only when the file is executed directly, not when imported.

# Examples and practice implementations start below.
from io import StringIO


def example_basic_print():
    print("Python", "is", "fun")


def example_sep_end():
    print("2026", "07", "07", sep="-")
    print("Loading", end="...")
    print("done")


def practice_redirect_output():
    buffer = StringIO()
    print("Saved to memory", file=buffer)
    return buffer.getvalue().strip()


def main():
    print("--- The print() Function ---")
    example_basic_print()
    example_sep_end()
    print("Captured:", practice_redirect_output())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- The print() Function ---
# Python is fun
# 2026-07-07
# Loading...done
# Captured: Saved to memory
# End Expected Output
