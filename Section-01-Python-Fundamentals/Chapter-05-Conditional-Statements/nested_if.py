# Topic: Nested if Statements
# Explanation: Nested if statements place one condition inside another.

# Syntax:
# age = 20
if age >= 18:
    if age >= 21:
        print("Adult")
    else:
        print("Young adult")

# Examples:
# age = 20
if age >= 18:
    if age >= 21:
        print("Adult")
    else:
        print("Young adult")

# Practice Programs:
# 1. Check age and membership status.
2. Check both login and role.

# Interview Questions:
# Q: When are nested if statements useful?
A: When several layers of conditions are required.

# Expected Output:
# Young adult

age = 20
if age >= 18:
    if age >= 21:
        print("Adult")
    else:
        print("Young adult")
