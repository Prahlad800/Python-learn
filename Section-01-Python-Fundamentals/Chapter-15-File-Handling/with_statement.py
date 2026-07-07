# Topic: with Statement
# Explanation: The with statement ensures files are closed automatically.

# Syntax:
# with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Using with")

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Examples:
# with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Using with")

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Practice Programs:
# 1. Use with to read a file.
2. Use with to write a file.

# Interview Questions:
# Q: Why is with preferred for file handling?
A: It manages resources safely and cleanly.

# Expected Output:
# Using with

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Using with")

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())
