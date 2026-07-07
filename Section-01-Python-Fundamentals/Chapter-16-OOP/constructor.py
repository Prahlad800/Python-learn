"""Learning file for Constructors."""

# Topic Name: Constructors
# Level: Intermediate
# __init__ initializes object state when a new object is created.
# Read the theory first, then run this file and modify examples.

# Theory
# __init__ initializes object state when a new object is created.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# def __init__(self, value):
#     self.value = value

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses constructors
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
class Course:
    def __init__(self, title, duration_hours):
        self.title = title
        self.duration_hours = duration_hours

    def summary(self):
        return f"{self.title}: {self.duration_hours} hours"


def example_constructor():
    course = Course("Python Basics", 12)
    print(course.summary())


def practice_create_course(title):
    return Course(title, 8)


def main():
    print("--- Constructors ---")
    example_constructor()
    print(practice_create_course("OOP").summary())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Constructors ---
# Python Basics: 12 hours
# OOP: 8 hours
# End Expected Output
