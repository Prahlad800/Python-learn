"""
Topic: The Print Function
Chapter: 01
Level: Beginner

Description:
    The `print()` function is the primary way to output data to the standard output device (console).
    It is versatile and accepts various arguments to format the output, handle separators, and manage line endings.

Real-Life Analogy:
    Think of the `print()` function as a megaphone. You can shout a single word, a whole sentence, 
    or have multiple people shout together. You can also decide if there should be a pause between words (sep) 
    or what should happen after shouting (end).

Key Concepts:
    - Multiple arguments
    - The `sep` parameter
    - The `end` parameter
    - Outputting to files (`file` parameter)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_print():
    # Printing a single string
    print("Hello, print function!")
    
    # Printing multiple items (automatically separated by spaces)
    print("Apples", "Bananas", "Cherries")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def print_with_separators_and_endings():
    # Using the 'sep' parameter to change the delimiter
    print("2024", "12", "25", sep="-")  # Prints: 2024-12-25
    
    # Using the 'end' parameter to prevent a newline
    print("Loading part 1", end=" ... ")
    print("Loading part 2", end=" ... ")
    print("Done!")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

import sys

def advanced_print():
    # Printing to standard error stream instead of standard out
    print("This is an error message!", file=sys.stderr)
    
    # Flushing the output buffer (useful in long-running processes)
    print("Processing data...", end="\r", flush=True)
    import time
    time.sleep(1)
    print("Data processed successfully!    ")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Forgetting that print() adds a newline by default, causing unwanted formatting.
# - Concatenating strings manually with '+' when passing multiple arguments is cleaner.
#   Bad: print("User: " + name + " is active.")
#   Good: print("User:", name, "is active.") or use f-strings.

# Best Practices:
# - Use f-strings for complex formatting instead of multiple print arguments.
# - Use the 'sep' parameter instead of manually adding delimiters to strings.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the default separator for multiple arguments in print()?
# A: A single space (" ").
#
# Q2: How do you prevent print() from adding a newline at the end?
# A: Pass the argument `end=""` (an empty string) or any other ending character.
#
# Q3: Can print() write directly to a file?
# A: Yes, by using the `file` parameter and passing a file object opened in write mode.
#
# Q4: What does the `flush` parameter do?
# A: It forces the output buffer to be written to the output stream immediately.
#
# Q5: Why does print("A", "B") output "A B" but print("A" + "B") output "AB"?
# A: The first passes two separate arguments separated by the default space separator. The second passes a single concatenated string.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Print three names separated by commas using the `sep` parameter.
# Exercise 2: Print a countdown from 3 to 1 on the same line.
# Exercise 3: Use an f-string to print a complex message containing variables.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # Print a formatted CSV-like row using 'sep'
    headers = ["ID", "Name", "Role"]
    print(headers[0], headers[1], headers[2], sep=",")
    print(101, "Alice", "Admin", sep=",")
    print(102, "Bob", "User", sep=",")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `print()` can accept infinitely many arguments.
# - `sep` changes the character(s) between arguments.
# - `end` changes what happens at the very end of the output.
# - `file` allows redirecting output to files or other streams.

if __name__ == "__main__":
    print("--- Basic Print ---")
    basic_print()
    print("\n--- Sep and End ---")
    print_with_separators_and_endings()
    print("\n--- Advanced Print ---")
    advanced_print()
    print("\n--- Mini Challenge ---")
    mini_challenge()
