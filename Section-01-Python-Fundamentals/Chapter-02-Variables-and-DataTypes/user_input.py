"""Learning file for User Input."""

# Topic Name: User Input
# Level: Beginner
# input() reads text from the keyboard; production code validates and converts that text before using it.
# Read the theory first, then run this file and modify examples.

# Theory
# input() reads text from the keyboard; production code validates and converts that text before using it.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# name = input('Name: ')
# age = int(input('Age: '))
# value.strip()

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses user input
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def parse_age(raw_age):
    cleaned = raw_age.strip()
    if not cleaned.isdigit():
        return None
    return int(cleaned)


def example_simulated_input():
    raw_name = "  Asha  "
    raw_age = " 21 "
    name = raw_name.strip()
    age = parse_age(raw_age)
    print(f"{name} is {age} years old.")


def practice_create_username(first_name, year):
    return f"{first_name.strip().lower()}{int(year)}"


def main():
    print("--- User Input ---")
    example_simulated_input()
    print("Username:", practice_create_username(" Prahlad ", "2026"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- User Input ---
# Asha is 21 years old.
# Username: prahlad2026
# End Expected Output
