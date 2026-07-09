"""
Topic: Basic Decorators
Chapter: 17
Level: Beginner

Description:
    A decorator in Python is a callable (usually a function) that takes another function as an argument and extends its behavior without modifying the original function's source code. Decorators are heavily used in frameworks like Flask or Django for routing, authentication, and logging.

Real-Life Analogy:
    Think of a decorator like gift wrapping. The original function is the gift inside. The gift wrapper (decorator) adds shiny paper and a bow to make it look nicer before and after it is presented, but the gift itself remains exactly the same.

Key Concepts:
    - Functions are first-class citizens in Python.
    - Inner functions (functions inside functions).
    - Returning functions from functions.
    - The @ syntactic sugar.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def simple_decorator(func):
    """A basic decorator that prints before and after the function execution."""
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@simple_decorator
def say_hello():
    """A simple function to say hello."""
    print("Hello, world!")

# Without the @ syntax, it would look like this:
# say_hello = simple_decorator(say_hello)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def log_execution(func):
    """Decorator to log when a function is executed."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished '{func.__name__}'")
        return result
    return wrapper

@log_execution
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

@log_execution
def greet_person(name: str, greeting: str = "Hello"):
    """Greets a person."""
    print(f"{greeting}, {name}!")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

import time

def measure_time(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIME] {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@measure_time
def slow_function():
    """A function that simulates a time-consuming task."""
    print("Starting a slow task...")
    time.sleep(1)
    print("Finished the slow task.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Forgetting to return the inner wrapper function.
# Mistake 2: Forgetting to use *args and **kwargs in the wrapper, limiting the decorator to specific signatures.

def bad_decorator(func):
    def wrapper():
        # This will fail if the decorated function takes arguments!
        func() 
    return wrapper

# Best Practice: Always use *args and **kwargs in your wrapper to ensure it works with any function signature.
def good_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a decorator in Python?
# A1: A decorator is a function that takes another function, extends its behavior, and returns a new function without modifying the original function's code.

# Q2: How does the @ symbol work in Python?
# A2: The @ symbol is syntactic sugar. `@decorator def func()` is equivalent to `func = decorator(func)`.

# Q3: Can a function have multiple decorators?
# A3: Yes, decorators can be chained. They are applied from the bottom up (closest to the function first).

# Q4: Why do we use *args and **kwargs in decorators?
# A4: To allow the decorator to wrap any function regardless of its parameter signature.

# Q5: What is a higher-order function?
# A5: A function that takes another function as an argument, or returns a function, or both. Decorators are an application of higher-order functions.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a decorator `uppercase_result` that converts the string returned by a function to uppercase.
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_result
def get_greeting():
    return "good morning"

# Exercise 2: Write a decorator `double_result` that doubles the numeric result of a function.
def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Create an authentication decorator.
# Write a decorator `requires_auth` that checks a global variable `IS_AUTHENTICATED`.
# If true, it runs the function; if false, it prints "Access Denied" and returns None.

IS_AUTHENTICATED = False

def requires_auth(func):
    def wrapper(*args, **kwargs):
        if IS_AUTHENTICATED:
            return func(*args, **kwargs)
        else:
            print("Access Denied!")
            return None
    return wrapper

@requires_auth
def view_secret_dashboard():
    print("Welcome to the secret dashboard!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Decorators wrap functions to add functionality.
# - They utilize Python's first-class functions (functions as objects).
# - Use the @ syntax for cleaner application.
# - Always design wrappers with *args and **kwargs for flexibility.

if __name__ == "__main__":
    print("--- Basic Syntax ---")
    say_hello()
    
    print("\n--- Practical Examples ---")
    add_numbers(5, 7)
    greet_person("Alice", greeting="Hi")
    
    print("\n--- Advanced Usage ---")
    slow_function()
    
    print("\n--- Practice Exercises ---")
    print(f"Uppercase greeting: {get_greeting()}")
    
    print("\n--- Mini Challenge ---")
    view_secret_dashboard()
    IS_AUTHENTICATED = True
    print("Logging in...")
    view_secret_dashboard()
