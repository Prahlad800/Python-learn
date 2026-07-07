"""Learning file for Modules."""

# Topic Name: Modules
# Level: Intermediate
# Modules split Python programs into reusable files and namespaces.
# Read the theory first, then run this file and modify examples.

# Theory
# Modules split Python programs into reusable files and namespaces.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# import math
# from pathlib import Path
# import module as alias

# Practice Programs
# 1. Move helper functions into a custom module.
# 2. Use built-in modules to calculate dates and statistics.
# 3. Explain why packages need clear module boundaries.

# Mini Project
# Build a tiny program that uses modules
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why split code into modules?
# A1. Modules make code reusable, organized, and easier to test.
# Q2. What is a package?
# A2. A package is a folder of related modules that can be imported together.

# Examples and practice implementations start below.
import math
from pathlib import Path


def example_import_math():
    print("Square root:", math.sqrt(49))
    print("Ceiling:", math.ceil(4.2))


def example_module_namespace():
    current_file = Path(__file__).name
    print("Current module file:", current_file)


def practice_circle_area(radius):
    return math.pi * radius ** 2


def main():
    print("--- Modules ---")
    example_import_math()
    example_module_namespace()
    print("Area:", round(practice_circle_area(3), 2))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Modules ---
# Square root: 7.0
# Ceiling: 5
# Current module file: modules.py
# Area: 28.27
# End Expected Output
