"""Learning file for List Basics."""

# Topic Name: List Basics
# Level: Beginner
# Lists store ordered, mutable collections and are ideal when items need to be added, removed, or changed.
# Read the theory first, then run this file and modify examples.

# Theory
# Lists store ordered, mutable collections and are ideal when items need to be added, removed, or changed.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# items = []
# items.append(value)
# items[index] = new_value

# Practice Programs
# 1. Create a marks list and calculate average marks.
# 2. Remove duplicates while preserving order.
# 3. Build a 3x3 matrix and print row totals.

# Mini Project
# Build a tiny program that uses list basics
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Are lists mutable?
# A1. Yes. You can add, remove, and modify list items in place.
# Q2. What is a list comprehension?
# A2. A compact expression for building a new list from an iterable.

# Examples and practice implementations start below.
def example_create_access_update():
    fruits = ["apple", "banana", "cherry"]
    print("First:", fruits[0])
    fruits[1] = "blueberry"
    print("Updated:", fruits)


def example_add_remove():
    numbers = [1, 2]
    numbers.append(3)
    numbers.remove(2)
    print("Numbers:", numbers)


def practice_average(marks):
    return sum(marks) / len(marks)


def main():
    print("--- List Basics ---")
    example_create_access_update()
    example_add_remove()
    print("Average:", practice_average([80, 90, 100]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- List Basics ---
# First: apple
# Updated: ['apple', 'blueberry', 'cherry']
# Numbers: [1, 3]
# Average: 90.0
# End Expected Output
