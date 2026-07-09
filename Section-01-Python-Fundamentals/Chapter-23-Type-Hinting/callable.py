"""
Topic: Callable Type Hints
Chapter: 23
Level: Intermediate

Description:
    In Python, functions are first-class citizens, meaning you can pass them as arguments 
    to other functions or return them. The `Callable` type hint allows you to define 
    the expected signature (parameters and return type) of a function passed as a variable.

Real-Life Analogy:
    Think of hiring a contractor for home renovation. You are a Manager (the main function). 
    You need to hire a Plumber (a callback function). You don't care WHO the plumber is, 
    but you demand they have a specific skill set: they must accept "pipes" as input and 
    return "fixed pipes". `Callable` enforces this specific skill set contract.

Key Concepts:
    - typing.Callable
    - Callback functions
    - Higher-order functions
    - Defining argument types and return types of callbacks
"""

from typing import Callable, Any

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Callable[[ArgType1, ArgType2], ReturnType]
# Example: A function that takes two ints and returns an int
MathOperation = Callable[[int, int], int]

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def execute_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """
    A higher-order function that takes another function as an argument.
    It expects `operation` to be a function taking two ints and returning an int.
    """
    print("Executing operation...")
    result: int = operation(x, y)
    return result

# You can use `...` (ellipsis) to indicate that the function takes any number 
# or type of arguments, but you still care about the return type.
def execute_anything(func: Callable[..., Any]) -> Any:
    """
    Executes a function with no arguments, or where we don't care about the args.
    """
    return func()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Callables returning Callables (Factory pattern)
def get_multiplier(factor: int) -> Callable[[int], int]:
    """
    Returns a function that multiplies its input by 'factor'.
    """
    def multiplier(n: int) -> int:
        return n * factor
    return multiplier

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting the list brackets for arguments in Callable.
# Bad: Callable[int, str]
# Good: Callable[[int], str]

# Mistake: Assuming kwargs can be specifically typed in a standard Callable.
# Detail: The standard `Callable` syntax `Callable[[int, str], bool]` only represents
# positional arguments. To type-hint complex signatures with kwargs, you typically
# need `typing.Protocol` (covered in a later lesson).

# Best Practices Checklist:
# - Use `Callable[..., ReturnType]` when you only care about what the function returns.
# - Use specific argument types `Callable[[A, B], C]` whenever possible for strictness.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does `Callable[[], None]` mean?
# A1: It represents a function that takes no arguments and returns nothing (None).

# Q2: Can you specify keyword arguments in a `Callable` type hint?
# A2: Not with the standard `Callable[[ArgTypes], ReturnType]` syntax. You need to use `typing.Protocol` with a `__call__` method to strictly type-hint keyword arguments.

# Q3: How do you hint a function that takes another function and an iterable, and applies the function to each element (like `map`)?
# A3: `def my_map(func: Callable[[Any], Any], items: Iterable[Any]) -> list[Any]:` (Using generics would be even better here).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function `apply_twice` that takes a `Callable[[str], str]` and a string, and applies the function to the string two times.
def apply_twice(func: Callable[[str], str], text: str) -> str:
    return func(func(text))

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def filter_list(items: list[int], condition: Callable[[int], bool]) -> list[int]:
    """
    Takes a list of integers and a condition function.
    Returns a new list containing only the integers that satisfy the condition.
    """
    return [item for item in items if condition(item)]

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `Callable` is used to type-hint functions passed as variables or arguments.
# - Syntax: `Callable[[Arg1, Arg2], ReturnType]`.
# - Use `Callable[..., ReturnType]` if argument types are variable or unknown.
# - Crucial for higher-order functions like map, filter, or custom decorators.

if __name__ == "__main__":
    print(f"Add 5 + 3: {execute_operation(5, 3, add)}")
    print(f"Subtract 10 - 4: {execute_operation(10, 4, subtract)}")
    
    times_three = get_multiplier(3)
    print(f"5 times 3: {times_three(5)}")
    
    def is_even(n: int) -> bool:
        return n % 2 == 0
        
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    print(f"Even numbers from {numbers}: {filter_list(numbers, is_even)}")
