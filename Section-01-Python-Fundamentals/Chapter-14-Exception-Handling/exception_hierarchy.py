"""
Topic: Exception Hierarchy
Chapter: 14
Level: Intermediate

Description:
    Exceptions in Python are organized in an object-oriented hierarchy.
    BaseException is the root, and Exception is the base class for most standard, non-system-exiting errors.
    Understanding this hierarchy helps you catch related errors effectively.

Real-Life Analogy:
    Think of a biological taxonomy. "Animal" is the base class. "Mammal" inherits from "Animal". "Dog" inherits from "Mammal".
    Catching "Mammal" will catch "Dog", "Cat", etc. Catching "Exception" catches almost all Python errors.

Key Concepts:
    - BaseException vs Exception
    - Built-in exceptions tree
    - Exception polymorphism
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Python's built-in exceptions form a tree.
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- Exception
#       +-- ArithmeticError
#            +-- ZeroDivisionError
#       +-- LookupError
#            +-- IndexError
#            +-- KeyError

def show_hierarchy_concept():
    try:
        # ZeroDivisionError is a subclass of ArithmeticError, which is a subclass of Exception
        x = 1 / 0
    except ArithmeticError as e:
        # Catching the parent class catches all its child classes!
        print(f"Caught an arithmetic error: {type(e).__name__}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def lookup_data(data, key_or_index):
    """Handles both IndexError and KeyError using their parent, LookupError."""
    try:
        return data[key_or_index]
    except LookupError as e:
        print(f"LookupError caught! Item not found. Details: {type(e).__name__} - {e}")
        return None

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def examine_mro(exception_class):
    """Prints the Method Resolution Order (MRO) to see the inheritance chain."""
    print(f"Inheritance chain for {exception_class.__name__}:")
    for base in exception_class.mro():
        print(f" -> {base.__name__}")
    print()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Catching `Exception` before specific errors.
# try:
#     x = 1 / 0
# except Exception:
#     print("Caught general exception")
# except ZeroDivisionError:
#     print("This will NEVER be reached!")

# Best Practice: Catch specific subclasses first, then broader parent classes.
# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("Specific handling for div by zero")
# except ArithmeticError:
#     print("General arithmetic handling")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the base class for all built-in exceptions in Python?
# A1: `BaseException`.
#
# Q2: Why should you generally inherit from `Exception` rather than `BaseException` for custom exceptions?
# A2: `BaseException` includes system-exiting exceptions like `SystemExit` and `KeyboardInterrupt`. Catching `Exception` avoids accidentally swallowing these critical signals.
#
# Q3: If `KeyError` and `IndexError` share a common parent, what is it?
# A3: They both inherit from `LookupError`.
#
# Q4: Why is exception order important in `try...except` blocks?
# A4: Python evaluates `except` blocks top-to-bottom. If a parent class is caught before its subclass, the subclass block becomes unreachable.
#
# Q5: How can you find out the parent classes of an exception?
# A5: Using the `__bases__` attribute or the `.mro()` method on the exception class.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a try-except block that catches `LookupError` for both list index out of range and missing dictionary keys.
# Exercise 2: Print the MRO for `FileNotFoundError`.
# Exercise 3: Intentionally order an `Exception` catch before `ValueError` and observe the unreachable code warning (conceptually).

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def advanced_calculator(a, b, op):
    """
    Mini Challenge: A calculator that explicitly demonstrates hierarchy handling.
    Catch ZeroDivisionError, then ArithmeticError, then Exception.
    """
    try:
        if op == '/':
            result = a / b
        elif op == '+':
            result = a + b
        elif op == '**':
            # This can cause an OverflowError, which is also an ArithmeticError
            result = a ** b
        else:
            raise RuntimeError("Unsupported operator")
        return result
    except ZeroDivisionError:
        print("Specific Error: You cannot divide by zero.")
    except ArithmeticError as e:
        print(f"Math Error ({type(e).__name__}): Number too large or invalid math operation.")
    except Exception as e:
        print(f"General Error: {e}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Exceptions are classes arranged in a hierarchy.
# - Catching a parent class automatically catches all its subclasses.
# - Always order `except` blocks from most specific to least specific.
# - Use `Exception` for generic errors, not `BaseException`.

if __name__ == "__main__":
    show_hierarchy_concept()
    
    my_list = [1, 2, 3]
    my_dict = {"a": 1}
    
    lookup_data(my_list, 10) # Triggers IndexError
    lookup_data(my_dict, "b") # Triggers KeyError
    
    examine_mro(ZeroDivisionError)
    examine_mro(FileNotFoundError)
    
    advanced_calculator(10, 0, '/')
    advanced_calculator(10.0, 1000000.0, '**') # OverflowError
    advanced_calculator(10, 5, 'unknown') # RuntimeError
