"""
Topic: Introduction to Type Hinting
Chapter: 23
Level: Beginner

Description:
    Type hinting in Python allows you to specify the expected data types of variables, 
    function parameters, and return values. While Python remains dynamically typed at 
    runtime, type hints help developers catch errors early using static type checkers 
    like `mypy` and improve IDE autocompletion.

Real-Life Analogy:
    Imagine a sorting facility for packages. Without labels, workers have to open each 
    box to see what's inside before deciding where it goes. Type hints are like putting 
    clear labels on the boxes ("Fragile/Glass", "Books", "Electronics"), so the workers 
    (and tools) immediately know how to handle them without opening them.

Key Concepts:
    - Basic types (int, float, str, bool)
    - Variable annotations
    - Function parameter and return type annotations
    - Dynamic typing vs Static typing
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Variable Type Hinting
# We use a colon followed by the type to annotate variables.
user_age: int = 25
user_name: str = "Alice"
is_active: bool = True
account_balance: float = 1500.50

def greet_user(name: str) -> str:
    """
    A basic function with type hints.
    Takes a string 'name' and returns a string.
    """
    return f"Hello, {name}!"

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def calculate_discount(price: float, discount_percent: int) -> float:
    """
    Calculates the final price after a discount.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100.")
    discount_amount: float = price * (discount_percent / 100)
    return price - discount_amount

def is_eligible_for_loan(age: int, salary: float, has_defaults: bool) -> bool:
    """
    Determines if a user is eligible for a loan.
    """
    if has_defaults:
        return False
    if age >= 21 and salary >= 30000.0:
        return True
    return False

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# In modern Python (3.9+), built-in collections can be directly hinted
user_roles: list[str] = ["admin", "editor", "viewer"]
user_scores: dict[str, int] = {"Alice": 95, "Bob": 82}

def process_scores(scores: dict[str, int]) -> float:
    """
    Calculates the average score from a dictionary of scores.
    """
    if not scores:
        return 0.0
    total: int = sum(scores.values())
    return total / len(scores)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Assuming type hints enforce types at runtime.
# Correction: Python does NOT stop you from passing an int when a str is expected.
# You must use a static type checker like `mypy` to enforce them.
# e.g., greet_user(123) will run but `mypy` will flag it.

# Mistake 2: Over-annotating obvious variables.
# Bad: count: int = 0
# Good: count = 0 (Type inference handles this easily)

# Best Practices Checklist:
# - Always annotate function signatures (parameters and return types).
# - Omit return type `-> None` only if the function is a simple script, but generally include it.
# - Use built-in types for collections in Python 3.9+ (`list`, `dict`) rather than `typing.List`.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Does Python type hinting improve runtime performance?
# A1: No. Type hints are completely ignored by the Python interpreter at runtime. They are purely for developer tooling and static analysis.

# Q2: How do you indicate that a function returns nothing?
# A2: You use `-> None`. Example: `def print_log(msg: str) -> None:`

# Q3: What happens if you violate a type hint?
# A3: At runtime, nothing happens (unless it causes a standard Python error). A static type checker will report an error during CI/CD or in the IDE.

# Q4: Can you use custom classes as type hints?
# A4: Yes, you can use any class name as a type hint. If the class is defined later in the file, you can use strings (e.g., `'MyClass'`) or `from __future__ import annotations`.

# Q5: What is the difference between dynamic typing and static typing?
# A5: Dynamic typing checks types at runtime (Python's default). Static typing checks types at compile time (or via a tool before running). Type hints give Python static typing capabilities.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function `multiply` that takes an int and a float and returns a float. Include type hints.
# Exercise 2: Create a variable `cities` that is a list of strings and initialize it.
# Exercise 3: Write a function `get_status` that takes a boolean `is_online` and returns the string "Online" or "Offline".

def get_status(is_online: bool) -> str:
    return "Online" if is_online else "Offline"

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def process_order(item_name: str, quantity: int, price_per_item: float, is_premium_member: bool) -> float:
    """
    Calculate the total cost of an order. Premium members get a 10% discount.
    Ensure to use type hints everywhere.
    """
    total_cost: float = quantity * price_per_item
    if is_premium_member:
        total_cost *= 0.9
    return total_cost

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Type hints clarify the expected types of variables, arguments, and return values.
# - They do not affect runtime behavior or performance.
# - Use `mypy` or IDEs to catch type inconsistencies early.
# - Functions use `: type` for params and `-> type` for returns.

if __name__ == "__main__":
    print(greet_user(user_name))
    print(f"Discounted price: ${calculate_discount(100.0, 15):.2f}")
    print(f"Average score: {process_scores(user_scores)}")
    print(f"Order total: ${process_order('Laptop', 2, 999.99, True):.2f}")
    print("All type hints introductory examples ran successfully.")
