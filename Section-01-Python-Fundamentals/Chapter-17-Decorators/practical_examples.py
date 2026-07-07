"""Learning file for Practical Decorator Examples."""

# Topic Name: Practical Decorator Examples
# Level: Advanced
# Practical decorators solve logging, timing, caching, validation, and permission problems.
# Read the theory first, then run this file and modify examples.

# Theory
# Practical decorators solve logging, timing, caching, validation, and permission problems.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# @timer
# @requires_role('admin')
# @memoize

# Practice Programs
# 1. Write a decorator that logs function calls.
# 2. Create a timer decorator.
# 3. Stack validation and formatting decorators.

# Mini Project
# Build a tiny program that uses practical decorator examples
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What does a decorator return?
# A1. Usually a wrapper function that replaces or enhances the original function.
# Q2. Why use functools.wraps?
# A2. It preserves metadata such as the original function name and docstring.

# Examples and practice implementations start below.
from functools import wraps


def require_role(required_role):
    def decorator(function):
        @wraps(function)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != required_role:
                return "Permission denied"
            return function(user, *args, **kwargs)

        return wrapper

    return decorator


def memoize(function):
    cache = {}

    @wraps(function)
    def wrapper(number):
        if number not in cache:
            cache[number] = function(number)
        return cache[number]

    return wrapper


@require_role("admin")
def delete_user(user, username):
    return f"{username} deleted by {user['name']}"


@memoize
def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def main():
    print("--- Practical Decorator Examples ---")
    print(delete_user({"name": "Asha", "role": "admin"}, "old_user"))
    print("Fib 8:", fibonacci(8))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Practical Decorator Examples ---
# old_user deleted by Asha
# Fib 8: 21
# End Expected Output
