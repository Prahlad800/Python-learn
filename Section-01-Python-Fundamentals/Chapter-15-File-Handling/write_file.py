# Topic: Writing Files
# Explanation: You can create or overwrite files using write mode.

# Syntax:
# with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learn Python")

# Examples:
# with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learn Python")

# Practice Programs:
# 1. Write a short paragraph to a file.
2. Create a file with your name.

# Interview Questions:
# Q: What does mode "w" do?
A: It opens the file for writing and overwrites existing content.

# Expected Output:
# A file named notes.txt is created with the text Learn Python

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learn Python")
