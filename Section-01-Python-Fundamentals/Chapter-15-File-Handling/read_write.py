"""
Topic: File Reading and Writing
Chapter: 15
Level: Beginner

Description:
    Reading and writing files is a fundamental skill in Python, allowing programs to store and retrieve data. You can read entire files, line by line, or write new content directly to a text file.

Real-Life Analogy:
    Think of a file like a physical notebook. Reading a file is like reading the notes you wrote previously, while writing is like adding new notes on a blank page.

Key Concepts:
    - open() function
    - read(), readline(), and readlines() methods
    - write() and writelines() methods
    - Closing files safely
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The open() function opens a file and returns a file object.
# Always make sure to close the file to free up system resources.

# Let's create a file and write to it.
file_obj = open("example_basic.txt", "w", encoding="utf-8")
file_obj.write("Hello, World!\n")
file_obj.write("This is a basic text file.\n")
file_obj.close()  # Always close your file!

# Now let's read the file back
file_obj = open("example_basic.txt", "r", encoding="utf-8")
content = file_obj.read()
print("Basic Read:")
print(content)
file_obj.close()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Reading line by line (Memory Efficient)
print("Reading Line by Line:")
file_obj = open("example_basic.txt", "r", encoding="utf-8")
for line in file_obj:
    print(line.strip())  # .strip() removes the newline character
file_obj.close()

# Example 2: Using readlines() to get a list of lines
file_obj = open("example_basic.txt", "r", encoding="utf-8")
lines = file_obj.readlines()
file_obj.close()
print(f"\nReadlines output: {lines}")

# Example 3: Writing multiple lines with writelines()
lines_to_write = ["First line.\n", "Second line.\n", "Third line.\n"]
file_obj = open("example_lines.txt", "w", encoding="utf-8")
file_obj.writelines(lines_to_write)
file_obj.close()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Using read(size) to read chunks of a file. This is useful for large files.
file_obj = open("example_lines.txt", "r", encoding="utf-8")
chunk = file_obj.read(5)  # Reads the first 5 characters
print(f"\nFirst chunk: '{chunk}'")
chunk2 = file_obj.read(5) # Reads the next 5 characters
print(f"Second chunk: '{chunk2}'")
file_obj.close()

# Seeking and Telling
# tell() gives current position, seek() moves the position
file_obj = open("example_lines.txt", "r", encoding="utf-8")
print(f"Initial position: {file_obj.tell()}")
file_obj.read(5)
print(f"Position after reading 5 chars: {file_obj.tell()}")
file_obj.seek(0) # Move back to start
print(f"Position after seek(0): {file_obj.tell()}")
file_obj.close()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Forgetting to close the file.
# Correction: Always call .close() or use a context manager (covered later).

# Mistake 2: Not specifying encoding.
# Correction: Always use encoding="utf-8" to avoid cross-platform character issues.

# Best Practice: Use absolute or relative paths carefully to avoid FileNotFoundError.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between read() and readlines()?
# A: read() reads the entire file as a single string, while readlines() reads all lines into a list of strings.

# Q2: Why is it important to close a file after using it?
# A: It frees up operating system resources and ensures that all buffered data is properly written to disk.

# Q3: What happens if you open a non-existent file in 'r' mode?
# A: A FileNotFoundError is raised.

# Q4: What does the .tell() method do?
# A: It returns the current byte position of the file pointer within the file.

# Q5: How can you read a large file without running out of memory?
# A: Iterate over the file object directly (e.g., `for line in file:`), which reads one line at a time.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a script to create a file called "greetings.txt" and write 3 different greetings into it.
# Hint: Use open() with 'w' mode and write().

# Exercise 2: Read "greetings.txt" and print the total number of characters in the file.
# Hint: Use read() and len().

# Exercise 3: Read "greetings.txt" and print each line in uppercase.
# Hint: Iterate over the file and use .upper().

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def log_message(filename, message):
    """
    Mini Challenge: Write a function that appends a message to a log file.
    It should open the file in append mode ('a'), write the message with a newline,
    and then close the file. Read it back and print all logs.
    """
    f = open(filename, "a", encoding="utf-8")
    f.write(message + "\n")
    f.close()
    
    f = open(filename, "r", encoding="utf-8")
    print(f"\nCurrent logs in {filename}:")
    print(f.read())
    f.close()

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The open() function creates a file object.
# - Use 'r' to read, 'w' to write (overwrites), 'a' to append.
# - read() gets all content; readlines() gets a list of lines.
# - Always close files or system resources may leak.
# - Iterating directly over the file object is memory-efficient for large files.

if __name__ == "__main__":
    log_message("mini_log.txt", "Log entry 1: System started.")
    log_message("mini_log.txt", "Log entry 2: Processing data.")
