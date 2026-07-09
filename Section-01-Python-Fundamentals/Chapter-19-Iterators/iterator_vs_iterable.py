"""
Topic: Iterator vs Iterable
Chapter: 19
Level: Beginner

Description:
    The terms "iterable" and "iterator" are often confused. An Iterable is an object that contains data and can be looped over (like a list or string). An Iterator is the active agent that does the actual looping and remembers where it is in the sequence. Every iterator is an iterable, but not every iterable is an iterator.

Real-Life Analogy:
    Iterable: A deck of cards. It contains all the cards.
    Iterator: The dealer. The dealer remembers whose turn it is and gives out the next card one by one when requested. 
    You get a dealer (iterator) from the deck (iterable) using `iter(deck)`.

Key Concepts:
    - Iterable: has `__iter__()` returning an iterator.
    - Iterator: has `__iter__()` (returns self) AND `__next__()`.
    - Iterables can be iterated multiple times. Iterators are one-use only (exhaustible).
"""

from collections.abc import Iterable, Iterator

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def definitions_demo() -> None:
    print("--- Section 1: Iterable vs Iterator ---")
    
    # Lists are Iterables
    my_list = [1, 2, 3] 
    
    # We create an Iterator FROM the Iterable
    my_iterator = iter(my_list)
    
    print(f"Is my_list an Iterable? {isinstance(my_list, Iterable)}")
    print(f"Is my_list an Iterator? {isinstance(my_list, Iterator)}")
    
    print(f"\nIs my_iterator an Iterable? {isinstance(my_iterator, Iterable)}")
    print(f"Is my_iterator an Iterator? {isinstance(my_iterator, Iterator)}")


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def reusability_demo() -> None:
    print("\n--- Section 2: Reusability ---")
    
    nums_iterable = [1, 2, 3]
    nums_iterator = iter([1, 2, 3])
    
    print("Iterating the Iterable (List):")
    print("Pass 1:", list(nums_iterable))
    print("Pass 2:", list(nums_iterable)) # Works perfectly again!
    
    print("\nIterating the Iterator:")
    print("Pass 1:", list(nums_iterator))
    print("Pass 2:", list(nums_iterator)) # Empty! The iterator is exhausted.


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def custom_classes_comparison() -> None:
    print("\n--- Section 3: Building Both ---")
    
    class MyIterator:
        def __init__(self): self.val = 0
        def __iter__(self): return self
        def __next__(self):
            if self.val >= 3: raise StopIteration
            self.val += 1
            return self.val
            
    class MyIterable:
        def __iter__(self):
            # Creates and returns a fresh iterator each time
            return MyIterator()
            
    iterable = MyIterable()
    
    print("Using Custom Iterable multiple times:")
    print([x for x in iterable])
    print([x for x in iterable])


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake: Treating an iterator like an iterable data store
    gen = (x for x in range(3))
    
    # Passing the iterator to multiple functions expecting full data
    def process_data(data):
        return sum(data)
        
    print("First call: ", process_data(gen)) # Returns 3
    print("Second call:", process_data(gen)) # Returns 0 (generator is empty!)
    
    # Best Practice: If multiple functions need to iterate over the data independently, 
    # pass an Iterable (like a list) or recreate the iterator/generator.


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the fundamental difference between an iterable and an iterator?
A1: An iterable is a collection of items (implements `__iter__` returning an iterator). An iterator is an object that traverses a collection and keeps state (implements `__next__` and `__iter__` returning itself). 

Q2: Why is a list not an iterator?
A2: Because it does not implement `__next__()`. It does not keep track of an internal state (like a pointer to the current element). You can iterate over a list from the beginning as many times as you want.

Q3: Are all iterators iterables?
A3: Yes. Iterators must implement `__iter__()` returning themselves, which satisfies the definition of an iterable.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Write code that checks whether a dictionary `{"a": 1, "b": 2}` is an Iterator. Then get an iterator from it and check that object.

Exercise 2:
Explain why `for x in iter([1,2,3]):` works just as well as `for x in [1,2,3]:`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: 
Write a function `inspect_object(obj)` that prints:
- "Iterable only" if it's an iterable but not an iterator.
- "Iterator" if it's both.
- "Neither" if it's neither.
Test it with: a list, a generator expression, and an integer.
"""

def inspect_object(obj) -> None:
    is_iterable = isinstance(obj, Iterable)
    is_iterator = isinstance(obj, Iterator)
    
    if is_iterator:
        print(f"{type(obj).__name__:<15}: Iterator")
    elif is_iterable:
        print(f"{type(obj).__name__:<15}: Iterable only")
    else:
        print(f"{type(obj).__name__:<15}: Neither")

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    inspect_object([1, 2, 3])
    inspect_object((x for x in range(3)))
    inspect_object(42)
    inspect_object(iter("hello"))


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- **Iterable**: Data container. Implements `__iter__()`. Can be iterated multiple times.
- **Iterator**: State-keeper. Implements `__iter__()` and `__next__()`. Consumed after one full iteration.
- You get an iterator from an iterable using the `iter()` function.
- All Iterators are Iterables, but Iterables are not Iterators.
"""

if __name__ == "__main__":
    definitions_demo()
    reusability_demo()
    custom_classes_comparison()
    common_mistakes()
    mini_challenge()
