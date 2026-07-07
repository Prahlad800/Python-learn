# Topic: Practical Decorator Examples
# Explanation: Decorators are often used for logging, authorization, and timing.

# Syntax:
# def log_calls(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(2, 3))

# Examples:
# def log_calls(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(2, 3))

# Practice Programs:
# 1. Create a timer decorator.
2. Create a logging decorator.

# Interview Questions:
# Q: Where are decorators commonly used?
A: In frameworks and libraries for cross-cutting concerns.

# Expected Output:
# Calling add
5

def log_calls(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(2, 3))
