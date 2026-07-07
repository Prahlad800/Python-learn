"""Learning file for Decision Making Practice."""

# Topic Name: Decision Making Practice
# Level: Beginner
# Decision Making Practice reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Decision Making Practice reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Write a grade calculator.
# 2. Check eligibility for a discount.
# 3. Build a menu using match-case.

# Mini Project
# Build a tiny program that uses decision making practice
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. When should you use elif?
# A1. Use elif when only one branch from several ordered choices should run.
# Q2. What is a truthy value?
# A2. A value that behaves like True in a boolean context.

# Examples and practice implementations start below.
def login_message(username, password):
    if username == "admin" and password == "secret":
        return "Welcome admin"
    if username == "admin":
        return "Wrong password"
    return "Unknown user"


def shipping_cost(cart_total, is_member):
    if is_member or cart_total >= 999:
        return 0
    return 79


def practice_grade_feedback(score):
    if score >= 90:
        return "Excellent"
    if score >= 70:
        return "Good"
    return "Keep practicing"


def main():
    print("--- Decision Making Practice ---")
    print(login_message("admin", "secret"))
    print("Shipping:", shipping_cost(700, True))
    print(practice_grade_feedback(86))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Decision Making Practice ---
# Welcome admin
# Shipping: 0
# Good
# End Expected Output
