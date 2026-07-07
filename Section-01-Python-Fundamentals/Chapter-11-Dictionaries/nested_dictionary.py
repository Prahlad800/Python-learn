"""Learning file for Nested Dictionaries."""

# Topic Name: Nested Dictionaries
# Level: Intermediate
# Nested dictionaries model hierarchical data such as students, users, products, and configuration.
# Read the theory first, then run this file and modify examples.

# Theory
# Nested dictionaries model hierarchical data such as students, users, products, and configuration.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# students['S1']['marks']
# for key, record in students.items(): ...

# Practice Programs
# 1. Create a student report dictionary.
# 2. Update inventory quantities safely.
# 3. Read nested dictionary values with get().

# Mini Project
# Build a tiny program that uses nested dictionaries
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What must dictionary keys be?
# A1. Keys must be hashable, such as strings, numbers, or tuples of immutable values.
# Q2. What does get() prevent?
# A2. It avoids KeyError by returning a default when the key is missing.

# Examples and practice implementations start below.
def example_nested_records():
    students = {
        "S1": {"name": "Asha", "marks": 92},
        "S2": {"name": "Ravi", "marks": 85},
    }
    for roll_no, record in students.items():
        print(roll_no, record["name"], record["marks"])


def example_safe_access():
    config = {"database": {"host": "localhost"}}
    print("Host:", config.get("database", {}).get("host", "missing"))


def practice_top_student(students):
    return max(students.items(), key=lambda item: item[1]["marks"])


def main():
    print("--- Nested Dictionaries ---")
    example_nested_records()
    example_safe_access()
    print("Top:", practice_top_student({"S1": {"marks": 70}, "S2": {"marks": 90}}))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Nested Dictionaries ---
# S1 Asha 92
# S2 Ravi 85
# Host: localhost
# Top: ('S2', {'marks': 90})
# End Expected Output
