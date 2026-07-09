"""
Topic: Exception Handling Practice
Chapter: 14
Level: Beginner/Intermediate/Advanced

Description:
    This file contains standalone practice exercises to solidify your understanding of Exception Handling in Python.

Key Concepts:
    - try/except/else/finally
    - Custom exceptions
    - Context managers
"""

# ============================================================
# EXERCISE 1: The Robust Calculator (Beginner)
# ============================================================
# Write a function `safe_divide(a, b)` that divides `a` by `b`.
# Handle ZeroDivisionError and TypeError.
# Use an else block to return the result if successful.
# Use a finally block to print "Division attempted."

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Inputs must be numbers"
    else:
        return result
    finally:
        print("Division attempted.")

# ============================================================
# EXERCISE 2: Custom Validation (Intermediate)
# ============================================================
# Create a custom exception called `PasswordTooShortError`.
# Write a function `register_password(pwd)` that raises this error if the password is less than 8 characters.

class PasswordTooShortError(Exception):
    pass

def register_password(pwd):
    if len(pwd) < 8:
        raise PasswordTooShortError(f"Password is {len(pwd)} chars. Must be at least 8.")
    return "Password registered successfully."

# ============================================================
# EXERCISE 3: File Parsing with Chaining (Advanced)
# ============================================================
# Create a custom exception `ConfigParseError`.
# Write a function `parse_int_config(config_dict, key)` that extracts a value and converts it to an int.
# If a KeyError or ValueError occurs, catch it and raise a `ConfigParseError` chained to the original exception using `from`.

class ConfigParseError(Exception):
    pass

def parse_int_config(config_dict, key):
    try:
        val = config_dict[key]
        return int(val)
    except (KeyError, ValueError) as e:
        raise ConfigParseError(f"Failed to parse config key '{key}'") from e

if __name__ == "__main__":
    # Test Exercise 1
    print("Ex 1:", safe_divide(10, 2))
    print("Ex 1:", safe_divide(10, 0))
    print("Ex 1:", safe_divide("10", 2))
    print("-" * 20)
    
    # Test Exercise 2
    try:
        register_password("1234567")
    except PasswordTooShortError as e:
        print("Ex 2 Error:", e)
    print("-" * 20)
    
    # Test Exercise 3
    my_config = {"port": "8080", "host": "localhost"}
    try:
        parse_int_config(my_config, "host") # Triggers ValueError -> ConfigParseError
    except ConfigParseError as e:
        print("Ex 3 Error:", e)
        print("Original cause:", e.__cause__)
