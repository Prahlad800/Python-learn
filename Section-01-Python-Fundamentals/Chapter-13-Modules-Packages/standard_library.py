"""
Topic: The Standard Library
Chapter: 13
Level: Beginner

Description:
    Python comes with "batteries included" – a large and powerful standard library.
    It contains built-in modules that provide solutions for many everyday programming tasks,
    such as file I/O, system calls, networking, and data manipulation.

Real-Life Analogy:
    Buying a smartphone that comes pre-installed with essential apps like a calculator, calendar, 
    and web browser. You don't have to download them; they are already there, ready to use.

Key Concepts:
    - Batteries included philosophy
    - Commonly used modules (os, sys, math, datetime, json, re)
    - Avoiding reinvention of the wheel
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The standard library is available immediately. You just need to import the modules.
import math
import datetime
import os

print(f"Pi is approximately {math.pi:.4f}")
print(f"Today is {datetime.date.today()}")
print(f"Current OS name: {os.name}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: JSON manipulation (json)
import json

data = {"name": "Alice", "age": 30, "city": "Wonderland"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

parsed_data = json.loads(json_string)
print(f"Parsed data age: {parsed_data['age']}")

# Example 2: Regular Expressions (re)
import re

email = "user@example.com"
is_valid = bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))
print(f"Is {email} a valid email format? {is_valid}")

# Example 3: Collections (collections)
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word counts: {word_count}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Using sys to interact with the Python interpreter
import sys

def check_python_version():
    """Checks the current python version."""
    version = sys.version_info
    print(f"Running Python {version.major}.{version.minor}.{version.micro}")

# Using itertools for efficient looping
import itertools

def generate_combinations():
    """Generates combinations of 2 from a list."""
    items = ['A', 'B', 'C']
    combs = list(itertools.combinations(items, 2))
    print(f"Combinations of {items}: {combs}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Re-implementing standard library functions.
# Don't write your own JSON parser or URL encoder. The standard library versions are 
# heavily tested, optimized, and secure.

# Best Practice: Familiarize yourself with the Python Module Index in the official documentation.
# Best Practice: Prefer standard library modules over third-party ones for basic tasks to reduce dependencies.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does "batteries included" mean in Python?
# A: It means Python comes with a large, robust standard library that can handle many common tasks 
#    without requiring third-party package installation.

# Q2: Which module would you use to interact with the operating system?
# A: The `os` module (and `pathlib` for paths).

# Q3: How do you parse a date string into a datetime object?
# A: Using `datetime.datetime.strptime()`.

# Q4: What is the purpose of the `sys` module?
# A: It provides access to some variables used or maintained by the interpreter and to functions 
#    that interact strongly with the interpreter (like `sys.argv`, `sys.exit`).

# Q5: Which module provides specialized container datatypes?
# A: The `collections` module (e.g., `Counter`, `defaultdict`, `namedtuple`).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Use `random` to generate a random number between 1 and 100
    import random
    print(f"Random number: {random.randint(1, 100)}")
    
    # Exercise 2: Use `urllib.parse` to parse a URL
    from urllib.parse import urlparse
    url = "https://www.example.com/path/to/page?name=ferret&color=purple"
    parsed = urlparse(url)
    print(f"Domain: {parsed.netloc}, Path: {parsed.path}, Query: {parsed.query}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Write a script that uses `random`, `string`, and `datetime`.
# It should generate a 10-character random string, and print it alongside the current timestamp.

def run_mini_challenge():
    import random
    import string
    import datetime
    
    chars = string.ascii_letters + string.digits
    random_str = "".join(random.choices(chars, k=10))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{now}] Generated ID: {random_str}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The Python Standard Library is a huge collection of pre-written modules.
# - It covers file I/O, networking, data structures, math, text processing, and more.
# - Always check the standard library before writing a complex utility function or installing a third-party package.

if __name__ == "__main__":
    check_python_version()
    generate_combinations()
    practice_exercises()
    run_mini_challenge()
