"""
Topic: Common Decorator Patterns
Chapter: 17
Level: Intermediate

Description:
    Certain patterns of decorators appear repeatedly in software engineering.
    Understanding these patterns helps you recognize and build robust, reusable decorators for common tasks.

Real-Life Analogy:
    Common patterns are like standard templates for documents. Instead of creating a contract from scratch, you use a template. In coding, instead of rewriting caching or retry logic everywhere, you use a standard decorator pattern.

Key Concepts:
    - Retries and backoffs.
    - Input validation.
    - Type enforcement.
    - Event registration.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import functools

# The Registration Pattern
# Often used in frameworks like Flask routing or event systems.
REGISTRY = {}

def register(name):
    """Registers a function in a global dictionary."""
    def decorator(func):
        REGISTRY[name] = func
        return func  # Note: we return the ORIGINAL function, not a wrapper!
    return decorator

@register("add")
def add(a, b):
    return a + b

@register("sub")
def subtract(a, b):
    return a - b

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# The Retry Pattern
import time

def retry_on_exception(exceptions=(Exception,), tries=3, delay=1):
    """Retries a function if it raises specified exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed with {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            raise RuntimeError(f"Function failed after {tries} attempts.")
        return wrapper
    return decorator

@retry_on_exception(exceptions=(ValueError,), tries=2)
def unstable_parse(data):
    if data == "bad":
        raise ValueError("Bad data format")
    return "Parsed Data"

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# The State Injector Pattern
# Injects extra arguments (like context, DB connections, etc.) into the function.

def inject_db_connection(func):
    """Injects a mock DB connection into the kwargs."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Setup DB (mock)
        db_conn = "[Database Connection Object]"
        # Inject it
        kwargs['db'] = db_conn
        
        try:
            return func(*args, **kwargs)
        finally:
            # Teardown DB
            print(f"Closing {db_conn}")
    return wrapper

@inject_db_connection
def get_user_data(user_id, db=None):
    print(f"Fetching user {user_id} using {db}")
    return {"id": user_id, "name": "Alice"}

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Injecting arguments that the original function isn't prepared to handle.
# If `get_user_data` didn't have `db=None` in its signature, `kwargs['db']` would cause a TypeError.

# Best Practice: Use standard patterns. Don't reinvent the wheel if libraries like `tenacity` (for retries) already exist.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a registration decorator?
# A1: A decorator that adds a function to a registry (like a dictionary) but usually returns the function unmodified.

# Q2: How do you implement a retry decorator?
# A2: By wrapping the function call in a `while` loop and a `try-except` block inside the wrapper function.

# Q3: Can a decorator change the arguments passed to a function?
# A3: Yes, a wrapper can inspect, modify, or add new arguments before calling the original function.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Create a `@require_role` decorator pattern that checks a global `CURRENT_ROLE` variable.
CURRENT_ROLE = "guest"

def require_role(role_needed):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_ROLE != role_needed:
                print(f"Access denied! Requires {role_needed}, you are {CURRENT_ROLE}.")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_database():
    print("Database deleted.")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Create a `@suppress_errors` decorator pattern that catches specific exceptions and returns a default value instead.

def suppress_errors(exceptions, default_return=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                print(f"Suppressed error: {e}")
                return default_return
        return wrapper
    return decorator

@suppress_errors((ZeroDivisionError,), default_return=0)
def divide(a, b):
    return a / b

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Registry Pattern: Stores functions without modifying them.
# - Retry Pattern: Handles transient failures.
# - Injection Pattern: Provides context/resources to a function seamlessly.
# - Authorization/Role Pattern: Standard way to protect routes or methods.

if __name__ == "__main__":
    print("--- Basic Syntax (Registry) ---")
    print("Registry keys:", REGISTRY.keys())
    print("10 + 5 =", REGISTRY["add"](10, 5))
    
    print("\n--- Practical Examples (Retry) ---")
    try:
        unstable_parse("bad")
    except RuntimeError as e:
        print(e)
        
    print("\n--- Advanced Usage (Injection) ---")
    get_user_data(42)
    
    print("\n--- Practice Exercises ---")
    delete_database()
    
    print("\n--- Mini Challenge ---")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")
