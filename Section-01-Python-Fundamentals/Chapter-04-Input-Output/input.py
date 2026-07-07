"""Learning file for Input Handling."""

# Topic Name: Input Handling
# Level: Beginner
# Robust input handling means reading strings, stripping whitespace, converting types, and validating bad data.
# Read the theory first, then run this file and modify examples.

# Theory
# Robust input handling means reading strings, stripping whitespace, converting types, and validating bad data.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# raw = input('Enter number: ')
# number = int(raw)
# if raw.strip(): ...

# Practice Programs
# 1. Read name and marks, then print a formatted report.
# 2. Format a bill with currency and tax.
# 3. Handle empty input with a default value.

# Mini Project
# Build a tiny program that uses input handling
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does input() return?
# A1. It always returns a string.
# Q2. Why use formatted output?
# A2. Formatting makes reports predictable, readable, and easier to maintain.

# Examples and practice implementations start below.
def read_number(raw_text):
    cleaned = raw_text.strip()
    if cleaned.lstrip("-").isdigit():
        return int(cleaned)
    raise ValueError("Input must be an integer.")


def example_validation():
    for raw in [" 42 ", "-7"]:
        print(f"{raw!r} ->", read_number(raw))


def practice_default_name(raw_name):
    return raw_name.strip() or "Guest"


def main():
    print("--- Input Handling ---")
    example_validation()
    print("Name:", practice_default_name("   "))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Input Handling ---
# ' 42 ' -> 42
# '-7' -> -7
# Name: Guest
# End Expected Output
