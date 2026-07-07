# Topic: Reading Files
# Explanation: Python can read text from files using open() and read().

# Syntax:
# with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python")

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Examples:
# with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python")

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Practice Programs:
# 1. Read a text file line by line.
2. Print the first line only.

# Interview Questions:
# Q: Why use with open()?
A: It automatically closes the file after the block ends.

# Expected Output:
# Hello from Python

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python")

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())
