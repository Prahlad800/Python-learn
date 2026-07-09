"""
Topic: Generics and TypeVar
Chapter: 23
Level: Advanced

Description:
    Sometimes you want a function or class to work with multiple types, but you want 
    to preserve the relationship between input types and output types. `TypeVar` allows 
    you to define Generics. If you pass an `int` in, you get an `int` back. If you pass 
    a `str`, you get a `str`.

Real-Life Analogy:
    Think of a generic storage box. It doesn't care if you put books or toys in it. 
    However, if you put books into the box, you expect to take books out of it, not toys. 
    Generics enforce that the type going in matches the type coming out.

Key Concepts:
    - typing.TypeVar
    - typing.Generic
    - Generic functions
    - Generic classes
    - Bounded TypeVars
"""

from typing import TypeVar, Generic, Any

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Define a Type Variable
T = TypeVar('T')

def get_first_item(items: list[T]) -> T:
    """
    A generic function. 
    If `items` is list[int], it returns int.
    If `items` is list[str], it returns str.
    """
    return items[0]

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Using multiple TypeVars
K = TypeVar('K')
V = TypeVar('V')

def get_keys(mapping: dict[K, V]) -> list[K]:
    """
    Returns a list of keys from a dictionary, preserving the key's type.
    """
    return list(mapping.keys())

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Bounded TypeVars
# Restricts T to be either an int or a float (or their subclasses)
Num = TypeVar('Num', int, float)

def double_number(num: Num) -> Num:
    """
    Accepts ONLY ints or floats, and returns the exact same type.
    (Different from Union[int, float], which doesn't guarantee the return 
    type matches the specific input type).
    """
    return num * 2

# Generic Classes
# Subclassing Generic[T] makes the class generic
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
        
    def push(self, item: T) -> None:
        self._items.append(item)
        
    def pop(self) -> T:
        return self._items.pop()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Confusing `TypeVar` with `Any` or `Union`.
# `Any`: The type checker ignores it.
# `Union[int, str]`: Input can be int or str, output can be int or str. The link is lost.
# `TypeVar('T', int, str)`: If input is int, output is int. If input is str, output is str. The link is preserved.

# Best Practices Checklist:
# - Name TypeVars with single uppercase letters (T, K, V, E) or CamelCase ending in 'T' (e.g., AnyStr).
# - Use Generics for container classes (custom lists, queues, trees).
# - In Python 3.12+, you can use the new syntax: `def get_first[T](items: list[T]) -> T:`

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why use `TypeVar` instead of just writing `Any`?
# A1: `TypeVar` preserves type safety. If you use `Any`, the type checker has no idea what comes out. `TypeVar` ties the output type to the input type.

# Q2: How do you restrict a `TypeVar` so it can only be a subclass of a specific class?
# A2: Use the `bound` argument: `T = TypeVar('T', bound=MyBaseClass)`.

# Q3: What is `Generic[T]` used for?
# A3: It is used as a base class to define a custom class that can hold or operate on generic types, like `class CustomList(Generic[T]):`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a generic function `swap` that takes two arguments of the same type and returns them as a tuple in reverse order.
T_swap = TypeVar('T_swap')

def swap(a: T_swap, b: T_swap) -> tuple[T_swap, T_swap]:
    return (b, a)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

Element = TypeVar('Element')

class Queue(Generic[Element]):
    """
    Implement a simple generic Queue class with enqueue and dequeue methods.
    """
    def __init__(self) -> None:
        self.elements: list[Element] = []
        
    def enqueue(self, item: Element) -> None:
        self.elements.insert(0, item)
        
    def dequeue(self) -> Element:
        if not self.elements:
            raise IndexError("dequeue from empty queue")
        return self.elements.pop()

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `TypeVar` creates variables that hold Types instead of data.
# - Generics establish strong relationships between parameters and return values.
# - Generic classes (`Generic[T]`) let you create type-safe data structures.
# - Bounded Generics restrict the types that can be substituted for the TypeVar.

if __name__ == "__main__":
    print(f"First item (int): {get_first_item([1, 2, 3])}")
    print(f"First item (str): {get_first_item(['a', 'b', 'c'])}")
    
    print(f"Double (int): {double_number(10)}")
    print(f"Double (float): {double_number(10.5)}")
    
    int_stack: Stack[int] = Stack()
    int_stack.push(10)
    int_stack.push(20)
    print(f"Stack pop: {int_stack.pop()}")
    
    q: Queue[str] = Queue()
    q.enqueue("First")
    q.enqueue("Second")
    print(f"Queue dequeue: {q.dequeue()}")
