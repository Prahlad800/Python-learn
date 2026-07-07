"""Learning file for Nested if Statements."""

# Topic Name: Nested if Statements
# Level: Beginner
# Nested if statements place decisions inside decisions; they are useful but should stay readable.
# Read the theory first, then run this file and modify examples.

# Theory
# Nested if statements place decisions inside decisions; they are useful but should stay readable.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# if outer_condition:
#     if inner_condition:
#         statement

# Practice Programs
# 1. Write a grade calculator.
# 2. Check eligibility for a discount.
# 3. Build a menu using match-case.

# Mini Project
# Build a tiny program that uses nested if statements
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When should you use elif?
# A1. Use elif when only one branch from several ordered choices should run.
# Q2. What is a truthy value?
# A2. A value that behaves like True in a boolean context.

# Examples and practice implementations start below.
def can_access_dashboard(is_logged_in, role):
    if is_logged_in:
        if role == "admin":
            return "Full access"
        return "Limited access"
    return "Please log in"


def example_nested_if():
    print(can_access_dashboard(True, "admin"))
    print(can_access_dashboard(True, "viewer"))
    print(can_access_dashboard(False, "admin"))


def practice_loan_check(income, credit_score):
    if income >= 30000:
        if credit_score >= 700:
            return "Approved"
        return "Needs review"
    return "Rejected"


def main():
    print("--- Nested if Statements ---")
    example_nested_if()
    print("Loan:", practice_loan_check(40000, 720))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Nested if Statements ---
# Full access
# Limited access
# Please log in
# Loan: Approved
# End Expected Output
