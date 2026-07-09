"""
Topic: Higher-Order Functions
Chapter: 7
Level: Intermediate

Description:
    A higher-order function is a function that either takes one or more functions as arguments, returns a function as its result, or both. They allow you to pass behavior around as data.

Real-Life Analogy:
    Think of a higher-order function as a manager in a company. The manager (higher-order function) takes instructions on what needs to be done and delegates the specific tasks to different employees (functions passed as arguments).

Key Concepts:
    - Functions as first-class citizens
    - Passing functions as arguments
    - Returning functions
    - Built-in higher-order functions (map, filter, reduce)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def shout(text: str) -> str:
    return text.upper()

def whisper(text: str) -> str:
    return text.lower()

# Higher-order function that takes another function as an argument
def greet(func, text: str):
    # 'func' is expected to be a callable (function)
    greeting = func(text)
    print(greeting)

print("--- Section 1 ---")
# Passing 'shout' and 'whisper' as arguments. We don't use (), we pass the name!
greet(shout, "Hello World")
greet(whisper, "Hello World")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

print("\n--- Section 2 ---")

# Example 1: Custom mapping function
def apply_to_list(func, data: list) -> list:
    """Applies a function to every item in a list."""
    result = []
    for item in data:
        result.append(func(item))
    return result

numbers = [1, 2, 3, 4, 5]
def square(x): return x * x

squared_numbers = apply_to_list(square, numbers)
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")

# Example 2: Returning a function
def get_math_operation(operator: str):
    def add(x, y): return x + y
    def subtract(x, y): return x - y
    
    if operator == '+':
        return add
    elif operator == '-':
        return subtract
    else:
        raise ValueError("Invalid operator")

math_func = get_math_operation('+')
print(f"Result of returned function (10 + 5): {math_func(10, 5)}")

# ============================================================
# SECTION 3: ADVANCED USAGE (BUILT-IN FUNCTIONS)
# ============================================================

print("\n--- Section 3 ---")
from functools import reduce

# Python has built-in higher order functions: map, filter, reduce

# 1. map(function, iterable)
# Applies function to every item of iterable
words = ["hello", "world", "python"]
lengths = list(map(len, words))
print(f"Lengths using map: {lengths}")

# 2. filter(function, iterable)
# Returns items from iterable where function returns True
def is_even(n): return n % 2 == 0
evens = list(filter(is_even, [1, 2, 3, 4, 5, 6]))
print(f"Evens using filter: {evens}")

# 3. reduce(function, iterable)
# Applies function of two arguments cumulatively to the items of iterable
# Note: In Python 3, reduce was moved to functools
def multiply(x, y): return x * y
product = reduce(multiply, [1, 2, 3, 4]) # (1*2) -> (2*3) -> (6*4) -> 24
print(f"Product using reduce: {product}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Calling the function instead of passing it
# INCORRECT: apply_to_list(square(), numbers) -> TypeError
# CORRECT: apply_to_list(square, numbers)
# You want to pass the function object, not the result of executing it.

# Best Practice: Use list comprehensions where applicable.
# While map and filter are great, list comprehensions are often considered more "Pythonic" and readable.
# Map equivalent: [square(x) for x in numbers]
# Filter equivalent: [x for x in [1,2,3,4,5,6] if is_even(x)]

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What makes a function a "higher-order function"?
# A: It either takes one or more functions as arguments, or it returns a function.

# Q2: In Python, why can you pass functions as arguments?
# A: Because functions in Python are "first-class citizens". They are objects, just like integers, strings, or lists, and can be passed around, assigned to variables, and returned.

# Q3: What is the difference between map() and filter()?
# A: `map()` transforms each item in an iterable by applying a function. `filter()` returns only the items for which the function evaluates to True.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a higher-order function `do_twice` that takes a function `f` and a value `x`, and applies `f` to `x` twice: `f(f(x))`.
def do_twice(f, x):
    return f(f(x))

def add_two(n): return n + 2

print("\n--- Practice Exercises ---")
print(f"do_twice with add_two starting at 5: {do_twice(add_two, 5)}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create a higher-order function `timer` that takes a function, runs it, and prints how long it took to execute.
import time

def timer(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Function {func.__name__} took {end_time - start_time:.5f} seconds to execute.")
    return result

def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

print("\n--- Mini Challenge ---")
timer(slow_function, 1000000)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Higher-order functions accept functions as arguments or return them.
# - Functions are objects and can be handled like any other data type.
# - `map`, `filter`, and `reduce` are standard higher-order functions.
# - When passing a function as an argument, omit the parentheses so it doesn't execute immediately.

if __name__ == "__main__":
    pass
