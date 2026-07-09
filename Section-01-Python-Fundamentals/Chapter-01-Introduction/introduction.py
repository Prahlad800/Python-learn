"""
Topic: Introduction to Python
Chapter: 01
Level: Beginner

Description:
    Python is a high-level, interpreted programming language known for its readability and simplicity.
    This file explores the core philosophy of Python, executing scripts, and the basic architecture
    of Python code.

Real-Life Analogy:
    Think of programming languages like different kinds of vehicles. C++ is like a manual-transmission 
    sports car (fast, but requires a lot of control). Python is like an automatic car with cruise control; 
    it abstracts away the difficult parts so you can focus on the destination (the logic).

Key Concepts:
    - High-level language characteristics
    - Interpreted execution
    - The Zen of Python (import this)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Python scripts are executed top-to-bottom.
# Statements do not require semicolons at the end.
# Blocks are defined by indentation rather than curly braces.

def run_intro():
    print("Welcome to the Introduction to Python!")
    print("Python code is designed to be highly readable.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Exploring basic data handling to show simplicity.
def calculate_area():
    # Calculating the area of a rectangle
    length = 10
    width = 5
    area = length * width
    print(f"The area of a rectangle with length {length} and width {width} is {area}.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced introspection to see Python's philosophy
def show_zen():
    # 'import this' is an Easter egg that prints the "Zen of Python"
    # To capture it without printing it automatically on import, we normally use context managers,
    # but for this script, we'll just print a couple of its principles.
    zen_lines = [
        "Beautiful is better than ugly.",
        "Explicit is better than implicit.",
        "Simple is better than complex."
    ]
    print("Core Python Philosophy (The Zen of Python excerpt):")
    for line in zen_lines:
        print(f" - {line}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Treating Python like C or Java by adding unnecessary semicolons.
# - Overcomplicating simple tasks. Python has many built-in functions.

# Best Practices:
# - Write readable code. Code is read more often than it is written.
# - Follow PEP 8 style guidelines.
# - Use descriptive variable names.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What are the key features of Python?
# A: It is an interpreted, dynamically typed, high-level language with clean syntax and automatic memory management.
#
# Q2: Who created Python and when was it first released?
# A: Guido van Rossum created Python, and it was first released in 1991.
#
# Q3: What is PEP 8?
# A: PEP 8 is the official style guide for Python code.
#
# Q4: How is Python executed?
# A: The Python interpreter compiles source code to bytecode (.pyc), which is then run on the Python Virtual Machine (PVM).
#
# Q5: What does dynamically typed mean?
# A: You don't have to declare the type of a variable when you create one. The type is determined at runtime.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a script that defines a variable and prints it.
# Exercise 2: Print three reasons why you are learning Python.
# Exercise 3: Use an f-string to print a sentence containing two variables.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    language = "Python"
    year = 1991
    creator = "Guido van Rossum"
    print(f"{language} was created by {creator} and first released in {year}.")
    print("It is known for its simplicity and readability.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Python emphasizes readability and simplicity.
# - It is widely used in web development, data science, automation, and more.
# - Understanding its philosophy makes you a better Python developer.

if __name__ == "__main__":
    run_intro()
    print()
    calculate_area()
    print()
    show_zen()
    print()
    mini_challenge()
