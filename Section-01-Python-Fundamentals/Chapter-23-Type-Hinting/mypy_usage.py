"""
Topic: Static Type Checking with Mypy
Chapter: 23
Level: Intermediate

Description:
    Type hints in Python do not throw errors at runtime. To actually find bugs, you 
    must run a static type checker. The most popular one is `mypy`. This file explains 
    how to use type checking concepts, including overriding the checker when it's wrong, 
    and casting variables to specific types.

Real-Life Analogy:
    Type hints are like road signs indicating a speed limit. Python (the car) will happily 
    ignore the signs and let you drive 100mph. `mypy` is the police officer with a radar gun; 
    it reads your code before you execute it and issues a ticket if it sees you violating 
    the signs.

Key Concepts:
    - Mypy (Static type checker)
    - type: ignore
    - typing.cast
    - Type narrowing (isinstance, assert)
"""

from typing import Any, cast

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def add_numbers(a: int, b: int) -> int:
    return a + b

# If you ran `mypy mypy_usage.py` in the terminal, the following line would raise:
# error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"
# But running `python mypy_usage.py` will result in a runtime TypeError.
# result = add_numbers(5, "10") 

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Type Narrowing
# Mypy is smart enough to understand `isinstance` checks.
def process_data(data: int | str) -> str:
    if isinstance(data, int):
        # Mypy knows `data` is an int here
        return str(data * 2)
    else:
        # Mypy knows `data` must be a str here
        return data.upper()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# 1. Casting
# Sometimes you know the type of a variable, but mypy doesn't.
# `cast(Type, value)` tells mypy to assume the value is of that Type.
# It does NOTHING at runtime (it just returns the value).
def get_user_from_db() -> Any:
    # Simulating a DB call that returns a dictionary
    return {"id": 1, "name": "Alice"}

user_data = get_user_from_db()
# Mypy thinks user_data is Any. We tell it it's a dict.
typed_user = cast(dict[str, Any], user_data)
print(typed_user["name"])

# 2. Type Ignore
# If mypy is giving a false positive or you just want it to shut up for a line,
# you use the `# type: ignore` comment.
dynamic_var = "String"
dynamic_var = 50  # type: ignore

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using `cast` to convert types.
# `cast` does NOT convert types. `cast(int, "5")` does not make the string an integer.
# It only lies to mypy. It will crash at runtime if you try to do math on it.
# To convert, use actual Python functions like `int("5")`.

# Best Practices Checklist:
# - Run `mypy` locally in your IDE and in your CI/CD pipeline.
# - Use `# type: ignore` sparingly and ideally add a specific error code like `# type: ignore[attr-defined]`.
# - Prefer type narrowing (`isinstance`) over `cast` whenever possible, as narrowing is safer.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Does `mypy` execute your code?
# A1: No, it performs static analysis by reading your source code.

# Q2: What is the difference between `int("5")` and `cast(int, "5")`?
# A2: `int("5")` performs a runtime conversion of a string to an integer. `cast(int, "5")` does nothing at runtime (returns the string "5") but tells mypy to pretend it is an integer.

# Q3: How does type narrowing work?
# A3: Type narrowing occurs when control flow constructs (like `if isinstance(var, type):` or `assert`) allow the static type checker to deduce a more specific type for a variable within a certain code block.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function `get_length` that takes `str | list`. Use `isinstance` to type narrow and return the length.
def get_length(item: str | list[Any]) -> int:
    if isinstance(item, str):
        return len(item)
    return len(item) # Mypy knows it's a list here

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def process_untyped_api(response: Any) -> list[str]:
    """
    Assume `response` is an untyped API return. We know it SHOULD be a list of strings, 
    but mypy thinks it's Any.
    Use `cast` to tell mypy it's a list of strings, then return it.
    """
    typed_response = cast(list[str], response)
    
    # Let's pretend to process it to prove it works
    return [s.upper() for s in typed_response]

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `mypy` is the standard static type checker for Python.
# - Type narrowing uses control flow (`isinstance`) to deduce types safely.
# - `cast()` forces the type checker to assume a type, without runtime conversion.
# - `# type: ignore` silences specific type checker warnings.

if __name__ == "__main__":
    print(process_data(10))
    print(process_data("hello"))
    print(f"Processed Any: {process_untyped_api(['a', 'b', 'c'])}")
    print("Mypy concepts demonstrated successfully.")
