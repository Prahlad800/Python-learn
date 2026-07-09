"""
Topic: The `operator` and `math` Modules
Chapter: 3
Level: Intermediate

Description:
    While Python has built-in symbols for operators (+, -, *, /), it also provides the `operator` module which contains function equivalents.
    The `math` module extends basic arithmetic with complex mathematical functions.

Real-Life Analogy:
    Using basic operators is like doing math on paper. Using the `operator` and `math` modules is like upgrading to a scientific calculator with pre-programmed functions.

Key Concepts:
    - operator.add, operator.sub, etc.
    - Using operators as functions for higher-order functions (like map, filter, reduce)
    - Advanced math operations from the math module
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import operator
import math

def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    a = 10
    b = 5
    
    # Equivalent to a + b
    res_add = operator.add(a, b)
    print(f"operator.add({a}, {b}) = {res_add}")
    
    # Equivalent to a * b
    res_mul = operator.mul(a, b)
    print(f"operator.mul({a}, {b}) = {res_mul}")
    
    # Using math module
    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.factorial(5) = {math.factorial(5)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================
from functools import reduce

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    numbers = [1, 2, 3, 4, 5]
    
    # Using reduce with operator.mul to get the product of a list
    product = reduce(operator.mul, numbers)
    print(f"Product of {numbers}: {product}")
    
    # Sorting a list of dictionaries by a specific key using itemgetter
    data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    sorted_data = sorted(data, key=operator.itemgetter('age'))
    print(f"Sorted data by age: {sorted_data}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    class CustomObj:
        def __init__(self, val):
            self.val = val
        def __repr__(self):
            return f"CustomObj({self.val})"
            
    objs = [CustomObj(5), CustomObj(1), CustomObj(3)]
    # operator.attrgetter is highly optimized in C
    objs.sort(key=operator.attrgetter('val'))
    print(f"Sorted objects by 'val' attribute: {objs}")
    
    # Method caller
    s = "hello world"
    up = operator.methodcaller('upper')
    print(f"Method caller 'upper' on '{s}': {up(s)}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Re-inventing the wheel using lambdas when an operator function exists (e.g., lambda x, y: x + y instead of operator.add).
# 2. Forgetting to import the module before using it.
#
# Best Practices:
# 1. Use `operator.itemgetter` and `operator.attrgetter` for sorting; they are faster and more readable than lambdas.
# 2. Rely on the `math` module for standard mathematical constants (math.pi, math.e) instead of hardcoding them.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: Why use `operator.add` instead of just using `+`?
# A: When you need to pass an operation as a function argument (e.g., to `reduce()` or `map()`), `operator.add` is much cleaner than writing a lambda.
#
# Q2: What does `operator.itemgetter(1)` do?
# A: It returns a callable that fetches the item at index 1 from its operand. Commonly used as a `key` function in sorting.
#
# Q3: Is `math.pow(x, y)` exactly the same as `x ** y`?
# A: Mostly, but `math.pow()` converts both arguments to floats and always returns a float, while `**` can return integers and handle complex numbers.
#
# Q4: How do you find the GCD of two numbers in Python?
# A: Using `math.gcd(a, b)`.
#
# Q5: What's the difference between `math.floor()` and `math.trunc()`?
# A: For positive numbers they are the same. For negative numbers, `math.floor(-2.5)` returns `-3` (moves towards negative infinity), while `math.trunc(-2.5)` returns `-2` (moves towards zero).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Use `reduce` and `operator.add` to sum a list of numbers.
# 2. Sort a list of tuples representing (x, y) coordinates based on the y-coordinate using `operator.itemgetter`.
# 3. Calculate the area of a circle using `math.pi`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # You have a list of user records. Filter out underage users, 
    # then sort the remaining users by their score in descending order using operator functions.
    users = [
        {"name": "Alice", "age": 22, "score": 85},
        {"name": "Bob", "age": 17, "score": 90},
        {"name": "Charlie", "age": 25, "score": 95},
        {"name": "Dave", "age": 19, "score": 80}
    ]
    
    # Filter using a list comprehension (or filter + lambda)
    adults = [u for u in users if u['age'] >= 18]
    
    # Sort using operator.itemgetter
    adults.sort(key=operator.itemgetter('score'), reverse=True)
    
    print("Top adult players:")
    for u in adults:
        print(f"{u['name']}: {u['score']}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - The `operator` module provides functional equivalents to built-in operators.
# - It is especially useful with higher-order functions like map, filter, and reduce.
# - `itemgetter` and `attrgetter` are powerful tools for sorting data structures.
# - The `math` module is the standard for advanced mathematical computations.

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mini_challenge()
