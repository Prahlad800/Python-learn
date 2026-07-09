"""
Topic: Recursion
Chapter: 7
Level: Intermediate / Advanced

Description:
    Recursion occurs when a function calls itself to solve a smaller instance of the same problem. A recursive function must have a base case to terminate and a recursive step to continue breaking down the problem.

Real-Life Analogy:
    Imagine looking up a word in a dictionary. The definition uses another word you don't know, so you look that word up. You keep looking up words (calling the same process) until you find a definition where you understand every word (the base case). Then you trace back your understanding to the original word.

Key Concepts:
    - Base case
    - Recursive step
    - Call stack
    - Recursion depth limits
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# A recursive function structure:
def simple_countdown(n: int) -> None:
    # 1. Base case: The condition to stop recursion
    if n <= 0:
        print("Blastoff!")
        return
    
    # 2. Do some work
    print(n)
    
    # 3. Recursive step: Call the function with a modified argument
    simple_countdown(n - 1)

print("Starting countdown:")
simple_countdown(3)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Factorial calculation
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Example 2: Summing elements in a list
def recursive_sum(numbers: list) -> int:
    if not numbers:  # Base case: empty list
        return 0
    # Recursive step: first element + sum of the rest
    return numbers[0] + recursive_sum(numbers[1:])

print(f"Sum of [1, 2, 3, 4, 5]: {recursive_sum([1, 2, 3, 4, 5])}")

# Example 3: Finding Fibonacci numbers
# 0, 1, 1, 2, 3, 5, 8...
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"6th Fibonacci number: {fibonacci(6)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

import sys

# Example 1: Checking recursion limit
print(f"Current recursion limit: {sys.getrecursionlimit()}")

# Example 2: Traversing nested structures (e.g., nested dictionaries)
def count_leaves(tree: dict | int | str) -> int:
    """Counts the number of non-dictionary leaf nodes in a nested structure."""
    if not isinstance(tree, dict):
        return 1  # Base case: it's a leaf
    
    count = 0
    for key, value in tree.items():
        count += count_leaves(value) # Recursive call
    return count

nested_data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "f": 4
        }
    },
    "g": 5
}
print(f"Number of leaves in nested data: {count_leaves(nested_data)}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Missing the base case
# If you forget the base case, the function will run until it hits the RecursionError.
# def infinite_recurse(): infinite_recurse() # Don't do this!

# Mistake 2: Not modifying the argument
# If the recursive step calls the function with the exact same argument, it never reaches the base case.

# Best Practice: Tail Recursion (Note: Python does not optimize tail recursion)
# Always consider if an iterative approach (like a while/for loop) would be better
# since deep recursion in Python can raise a RecursionError and uses more memory.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What are the two main parts of a recursive function?
# A: The base case (which stops the recursion) and the recursive step (which reduces the problem).

# Q2: What happens if a recursive function lacks a base case?
# A: It results in infinite recursion, eventually crashing with a RecursionError due to call stack overflow.

# Q3: Why might recursion be worse than iteration?
# A: Recursion uses more memory because each function call adds a new frame to the call stack. Python has a maximum recursion depth.

# Q4: Can every recursive function be written iteratively?
# A: Yes, any recursive algorithm can be rewritten using iteration and an explicit stack data structure.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a recursive function to reverse a string.
def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

# Exercise 2: Write a recursive function to calculate a raised to the power of b.
def power(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * power(a, b - 1)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Write a recursive function `is_palindrome(word)` that returns True if the word
# is a palindrome, and False otherwise. Treat empty strings or single characters as True.
def is_palindrome(word: str) -> bool:
    # Base case: string is 0 or 1 character long
    if len(word) <= 1:
        return True
    
    # Check if first and last characters match
    if word[0] != word[-1]:
        return False
        
    # Recursive step: check the substring without first and last characters
    return is_palindrome(word[1:-1])

print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
print(f"Is 'hello' a palindrome? {is_palindrome('hello')}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Recursion is a technique where a function calls itself.
# - It requires a base case to prevent infinite loops (RecursionError).
# - It breaks problems into smaller, identical subproblems.
# - It can be elegant for traversing trees or nested structures but uses more memory than iteration.

if __name__ == "__main__":
    pass
