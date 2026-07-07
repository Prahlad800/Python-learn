# Topic: try-except
# Explanation: try-except handles errors without crashing the whole program.

# Syntax:
# try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Examples:
# try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Practice Programs:
# 1. Catch a ValueError.
2. Catch a TypeError.

# Interview Questions:
# Q: What is exception handling?
A: It manages runtime errors gracefully.

# Expected Output:
# Cannot divide by zero

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
