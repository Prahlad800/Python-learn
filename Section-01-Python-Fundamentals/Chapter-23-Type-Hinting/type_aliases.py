"""
Topic: Type Aliases
Chapter: 23
Level: Intermediate

Description:
    Complex type hints can become very long and difficult to read. Type Aliases 
    allow you to assign a complex type to a variable and use that variable as a type 
    hint. Python 3.10 introduced the `TypeAlias` annotation to make aliases explicit.
    `NewType` creates distinct types for the static type checker, preventing accidental 
    mixing of identical underlying types (e.g., UserId vs OrderId, both ints).

Real-Life Analogy:
    Instead of writing "The person who fixes the pipes in the house" every time, 
    we create an alias: "Plumber". `NewType` is like having two identical boxes, 
    but one is strictly for "Apples" and the other for "Oranges". Even though both 
    hold fruit, the system prevents you from putting an Apple in the Orange box.

Key Concepts:
    - Simple Type Aliases
    - typing.TypeAlias (Python 3.10+)
    - typing.NewType
    - Readability of complex signatures
"""

from typing import TypeAlias, NewType

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Simple Type Alias (Pre Python 3.10)
# We just assign a type to a variable
Vector2D = tuple[float, float]

def move_character(position: Vector2D) -> Vector2D:
    return (position[0] + 1.0, position[1] + 1.0)

# Explicit Type Alias (Python 3.10+)
# Much safer as it explicitly tells the checker this is an alias, not a variable.
Point: TypeAlias = tuple[int, int]
Polygon: TypeAlias = list[Point]

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Complex Aliases make code vastly more readable
ServerResponse: TypeAlias = dict[str, str | int | list[dict[str, str]]]

def parse_response(response: ServerResponse) -> bool:
    """
    Parses a complex server response without cluttering the signature.
    """
    return response.get("status") == 200

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# NewType
# Used to create distinct types. A NewType of an int is treated as a subclass of int
# by the type checker, but at runtime it's exactly the same as an int (zero overhead).

UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)

def get_user_data(user_id: UserId) -> str:
    return f"Data for user {user_id}"

# Example Usage:
user_1 = UserId(42)
order_1 = OrderId(42)

# get_user_data(user_1)  # Valid!
# get_user_data(order_1) # type checker ERROR! OrderId is not UserId
# get_user_data(42)      # type checker ERROR! int is not UserId

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Modifying type aliases at runtime.
# Type aliases should be constants. Do not reassign them inside functions.

# Mistake: Confusing `TypeAlias` with `NewType`.
# `TypeAlias` just gives a new name to an existing type (interchangeable).
# `NewType` creates a strictly different type in the eyes of the type checker.

# Best Practices Checklist:
# - Use `TypeAlias` (from `typing` or Python 3.12+ `type` keyword) for complex nested structures.
# - Use `NewType` for IDs, specific strings (like passwords vs normal text), or strict domain modeling to avoid mixing them up.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the primary benefit of a Type Alias?
# A1: Improved code readability and maintainability, especially for deeply nested generic types like lists of dictionaries.

# Q2: At runtime, what is the type of a variable created with `UserId = NewType('UserId', int)`?
# A2: At runtime, it is exactly an `int`. `NewType` has virtually zero runtime overhead.

# Q3: In Python 3.12, what is the new syntax for type aliases?
# A3: Python 3.12 introduced the `type` statement: `type Point = tuple[float, float]`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a type alias `Matrix` that represents a list of lists of floats.
Matrix: TypeAlias = list[list[float]]

# Exercise 2: Create two NewTypes, `USD` and `EUR` based on float. 
USD = NewType('USD', float)
EUR = NewType('EUR', float)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

PatientId = NewType('PatientId', str)
DoctorId = NewType('DoctorId', str)
Schedule: TypeAlias = dict[DoctorId, list[PatientId]]

def assign_patient(schedule: Schedule, doctor: DoctorId, patient: PatientId) -> Schedule:
    """
    Assign a patient to a doctor's schedule using the strict NewTypes and TypeAliases.
    """
    if doctor not in schedule:
        schedule[doctor] = []
    schedule[doctor].append(patient)
    return schedule

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Type Aliases (`TypeAlias`) simplify long, unreadable type hints.
# - `NewType` creates distinct types for strict checking, preventing bugs like passing an OrderId instead of a UserId.
# - Python 3.10+ uses `TypeAlias`, and Python 3.12+ uses the `type` keyword for native alias support.

if __name__ == "__main__":
    start_pos: Vector2D = (0.0, 0.0)
    print(f"Moved position: {move_character(start_pos)}")
    
    my_schedule: Schedule = {}
    doc = DoctorId("DOC-123")
    pat = PatientId("PAT-999")
    
    updated = assign_patient(my_schedule, doc, pat)
    print(f"Updated Schedule: {updated}")
