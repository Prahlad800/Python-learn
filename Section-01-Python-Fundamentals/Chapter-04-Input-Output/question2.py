"""Learning file for I/O Practice: Report Card."""

# Topic Name: I/O Practice: Report Card
# Level: Beginner
# I/O Practice: Report Card reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# I/O Practice: Report Card reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Read name and marks, then print a formatted report.
# 2. Format a bill with currency and tax.
# 3. Handle empty input with a default value.

# Mini Project
# Build a tiny program that uses i/o practice: report card
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does input() return?
# A1. It always returns a string.
# Q2. Why use formatted output?
# A2. Formatting makes reports predictable, readable, and easier to maintain.

# Examples and practice implementations start below.
def calculate_grade(marks):
    average = sum(marks) / len(marks)
    grade = "A" if average >= 90 else "B" if average >= 75 else "C"
    return average, grade


def example_report_card():
    average, grade = calculate_grade([88, 92, 95])
    print(f"Average: {average:.1f}")
    print(f"Grade: {grade}")


def practice_subject_line(subject, marks):
    return f"{subject:<10}: {marks:>3}/100"


def main():
    print("--- I/O Practice: Report Card ---")
    example_report_card()
    print(practice_subject_line("Python", 96))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- I/O Practice: Report Card ---
# Average: 91.7
# Grade: A
# Python    :  96/100
# End Expected Output
