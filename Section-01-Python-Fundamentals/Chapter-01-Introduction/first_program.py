"""Learning file for First Python Program."""

# Topic Name: First Python Program
# Level: Beginner
# A first program teaches execution order, string literals, variables, and the main guard used in real projects.
# Read the theory first, then run this file and modify examples.

# Theory
# A first program teaches execution order, string literals, variables, and the main guard used in real projects.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# print('Hello, World!')
# message = 'Welcome'
# def main(): ...

# Practice Programs
# 1. Print your name, city, and learning goal.
# 2. Create a short script with a main() function.
# 3. Add comments that explain the purpose of each line.

# Mini Project
# Build a tiny program that uses first python program
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why is Python popular?
# A1. It is readable, versatile, has a huge ecosystem, and supports many programming styles.
# Q2. What does the main guard do?
# A2. It lets code run only when the file is executed directly, not when imported.

# Examples and practice implementations start below.
def greet(name):
    return f"Hello, {name}! Welcome to Python."


def example_variables():
    language = "Python"
    year = 1991
    print(f"{language} first appeared in {year}.")


def practice_profile_card(name, course):
    return f"Student: {name} | Course: {course}"


def main():
    print("--- First Python Program ---")
    print(greet("Learner"))
    example_variables()
    print(practice_profile_card("Asha", "Python Basics"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- First Python Program ---
# Hello, Learner! Welcome to Python.
# Python first appeared in 1991.
# Student: Asha | Course: Python Basics
# End Expected Output
