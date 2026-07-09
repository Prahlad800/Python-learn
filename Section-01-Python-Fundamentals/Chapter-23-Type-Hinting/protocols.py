"""
Topic: Protocols (Structural Subtyping)
Chapter: 23
Level: Advanced

Description:
    Python uses "duck typing" natively (if it walks like a duck and quacks like a duck, 
    it's a duck). `Protocol` brings duck typing to the static type checker. Instead of 
    checking if an object inherits from a specific class (Nominal subtyping), `Protocol` 
    checks if an object has specific methods and attributes (Structural subtyping).

Real-Life Analogy:
    Imagine you need a "Screwdriver". You don't care what brand it is (Nominal), or if 
    it's technically a swiss-army knife. As long as it has the ability to `turn_screw()` 
    (Structural), you will accept it. Protocol defines the `turn_screw()` requirement.

Key Concepts:
    - typing.Protocol
    - Structural Subtyping vs Nominal Subtyping
    - Duck Typing with static checks
"""

from typing import Protocol, Any

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Define a Protocol
# Any class that implements a `.fly()` method returning a string 
# implicitly satisfies this Protocol. No inheritance needed!
class Flyer(Protocol):
    def fly(self) -> str:
        ... # Ellipsis is used in protocol method bodies

class Bird:
    def fly(self) -> str:
        return "Bird is flying through the sky."

class Airplane:
    def fly(self) -> str:
        return "Airplane engines are roaring."
        
class Dog:
    def bark(self) -> str:
        return "Woof!"

def make_it_fly(entity: Flyer) -> None:
    """
    Accepts anything that matches the Flyer protocol.
    """
    print(entity.fly())

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Protocols can also require properties/attributes
class Item(Protocol):
    price: float
    name: str

def calculate_total(items: list[Item]) -> float:
    return sum(item.price for item in items)

class Book:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

class Service:
    def __init__(self, name: str, hourly_rate: float, hours: float) -> None:
        self.name = name
        self.price = hourly_rate * hours

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Protocols can be generic too
from typing import TypeVar

T = TypeVar('T')

class SupportsClose(Protocol[T]):
    def close(self) -> None:
        ...
        
def safely_close(resource: SupportsClose[Any]) -> None:
    try:
        resource.close()
        print("Resource closed safely.")
    except Exception as e:
        print(f"Failed to close: {e}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Inheriting from a Protocol in your concrete class.
# Correction: You *can* inherit from a Protocol to enforce the contract strictly
# at class definition time, but the whole point of Protocols is that you DON'T 
# have to inherit. The type checker matches it structurally.

# Mistake: Writing logic inside Protocol methods.
# Protocols should only contain method signatures with `...` or `pass`.

# Best Practices Checklist:
# - Use Protocols when defining interfaces for third-party classes you can't modify.
# - Use `abc.ABC` (Abstract Base Classes) when you want to share concrete implementations or strictly enforce inheritance. Use Protocols for pure duck-typing.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between an ABC (Abstract Base Class) and a Protocol?
# A1: ABCs enforce Nominal subtyping (you must explicitly inherit from the ABC). Protocols enforce Structural subtyping (duck typing; the class just needs the right methods, no inheritance required).

# Q2: How do you indicate the body of a Protocol method?
# A2: Use the ellipsis `...`.

# Q3: If a Protocol defines a method `process(self, data: str)`, and a class defines `process(self, data: Any)`, does the class satisfy the Protocol?
# A3: Yes, because `Any` can accept `str`. But if the class defined `process(self, data: int)`, it would fail the Protocol check.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Define a protocol `Logger` that requires a method `log(self, message: str) -> None`.
class Logger(Protocol):
    def log(self, message: str) -> None:
        ...

# Exercise 2: Create a `ConsoleLogger` class that satisfies the `Logger` protocol.
class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"LOG: {message}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Drawing a Circle 〇"

class Square:
    def draw(self) -> str:
        return "Drawing a Square □"

def render_scene(shapes: list[Drawable]) -> None:
    """
    Takes a list of Drawable objects and calls draw() on each.
    """
    for shape in shapes:
        print(shape.draw())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `Protocol` enables structural subtyping (static duck typing).
# - A class satisfies a protocol simply by having the matching attributes and methods.
# - Excellent for decoupling code and defining strict interfaces without forcing complex inheritance trees.

if __name__ == "__main__":
    make_it_fly(Bird())
    make_it_fly(Airplane())
    # make_it_fly(Dog()) # Mypy would flag this as an error!
    
    cart = [Book("Python 101", 29.99), Service("Consulting", 100.0, 2.5)]
    print(f"Cart Total: ${calculate_total(cart):.2f}")
    
    logger = ConsoleLogger()
    logger.log("Protocol script executed.")
    
    render_scene([Circle(), Square()])
