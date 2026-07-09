"""
Topic: Import Basics
Chapter: 13
Level: Beginner

Description:
    Modules in Python are simply Python files with the .py extension, containing Python definitions and statements.
    To use these definitions (like functions, classes, and variables) in another file, you use the `import` statement.

Real-Life Analogy:
    Imagine you are building a car. You don't manufacture every single bolt and wire yourself; instead, you source parts
    from different suppliers. Importing a module is like bringing in a pre-made engine or stereo system from a supplier 
    so you can use it in your car.

Key Concepts:
    - import statement
    - from ... import ...
    - aliasing using `as`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Basic import
import math

# Using a function from the imported module
result = math.sqrt(16)
print(f"Square root of 16 is: {result}")

# Importing specific functions from a module
from math import pi, pow

print(f"Value of pi: {pi}")
print(f"2 to the power of 3: {pow(2, 3)}")

# Aliasing a module for convenience
import datetime as dt

current_time = dt.datetime.now()
print(f"Current time: {current_time}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

import random

def generate_random_password(length: int) -> str:
    """Generates a random password of given length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print(f"Random 12-char password: {generate_random_password(12)}")

from statistics import mean, median

def analyze_scores(scores: list[float]) -> dict[str, float]:
    """Returns the mean and median of a list of scores."""
    return {
        "mean": mean(scores),
        "median": median(scores)
    }

scores_list = [85.5, 90.0, 78.5, 92.0, 88.0]
print(f"Score analysis: {analyze_scores(scores_list)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Using importlib for dynamic imports
import importlib

def dynamic_import(module_name: str):
    """Dynamically imports a module based on a string name."""
    try:
        module = importlib.import_module(module_name)
        print(f"Successfully imported {module_name}")
        return module
    except ImportError:
        print(f"Failed to import {module_name}")
        return None

json_module = dynamic_import("json")
if json_module:
    data = json_module.dumps({"key": "value"})
    print(f"Serialized data: {data}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Shadowing built-in module names
# If you name your file `math.py`, you won't be able to import the built-in `math` module.

# Mistake 2: Wildcard imports (from module import *)
# This pollutes the global namespace and makes it hard to track where functions came from.
# Bad: from math import *
# Good: from math import sin, cos

# Best Practice: Keep imports at the top of the file.
# Best Practice: Order imports: standard library, third-party, local application/library specific.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between `import module` and `from module import function`?
# A: `import module` brings the module object into your namespace, requiring `module.function()`. 
#    `from module import function` brings only the specific function directly into your namespace.

# Q2: Why is `from module import *` considered bad practice?
# A: It makes it unclear which names are present in the namespace, confusing readers and static analysis tools. 
#    It can also lead to naming conflicts if multiple modules define the same name.

# Q3: How do you rename a module upon import?
# A: By using the `as` keyword, e.g., `import pandas as pd`.

# Q4: What happens if you import a module multiple times?
# A: Python caches the imported module in `sys.modules`. Subsequent imports just fetch the cached reference, 
#    so the module code is only executed once.

# Q5: Can you import a module conditionally?
# A: Yes, you can place `import` statements inside `if` blocks or functions.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Import the `os` module and print the current working directory.
# Exercise 2: Import `choice` from `random` and pick a random fruit from a list.
# Exercise 3: Import the `time` module as `t` and use `t.sleep(1)` to pause execution for 1 second.

def practice_exercises():
    # 1
    import os
    print(f"Current Directory: {os.getcwd()}")
    
    # 2
    from random import choice
    fruits = ["apple", "banana", "cherry"]
    print(f"Random fruit: {choice(fruits)}")
    
    # 3
    import time as t
    print("Sleeping...")
    t.sleep(1)
    print("Awake!")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Write a function that imports the `calendar` module and prints the calendar for the current month.
# Use `datetime` to get the current year and month.

def print_current_month_calendar():
    import calendar
    import datetime
    
    now = datetime.datetime.now()
    cal = calendar.month(now.year, now.month)
    print("Current Month Calendar:")
    print(cal)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The `import` statement allows you to use code from other files.
# - `from ... import ...` imports specific components.
# - Use `as` to alias modules or functions to avoid name collisions or for brevity.
# - Avoid wildcard imports (`*`) to maintain clean namespaces.
# - Dynamic imports can be achieved using the `importlib` module.

if __name__ == "__main__":
    practice_exercises()
    print_current_month_calendar()
