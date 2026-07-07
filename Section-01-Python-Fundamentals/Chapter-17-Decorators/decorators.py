"""Learning file for Decorators."""

# Topic Name: Decorators
# Level: Advanced
# Decorators wrap functions to add behavior without changing the original function body.
# Read the theory first, then run this file and modify examples.

# Theory
# Decorators wrap functions to add behavior without changing the original function body.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# @decorator
# def function(): ...

# Practice Programs
# 1. Write a decorator that logs function calls.
# 2. Create a timer decorator.
# 3. Stack validation and formatting decorators.

# Mini Project
# Build a tiny program that uses decorators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does a decorator return?
# A1. Usually a wrapper function that replaces or enhances the original function.
# Q2. Why use functools.wraps?
# A2. It preserves metadata such as the original function name and docstring.

# Examples and practice implementations start below.
from functools import wraps


def uppercase_result(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()

    return wrapper


@uppercase_result
def greet(name):
    return f"Hello, {name}"


def practice_repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return [function(*args, **kwargs) for _ in range(times)]

        return wrapper

    return decorator


def main():
    print("--- Decorators ---")
    print(greet("Asha"))

    @practice_repeat(3)
    def say_done():
        return "done"

    print(say_done())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Decorators ---
# HELLO, ASHA
# ['done', 'done', 'done']
# End Expected Output
