"""Learning file for Classes and Objects."""

# Topic Name: Classes and Objects
# Level: Intermediate
# Classes define blueprints; objects are instances that hold data and behavior together.
# Read the theory first, then run this file and modify examples.

# Theory
# Classes define blueprints; objects are instances that hold data and behavior together.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# class Student:
#     def method(self): ...
# student = Student()

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses classes and objects
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
class Student:
    def set_details(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks >= 40


def example_object():
    student = Student()
    student.set_details("Asha", 92)
    print(student.name, "passed:", student.is_passed())


def practice_create_student(name, marks):
    student = Student()
    student.set_details(name, marks)
    return student


def main():
    print("--- Classes and Objects ---")
    example_object()
    learner = practice_create_student("Ravi", 35)
    print(learner.name, "passed:", learner.is_passed())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Classes and Objects ---
# Asha passed: True
# Ravi passed: False
# End Expected Output
