"""Learning file for if-else Statement."""

# Topic Name: if-else Statement
# Level: Beginner
# if-else chooses one of two paths so programs can respond to different situations.
# Read the theory first, then run this file and modify examples.

# Theory
# if-else chooses one of two paths so programs can respond to different situations.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# if condition:
#     true_block
# else:
#     false_block

# Practice Programs
# 1. Write a grade calculator.
# 2. Check eligibility for a discount.
# 3. Build a menu using match-case.

# Mini Project
# Build a tiny program that uses if-else statement
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When should you use elif?
# A1. Use elif when only one branch from several ordered choices should run.
# Q2. What is a truthy value?
# A2. A value that behaves like True in a boolean context.

# Examples and practice implementations start below.
def example_if_else():
    age = 17
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible yet")


def example_password_check(password):
    if len(password) >= 8:
        return "Strong enough"
    return "Too short"


def practice_pass_fail(marks):
    return "Pass" if marks >= 40 else "Fail"


def main():
    print("--- if-else Statement ---")
    example_if_else()
    print(example_password_check("python123"))
    print("Result:", practice_pass_fail(72))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- if-else Statement ---
# Not eligible yet
# Strong enough
# Result: Pass
# End Expected Output
