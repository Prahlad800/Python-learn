"""
Topic: File Modes
Chapter: 15
Level: Beginner

Description:
    File modes determine the actions you can perform on a file when you open it. By choosing the right mode, you ensure that you don't accidentally overwrite important data while appending, or try to read a file that you only opened for writing.

Real-Life Analogy:
    Think of file modes as different types of access passes. 'r' is a read-only pass for a museum exhibit, 'w' is a blank canvas where you draw over anything that was there, and 'a' is a visitor logbook where you can only add your name at the end.

Key Concepts:
    - 'r' (Read): Default mode. Opens a file for reading. Error if it doesn't exist.
    - 'w' (Write): Opens a file for writing. Creates a new file if it doesn't exist or truncates it.
    - 'a' (Append): Opens for writing, appending to the end of the file.
    - 'r+' / 'w+' / 'a+': Plus modes for both reading and writing.
    - 'x' (Exclusive creation): Creates a file, failing if it already exists.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The mode is passed as the second argument to open().
# Mode 'w': Write mode (overwrites)
with open("mode_example.txt", "w", encoding="utf-8") as f:
    f.write("Initial content.\n")

# Mode 'r': Read mode (default)
with open("mode_example.txt", "r", encoding="utf-8") as f:
    print("Read Mode ('r'):", f.read().strip())

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Append Mode ('a')
# Appending adds to the end without truncating existing content
with open("mode_example.txt", "a", encoding="utf-8") as f:
    f.write("Appended content.\n")

with open("mode_example.txt", "r", encoding="utf-8") as f:
    print("\nAfter Append ('a'):")
    print(f.read().strip())

# Example 2: Exclusive Creation ('x')
# This mode is useful when you want to ensure you don't overwrite an existing file.
try:
    with open("mode_example.txt", "x", encoding="utf-8") as f:
        f.write("This will fail because the file exists.\n")
except FileExistsError:
    print("\nExclusive Creation ('x') failed: File already exists!")

# Creating a new file successfully with 'x'
import os
if os.path.exists("new_exclusive.txt"):
    os.remove("new_exclusive.txt")

with open("new_exclusive.txt", "x", encoding="utf-8") as f:
    f.write("Created exclusively!")
    print("Successfully created 'new_exclusive.txt' using 'x' mode.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 1: Read and Write ('r+')
# 'r+' opens for both reading and writing, without truncating the file.
with open("mode_example.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    f.write("Writing at the end via r+.\n")

# Example 2: Write and Read ('w+')
# 'w+' truncates the file first, then allows reading and writing.
with open("w_plus_example.txt", "w+", encoding="utf-8") as f:
    f.write("Writing fresh content.")
    f.seek(0) # Move to start to read
    print("\nRead after write ('w+'):", f.read())

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Using 'w' when you mean 'a', unintentionally wiping out the file.
# Correction: Double-check your mode string before opening the file.

# Mistake 2: Trying to read a file opened in 'w' or 'a' mode without a '+'.
# Correction: A file opened in 'w' cannot be read. Use 'w+' or reopen in 'r' mode.

# Best Practice: Use 'x' mode for temporary files or initial setup files to prevent accidental data loss.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What happens if you open a non-existent file in 'r' mode?
# A: Python raises a FileNotFoundError.

# Q2: What is the difference between 'w' and 'a' modes?
# A: 'w' truncates (empties) the file before writing, whereas 'a' preserves existing content and writes at the end.

# Q3: What does the '+' do in file modes like 'r+' or 'w+'?
# A: It allows both reading and writing on the same file object.

# Q4: How does 'r+' differ from 'w+'?
# A: 'r+' does not truncate the file and requires the file to exist. 'w+' truncates the file to zero bytes if it exists, or creates it if it doesn't.

# Q5: Why use the 'x' mode?
# A: To securely create a file, ensuring you aren't accidentally overwriting an existing file with the same name.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Open a file in 'w' mode and write the numbers 1 to 5, one per line.

# Exercise 2: Open the same file in 'a' mode and append the numbers 6 to 10.

# Exercise 3: Open the file in 'r+' mode, read its contents, and write "DONE" at the end.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def safe_write(filename, content):
    """
    Mini Challenge: Write a function that safely writes content to a file.
    If the file exists, append to it. If it doesn't, create it.
    (Hint: 'a' mode does exactly this natively!)
    Print the contents after writing.
    """
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(content + "\n")
        f.seek(0)
        print(f"\nContents of {filename}:")
        print(f.read().strip())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - 'r' is for reading (default).
# - 'w' is for writing (overwrites everything).
# - 'a' is for appending (adds to the end).
# - 'x' is for exclusive creation (fails if file exists).
# - Adding '+' (e.g., 'r+', 'w+', 'a+') enables both reading and writing.

if __name__ == "__main__":
    safe_write("safe_challenge.txt", "First run.")
    safe_write("safe_challenge.txt", "Second run.")
