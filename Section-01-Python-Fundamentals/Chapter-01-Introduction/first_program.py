"""
Topic: First Program (Hello World)
Chapter: 01
Level: Beginner

Description:
    This is the traditional first step in learning any programming language. 
    It demonstrates how to write a simple script that outputs text to the screen.
    This simple action proves that the environment is set up correctly and running code.

Real-Life Analogy:
    Imagine turning on a new walkie-talkie and saying "Test, 1, 2, 3" to ensure the other person can hear you. 
    Writing "Hello World" is the equivalent of verifying your code can "speak" to the computer.

Key Concepts:
    - The `print()` function
    - String literals (text surrounded by quotes)
    - Code execution flow
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The most basic Python program consists of a single line using the print function.
# The print() function tells Python to display whatever is inside the parentheses.
# "Hello, World!" is a string literal, which is text enclosed in double quotes.

def basic_hello_world():
    print("Hello, World!")
    print('Hello again, using single quotes!')

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Here are intermediate examples of greeting different users or using variables.

def practical_greetings():
    # Storing a name in a variable and printing it
    user_name = "Alice"
    print("Hello, " + user_name + "! Welcome to Python.")
    
    # Printing multiple items
    print("System Status:", "Online", "Ready to process commands.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Printing with formatted strings (f-strings) and changing the end character.

def advanced_printing():
    version = 3.12
    # f-strings allow embedding expressions inside string literals
    print(f"Running Python version {version} - Hello, World!")
    
    # The 'end' parameter changes what is printed at the end of the line (default is newline)
    print("Loading", end="... ")
    print("Done!")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# 1. Forgetting parentheses: print "Hello" (Valid in Python 2, syntax error in Python 3)
# 2. Missing quotes: print(Hello) (Raises NameError because Hello is treated as a variable)
# 3. Mismatched quotes: print("Hello') (SyntaxError)

# Best Practices:
# - Use double quotes for strings that contain single quotes: "It's a beautiful day"
# - Keep your first programs simple to ensure your environment is working before adding complexity.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does the print() function do?
# A: It outputs text or other data to the standard output (usually the console).
#
# Q2: Is Python compiled or interpreted?
# A: Python is an interpreted language, meaning code is executed line by line.
#
# Q3: What happens if you forget quotes around the text in print()?
# A: Python will attempt to evaluate the text as variables or expressions, typically resulting in a NameError or SyntaxError.
#
# Q4: Why is 'Hello World' traditionally the first program written?
# A: It acts as a sanity check to verify that the compiler/interpreter, development environment, and runtime are correctly installed.
#
# Q5: How do you print multiple words separated by spaces without putting the spaces in the string?
# A: Pass them as separate arguments: print("Hello", "World")

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a program that prints your name.
# Hint: Use print("Your Name")
#
# Exercise 2: Print a multi-line message using three separate print statements.
# Hint: Call print() three times.
#
# Exercise 3: Print "Python is awesome!" using both single and double quotes.
# Hint: print('text') and print("text")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Write a script that prints a personalized welcome message.
# It should print:
# "Welcome to Python Programming!"
# "Starting initialization..."
# "Initialization complete. Hello, Admin!"

def mini_challenge():
    print("Welcome to Python Programming!")
    print("Starting initialization...")
    print("Initialization complete. Hello, Admin!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `print()` is the built-in function to output data to the console.
# - Strings must be enclosed in quotes (single or double).
# - A working "Hello, World!" proves your Python installation is functional.

if __name__ == "__main__":
    print("--- Basic Hello World ---")
    basic_hello_world()
    print("\n--- Practical Greetings ---")
    practical_greetings()
    print("\n--- Advanced Printing ---")
    advanced_printing()
    print("\n--- Mini Challenge ---")
    mini_challenge()
