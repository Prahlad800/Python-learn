"""Learning file for Inheritance."""

# Topic Name: Inheritance
# Level: Intermediate
# Inheritance shares behavior from a parent class to child classes.
# Read the theory first, then run this file and modify examples.

# Theory
# Inheritance shares behavior from a parent class to child classes.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# class Child(Parent):
#     pass
# super().__init__()

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses inheritance
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} works"


class Developer(Employee):
    def work(self):
        return f"{self.name} writes code"


def example_inheritance():
    employee = Employee("Asha")
    developer = Developer("Ravi")
    print(employee.work())
    print(developer.work())


def practice_team_report(team):
    return [member.work() for member in team]


def main():
    print("--- Inheritance ---")
    example_inheritance()
    print("Team:", practice_team_report([Developer("Meera")]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Inheritance ---
# Asha works
# Ravi writes code
# Team: ['Meera writes code']
# End Expected Output
