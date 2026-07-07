"""Learning file for Conditional Practice Programs."""

# Topic Name: Conditional Practice Programs
# Level: Beginner
# Conditional Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Conditional Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Write a grade calculator.
# 2. Check eligibility for a discount.
# 3. Build a menu using match-case.

# Mini Project
# Build a tiny program that uses conditional practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When should you use elif?
# A1. Use elif when only one branch from several ordered choices should run.
# Q2. What is a truthy value?
# A2. A value that behaves like True in a boolean context.

# Examples and practice implementations start below.
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def ticket_price(age):
    if age < 5:
        return 0
    if age <= 18:
        return 100
    if age >= 60:
        return 120
    return 180


def practice_largest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c


def main():
    print("--- Conditional Practice Programs ---")
    print("2024 leap year:", is_leap_year(2024))
    print("Ticket for age 16:", ticket_price(16))
    print("Largest:", practice_largest(7, 11, 3))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Conditional Practice Programs ---
# 2024 leap year: True
# Ticket for age 16: 100
# Largest: 11
# End Expected Output
