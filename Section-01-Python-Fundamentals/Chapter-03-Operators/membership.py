"""Learning file for Membership Operators."""

# Topic Name: Membership Operators
# Level: Beginner
# Membership operators test whether a value exists inside a container such as a string, list, tuple, set, or dict keys.
# Read the theory first, then run this file and modify examples.

# Theory
# Membership operators test whether a value exists inside a container such as a string, list, tuple, set, or dict keys.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# item in collection
# item not in collection
# 'py' in 'python'

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses membership operators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
def example_membership():
    skills = ["Python", "Git", "SQL"]
    print("Python in skills:", "Python" in skills)
    print("Java not in skills:", "Java" not in skills)


def example_dictionary_membership():
    profile = {"name": "Asha", "role": "Developer"}
    print("'role' key exists:", "role" in profile)


def practice_vowel_check(letter):
    return letter.lower() in "aeiou"


def main():
    print("--- Membership Operators ---")
    example_membership()
    example_dictionary_membership()
    print("Is 'e' a vowel:", practice_vowel_check("e"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Membership Operators ---
# Python in skills: True
# Java not in skills: True
# 'role' key exists: True
# Is 'e' a vowel: True
# End Expected Output
