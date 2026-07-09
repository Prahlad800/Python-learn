"""
Topic: Dataclasses
Chapter: 16
Level: Intermediate

Description:
    Introduced in Python 3.7, `dataclasses` provide a decorator that automatically generates 
    boilerplate code (like `__init__`, `__repr__`, `__eq__`) for classes that primarily exist 
    to store data. They significantly reduce the amount of code needed to create simple classes.

Real-Life Analogy:
    Imagine filling out a standardized form (like a DMV application). You don't need to write 
    a custom essay explaining your name and address; you just fill in the blanks. Dataclasses 
    give Python classes a standardized "form-like" structure, handling the boring setup for you.

Key Concepts:
    - `@dataclass` decorator
    - Type hints (required for dataclasses)
    - Default values and `field()`
    - `__post_init__` method
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

from dataclasses import dataclass

# Regular class approach (Boilerplate-heavy)
class RegularUser:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
    def __repr__(self):
        return f"RegularUser(username='{self.username}', age={self.age})"
    def __eq__(self, other):
        if isinstance(other, RegularUser):
            return self.username == other.username and self.age == other.age
        return False

# Dataclass approach (Clean and concise)
@dataclass
class DataUser:
    username: str
    age: int

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    reg_user1 = RegularUser("alice", 30)
    reg_user2 = RegularUser("alice", 30)
    
    data_user1 = DataUser("bob", 25)
    data_user2 = DataUser("bob", 25)
    
    print(reg_user1)
    print(data_user1) # Automatically has a nice __repr__
    
    print(f"Regular equality: {reg_user1 == reg_user2}")
    print(f"Dataclass equality: {data_user1 == data_user2}") # Automatically has __eq__

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (DEFAULTS AND FIELD)
# ============================================================

from dataclasses import field
from typing import List

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    # Provide a default value
    quantity_on_hand: int = 0
    # Use field() for mutable defaults (like lists or dicts) to avoid sharing references
    tags: List[str] = field(default_factory=list)

def practical_examples():
    print("\n--- Practical Examples ---")
    item1 = InventoryItem("Laptop", 1000.0)
    item2 = InventoryItem("Mouse", 25.0, 50, ["electronics", "accessory"])
    
    print(item1)
    print(item2)

# ============================================================
# SECTION 3: ADVANCED USAGE (POST-INIT AND FROZEN)
# ============================================================

# frozen=True makes the instance immutable (read-only) after initialization
@dataclass(frozen=True)
class Coordinate:
    x: float
    y: float

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False) # Not passed in __init__
    
    def __post_init__(self):
        # Runs automatically immediately after __init__
        self.area = self.width * self.height

def advanced_usage():
    print("\n--- Advanced Usage ---")
    coord = Coordinate(10.5, 20.2)
    print(f"Coordinate: {coord}")
    # coord.x = 15.0 # This would raise a FrozenInstanceError because frozen=True
    
    rect = Rectangle(4, 5)
    print(f"Rectangle area calculated in __post_init__: {rect.area}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a mutable default directly (e.g., tags: list = [])
# This will cause all instances to share the exact same list in memory!
# Correction: ALWAYS use `field(default_factory=list)` for mutable defaults.

# Best Practice: Use dataclasses whenever you find yourself writing a class just to hold data 
# with a basic `__init__` and `__repr__`.
# Best Practice: Type hints are strictly required for a variable to be recognized as a dataclass field.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is a dataclass?
A: A feature in Python (via the `@dataclass` decorator) that automatically generates special methods like `__init__`, `__repr__`, and `__eq__` for classes meant to store data.

Q2: Why use `field(default_factory=list)` instead of just `=[]`?
A: Because standard default arguments are evaluated only once when the class is defined. `[]` would cause all instances to share the exact same list in memory. `default_factory` creates a new list for every instance.

Q3: What does `frozen=True` do in a dataclass?
A: It makes the instances of that class immutable. You cannot change their attributes after they are created.

Q4: What is the purpose of `__post_init__`?
A: It allows you to run custom setup or validation logic immediately after the auto-generated `__init__` method finishes.

Q5: Are type hints required for dataclasses?
A: Yes, the `@dataclass` decorator specifically looks for variables with type annotations to determine what should be treated as a field.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `Movie` dataclass with `title`, `director`, and `release_year`.
Exercise 2: Create a `ShoppingCart` dataclass with an `items` list (use default_factory) and a `total_price` calculated in `__post_init__`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

@dataclass(order=True)
class Player:
    # order=True automatically generates __lt__, __le__, __gt__, __ge__ based on fields in order
    score: int
    name: str = field(compare=False) # Exclude name from comparison

def mini_challenge():
    print("\n--- Mini Challenge ---")
    p1 = Player(score=100, name="Alice")
    p2 = Player(score=150, name="Bob")
    p3 = Player(score=50, name="Charlie")
    
    players = [p1, p2, p3]
    
    # Sorting works because order=True generates comparison operators based on 'score'
    players.sort(reverse=True)
    
    print("Leaderboard:")
    for rank, p in enumerate(players, 1):
        print(f"{rank}. {p.name} - {p.score}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- `@dataclass` writes boilerplate code for you (`__init__`, `__repr__`, `__eq__`).
- Type hints are required for fields.
- Use `field(default_factory=...)` for mutable default values.
- `__post_init__` handles logic that needs to run after initialization.
- `frozen=True` makes the class immutable.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
