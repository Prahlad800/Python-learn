"""
Topic: Decorator Practice Exercises
Chapter: 17
Level: Intermediate

Description:
    This file contains a series of exercises to test your understanding of decorators.
    Try to solve them without looking at the solutions in the previous files.

Real-Life Analogy:
    Like a gym circuit training session. You'll rotate through different exercises focusing on various muscles: syntax, arguments, wraps, and classes.

Key Concepts:
    - Applying decorators.
    - Writing custom decorators.
    - Parameterized decorators.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Exercise 1: Write a decorator `greet` that prints "Welcome!" before calling the function.
def greet(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        return func(*args, **kwargs)
    return wrapper

@greet
def say_name(name):
    print(f"My name is {name}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Exercise 2: Write a decorator `timer` that prints how long a function takes to execute.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.5f}s")
        return result
    return wrapper

@timer
def count_to_million():
    return sum(range(1000000))

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Exercise 3: Write a decorator with arguments `repeat(n)` that runs the function `n` times.
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def alert():
    print("WARNING!")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Exercise 4: Fix this broken decorator!
# Hint: it doesn't return anything, and it doesn't accept arguments.
"""
def broken_logger(func):
    def wrapper():
        print("Logging...")
        func()
    return wrapper
"""

# Fixed version:
def fixed_logger(func):
    def wrapper(*args, **kwargs):
        print("Logging...")
        return func(*args, **kwargs)
    return wrapper

@fixed_logger
def add(x, y):
    return x + y

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Mentally answer these:
# 1. Why do we need `*args` and `**kwargs` in the wrapper function?
# 2. What happens if you forget to return the original function's result inside the wrapper?
# 3. How do you preserve the original function's name and docstring?

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 5: Write a class-based decorator `LimitCalls` that only allows a function to be called X times.
class LimitCalls:
    def __init__(self, limit):
        self.limit = limit
        self.calls = 0
        self.func = None
        
    def __call__(self, func):
        self.func = func
        def wrapper(*args, **kwargs):
            if self.calls >= self.limit:
                print("Call limit reached.")
                return None
            self.calls += 1
            return self.func(*args, **kwargs)
        return wrapper

# Note: Using it as @LimitCalls(2) means __call__ acts as the decorator factory!
@LimitCalls(2)
def ping():
    print("Pong!")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Create an HTML tag generator decorator.
# It should take a tag name as an argument (e.g., 'b', 'i', 'p') and wrap the function's return value in that HTML tag.

def html_tag(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return f"<{tag}>{content}</{tag}>"
        return wrapper
    return decorator

@html_tag("b")
@html_tag("i")
def generate_text():
    return "Important text"

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# Practice makes perfect! Understanding the 3 levels of nesting in parameterized decorators is the hardest part.

if __name__ == "__main__":
    print("--- Exercise 1 ---")
    say_name("Alice")
    
    print("\n--- Exercise 2 ---")
    count_to_million()
    
    print("\n--- Exercise 3 ---")
    alert()
    
    print("\n--- Exercise 4 ---")
    print("Result:", add(5, 7))
    
    print("\n--- Exercise 5 ---")
    ping()
    ping()
    ping() # Limit reached
    
    print("\n--- Mini Challenge ---")
    print(generate_text())
