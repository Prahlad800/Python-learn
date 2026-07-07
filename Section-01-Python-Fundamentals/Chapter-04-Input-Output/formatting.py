"""Learning file for String Formatting."""

# Topic Name: String Formatting
# Level: Beginner
# format() and percent formatting let you build strings with placeholders and formatted numeric values.
# Read the theory first, then run this file and modify examples.

# Theory
# format() and percent formatting let you build strings with placeholders and formatted numeric values.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# '{} scored {}'.format(name, marks)
# '{name}: {marks}'.format(name='Asha', marks=91)
# '%.2f' % price

# Practice Programs
# 1. Read name and marks, then print a formatted report.
# 2. Format a bill with currency and tax.
# 3. Handle empty input with a default value.

# Mini Project
# Build a tiny program that uses string formatting
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does input() return?
# A1. It always returns a string.
# Q2. Why use formatted output?
# A2. Formatting makes reports predictable, readable, and easier to maintain.

# Examples and practice implementations start below.
def example_format_method():
    name = "Asha"
    score = 91.567
    print("{} scored {:.1f}%".format(name, score))


def example_named_placeholders():
    print("{city} temperature: {temp}C".format(city="Delhi", temp=32))


def practice_percent_format(price, quantity):
    return "Total: %.2f" % (price * quantity)


def main():
    print("--- String Formatting ---")
    example_format_method()
    example_named_placeholders()
    print(practice_percent_format(19.99, 3))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- String Formatting ---
# Asha scored 91.6%
# Delhi temperature: 32C
# Total: 59.97
# End Expected Output
