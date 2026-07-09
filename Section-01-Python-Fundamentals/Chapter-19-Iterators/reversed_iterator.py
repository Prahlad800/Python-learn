"""
Topic: Reversed Iterator
Chapter: 19
Level: Intermediate

Description:
    Python allows you to iterate over sequences in reverse order efficiently using the built-in `reversed()` function. Unlike slicing (`[::-1]`), which creates a full copy of the list in memory, `reversed()` returns an iterator that traverses the existing collection backwards. You can also implement custom reverse iteration by defining the `__reversed__()` magic method in your classes.

Real-Life Analogy:
    Imagine reading a book from the last page to the first. Using slicing `[::-1]` is like photocopying the entire book backwards and then reading the copy. Using `reversed()` is like simply turning the pages of the original book from right to left.

Key Concepts:
    - The `reversed()` built-in function
    - Slicing vs reversed()
    - The `__reversed__()` magic method
"""

import sys

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_reversed() -> None:
    print("--- Section 1: Basic Reversed ---")
    
    words = ["Python", "is", "awesome"]
    
    # reversed() returns a list_reverseiterator object
    rev_iter = reversed(words)
    print(f"Type: {type(rev_iter)}")
    
    print("Iterating backwards:")
    for word in rev_iter:
        print(word)


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def efficiency_demo() -> None:
    print("\n--- Section 2: Memory Efficiency ---")
    
    # A large list
    large_list = list(range(1_000_000))
    
    # Slicing creates a new list in memory
    sliced_reversed = large_list[::-1]
    
    # reversed() creates a lightweight iterator
    lazy_reversed = reversed(large_list)
    
    print(f"Size of sliced list: {sys.getsizeof(sliced_reversed)} bytes")
    print(f"Size of reversed iterator: {sys.getsizeof(lazy_reversed)} bytes")


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

class Countdown:
    """A custom sequence that supports both normal and reverse iteration."""
    def __init__(self, start: int):
        self.start = start
        
    def __iter__(self):
        """Normal iteration (e.g., 5, 4, 3, 2, 1)"""
        current = self.start
        while current > 0:
            yield current
            current -= 1
            
    def __reversed__(self):
        """Reverse iteration triggered by reversed() (e.g., 1, 2, 3, 4, 5)"""
        current = 1
        while current <= self.start:
            yield current
            current += 1

def custom_reversed_demo() -> None:
    print("\n--- Section 3: Custom __reversed__ Method ---")
    cd = Countdown(5)
    
    print("Normal iteration:")
    print(list(cd))
    
    print("Reversed iteration:")
    print(list(reversed(cd)))


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake: Trying to use reversed() on unordered collections like sets or dicts (before Python 3.8)
    my_set = {1, 2, 3}
    try:
        reversed(my_set)
    except TypeError as e:
        print(f"Error on set: {e}")
        
    # Mistake: Using reversed() on standard generators/iterators
    # Iterators generally cannot be reversed because they compute values on the fly one-way.
    gen = (x for x in range(5))
    try:
        reversed(gen)
    except TypeError as e:
        print(f"Error on generator: {e}")
        
    # Best Practice: Only use reversed() on sequences (lists, strings, tuples) or objects implementing __reversed__.


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the difference between `my_list[::-1]` and `reversed(my_list)`?
A1: `my_list[::-1]` creates a shallow copy of the entire list in reverse order (eager, consumes memory). `reversed(my_list)` returns an iterator that traverses the original list backwards (lazy, memory efficient).

Q2: Can you call `reversed()` on a generator?
A2: No. Generators are forward-only iterators. To reverse generator output, you must cast it to a list first, e.g., `reversed(list(gen))`, which negates the memory benefits of the generator.

Q3: How do you make a custom class support the `reversed()` function?
A3: By implementing the `__reversed__(self)` dunder method, which should return an iterator yielding elements in reverse order.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Write a loop that prints the characters of the string "ITERATORS" in reverse without using slicing.

Exercise 2:
Create a custom class `Vowels` containing `['A', 'E', 'I', 'O', 'U']`. Implement `__iter__` and `__reversed__` so it can be traversed in both directions.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: 
Write a function `is_palindrome_lazy(s: str)` that checks if a string is a palindrome.
It must use `zip()` and `reversed()` to check characters from the outside in, and it should stop early if a mismatch is found, without creating sliced copies of the string.
"""

def is_palindrome_lazy(s: str) -> bool:
    # We only need to check the first half against the reversed second half
    # zip will naturally pair them up.
    for forward_char, backward_char in zip(s, reversed(s)):
        if forward_char != backward_char:
            return False
    return True

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    words = ["racecar", "python", "kayak"]
    
    for w in words:
        print(f"Is '{w}' a palindrome? {is_palindrome_lazy(w)}")


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- `reversed()` returns a lazy iterator traversing a sequence in reverse.
- It is far more memory-efficient than slicing `[::-1]` for large sequences.
- You can customize reverse iteration in your own classes using `__reversed__()`.
- Unordered collections (sets) and forward-only iterators (generators) cannot be directly reversed.
"""

if __name__ == "__main__":
    basic_reversed()
    efficiency_demo()
    custom_reversed_demo()
    common_mistakes()
    mini_challenge()
