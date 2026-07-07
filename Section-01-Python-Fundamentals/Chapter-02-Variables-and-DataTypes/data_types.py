"""Learning file for Built-in Data Types."""

# Topic Name: Built-in Data Types
# Level: Beginner
# Python ships with built-in types for numbers, text, sequences, mappings, sets, booleans, and None.
# Read the theory first, then run this file and modify examples.

# Theory
# Python ships with built-in types for numbers, text, sequences, mappings, sets, booleans, and None.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# age = 21
# price = 99.5
# skills = ['Python', 'SQL']
# profile = {'name': 'Asha'}

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses built-in data types
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def example_builtin_types():
    samples = {
        "int": 10,
        "float": 10.5,
        "str": "Python",
        "bool": True,
        "list": [1, 2, 3],
        "tuple": ("x", "y"),
        "dict": {"course": "Python"},
        "set": {"red", "blue"},
        "none": None,
    }
    for name, value in samples.items():
        print(f"{name}: {type(value).__name__}")


def example_mutability():
    skills = ["Python"]
    skills.append("Git")
    print("Mutable list:", skills)


def practice_type_report(value):
    return f"{value!r} is {type(value).__name__}"


def main():
    print("--- Built-in Data Types ---")
    example_builtin_types()
    example_mutability()
    print(practice_type_report(3.14))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Built-in Data Types ---
# int: int
# float: float
# str: str
# bool: bool
# list: list
# tuple: tuple
# dict: dict
# set: set
# none: NoneType
# Mutable list: ['Python', 'Git']
# 3.14 is float
# End Expected Output
