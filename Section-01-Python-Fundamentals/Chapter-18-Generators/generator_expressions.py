"""
Topic: Generator Expressions
Chapter: 18
Level: Intermediate

Description:
    Generator expressions provide a concise syntax for creating generators, much like list 
    comprehensions do for lists. The main difference is that generator expressions use 
    parentheses `()` instead of square brackets `[]`. They are more memory-efficient than 
    list comprehensions because they yield items one by one instead of building the whole list.

Real-Life Analogy:
    List Comprehension: Printing an entire 100-page book at once before you start reading.
    Generator Expression: Printing one page at a time, reading it, and then printing the next page.

Key Concepts:
    - Syntax: (expression for item in iterable)
    - Memory footprint comparison
    - Use cases vs List Comprehensions
"""
import sys
from typing import Iterator

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# List Comprehension (uses brackets)
squares_list = [x * x for x in range(5)]

# Generator Expression (uses parentheses)
squares_gen = (x * x for x in range(5))

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Summing values (you don't need double parentheses for built-in functions)
sum_of_squares = sum(x * x for x in range(10))

# Filtering items
even_squares = (x * x for x in range(10) if x % 2 == 0)

# Transforming text
words = ["hello", "world", "python", "generators"]
uppercase_words = (word.upper() for word in words)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Nested Generator Expressions (Flattening a 2D list lazily)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_gen = (num for row in matrix for num in row)

# Chaining Generator Expressions
# You can pass one generator expression into another
lines = ("  line 1  ", "line 2\n", "  line 3\t")
stripped = (line.strip() for line in lines)
upper_stripped = (line.upper() for line in stripped)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Trying to index a generator expression (e.g., gen[0])
# Correction: Generators do not support indexing. You must convert to a list or use next().

# Mistake: Iterating over a generator expression twice.
# Correction: Generator expressions are exhausted after one iteration.

# Best Practice: Use generator expressions for large datasets where you only need to iterate
# through the data once, such as when using sum(), max(), min(), or writing to a file.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the syntax difference between a list comprehension and a generator expression?
# A1: List comprehensions use `[]`, while generator expressions use `()`.
#
# Q2: When would you use a list comprehension over a generator expression?
# A2: When you need to iterate over the data multiple times, need to index the data, or 
#     the dataset is small enough that memory is not a concern.
#
# Q3: Why can't you use `len()` on a generator expression?
# A3: Because the generator evaluates lazily and doesn't know how many items it has until 
#     it's exhausted.
#
# Q4: Are generator expressions faster than list comprehensions?
# A4: Not always. Building a list can be slightly faster for small datasets due to C-level
#     optimizations, but generators save significant memory and time for large datasets.
#
# Q5: Can you use nested loops in a generator expression?
# A5: Yes, they follow the exact same syntax rules as list comprehensions.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a generator expression that yields cubes of numbers from 1 to 20.
# Exercise 2: Use a generator expression to find the maximum value of the function f(x) = x^2 - 5x + 6 for x in range(-10, 10).
# Exercise 3: Create a generator expression that reads a list of filenames and yields only those ending in ".py".

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a single generator expression that takes a list of mixed types
# and yields only the string values, converted to lowercase.

def filter_lowercase_strings(mixed_data: list) -> Iterator[str]:
    """Yields only lowercase versions of the strings in the list."""
    return (item.lower() for item in mixed_data if isinstance(item, str))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Generator expressions use `()` and generate items lazily.
# - They are highly memory-efficient compared to list comprehensions.
# - They can be passed directly into functions like sum(), min(), max().
# - They only allow a single iteration pass.

if __name__ == "__main__":
    print("--- Memory Comparison ---")
    list_comp = [x for x in range(100000)]
    gen_expr = (x for x in range(100000))
    print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator expression size: {sys.getsizeof(gen_expr)} bytes")
    
    print("\n--- Practical Examples ---")
    print(f"Sum of squares: {sum_of_squares}")
    print(f"Even squares: {list(even_squares)}")
    
    print("\n--- Advanced Usage ---")
    print(f"Flattened matrix: {list(flat_gen)}")
    print(f"Chained generators: {list(upper_stripped)}")
    
    print("\n--- Mini Challenge ---")
    mixed = [1, "HELLO", 3.14, "World", None, "PYTHON"]
    print(list(filter_lowercase_strings(mixed)))
