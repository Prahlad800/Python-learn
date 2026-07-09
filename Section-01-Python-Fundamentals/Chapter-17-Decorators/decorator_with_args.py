"""
Topic: Decorators with Arguments
Chapter: 17
Level: Intermediate

Description:
    Sometimes we want our decorators to take their own arguments to customize their behavior. 
    To achieve this, we need a "decorator factory"—a function that takes the arguments and returns a decorator.

Real-Life Analogy:
    Imagine buying a custom coffee. The barista (decorator factory) takes your preferences like "extra shot" or "almond milk" (arguments), and creates a customized process (decorator) to prepare your base coffee (original function).

Key Concepts:
    - Decorator factories (functions returning decorators).
    - Three levels of nested functions.
    - Passing arguments to control decorator behavior dynamically.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def repeat(num_times: int):
    """
    Decorator factory that repeats the execution of the decorated function.
    Notice the 3 levels of nesting: factory -> decorator -> wrapper.
    """
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name: str):
    """Greets someone multiple times."""
    print(f"Hello, {name}!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def delay_execution(seconds: int):
    """Decorator that delays function execution by a given number of seconds."""
    import time
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Sleeping for {seconds} second(s) before calling {func.__name__}...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay_execution(seconds=1)
def quick_task():
    print("Task completed after delay.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def type_check(*arg_types):
    """
    Decorator that checks if the positional arguments match the specified types.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check length to avoid index out of bounds
            if len(args) != len(arg_types):
                raise ValueError(f"Expected {len(arg_types)} arguments, got {len(args)}")
            
            for i, (arg, expected_type) in enumerate(zip(args, arg_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} must be {expected_type.__name__}, got {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def multiply(a, b):
    return a * b

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting the outer factory function when creating decorators with arguments.
# A decorator with arguments MUST return a decorator function.

# Best Practice: Use clear variable names for the three layers:
# 1. factory_name
# 2. decorator
# 3. wrapper

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How do you create a decorator that accepts arguments?
# A1: You wrap the decorator inside another function (a factory). The outer function accepts the arguments and returns the actual decorator.

# Q2: How many nested functions are required for a decorator with arguments?
# A2: Three. The factory function, the decorator function, and the wrapper function.

# Q3: Why is it called a decorator factory?
# A3: Because the outer function builds and returns a customized decorator based on the parameters passed to it.

# Q4: Can a decorator with arguments also be used without arguments?
# A4: Normally no, unless it is designed with a smart signature (using default arguments and checking if the first arg is callable), but it gets complex.

# Q5: What is the benefit of parameterized decorators?
# A5: They allow for highly reusable decorators. Instead of writing separate decorators for `@repeat_twice` and `@repeat_thrice`, you write one `@repeat(n)`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a decorator `@prefix_logger(prefix)` that prepends a string prefix to the function output log.
def prefix_logger(prefix: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_logger("[SYSTEM]")
def system_startup():
    print("System is starting...")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Create a `@rate_limit(max_calls)` decorator that limits how many times a function can be called.
# If it exceeds max_calls, it should print a warning and return None.

def rate_limit(max_calls: int):
    def decorator(func):
        # We attach state to the wrapper function itself
        wrapper.calls = 0
        def wrapper(*args, **kwargs):
            if wrapper.calls >= max_calls:
                print(f"Rate limit exceeded for {func.__name__}!")
                return None
            wrapper.calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=2)
def api_request():
    print("Fetching data from API...")
    return "Data"

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Decorators with arguments require a "factory" function.
# - The factory takes the arguments and returns the decorator.
# - The decorator takes the function and returns the wrapper.
# - This allows decorators to be customized and highly reusable.

if __name__ == "__main__":
    print("--- Basic Syntax ---")
    greet("Alice")
    
    print("\n--- Practical Examples ---")
    quick_task()
    
    print("\n--- Advanced Usage ---")
    print(f"Multiply 4 x 5 = {multiply(4, 5)}")
    try:
        multiply(4, "5") # This should raise a TypeError
    except TypeError as e:
        print(f"Caught expected error: {e}")
        
    print("\n--- Practice Exercises ---")
    system_startup()
    
    print("\n--- Mini Challenge ---")
    api_request() # call 1
    api_request() # call 2
    api_request() # call 3 - rate limit exceeded
