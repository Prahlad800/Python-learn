"""
Topic: Class Decorators
Chapter: 17
Level: Advanced

Description:
    Decorators are not limited to functions; they can also be applied to classes.
    Additionally, a decorator itself can be implemented as a class instead of a function by using the `__call__` dunder method.

Real-Life Analogy:
    Class as a Decorator: An auditing firm (class decorator) that you hire to monitor a business (the function). It holds its own state and resources.
    Decorating a Class: Adding a security system to an entire office building (class) rather than just a single room (method).

Key Concepts:
    - Decorating a class (modifying a class definition).
    - Implementing a decorator as a class using `__init__` and `__call__`.
    - Managing state within a decorator class.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# 1. Class as a Decorator (Stateful Decorator)
class CountCalls:
    """A decorator implemented as a class to keep track of function calls."""
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# 2. Decorating a Class
def add_repr(cls):
    """A class decorator that adds a __repr__ method to a class based on its attributes."""
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{cls.__name__}({attrs})"
    
    cls.__repr__ = __repr__
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Class Decorators with Arguments
class ValidateRange:
    """A class decorator with arguments to validate the return value of a function."""
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not (self.min_val <= result <= self.max_val):
                raise ValueError(f"Result {result} out of range [{self.min_val}, {self.max_val}]")
            return result
        return wrapper

@ValidateRange(min_val=0, max_val=100)
def get_score(score):
    return score

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a class decorator on a method without implementing the descriptor protocol (__get__).
# When decorating class methods with a class-based decorator, the `self` argument can get lost.

# Best Practice: For function decorators, function-based decorators are generally simpler. 
# Use class-based decorators primarily when you need to maintain complex state (like a cache or connection pool).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Can you implement a decorator as a class?
# A1: Yes, by defining the `__init__` method to accept the function and the `__call__` method to make the class instance callable like a function.

# Q2: Can you decorate a class?
# A2: Yes, a class decorator takes a class as an argument, modifies it (like adding methods or properties), and returns it.

# Q3: Why would you use a class to create a decorator instead of a function?
# A3: Classes are useful for decorators that need to maintain state (like counting calls or caching results) because instance variables are persistent across calls.

# Q4: What is the `__call__` method used for in a class decorator?
# A4: It allows an instance of the class to be called as a function. This is where the wrapper logic is placed.

# Q5: Does `functools.wraps` work on class-based decorators?
# A5: Yes, but you typically apply it inside the `__init__` method or by updating the class instance dictionary manually.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a class decorator `@singleton` that ensures only one instance of a class is ever created.

def singleton(cls):
    """A decorator that turns a class into a singleton."""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
        
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Initializing database connection...")
        self.connected = True

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Create a class-based decorator `Logger` that logs the time a function was called to a file (or just prints it).
import time

class Logger:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{timestamp}] Calling {self.func.__name__}")
        return self.func(*args, **kwargs)

@Logger
def perform_action():
    print("Action performed.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Classes can act as decorators using `__init__` and `__call__`.
# - State management is easier with class-based decorators.
# - You can decorate entire classes to augment them with new properties or methods (like dataclasses do!).
# - The Singleton pattern is commonly implemented using a class decorator.

if __name__ == "__main__":
    print("--- Basic Syntax ---")
    say_hello()
    say_hello()
    
    print("\n--- Practical Examples ---")
    p = Person("Bob", 30)
    print(p) # Uses the dynamically added __repr__
    
    print("\n--- Advanced Usage ---")
    print(f"Valid score: {get_score(85)}")
    try:
        get_score(150)
    except ValueError as e:
        print(f"Caught error: {e}")
        
    print("\n--- Practice Exercises ---")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Are db1 and db2 the same object? {db1 is db2}")
    
    print("\n--- Mini Challenge ---")
    perform_action()
