# Topic: finally Block
# Explanation: The finally block runs regardless of whether an exception occurs.

# Syntax:
# try:
    print("Hello")
finally:
    print("This always runs")

# Examples:
# try:
    print("Hello")
finally:
    print("This always runs")

# Practice Programs:
# 1. Use finally with a division operation.
2. Print a cleanup message.

# Interview Questions:
# Q: When does finally run?
A: It runs no matter what, even after an exception.

# Expected Output:
# Hello
This always runs

try:
    print("Hello")
finally:
    print("This always runs")
