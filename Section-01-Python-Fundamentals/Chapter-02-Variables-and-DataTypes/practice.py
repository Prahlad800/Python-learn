"""Learning file for Variables Practice."""

# Topic Name: Variables Practice
# Level: Beginner
# Variables Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Variables Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses variables practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
def student_record(name, age, marks):
    status = "Pass" if marks >= 40 else "Fail"
    return {"name": name, "age": age, "marks": marks, "status": status}


def swap_three(a, b, c):
    return c, a, b


def practice_total_price(price, quantity):
    return price * quantity


def main():
    print("--- Variables Practice ---")
    print(student_record("Asha", 21, 88))
    print("Rotated:", swap_three("a", "b", "c"))
    print("Total price:", practice_total_price(99, 3))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Variables Practice ---
# {'name': 'Asha', 'age': 21, 'marks': 88, 'status': 'Pass'}
# Rotated: ('c', 'a', 'b')
# Total price: 297
# End Expected Output
