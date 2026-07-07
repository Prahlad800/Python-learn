# Topic: raise Statement
# Explanation: The raise statement triggers exceptions intentionally.

# Syntax:
# age = -1
if age < 0:
    raise ValueError("Age cannot be negative")

# Examples:
# age = -1
if age < 0:
    raise ValueError("Age cannot be negative")

# Practice Programs:
# 1. Raise a TypeError manually.
2. Raise a custom message for invalid input.

# Interview Questions:
# Q: Why use raise?
A: To signal invalid logic or unexpected data.

# Expected Output:
# ValueError: Age cannot be negative

age = -1
if age < 0:
    raise ValueError("Age cannot be negative")
