"""
Topic: Chaining Iterators
Chapter: 19
Level: Intermediate

Description:
    Chaining iterators is the process of combining multiple iterables into a single continuous iterator. Instead of concatenating lists (which creates a new, large list in memory), chaining allows you to iterate over the first collection, and when it is exhausted, seamlessly move on to the next collection. This is highly memory-efficient.

Real-Life Analogy:
    Imagine several playlists of songs. If you concatenate them eagerly, you burn them all onto one giant CD. If you chain them (lazy), the DJ just puts the first playlist on, and the moment it finishes, the DJ hits play on the second playlist.

Key Concepts:
    - `itertools.chain()`
    - Memory efficiency vs list concatenation
    - Unpacking with `itertools.chain.from_iterable()`
"""

import itertools
import sys

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_chaining() -> None:
    print("--- Section 1: Basic Chaining ---")
    
    list1 = [1, 2, 3]
    tuple1 = (4, 5, 6)
    string1 = "78"
    
    # Using itertools.chain to combine disparate iterables seamlessly
    chained = itertools.chain(list1, tuple1, string1)
    
    print("Chained output:")
    for item in chained:
        print(item, end=" ")
    print("\n")


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def efficiency_comparison() -> None:
    print("--- Section 2: Memory Efficiency ---")
    
    # Two large ranges
    r1 = range(1_000_000)
    r2 = range(1_000_000, 2_000_000)
    
    # Bad way: List concatenation (evaluates immediately, heavy memory usage)
    # combined_list = list(r1) + list(r2) 
    
    # Good way: Chaining (lazy evaluation)
    chained_iter = itertools.chain(r1, r2)
    
    # The chain object takes almost no memory, regardless of data size!
    print(f"Size of chain object: {sys.getsizeof(chained_iter)} bytes")
    
    # We can still get elements normally
    print(f"First item: {next(chained_iter)}")


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def chain_from_iterable_demo() -> None:
    print("\n--- Section 3: chain.from_iterable() ---")
    
    # Sometimes you have a single iterable that CONTAINS multiple iterables (e.g., list of lists)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Instead of itertools.chain(matrix[0], matrix[1], matrix[2])...
    # Use chain.from_iterable() to flatten it!
    flattened = itertools.chain.from_iterable(matrix)
    
    print("Flattened matrix:")
    print(list(flattened))


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake: Using chain() when you have a list of lists.
    list_of_lists = [[1, 2], [3, 4]]
    
    # This just iterates over the outer list, yielding [1, 2] then [3, 4]
    wrong_chain = itertools.chain(list_of_lists)
    print("Wrong way: ", list(wrong_chain))
    
    # Best Practice: Use * unpacking or from_iterable
    right_chain_1 = itertools.chain(*list_of_lists)
    right_chain_2 = itertools.chain.from_iterable(list_of_lists)
    
    print("Right way 1:", list(right_chain_1))
    print("Right way 2:", list(right_chain_2))


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the difference between `list1 + list2` and `itertools.chain(list1, list2)`?
A1: The `+` operator creates a new list in memory containing all elements of both lists. `itertools.chain` creates a lightweight iterator that pulls elements from the first list until exhausted, then pulls from the second, saving memory and time.

Q2: How do you flatten a 2D list into a 1D iterator?
A2: Using `itertools.chain.from_iterable(list_of_lists)`.

Q3: Can you chain iterators of different types?
A3: Yes, `chain()` works with any iterables (lists, strings, sets, generators, etc.) simultaneously.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Write a function that takes three file names. Create an iterator that chains the reading of all three files line-by-line without loading them all into memory at once.

Exercise 2:
Given `data = (range(5), [10, 11], "XYZ")`, flatten and print it using `itertools.chain.from_iterable()`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: Custom Chain Function.
Write your own generator function called `my_chain(*iterables)` that mimics the behavior of `itertools.chain()`.
"""

def my_chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    custom = my_chain([1, 2], ['a', 'b'], "END")
    print("Custom chain output:")
    print(list(custom))


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Chaining iterators combines multiple sequences into one continuous sequence.
- `itertools.chain(*args)` takes individual iterables as arguments.
- `itertools.chain.from_iterable(iterable)` takes a single iterable containing other iterables.
- Chaining is evaluated lazily, avoiding massive memory allocations common with list concatenation.
"""

if __name__ == "__main__":
    basic_chaining()
    efficiency_comparison()
    chain_from_iterable_demo()
    common_mistakes()
    mini_challenge()
