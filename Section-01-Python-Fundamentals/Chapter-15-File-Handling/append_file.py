# Topic: Appending to Files
# Explanation: The append mode adds new content without deleting existing content.

# Syntax:
# with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nKeep practicing")

# Examples:
# with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nKeep practicing")

# Practice Programs:
# 1. Append a sentence to an existing file.
2. Create a log file with multiple lines.

# Interview Questions:
# Q: What does mode "a" do?
A: It appends data to the end of the file.

# Expected Output:
# The file contains the original text plus the new line

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nKeep practicing")
