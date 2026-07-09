"""
Topic: Preserving Metadata with functools.wraps
Chapter: 17
Level: Intermediate

Description:
    When you decorate a function, the wrapper function replaces the original function. 
    This means the original function's name, docstring, and other metadata are lost. 
    The `functools.wraps` decorator is used inside your decorator to copy this metadata 
    from the original function to the wrapper function.

Real-Life Analogy:
    Imagine an undercover police officer putting on a disguise (the wrapper). 
    Without a badge, people think they are just a regular person. 
    `functools.wraps` is like giving them a badge to carry on the outside of their disguise, 
    so their true identity (name and purpose) is still known.

Key Concepts:
    - Function metadata (`__name__`, `__doc__`, `__module__`).
    - The `functools` module.
    - Best practices for writing robust decorators.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Without functools.wraps
def broken_decorator(func):
    def wrapper(*args, **kwargs):
        """This is the wrapper's docstring."""
        return func(*args, **kwargs)
    return wrapper

@broken_decorator
def example_func1():
    """This is the original function's docstring."""
    pass

print("Without wraps:")
print("Name:", example_func1.__name__)
print("Docstring:", example_func1.__doc__)

import functools

# With functools.wraps
def proper_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper's docstring, but it gets overwritten by wraps."""
        return func(*args, **kwargs)
    return wrapper

@proper_decorator
def example_func2():
    """This is the original function's docstring."""
    pass

print("\nWith wraps:")
print("Name:", example_func2.__name__)
print("Docstring:", example_func2.__doc__)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def require_ints(func):
    """A decorator to ensure all arguments are integers."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("All arguments must be integers.")
        return func(*args, **kwargs)
    return wrapper

@require_ints
def add_three_numbers(a, b, c):
    """Adds three integers together."""
    return a + b + c

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# functools.wraps is especially important when using tools like Sphinx or 
# pydoc for documentation generation, or when debugging code.

def debug_info(func):
    """Decorator that prints debug info."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} in module {func.__module__}")
        return func(*args, **kwargs)
    return wrapper

@debug_info
def process_data(data):
    """Processes a list of data items."""
    return [d * 2 for d in data]

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to use @functools.wraps when writing decorators for public APIs or libraries.
# This makes it impossible for users to access the docstrings via help(func).

# Best Practice: ALWYAS use @functools.wraps when writing a decorator. It's an industry standard.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What problem does functools.wraps solve?
# A1: It preserves the original function's metadata (like __name__ and __doc__) which would otherwise be overwritten by the wrapper function.

# Q2: How do you use functools.wraps?
# A2: You apply it as a decorator to the inner wrapper function, passing the original function as an argument: `@functools.wraps(func)`.

# Q3: Does functools.wraps modify the behavior of the decorated function?
# A3: No, it only copies the metadata attributes from the original function to the wrapper function.

# Q4: Why is preserving metadata important?
# A4: For debugging, introspection (using functions like `help()`), and documentation generators.

# Q5: Can functools.wraps be used on class methods?
# A5: Yes, it works identically on functions and class methods.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a decorator `timer` that measures execution time and uses `functools.wraps` to preserve the original docstring.
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper

@timer
def sleepy_function():
    """Sleeps for half a second."""
    time.sleep(0.5)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Create a `@deprecated` decorator.
# It should print a warning that the function is deprecated, but still execute it.
# Ensure you use `functools.wraps` so the original function's help text is intact.
import warnings

def deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(f"Call to deprecated function {func.__name__}.", category=DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)
    return wrapper

@deprecated
def old_api_call():
    """This function fetches data from the old API."""
    print("Fetching from v1 API...")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - A decorator naturally overwrites the wrapped function's identity.
# - Use `functools.wraps(func)` on the inner wrapper to fix this.
# - It is highly recommended to ALWAYS use it when writing decorators.
# - Retains `__name__`, `__doc__`, `__module__`, and annotations.

if __name__ == "__main__":
    print("\n--- Practical Examples ---")
    print(add_three_numbers(1, 2, 3))
    print("Add three numbers help:")
    help(add_three_numbers)
    
    print("\n--- Advanced Usage ---")
    print(process_data([1, 2, 3]))
    
    print("\n--- Practice Exercises ---")
    sleepy_function()
    
    print("\n--- Mini Challenge ---")
    old_api_call()
