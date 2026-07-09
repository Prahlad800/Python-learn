"""
Topic: Context Managers (The 'with' statement)
Chapter: 15
Level: Intermediate

Description:
    Context managers provide a clean and robust way to handle resource management, such as opening and closing files. Using the 'with' statement ensures that cleanup operations like `.close()` are automatically performed, even if an exception occurs during execution.

Real-Life Analogy:
    Imagine a library where you borrow a book. The context manager is like a magical librarian who automatically takes the book out of your hands and places it back on the shelf the moment you step out of the reading area, regardless of whether you finished reading or left in a hurry.

Key Concepts:
    - The 'with' statement
    - Automatic resource cleanup
    - Handling exceptions safely
    - Custom context managers (contextlib)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The traditional way (requires manual closing)
f = open("context_test.txt", "w", encoding="utf-8")
f.write("Testing context managers.\n")
f.close()  # If an error happens before this, the file stays open!

# The modern way using 'with'
# The file is automatically closed when the indented block finishes
with open("context_test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Content:", content.strip())

# To prove it's closed:
print("Is file closed?", file.closed)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Writing multiple lines safely
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("context_lines.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# Example 2: Reading line by line safely
print("\nReading safely:")
with open("context_lines.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Example 3: Handling exceptions within the block
try:
    with open("context_lines.txt", "r", encoding="utf-8") as f:
        data = f.read()
        # Simulating an error
        raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"\nCaught an exception: {e}")
    # The file 'f' is still correctly closed!
    print("Is file closed after exception?", f.closed)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 1: Opening multiple files simultaneously
# You can manage multiple resources in a single 'with' statement
with open("source.txt", "w") as src:
    src.write("Copy me!")

with open("source.txt", "r") as src, open("dest.txt", "w") as dest:
    dest.write(src.read())

print("\nMultiple context managers executed successfully.")

# Example 2: Creating a custom Context Manager class
class MyTimer:
    import time
    def __enter__(self):
        self.start = self.time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = self.time.time()
        print(f"Time taken: {end - self.start:.5f} seconds")

with MyTimer():
    # Simulate some work
    sum(range(1000000))

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Trying to read/write a file object after the 'with' block.
# Correction: All file operations must be indented under the 'with' statement.

# Mistake 2: Not using 'with' for temporary files or network connections.
# Correction: Always use 'with' when dealing with external resources to prevent leaks.

# Best Practice: Limit the amount of code inside the 'with' block to only what's necessary for the file operation.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the main advantage of the 'with' statement when opening files?
# A: It guarantees that the file will be closed automatically, even if an exception occurs, preventing resource leaks.

# Q2: Which magic methods are required to create a custom context manager?
# A: `__enter__()` and `__exit__()`.

# Q3: Can you open multiple files in a single 'with' statement?
# A: Yes, by separating them with commas: `with open('a') as a, open('b') as b:`

# Q4: What happens if an exception is raised inside a 'with' block?
# A: The `__exit__()` method is called (which closes the file for `open()`), and then the exception is propagated outward.

# Q5: Does the variable created by 'as' (e.g., 'f' in 'as f') disappear after the 'with' block?
# A: No, the variable 'f' still exists, but the file it points to is closed, so you cannot read/write to it.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Use a 'with' statement to write a list of your favorite colors to a file.

# Exercise 2: Use a 'with' statement to read the colors file and print them in reverse order.

# Exercise 3: Use a single 'with' statement to read from one file and append its contents to another file.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def process_logs(input_log, output_log):
    """
    Mini Challenge: Write a function that reads a log file, filters out lines 
    containing the word "ERROR", and writes only those error lines to an output log file.
    Use context managers for both files safely.
    """
    # Setup dummy data
    with open(input_log, "w") as f:
        f.write("INFO: System started\n")
        f.write("ERROR: Missing dependencies\n")
        f.write("WARN: High memory usage\n")
        f.write("ERROR: Connection failed\n")

    # Processing
    with open(input_log, "r") as infile, open(output_log, "w") as outfile:
        for line in infile:
            if "ERROR" in line:
                outfile.write(line)
    
    # Verify
    with open(output_log, "r") as f:
        print("\nFiltered Errors:")
        print(f.read().strip())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Context managers automate resource management (e.g., closing files).
# - The 'with' keyword invokes a context manager.
# - It ensures safe cleanup even when errors occur.
# - Multiple resources can be managed in one line.
# - You can build custom context managers using __enter__ and __exit__.

if __name__ == "__main__":
    process_logs("system.log", "errors.log")
