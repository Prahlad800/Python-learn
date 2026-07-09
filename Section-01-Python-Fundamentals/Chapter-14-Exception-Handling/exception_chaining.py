"""
Topic: Exception Chaining
Chapter: 14
Level: Advanced

Description:
    Exception chaining (using the `raise ... from ...` syntax) allows you to raise a new exception while preserving the context of the original exception that caused it.
    This provides a complete traceback from the root cause to the final error.

Real-Life Analogy:
    Imagine your car won't start (Final Exception: CarNotStartingError). Why? Because the battery is dead (Root Exception: DeadBatteryError). Exception chaining tells the mechanic: "The car won't start *because* the battery is dead."

Key Concepts:
    - raise Exception from OriginalException
    - __cause__ attribute
    - __context__ attribute
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_chaining():
    try:
        # Simulate a root cause error
        1 / 0
    except ZeroDivisionError as e:
        # Raise a new, more descriptive error, chaining it to the original
        raise ValueError("Invalid mathematical operation attempted.") from e

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

class DatabaseConnectionError(Exception):
    pass

def fetch_user_data():
    try:
        # Simulate a low-level network error
        raise ConnectionResetError("Network connection reset by peer.")
    except ConnectionResetError as e:
        # Wrap it in a domain-specific error
        raise DatabaseConnectionError("Failed to fetch user data from the database.") from e

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def explicit_chaining_removal():
    """
    Sometimes you WANT to hide the original exception (e.g., for security reasons so internal paths aren't leaked).
    Use `raise ... from None`.
    """
    try:
        # Simulate internal secret failure
        open("secret_internal_file.txt")
    except FileNotFoundError as e:
        # Hide the fact that a file was missing, just return a generic error
        raise RuntimeError("A system configuration error occurred.") from None

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Raising a new exception without chaining, which loses the traceback of the root cause.
# try:
#     1 / 0
# except ZeroDivisionError:
#     raise ValueError("Math failed") # Loses the ZeroDivisionError traceback!

# Best Practice: Always use `from e` when wrapping exceptions so developers can trace the bug to its absolute origin.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does `raise NewException from e` do in Python?
# A1: It implements exception chaining. It raises `NewException` and sets its `__cause__` attribute to `e`, preserving the traceback of both errors.
#
# Q2: What is the difference between `__cause__` and `__context__` in exceptions?
# A2: `__cause__` is set explicitly using `raise ... from`. `__context__` is set automatically by Python when an exception is raised inside an `except` block.
#
# Q3: How do you suppress exception chaining?
# A3: By using `raise NewException from None`. This clears the `__cause__` and prevents the display of the original exception.
#
# Q4: Why would you want to use exception chaining?
# A4: To translate low-level implementation details (like a KeyError) into high-level domain errors (like UserNotFoundError) while still allowing developers to see exactly what failed underneath.
#
# Q5: Does Python 2 support `raise from`?
# A5: No, exception chaining using `raise ... from` was introduced in Python 3.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function that converts a string to an integer, catching ValueError and raising a custom InvalidInputError from it.
# Exercise 2: Demonstrate implicit chaining (raising an error inside an except block without `from`).
# Exercise 3: Use `from None` to hide a ZeroDivisionError behind a generic ValueError.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class ConfigurationError(Exception):
    pass

def load_config(filename):
    """
    Mini Challenge: Load a configuration dictionary. 
    If a KeyError occurs because a key is missing, chain it to a ConfigurationError.
    """
    mock_config = {"host": "localhost"}
    
    try:
        # Intentional KeyError
        port = mock_config["port"]
        return port
    except KeyError as original_error:
        raise ConfigurationError(f"Missing required configuration key: {original_error}") from original_error

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Exception chaining links a new exception to the original exception that caused it.
# - Use `raise NewException from old_exception`.
# - Use `raise NewException from None` to intentionally hide the root cause.
# - Exception chaining provides invaluable tracebacks for debugging complex systems.

if __name__ == "__main__":
    try:
        simple_chaining()
    except ValueError as e:
        print(f"Caught explicitly chained error: {e}")
        print(f"Root cause was: {e.__cause__}\n")

    try:
        fetch_user_data()
    except DatabaseConnectionError as e:
        print(f"Caught database error: {e}")
        print(f"Root cause: {e.__cause__}\n")
        
    try:
        explicit_chaining_removal()
    except RuntimeError as e:
        print(f"Caught suppressed chain error: {e}")
        print(f"Root cause is hidden! __cause__ is: {e.__cause__}\n")

    try:
        load_config("app.conf")
    except ConfigurationError as e:
        print(f"Config error: {e}")
