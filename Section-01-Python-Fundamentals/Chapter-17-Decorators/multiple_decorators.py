"""Learning file for Multiple Decorators."""

# Topic Name: Multiple Decorators
# Level: Advanced
# Multiple decorators stack wrappers and run in a predictable order.
# Read the theory first, then run this file and modify examples.

# Theory
# Multiple decorators stack wrappers and run in a predictable order.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# @outer
# @inner
# def function(): ...

# Practice Programs
# 1. Write a decorator that logs function calls.
# 2. Create a timer decorator.
# 3. Stack validation and formatting decorators.

# Mini Project
# Build a tiny program that uses multiple decorators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does a decorator return?
# A1. Usually a wrapper function that replaces or enhances the original function.
# Q2. Why use functools.wraps?
# A2. It preserves metadata such as the original function name and docstring.

# Examples and practice implementations start below.
from functools import wraps


def add_prefix(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return "Result: " + function(*args, **kwargs)

    return wrapper


def add_suffix(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) + "!"

    return wrapper


@add_prefix
@add_suffix
def message():
    return "success"


def main():
    print("--- Multiple Decorators ---")
    print(message())
    print("Order: function -> add_suffix -> add_prefix")


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Multiple Decorators ---
# Result: success!
# Order: function -> add_suffix -> add_prefix
# End Expected Output
