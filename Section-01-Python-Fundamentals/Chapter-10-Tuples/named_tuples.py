"""
Topic: Named Tuples
Chapter: 10
Level: Advanced

Description:
    Named tuples assign meaning to each position in a tuple and allow for more readable, 
    self-documenting code. They can be used wherever regular tuples are used, and they 
    add the ability to access fields by name instead of just position index.

Real-Life Analogy:
    A regular tuple is like a receipt that just has numbers, so you have to remember 
    that the 1st number is the date and the 2nd is the total. A Named Tuple is like a 
    properly labeled receipt where it explicitly says "Date: ..." and "Total: ...".

Key Concepts:
    - collections.namedtuple
    - typing.NamedTuple (Type-hinted modern approach)
    - Access by attribute name vs index
    - Immutability of named tuples
"""

from collections import namedtuple
from typing import NamedTuple

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_named_tuples() -> None:
    # 1. Using collections.namedtuple
    # Syntax: namedtuple('TypeName', 'field_names_as_string_or_list')
    Point = namedtuple('Point', ['x', 'y'])
    
    # Creating an instance
    p1 = Point(10, 20)
    
    # Accessing via index (like normal tuple)
    print(f"Index access: x={p1[0]}, y={p1[1]}")
    
    # Accessing via name (the namedtuple advantage!)
    print(f"Name access: x={p1.x}, y={p1.y}")
    
    # It is still immutable!
    try:
        p1.x = 99
    except AttributeError as e:
        print(f"Expected Error: {e}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples() -> None:
    # Perfect for representing database rows or CSV records
    Employee = namedtuple('Employee', 'emp_id name role salary')
    
    emp1 = Employee(1, "Alice", "Developer", 85000)
    emp2 = Employee(2, "Bob", "Manager", 95000)
    
    employees = [emp1, emp2]
    
    print("\nEmployee Directory:")
    for emp in employees:
        print(f"{emp.name} works as a {emp.role} earning ${emp.salary}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# 2. Using typing.NamedTuple (Modern, preferred approach)
class Car(NamedTuple):
    make: str
    model: str
    year: int
    is_electric: bool = False  # Supports default values!

def advanced_usage() -> None:
    # Creating an instance using the type-hinted NamedTuple class
    car1 = Car("Tesla", "Model 3", 2023, is_electric=True)
    car2 = Car("Toyota", "Camry", 2020) # is_electric defaults to False
    
    print(f"\nCar 1: {car1}")
    print(f"Car 2: {car2}")
    
    # They have useful built-in methods starting with an underscore
    # Convert to dictionary:
    if hasattr(car1, '_asdict'):
        print(f"As Dictionary: {car1._asdict()}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    Color = namedtuple('Color', 'r g b')
    c = Color(255, 0, 0)
    
    # Mistake: Thinking namedtuples are mutable just because they look like objects
    # c.r = 100 # Raises AttributeError
    
    # Best Practice: Use `_replace()` to create a new namedtuple with modified fields
    new_c = c._replace(r=100)
    print(f"\nReplaced Color: {new_c}")
    
    # Best Practice: Prefer `typing.NamedTuple` for Python 3.6+ as it supports 
    # type hints and is much more readable.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What problem do Named Tuples solve?
A: They solve the readability problem of regular tuples by allowing elements to be accessed by name rather than just integer indices, while keeping the memory efficiency of a tuple.

Q2: Are Named Tuples mutable?
A: No, they are strictly immutable subclasses of the built-in tuple.

Q3: How do you change a value in a Named Tuple?
A: You cannot change it in place. You must create a new instance, typically using the `_replace()` method.

Q4: What is the difference between `collections.namedtuple` and `typing.NamedTuple`?
A: `typing.NamedTuple` allows you to define fields using class syntax with type hints and default values, making it cleaner and more robust for modern Python development.

Q5: Does a Named Tuple use more memory than a regular tuple?
A: No, they have exactly the same memory footprint as a regular tuple because they do not have a per-instance dictionary (`__dict__`).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Create a typing.NamedTuple called 'Movie' with fields: title (str), director (str), year (int).
    Exercise 2: Instantiate it and print the director's name using dot notation.
    """
    class Movie(NamedTuple):
        title: str
        director: str
        year: int
        
    m = Movie("Inception", "Christopher Nolan", 2010)
    print(f"\nMovie Director: {m.director}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: Create a list of `Product` named tuples (id, name, price). 
    Write a function that finds and returns the name of the most expensive product.
    """
    class Product(NamedTuple):
        id: int
        name: str
        price: float
        
    inventory = [
        Product(1, "Mouse", 25.99),
        Product(2, "Keyboard", 75.50),
        Product(3, "Monitor", 300.00)
    ]
    
    def find_most_expensive(items: list) -> str:
        # Using max() with a key function
        most_expensive = max(items, key=lambda p: p.price)
        return most_expensive.name
        
    print(f"\nMost expensive product: {find_most_expensive(inventory)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Named Tuples provide named fields for tuple elements.
- They are completely backwards compatible with regular tuples (indexable, iterable).
- Use `collections.namedtuple` for quick runtime creations.
- Use `typing.NamedTuple` for clean, type-hinted, class-like definitions.
- Modify them by creating new instances via the `_replace()` method.
- They are a lightweight alternative to full custom classes when you just need a data container.
"""

if __name__ == "__main__":
    basic_named_tuples()
    practical_examples()
    advanced_usage()
    common_mistakes()
    practice_exercises()
    mini_challenge()
