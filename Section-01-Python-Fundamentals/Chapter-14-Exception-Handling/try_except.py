"""
Topic: Try-Except Blocks
Chapter: 14
Level: Beginner

Description:
    Exception handling allows a program to gracefully deal with errors instead of crashing.
    The `try` block contains code that might throw an exception, and the `except` block catches and handles it.

Real-Life Analogy:
    Imagine riding a bicycle. The `try` block is you riding normally. The `except` block is your helmet and pads—if you fall (an error occurs), they protect you from a serious injury (a program crash).

Key Concepts:
    - try block
    - except block
    - Exception types
    - Catching multiple exceptions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The try-except block allows you to catch errors and prevent crashes.
def basic_division():
    try:
        # This will cause a ZeroDivisionError
        result = 10 / 0
        print(f"Result is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Catching different types of errors
def basic_type_error():
    try:
        # This will cause a TypeError
        result = "Hello" + 5
    except TypeError:
        print("Error: Cannot add string and integer!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def convert_to_integer(value):
    """Safely converts a string to an integer."""
    try:
        return int(value)
    except ValueError:
        print(f"Warning: '{value}' is not a valid number. Returning 0.")
        return 0

def get_item_from_list(data_list, index):
    """Safely gets an item from a list by index."""
    try:
        return data_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds for list of length {len(data_list)}.")
        return None

def read_file_content(filename):
    """Safely attempts to read a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def catch_multiple_exceptions(data, key):
    """Catches multiple specific exceptions in one block or separate blocks."""
    try:
        value = data[key]
        result = 100 / value
        return result
    except (KeyError, TypeError) as e:
        print(f"Data error occurred: {e}")
    except ZeroDivisionError:
        print("Math error: Division by zero is not allowed.")
    except Exception as e:
        # Catch-all for any other unforeseen exceptions
        print(f"An unexpected error occurred: {e}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Catching everything silently (Bare except)
# try:
#     do_something()
# except:
#     pass

# Best Practice: Catch specific exceptions and handle them appropriately.
# try:
#     do_something()
# except ValueError as e:
#     print(f"ValueError occurred: {e}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the purpose of the `try...except` block in Python?
# A1: It is used for exception handling. The `try` block lets you test a block of code for errors, while `except` lets you handle the error.
#
# Q2: Is it a good practice to use a bare `except:` clause?
# A2: No. A bare `except:` catches all exceptions, including KeyboardInterrupt and SystemExit, which can make debugging difficult and hide unexpected bugs.
#
# Q3: How do you catch multiple exceptions in a single `except` block?
# A3: By specifying a tuple of exception types, e.g., `except (ValueError, TypeError):`.
#
# Q4: What is the `Exception` class in Python?
# A4: It is the base class for all built-in, non-system-exiting exceptions.
#
# Q5: Can an exception be ignored completely?
# A5: Yes, by using the `pass` statement in the `except` block, though it's generally discouraged unless intentional (often called "swallowing" exceptions).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function that takes user input and converts it to a float, using try-except to handle invalid inputs.
# Exercise 2: Write a script that attempts to open 'config.txt', handling the FileNotFoundError.
# Exercise 3: Create a dictionary lookup function that handles KeyError gracefully.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def safe_calculator(num1, num2, op):
    """
    Mini Challenge: Implement a safe calculator that takes two numbers and an operator.
    Handle ValueError (invalid number), ZeroDivisionError (division by zero), and KeyError (invalid operator).
    """
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    
    try:
        val1 = float(num1)
        val2 = float(num2)
        
        result = ops[op](val1, val2)
        print(f"Result of {val1} {op} {val2} = {result}")
    except ValueError:
        print("Error: Invalid number entered. Must be numeric.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except KeyError:
        print(f"Error: Invalid operator '{op}'. Supported operators are +, -, *, /.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The `try` block encloses code that might fail.
# - The `except` block executes if an exception is raised.
# - Always catch specific exceptions before general ones.
# - Access the exception object using `as e` for more details.

if __name__ == "__main__":
    basic_division()
    basic_type_error()
    print(convert_to_integer("123"))
    print(convert_to_integer("abc"))
    
    print("\n--- Mini Challenge ---")
    safe_calculator(10, 5, '+')
    safe_calculator(10, 0, '/')
    safe_calculator("abc", 5, '+')
    safe_calculator(10, 5, '^')
