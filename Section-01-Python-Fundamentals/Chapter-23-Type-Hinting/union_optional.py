"""
Topic: Union and Optional
Chapter: 23
Level: Intermediate

Description:
    Often, a variable might hold more than one type of data, or it might hold a value 
    OR `None`. The `Union` type allows you to specify multiple possible types, while 
    `Optional` is a specific shortcut for a type or `None`. In modern Python (3.10+), 
    the `|` operator provides a cleaner syntax for Unions.

Real-Life Analogy:
    Imagine a form field that asks for your contact information. You can provide EITHER 
    a Phone Number (int) OR an Email Address (str). This is a `Union`. Sometimes, providing 
    a middle name is optional; you provide a string OR nothing (`None`). This is `Optional`.

Key Concepts:
    - typing.Union
    - typing.Optional
    - The bitwise OR operator `|` (Python 3.10+)
    - Handling `None` safely
"""

from typing import Union, Optional

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Union: The variable can be an int OR a float
identifier: Union[int, str] = 101
identifier = "ID-101"  # Also valid

# Optional: The variable can be a string OR None
# Optional[str] is exactly equivalent to Union[str, None]
middle_name: Optional[str] = None
middle_name = "James"

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def format_id(user_id: Union[int, str]) -> str:
    """
    Formats a user ID, handling both integer and string inputs.
    """
    if isinstance(user_id, int):
        return f"USER-{user_id:04d}"
    return user_id.upper()

def get_user_email(user_id: int) -> Optional[str]:
    """
    Simulates fetching a user's email. Sometimes a user doesn't have an email,
    so it returns None.
    """
    database: dict[int, str] = {1: "alice@example.com", 2: "bob@example.com"}
    return database.get(user_id) # .get() returns None if key not found

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Python 3.10+ introduces the `|` syntax for Unions.
# This makes type hints much cleaner!
PriceType = int | float  # Equivalent to Union[int, float]
MaybeString = str | None # Equivalent to Optional[str]

def calculate_tax(amount: int | float, tax_rate: float | None = None) -> float:
    """
    Calculates tax. If tax_rate is None, defaults to 0.20.
    Utilizes Python 3.10+ union syntax.
    """
    actual_rate: float = tax_rate if tax_rate is not None else 0.20
    return float(amount) * actual_rate

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Forgetting to handle the `None` case when using `Optional`.
# Bad:
# def print_length(text: Optional[str]) -> None:
#     print(len(text))  # TypeError if text is None!

# Correction: Always check for None.
# def print_length(text: Optional[str]) -> None:
#     if text is not None:
#         print(len(text))

# Best Practices Checklist:
# - Use `X | None` instead of `Optional[X]` if you are on Python 3.10+.
# - Use `is not None` to explicitly check Optional variables before using their methods.
# - Keep Unions small (2-3 types). If you have more, you might need a common base class or Protocol.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between `Optional[int]` and `Union[int, None]`?
# A1: There is no difference. `Optional[T]` is just syntactic sugar for `Union[T, None]`.

# Q2: Can a function return `Union[int, str]`? Is it a good practice?
# A2: Yes, it can. However, returning mixed types can make the function harder for the caller to use, as they must use `isinstance()` to check the return type. It's often better to return a single type if possible.

# Q3: How do you write a Union of three types using the Python 3.10 syntax?
# A3: `type1 | type2 | type3`. For example: `int | float | complex`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function `parse_value` that takes a `str | int` and returns an `int`. If it's a string, try to convert it.
def parse_value(val: str | int) -> int:
    return int(val)

# Exercise 2: Write a function `find_user` that takes a list of names and a target name. Return the target name if found, else None.
def find_user(names: list[str], target: str) -> str | None:
    return target if target in names else None

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def process_api_response(response_data: dict[str, str | int | None]) -> str:
    """
    Takes a dictionary where values can be strings, integers, or None.
    Extract the 'status' key. If it's None or missing, return 'UNKNOWN'.
    If it's an int, convert to str. If it's a string, return it as uppercase.
    """
    status: str | int | None = response_data.get('status')
    
    if status is None:
        return 'UNKNOWN'
    if isinstance(status, int):
        return str(status)
    return status.upper()

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `Union` specifies that a variable can be one of multiple types.
# - `Optional[T]` means a variable is of type `T` or `None`.
# - In Python 3.10+, prefer the pipe operator `|` (e.g., `str | None`).
# - Always perform `is None` checks when working with Optional types to satisfy type checkers.

if __name__ == "__main__":
    print(f"Format int ID: {format_id(42)}")
    print(f"Format str ID: {format_id('a-99')}")
    print(f"Email for 1: {get_user_email(1)}")
    print(f"Email for 99: {get_user_email(99)}")
    print(f"Tax: {calculate_tax(100, None)}")
    
    api_res: dict[str, str | int | None] = {"status": "success", "data": None}
    print(f"API Status: {process_api_response(api_res)}")
