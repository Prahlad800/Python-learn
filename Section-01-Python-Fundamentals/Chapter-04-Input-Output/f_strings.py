"""Learning file for F-Strings."""

# Topic Name: F-Strings
# Level: Beginner
# F-strings are modern Python's most readable way to embed expressions inside strings.
# Read the theory first, then run this file and modify examples.

# Theory
# F-strings are modern Python's most readable way to embed expressions inside strings.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# f'{name} scored {marks}'
# f'{price:.2f}'
# f'{value=}'

# Practice Programs
# 1. Read name and marks, then print a formatted report.
# 2. Format a bill with currency and tax.
# 3. Handle empty input with a default value.

# Mini Project
# Build a tiny program that uses f-strings
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does input() return?
# A1. It always returns a string.
# Q2. Why use formatted output?
# A2. Formatting makes reports predictable, readable, and easier to maintain.

# Examples and practice implementations start below.
def example_f_string():
    name = "Asha"
    marks = 94
    print(f"{name} scored {marks} marks.")


def example_format_specs():
    price = 1234.5
    ratio = 0.875
    print(f"Price: Rs.{price:,.2f}")
    print(f"Success: {ratio:.1%}")


def practice_debug_value(value):
    return f"{value=}"


def main():
    print("--- F-Strings ---")
    example_f_string()
    example_format_specs()
    print(practice_debug_value(42))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- F-Strings ---
# Asha scored 94 marks.
# Price: Rs.1,234.50
# Success: 87.5%
# value=42
# End Expected Output
