"""Learning file for Built-in Modules."""

# Topic Name: Built-in Modules
# Level: Intermediate
# Built-in modules provide battle-tested functionality without installing external packages.
# Read the theory first, then run this file and modify examples.

# Theory
# Built-in modules provide battle-tested functionality without installing external packages.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# import math
# import statistics
# from datetime import date

# Practice Programs
# 1. Move helper functions into a custom module.
# 2. Use built-in modules to calculate dates and statistics.
# 3. Explain why packages need clear module boundaries.

# Mini Project
# Build a tiny program that uses built-in modules
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why split code into modules?
# A1. Modules make code reusable, organized, and easier to test.
# Q2. What is a package?
# A2. A package is a folder of related modules that can be imported together.

# Examples and practice implementations start below.
import math
import statistics
from datetime import date


def example_math_statistics():
    values = [10, 20, 30, 40]
    print("Mean:", statistics.mean(values))
    print("Hypotenuse:", math.hypot(3, 4))


def example_datetime():
    today = date(2026, 7, 7)
    print("ISO date:", today.isoformat())


def practice_population_std(values):
    return round(statistics.pstdev(values), 2)


def main():
    print("--- Built-in Modules ---")
    example_math_statistics()
    example_datetime()
    print("Std dev:", practice_population_std([2, 4, 4, 4, 5, 5, 7, 9]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Built-in Modules ---
# Mean: 25
# Hypotenuse: 5.0
# ISO date: 2026-07-07
# Std dev: 2.0
# End Expected Output
