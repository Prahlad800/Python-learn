"""
Topic: The typing Module
Chapter: 23
Level: Beginner / Intermediate

Description:
    Before Python 3.9 introduced native type hinting for collections (like `list` and `dict`), 
    the `typing` module was required to hint complex data structures. The `typing` module 
    also provides advanced types like `Any`, `Iterable`, `Sequence`, and `Mapping` which are 
    essential for robust type definitions.

Real-Life Analogy:
    Think of the `typing` module as an advanced catalog system in a library. While basic 
    labels ("Book", "Magazine") work for general sorting, the `typing` module provides 
    specific sub-categories ("A list of Science Fiction Books", "A mapping of Author to 
    their Publications") to organize things meticulously.

Key Concepts:
    - Any
    - Sequence vs Iterable
    - Mapping vs Dict
    - Legacy typing types (List, Dict, Set, Tuple) vs Python 3.9+ built-ins
"""

from typing import Any, Iterable, Sequence, Mapping

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# `Any` indicates that a variable can be of any type. Use sparingly!
mystery_variable: Any = "Could be a string"
mystery_variable = 42  # Now it's an int, static checker won't complain

def print_anything(item: Any) -> None:
    print(f"Item is: {item}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Iterable: Anything you can loop over (lists, tuples, sets, strings)
def sum_all_numbers(numbers: Iterable[float]) -> float:
    """
    Takes any iterable of floats and returns their sum.
    """
    return sum(numbers)

# Sequence: An iterable with a specific length and element order (lists, tuples, strings)
# Sets are Iterables, but NOT Sequences (they lack order/indexing).
def get_first_element(items: Sequence[Any]) -> Any:
    """
    Returns the first element of a sequence.
    """
    if items:
        return items[0]
    return None

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Mapping: A read-only type for dictionary-like objects
def print_config(config: Mapping[str, Any]) -> None:
    """
    Takes a mapping (like a dict) of string keys to Any values.
    Using Mapping instead of dict signifies that we won't mutate it.
    """
    for key, value in config.items():
        print(f"{key} -> {value}")

# Tuple types: Specify types for specific positions, or variable length
# Python 3.9+: tuple[int, str] or tuple[int, ...]
coordinates: tuple[float, float] = (10.5, 20.1)
varying_ints: tuple[int, ...] = (1, 2, 3, 4, 5)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using `Any` too often.
# Correction: If everything is `Any`, you lose the benefits of type hinting. 
# Try to be as specific as possible.

# Best Practices Checklist:
# - Prefer `Iterable` over `list` for function arguments if you only need to iterate.
# - Prefer `Sequence` over `list` if you only need to read and index.
# - Prefer `Mapping` over `dict` if you only need to read key/value pairs.
# - This adherence to abstract base classes makes your functions more flexible.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: When should you use `Any`?
# A1: When integrating with legacy, untyped code, or when a function genuinely works with any Python object and you cannot be more specific (like `print()`).

# Q2: What is the difference between `Sequence` and `Iterable`?
# A2: An `Iterable` can be looped over (e.g., generators, sets). A `Sequence` is an `Iterable` that also supports indexing and has a known length (e.g., lists, tuples).

# Q3: Why is it better to type hint a parameter as `Mapping` instead of `dict`?
# A3: `Mapping` indicates the function will only read from the dictionary, not modify it. It also allows passing other dict-like classes (like `collections.defaultdict` or custom mapping classes).

# Q4: Are `typing.List` and `list` the same in Python 3.9+?
# A4: Functionally for type hinting, yes. `list[int]` is preferred in Python 3.9+ over `typing.List[int]`. `typing.List` is kept for backward compatibility.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function that takes an `Iterable[str]` and returns a single concatenated `str`.
def concat_strings(strings: Iterable[str]) -> str:
    return "".join(strings)

# Exercise 2: Write a function that takes a `Mapping[str, int]` and returns a list of its keys.
def extract_keys(m: Mapping[str, int]) -> list[str]:
    return list(m.keys())

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def process_data_pipeline(data: Sequence[Mapping[str, Any]]) -> list[str]:
    """
    Accepts a sequence of mappings (like a list of dicts from a JSON response).
    Returns a list of strings representing the 'id' field of each mapping if it exists.
    """
    result: list[str] = []
    for entry in data:
        if "id" in entry and isinstance(entry["id"], str):
            result.append(entry["id"])
    return result

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `typing` provides advanced abstract types (`Iterable`, `Sequence`, `Mapping`).
# - Use abstract types for function parameters to make them more flexible.
# - `Any` disables type checking; use it only as a last resort.
# - Use Python 3.9+ built-ins (`list`, `dict`, `tuple`) for modern type hinting.

if __name__ == "__main__":
    print_anything(42)
    print(f"Sum of (1.5, 2.5): {sum_all_numbers((1.5, 2.5))}")
    print(f"First element: {get_first_element(['apple', 'banana'])}")
    print_config({"host": "localhost", "port": 8080})
    
    sample_data: list[dict[str, Any]] = [{"id": "user123"}, {"name": "Bob"}, {"id": "user456"}]
    print(f"Processed IDs: {process_data_pipeline(sample_data)}")
