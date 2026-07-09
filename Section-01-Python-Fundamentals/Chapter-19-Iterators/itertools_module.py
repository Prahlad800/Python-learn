"""
Topic: Itertools Module
Chapter: 19
Level: Intermediate

Description:
    The `itertools` module is a built-in Python library that provides a collection of fast, memory-efficient tools for working with iterators. It standardizes a core set of fast, memory-efficient tools that are useful by themselves or in combination. It provides infinite iterators, iterators terminating on the shortest input sequence, and combinatoric generators.

Real-Life Analogy:
    Think of `itertools` like a Swiss Army knife for assembly lines (iterators). Instead of building custom machines to group items, combine streams, or repeat elements, `itertools` gives you pre-built, highly optimized tools to snap onto your assembly line.

Key Concepts:
    - Infinite iterators: `count`, `cycle`, `repeat`
    - Finite iterators: `chain`, `islice`, `compress`, `filterfalse`
    - Combinatoric iterators: `product`, `permutations`, `combinations`
"""

import itertools
import time

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_infinite_iterators() -> None:
    print("--- Section 1: Infinite Iterators ---")
    
    # 1. itertools.count(start, step)
    counter = itertools.count(start=10, step=5)
    print("count(): ", [next(counter) for _ in range(5)])
    
    # 2. itertools.cycle(iterable)
    cycler = itertools.cycle(['A', 'B', 'C'])
    print("cycle(): ", [next(cycler) for _ in range(7)])
    
    # 3. itertools.repeat(object, times)
    repeater = itertools.repeat("Python", 3)
    print("repeat():", list(repeater))


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_finite_iterators() -> None:
    print("\n--- Section 2: Finite Iterators ---")
    
    # itertools.chain() - combines multiple iterables
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    chained = itertools.chain(list1, list2)
    print("chain():   ", list(chained))
    
    # itertools.islice() - slices an iterator (since standard slicing [:] doesn't work on iterators)
    infinite_nums = itertools.count(0)
    sliced = itertools.islice(infinite_nums, 10, 15)  # Get items from index 10 to 14
    print("islice():  ", list(sliced))
    
    # itertools.compress() - filters an iterable using a boolean mask
    data = ['apple', 'banana', 'cherry', 'date']
    selectors = [True, False, True, False]
    compressed = itertools.compress(data, selectors)
    print("compress():", list(compressed))


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def combinatoric_iterators() -> None:
    print("\n--- Section 3: Combinatoric Iterators ---")
    
    items = ['A', 'B', 'C']
    
    # Cartesian product (like nested loops)
    prod = itertools.product([1, 2], ['X', 'Y'])
    print("product():      ", list(prod))
    
    # Permutations (all possible orderings, order matters)
    perms = itertools.permutations(items, 2)
    print("permutations(): ", list(perms))
    
    # Combinations (all possible groupings, order doesn't matter)
    combs = itertools.combinations(items, 2)
    print("combinations(): ", list(combs))
    
    # Combinations with replacement
    combs_repl = itertools.combinations_with_replacement(items, 2)
    print("comb_with_repl():", list(combs_repl))


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake: Converting an infinite iterator to a list
    # DO NOT DO THIS: list(itertools.count()) -> Memory Error / Crash
    
    # Mistake: Exhausting an iterator and trying to use it again
    grouped = itertools.chain([1, 2], [3, 4])
    print("First pass: ", list(grouped))
    print("Second pass:", list(grouped)) # Prints empty list!
    
    # Best Practice: Store as list if you need it multiple times, or recreate the iterator.


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: Why use `itertools` instead of regular loops or list comprehensions?
A1: `itertools` functions return iterators, meaning they are evaluated lazily. This saves memory and can drastically improve performance when working with large datasets.

Q2: How do you slice an iterator in Python?
A2: You cannot use standard bracket slicing `[start:stop]` on an iterator. You must use `itertools.islice(iterator, start, stop)`.

Q3: What is the difference between permutations and combinations in `itertools`?
A3: Permutations care about order (AB is different from BA). Combinations do not care about order (AB is the same as BA, so it only returns one of them).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Use `itertools.cycle` and `zip` to pair a list of 10 numbers [1 to 10] with alternating strings 'Odd' and 'Even'.

Exercise 2:
Use `itertools.groupby` to group a sorted list of words by their first letter.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: Write a script that generates all possible 3-digit pin codes (000-999) using `itertools.product`, and finds how many of those pins contain the digit '7'.
"""

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    digits = [str(i) for i in range(10)]
    
    # Generate all 3-digit combinations
    all_pins = itertools.product(digits, repeat=3)
    
    # Filter and count those containing '7'
    pins_with_7 = 0
    for pin_tuple in all_pins:
        if '7' in pin_tuple:
            pins_with_7 += 1
            
    print(f"Total 3-digit pins containing '7': {pins_with_7}")


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- The `itertools` module is essential for fast, memory-efficient iteration.
- Infinite iterators (`count`, `cycle`) must be bounded (e.g., via `islice` or loop breaks).
- Combinatoric iterators (`product`, `permutations`) replace deeply nested loops.
- All tools in `itertools` return iterators, meaning they yield data lazily.
"""

if __name__ == "__main__":
    basic_infinite_iterators()
    practical_finite_iterators()
    combinatoric_iterators()
    common_mistakes()
    mini_challenge()
