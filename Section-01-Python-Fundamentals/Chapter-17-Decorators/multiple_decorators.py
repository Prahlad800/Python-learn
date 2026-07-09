"""
Topic: Chaining Multiple Decorators
Chapter: 17
Level: Intermediate

Description:
    In Python, you can apply more than one decorator to a single function. 
    This is called decorator chaining. The decorators are applied from the bottom up, 
    meaning the decorator closest to the function is executed first, wrapping the function. 
    The next decorator then wraps the result of the previous one.

Real-Life Analogy:
    Think of putting on winter clothes. First, you put on a shirt (the original function). 
    Then you put on a sweater (inner decorator). Finally, you put on a heavy coat (outer decorator). 
    The sweater is applied first because it's closest to the shirt.

Key Concepts:
    - Multiple decorators using stacked `@` syntax.
    - Order of execution (bottom to top for wrapping, top to bottom for execution flow).
    - Separation of concerns by composing multiple small decorators.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@make_bold
@make_italic
def format_text():
    return "Hello, World!"

# This is equivalent to:
# format_text = make_bold(make_italic(format_text))

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def log_route(func):
    def wrapper(*args, **kwargs):
        print(f"[ROUTING] Accessing route: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def require_authentication(func):
    def wrapper(*args, **kwargs):
        print("[AUTH] Checking user credentials...")
        # Assume valid for this example
        print("[AUTH] User authenticated.")
        return func(*args, **kwargs)
    return wrapper

# The order matters! We want to log the route access before authenticating.
@log_route
@require_authentication
def view_profile(user_id):
    return f"Profile data for user {user_id}"

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

import time

def retry(times):
    """Decorator to retry a function if it fails."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}. Retrying...")
                    time.sleep(0.5)
            raise Exception(f"Failed after {times} attempts.")
        return wrapper
    return decorator

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution took {end - start:.4f}s")
        return result
    return wrapper

@measure_time
@retry(times=3)
def unstable_network_call():
    import random
    if random.choice([True, False, False]):
        raise ConnectionError("Network timeout")
    return "Data retrieved successfully!"

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Getting the order wrong.
# If you place `@require_authentication` above `@log_route`, a failed authentication 
# might prevent the route access from being logged at all!

# Best Practice: Think of decorators as an onion. 
# The one on top is the outermost layer and is entered first during execution, 
# but applied last during function creation.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What happens when you apply multiple decorators to a function?
# A1: They are chained. The function is wrapped by the bottom-most decorator first, and the resulting wrapper is wrapped by the decorator above it.

# Q2: In what order do decorators execute?
# A2: When the function is CALLED, execution flows from the top decorator down to the function, and then returns back up the chain.

# Q3: Can a function have three or more decorators?
# A3: Yes, there is no hard limit to how many decorators you can chain.

# Q4: Why is decorator composition useful?
# A4: It adheres to the Single Responsibility Principle. Instead of one massive decorator doing logging, timing, and auth, you have three distinct decorators.

# Q5: Does `functools.wraps` work with multiple decorators?
# A5: Yes, as long as every decorator in the chain uses `functools.wraps`, the original function's metadata will bubble up to the outermost wrapper.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write two decorators: `@split_string` and `@to_lowercase`.
# Apply them to a function returning "HELLO WORLD" so it returns ['hello', 'world'].

def to_lowercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper

def split_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.split()
    return wrapper

@split_string
@to_lowercase
def get_message():
    return "HELLO WORLD"

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Combine a parameter validation decorator and an output formatting decorator.
def validate_positive(func):
    def wrapper(amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return func(amount)
    return wrapper

def format_currency(func):
    def wrapper(amount):
        result = func(amount)
        return f"${result:.2f}"
    return wrapper

@format_currency
@validate_positive
def get_discount(amount):
    return amount * 0.90  # 10% discount

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Multiple decorators can be stacked on a single function.
# - Wrapping happens Bottom -> Up.
# - Execution flow happens Top -> Down (and back Up for the return).
# - Chaining promotes modular, reusable decorator functions.

if __name__ == "__main__":
    print("--- Basic Syntax ---")
    print(format_text())
    
    print("\n--- Practical Examples ---")
    print(view_profile(101))
    
    print("\n--- Advanced Usage ---")
    try:
        print(unstable_network_call())
    except Exception as e:
        print(e)
        
    print("\n--- Practice Exercises ---")
    print(get_message())
    
    print("\n--- Mini Challenge ---")
    print(f"Discounted amount: {get_discount(100)}")
    try:
        get_discount(-50)
    except ValueError as e:
        print(f"Caught error: {e}")
