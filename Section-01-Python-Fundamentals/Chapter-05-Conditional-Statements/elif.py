"""Learning file for elif Ladder."""

# Topic Name: elif Ladder
# Level: Beginner
# elif ladders choose one branch from many ordered conditions.
# Read the theory first, then run this file and modify examples.

# Theory
# elif ladders choose one branch from many ordered conditions.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# if score >= 90:
# elif score >= 75:
# else:

# Practice Programs
# 1. Write a grade calculator.
# 2. Check eligibility for a discount.
# 3. Build a menu using match-case.

# Mini Project
# Build a tiny program that uses elif ladder
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When should you use elif?
# A1. Use elif when only one branch from several ordered choices should run.
# Q2. What is a truthy value?
# A2. A value that behaves like True in a boolean context.

# Examples and practice implementations start below.
def grade_from_score(score):
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "Needs practice"


def example_elif():
    for score in [95, 82, 66, 45]:
        print(score, "->", grade_from_score(score))


def practice_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Healthy"
    return "Review lifestyle"


def main():
    print("--- elif Ladder ---")
    example_elif()
    print("BMI 22:", practice_bmi_category(22))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- elif Ladder ---
# 95 -> A
# 82 -> B
# 66 -> C
# 45 -> Needs practice
# BMI 22: Healthy
# End Expected Output
