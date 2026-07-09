"""
Topic: Function Annotations (Type Hints)
Chapter: 7
Level: Intermediate

Description:
    Function annotations, also known as type hints, allow you to specify the expected types of arguments and return values for functions. While Python does not enforce these types at runtime, they are extremely useful for documentation, IDE autocomplete, and static type checking using tools like `mypy`.

Real-Life Analogy:
    Think of annotations like a dress code on a party invitation. The invitation says "Black Tie Only" (the type hint). You can technically show up in a t-shirt (Python won't stop you from running the code), but the bouncer (a static type checker like `mypy`) will complain before you get in.

Key Concepts:
    - Argument annotations `:`
    - Return annotations `->`
    - The `typing` module (List, Dict, Tuple, Optional, Any)
    - Static type checking vs Dynamic typing
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# A function without annotations
def greet_untyped(name):
    return "Hello, " + name

# A function WITH annotations
def greet_typed(name: str) -> str:
    return "Hello, " + name

print("--- Section 1 ---")
print(greet_typed("Alice"))

# Note: Python does NOT enforce these at runtime!
# This will run fine, even though it violates the type hint.
# print(greet_typed(123)) # Returns "Hello, 123" if string concatenation allowed it, but here it causes TypeError for str+int.

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (THE TYPING MODULE)
# ============================================================

print("\n--- Section 2 ---")
# In Python 3.9+, you can use standard collections directly (list, dict).
# For older versions, or complex types, you import from `typing`.
from typing import List, Dict, Tuple, Optional, Any

# Example 1: Lists and Dictionaries
def process_scores(scores: list[int]) -> dict[str, float]:
    """Takes a list of ints, returns a dict with string keys and float values."""
    if not scores:
        return {"average": 0.0}
    avg = sum(scores) / len(scores)
    return {"average": avg}

print(process_scores([80, 90, 100]))

# Example 2: Optional
# Optional[str] means the argument can be a string OR None.
def get_user_status(user_id: int, status_override: Optional[str] = None) -> str:
    if status_override:
        return status_override
    return "active"

print(get_user_status(101))
print(get_user_status(101, "suspended"))

# Example 3: Multiple Return Types (Tuple)
def get_coordinates() -> tuple[float, float]:
    return (40.7128, -74.0060)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

print("\n--- Section 3 ---")
from typing import Union, Callable

# Example 1: Union (Variable can be one of multiple types)
# In Python 3.10+, you can use `int | float` instead of `Union[int, float]`
def double_value(val: Union[int, float]) -> Union[int, float]:
    return val * 2

print(f"Double int: {double_value(5)}")
print(f"Double float: {double_value(3.14)}")

# Example 2: Annotating functions as arguments (Callable)
# Callable[[ArgType1, ArgType2], ReturnType]
def execute_operation(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

def add(a: int, b: int) -> int:
    return a + b

print(f"Execute Callable: {execute_operation(add, 10, 20)}")

# Inspecting annotations at runtime
print(f"Annotations for execute_operation: {execute_operation.__annotations__}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Confusing annotations with runtime enforcement
# Type hints DO NOT make Python statically typed or faster. They are just hints.
# If you want enforcement, you must run a tool like `mypy my_script.py` in your terminal.

# Mistake 2: Overcomplicating types
# Don't make types so complex that they are harder to read than the code itself.
# Use `Any` if a variable truly can be anything and it's too hard to define.

# Best Practice: Use type hints for all public functions and APIs.
# It drastically improves the developer experience in IDEs like VSCode and PyCharm.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Does Python enforce type hints at runtime?
# A: No. Python remains a dynamically typed language. Type hints are ignored by the Python interpreter during execution.

# Q2: How do you check if your code adheres to your type hints?
# A: By using static type checking tools like `mypy`, `pyright`, or through IDE integrations.

# Q3: What is the purpose of the `Optional` type hint?
# A: It indicates that a variable could be of a specific type OR `None`. `Optional[X]` is equivalent to `Union[X, None]`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Add type hints to this function.
# def repeat_word(word, times): return word * times

def repeat_word(word: str, times: int) -> str:
    return word * times

# Exercise 2: Write a function `parse_data` that takes a dictionary mapping strings to integers,
# and returns a list of strings.
def parse_data(data: dict[str, int]) -> list[str]:
    return list(data.keys())

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create a typed function `format_users` that takes a list of dictionaries.
# Each dictionary represents a user with a "name" (str) and an optional "age" (int).
# The function should return a list of formatted strings.

from typing import List, Dict, Any

def format_users(users: List[Dict[str, Any]]) -> List[str]:
    result = []
    for user in users:
        name = user.get("name", "Unknown")
        age = user.get("age")
        if age is not None:
            result.append(f"{name} is {age} years old.")
        else:
            result.append(f"{name}'s age is unknown.")
    return result

print("\n--- Mini Challenge ---")
user_data = [{"name": "Alice", "age": 30}, {"name": "Bob"}]
print(format_users(user_data))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Type hints use `:` for arguments and `->` for return values.
# - They are not enforced at runtime by Python.
# - They vastly improve IDE autocomplete and code readability.
# - Use the `typing` module (or modern built-ins like `list`, `dict`) for complex types.
# - Use tools like `mypy` to statically check your code for type errors.

if __name__ == "__main__":
    pass
