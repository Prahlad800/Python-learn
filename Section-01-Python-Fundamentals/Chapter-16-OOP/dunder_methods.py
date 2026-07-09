"""
Topic: Dunder (Magic) Methods
Chapter: 16
Level: Intermediate

Description:
    Dunder methods (short for "Double Under") are special built-in methods in Python that 
    start and end with double underscores, like `__init__` or `__str__`. They allow you to 
    define how objects of your class behave with built-in operations (like +, -, len(), print()).

Real-Life Analogy:
    Imagine giving your custom robot specific instructions on how to react to standard human 
    gestures. If someone waves (a standard built-in action), the robot knows to wave back 
    because you programmed its "wave response" (the dunder method).

Key Concepts:
    - Initialization: `__init__`
    - String Representation: `__str__` and `__repr__`
    - Operator Overloading: `__add__`, `__sub__`, `__eq__`
    - Collection Emulation: `__len__`, `__getitem__`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        
    # Controls what print(object) outputs
    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"
        
    # Controls the official string representation (useful for debugging)
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.pages})"
        
    # Controls the behavior of len(object)
    def __len__(self) -> int:
        return self.pages

def basic_syntax_examples():
    print("--- Basic Syntax ---")
    my_book = Book("The Hobbit", "J.R.R. Tolkien", 310)
    
    print(my_book)             # Uses __str__
    print(repr(my_book))       # Uses __repr__
    print(len(my_book))        # Uses __len__

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (OPERATOR OVERLOADING)
# ============================================================

class Vector:
    """A 2D Vector class demonstrating operator overloading."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
        
    # Overloading the '+' operator
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector to Vector")
        
    # Overloading the '==' operator
    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

def practical_examples():
    print("\n--- Practical Examples ---")
    v1 = Vector(2, 4)
    v2 = Vector(3, -1)
    
    v3 = v1 + v2  # Uses __add__
    print(f"v1 + v2 = {v3}")
    
    v4 = Vector(2, 4)
    print(f"v1 == v4 is {v1 == v4}") # Uses __eq__

# ============================================================
# SECTION 3: ADVANCED USAGE (COLLECTION EMULATION)
# ============================================================

class DeckOfCards:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]
        
    def __len__(self) -> int:
        return len(self.cards)
        
    # Allows indexing (e.g., deck[0]) and iteration (e.g., for card in deck)
    def __getitem__(self, position: int):
        return self.cards[position]

def advanced_usage():
    print("\n--- Advanced Usage ---")
    deck = DeckOfCards()
    print(f"Deck size: {len(deck)}")
    print(f"First card: {deck[0]}")
    print(f"Last card: {deck[-1]}")
    
    # Because __getitem__ is implemented, we can iterate over it!
    print("Top 3 cards:")
    for card in deck[:3]:
        print(f" - {card}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Returning non-strings from __str__ or non-integers from __len__
class BadClass:
    def __str__(self):
        return 123  # TypeError: __str__ returned non-string
        
    def __len__(self):
        return "five" # TypeError: 'str' object cannot be interpreted as an integer

# Best Practice: Always implement `__repr__`. If `__str__` is not defined, Python falls back to `__repr__`. 
# `__repr__` should ideally look like a valid Python expression that could be used to recreate the object.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What are dunder methods?
A: Dunder methods are special methods with double underscores before and after their names. They allow you to define custom behavior for built-in Python operations.

Q2: What is the difference between `__str__` and `__repr__`?
A: `__str__` is intended to be human-readable, for end users. `__repr__` is intended for developers for debugging, and should ideally be a valid Python expression to recreate the object.

Q3: How do you overload the `+` operator?
A: By implementing the `__add__(self, other)` dunder method.

Q4: What method enables an object to be iterated over in a `for` loop if `__iter__` is missing?
A: Python will fall back to using the `__getitem__` method if it is defined.

Q5: Why shouldn't you invent your own dunder methods (e.g., `__my_method__`)?
A: Python reserves the double underscore namespace for language-level features. Inventing your own might conflict with future Python updates.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1: Create a `Wallet` class containing an amount of money. Implement `__add__` to combine two wallets and `__str__` to print the balance.
Exercise 2: Create a `ShoppingCart` class. Implement `__len__` to return the number of items and `__getitem__` to get an item by index.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

class Currency:
    def __init__(self, amount: float, symbol: str = "$"):
        self.amount = amount
        self.symbol = symbol
        
    def __str__(self):
        return f"{self.symbol}{self.amount:.2f}"
        
    def __repr__(self):
        return f"Currency({self.amount}, '{self.symbol}')"
        
    def __add__(self, other):
        if isinstance(other, Currency) and self.symbol == other.symbol:
            return Currency(self.amount + other.amount, self.symbol)
        raise ValueError("Cannot add different currencies or non-currency types")
        
    def __lt__(self, other):
        # Less than operator (<)
        if isinstance(other, Currency) and self.symbol == other.symbol:
            return self.amount < other.amount
        raise ValueError("Cannot compare")

def mini_challenge():
    print("\n--- Mini Challenge ---")
    c1 = Currency(10.50)
    c2 = Currency(5.25)
    
    total = c1 + c2
    print(f"Total: {total}")
    
    print(f"Is {c1} less than {c2}? {c1 < c2}")
    
    items = [Currency(20), Currency(5), Currency(15)]
    # Sorting works because we implemented __lt__!
    items.sort()
    print(f"Sorted items: {[str(item) for item in items]}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Dunder methods define custom behaviors for built-in operations.
- `__init__` sets up the object.
- `__str__` (user friendly) and `__repr__` (developer friendly) handle string formatting.
- Mathematical operators (+, -, *, /) are handled by `__add__`, `__sub__`, etc.
- Comparisons (==, <, >) use `__eq__`, `__lt__`, `__gt__`.
"""

if __name__ == "__main__":
    basic_syntax_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
