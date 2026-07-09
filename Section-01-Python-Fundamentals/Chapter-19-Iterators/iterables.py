"""
Topic: Iterables
Chapter: 19
Level: Beginner

Description:
    An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop. Common iterables include lists, tuples, strings, dictionaries, and sets. In Python, an object is considered iterable if it implements the `__iter__()` method, which returns an iterator.

Real-Life Analogy:
    Think of a book as an iterable. The book itself isn't a single action, but it contains pages. You can flip through the pages one by one. The book is the iterable (holds the data), and the act of reading page-by-page is using an iterator.

Key Concepts:
    - Iterable vs non-iterable
    - The `__iter__()` magic method
    - Using `iter()` to check for iterability
    - Built-in iterables
"""

from typing import Iterable, Any

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_iterables() -> None:
    """Demonstrate basic built-in iterables."""
    print("--- Section 1: Basic Iterables ---")
    
    # Strings are iterables
    text = "Hello"
    print("Iterating over a string:")
    for char in text:
        print(char, end=" ")
    print("\n")
    
    # Lists and Tuples are iterables
    numbers = (1, 2, 3)
    print("Iterating over a tuple:")
    for num in numbers:
        print(num, end=" ")
    print("\n")
    
    # Dictionaries are iterables (iterates over keys by default)
    user = {"name": "Alice", "age": 30}
    print("Iterating over a dict:")
    for key in user:
        print(key, end=" ")
    print("\n")


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def check_if_iterable(obj: Any) -> bool:
    """A helper function to determine if an object is iterable."""
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def testing_iterability() -> None:
    """Show how to test if an object is iterable."""
    print("--- Section 2: Testing Iterability ---")
    
    items = [
        [1, 2, 3],        # List (Iterable)
        "Python",         # String (Iterable)
        42,               # Integer (Not iterable)
        3.14,             # Float (Not iterable)
        {"a": 1},         # Dict (Iterable)
        True              # Boolean (Not iterable)
    ]
    
    for item in items:
        status = "Iterable" if check_if_iterable(item) else "Not Iterable"
        print(f"Object: {str(item):<10} | Type: {type(item).__name__:<8} | {status}")


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def custom_iterable_basic() -> None:
    """Demonstrate creating a minimal custom iterable using a class."""
    print("\n--- Section 3: Custom Iterable ---")
    
    class Countdown:
        """A simple iterable class representing a countdown."""
        def __init__(self, start: int):
            self.start = start
            
        def __iter__(self):
            # The __iter__ method must return an iterator.
            # In this simple example, we return a generator which is an iterator.
            current = self.start
            while current > 0:
                yield current
                current -= 1
                
    # Using the custom iterable
    cd = Countdown(5)
    print("Countdown from 5:")
    for number in cd:
        print(number, end=" ")
    print()
    
    # Unlike a bare iterator, our Countdown iterable can be iterated multiple times!
    print("Countdown again:")
    for number in cd:
        print(number, end=" ")
    print()


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Show common pitfalls with iterables."""
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake: Trying to iterate over an integer
    try:
        for x in 100:
            print(x)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
        
    # Best Practice: Use `range()` when you need to iterate a specific number of times
    print("Using range:")
    for x in range(3):
        print(x, end=" ")
    print()


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What makes an object iterable in Python?
A1: An object is iterable if it implements the `__iter__()` method, which returns an iterator, or if it implements the `__getitem__()` method that can take sequential integer indices starting from zero.

Q2: How can you check if an object is iterable?
A2: You can use `try: iter(obj) except TypeError: pass`, or use `isinstance(obj, collections.abc.Iterable)`.

Q3: Are all iterables iterators?
A3: No. All iterators are iterables (because iterators must have an `__iter__` method that returns themselves), but not all iterables are iterators. A list is an iterable, but it is not an iterator (it doesn't have a `__next__` method).

Q4: Why can you iterate over a list multiple times?
A4: Because each time you use a `for` loop on a list, the list's `__iter__()` method is called, which creates and returns a brand new iterator object starting from the beginning.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Write a function `filter_iterables(lst)` that takes a list of mixed types and returns a new list containing only the items that are iterable.

Exercise 2:
Create a custom class `MyWord` that wraps a string. Make the class iterable so that iterating over it yields the words in the string (split by spaces) rather than individual characters.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: Build a `DeckOfCards` class. It should not be an iterator itself, but an iterable. When a user iterates over it, it should yield cards (e.g., 'Ace of Spades', '2 of Hearts'). Ensure that iterating over the deck a second time yields a fresh deck sequence.
"""

class DeckOfCards:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
    def __iter__(self):
        # Using a generator expression to easily create an iterator
        return (f"{rank} of {suit}" for suit in self.suits for rank in self.ranks)

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    deck = DeckOfCards()
    
    # Just draw the first 5 cards to demonstrate
    print("Drawing first 5 cards:")
    deck_iterator = iter(deck)
    for _ in range(5):
        print(next(deck_iterator))


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Iterables are collections or objects that can be looped over.
- To be iterable, an object must implement `__iter__()`.
- Lists, tuples, dictionaries, strings, and sets are all built-in iterables.
- You can iterate over an iterable multiple times, unlike an iterator which is consumed.
- Use `isinstance(obj, typing.Iterable)` or `iter(obj)` with `try/except` to test for iterability.
"""

if __name__ == "__main__":
    basic_iterables()
    testing_iterability()
    custom_iterable_basic()
    common_mistakes()
    mini_challenge()
