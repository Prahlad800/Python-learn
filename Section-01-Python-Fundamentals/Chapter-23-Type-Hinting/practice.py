"""
Topic: Type Hinting Practice Exercises
Chapter: 23
Level: All Levels

Description:
    This file contains exercises to practice all the type hinting concepts learned 
    in this chapter. Fill in the missing type hints for each exercise.

Real-Life Analogy:
    Just like practicing scales on a piano, or doing drills in soccer, you need 
    to write type hints repeatedly to build muscle memory and understand when 
    to use Unions, Callables, and Generics.

Key Concepts:
    - Basic Types
    - Collections
    - Unions and Optionals
    - Callables
    - Generics
"""

from typing import Any, Callable, TypeVar, Protocol, Optional, Sequence

# ============================================================
# EXERCISE 1: BASIC TYPES & COLLECTIONS
# ============================================================
# Task: Add type hints to parameters and return types.
# It takes a list of strings, an integer multiplier, and returns a list of strings.

def multiply_strings(strings: list[str], multiplier: int) -> list[str]:
    return [s * multiplier for s in strings]

# ============================================================
# EXERCISE 2: UNION & OPTIONAL
# ============================================================
# Task: Add type hints. 'value' can be int, float, or string. 
# 'default' can be an int or None. The return type should be a float.

def normalize_value(value: int | float | str, default: Optional[int] = None) -> float:
    try:
        return float(value)
    except ValueError:
        if default is not None:
            return float(default)
        return 0.0

# ============================================================
# EXERCISE 3: CALLABLES
# ============================================================
# Task: Add type hints. 'data' is a list of integers. 'transformer' is a function 
# that takes an int and returns a string. The function returns a list of strings.

def apply_transformation(data: list[int], transformer: Callable[[int], str]) -> list[str]:
    return [transformer(item) for item in data]

# ============================================================
# EXERCISE 4: GENERICS
# ============================================================
# Task: Create a generic function that takes a sequence of any type and returns 
# a tuple containing the first and last elements of that exact type.

T = TypeVar('T')

def get_edges(items: Sequence[T]) -> tuple[T, T]:
    if not items:
        raise ValueError("Sequence cannot be empty")
    return (items[0], items[-1])

# ============================================================
# EXERCISE 5: PROTOCOLS
# ============================================================
# Task: Define a Protocol called `JSONSerializable` that requires a method 
# `to_json(self) -> str`. Then, type hint the function below.

class JSONSerializable(Protocol):
    def to_json(self) -> str:
        ...

def print_json_representation(obj: JSONSerializable) -> None:
    print(obj.to_json())

# ============================================================
# EXERCISE 6: TYPE ALIASES & NEWTYPE
# ============================================================
# Task: Create a NewType 'EmployeeId' for integers.
# Create a TypeAlias 'PayrollDict' for a dictionary mapping EmployeeId to floats.

from typing import NewType, TypeAlias

EmployeeId = NewType('EmployeeId', int)
PayrollDict: TypeAlias = dict[EmployeeId, float]

def process_payroll(payroll: PayrollDict) -> float:
    return sum(payroll.values())

# ============================================================
# RUN TESTS
# ============================================================

if __name__ == "__main__":
    print("Testing Exercise 1:", multiply_strings(["a", "b"], 3))
    print("Testing Exercise 2:", normalize_value("3.14"))
    print("Testing Exercise 3:", apply_transformation([1, 2, 3], str))
    print("Testing Exercise 4:", get_edges([10, 20, 30]))
    
    class FakeUser:
        def to_json(self) -> str:
            return '{"name": "test"}'
            
    print("Testing Exercise 5:")
    print_json_representation(FakeUser())
    
    pr: PayrollDict = {EmployeeId(1): 1500.0, EmployeeId(2): 2000.0}
    print("Testing Exercise 6:", process_payroll(pr))
    
    print("\nAll practice exercises executed successfully.")
