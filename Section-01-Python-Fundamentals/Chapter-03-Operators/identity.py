"""
Topic: Identity Operators
Chapter: 3
Level: Intermediate

Description:
    Identity operators are used to compare the memory locations of two objects.
    They check if two variables point to the EXACT same object in memory, not just if their values are equal.

Real-Life Analogy:
    `==` is like checking if two identical cars have the same make and model.
    `is` is like checking if two people are looking at the exact same physical car in the parking lot.

Key Concepts:
    - is
    - is not
    - The id() function
    - Object interning (small integers and short strings)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = a (c points to a)")

    print(f"\nValues are equal? a == b: {a == b}")
    print(f"Are they the SAME object? a is b: {a is b}")
    
    print(f"Values are equal? a == c: {a == c}")
    print(f"Are they the SAME object? a is c: {a is c}")
    
    print(f"\nMemory IDs:")
    print(f"id(a): {id(a)}")
    print(f"id(b): {id(b)}")
    print(f"id(c): {id(c)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================
def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Example 1: Checking for None
    # 'is' should ALWAYS be used to check for None according to PEP 8
    my_var = None
    if my_var is None:
        print("my_var has no value.")

    # Example 2: Identity with singletons like True/False
    flag = True
    if flag is True:
        print("The flag is explicitly True.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Integer interning (CPython implementation detail)
    # CPython caches small integers from -5 to 256 for performance.
    x = 100
    y = 100
    print(f"Small integers (-5 to 256): 100 is 100 -> {x is y}")

    x = 1000
    y = 1000
    print(f"Large integers (outside cache): 1000 is 1000 -> {x is y} (May vary depending on how script is run)")

    # String interning
    # Short strings without special characters are often interned.
    s1 = "hello"
    s2 = "hello"
    print(f"Short string interning: 'hello' is 'hello' -> {s1 is s2}")

    s3 = "hello world!"
    s4 = "hello world!"
    # Long strings with spaces or special chars might not be interned (though in recent Python versions, more string literals are).
    print(f"s3 is s4? {s3 is s4}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Using `is` when you mean `==`. `is` checks memory address, `==` checks value equality.
# 2. Relying on integer or string interning for program logic. It's an implementation detail and not guaranteed across Python versions/implementations.
#
# Best Practices:
# 1. ALWAYS use `is` to compare with `None` (e.g., `if var is None:`).
# 2. Use `==` for almost all standard value comparisons (strings, numbers, lists, etc.).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: What is the difference between `is` and `==`?
# A: `==` checks for value equality (calls `__eq__`), while `is` checks for object identity (if they share the same memory address via `id()`).
#
# Q2: Why does `a = 256; b = 256; a is b` evaluate to True, but `a = 257; b = 257; a is b` evaluates to False in the REPL?
# A: CPython caches integers from -5 to 256. Variables assigned to these values point to the same pre-created objects. 257 is outside the cache, so new objects are created.
#
# Q3: How should you check if a variable is `None`?
# A: `var is None`.
#
# Q4: Does `type(x) is list` work?
# A: Yes, because types/classes are singleton objects in memory. However, `isinstance(x, list)` is preferred as it handles inheritance.
#
# Q5: Can `id()` be reused?
# A: Yes, if an object is destroyed (garbage collected), its memory address (and thus its `id()`) can be reused for a new object.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Create two identical lists. Use both `==` and `is` to compare them and print the results.
# 2. Assign one list to a new variable. Check their identity using `is`.
# 3. Write a function that takes an argument and prints "It's None!" if the argument is exactly `None` using the identity operator.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Determine the behavior of copying lists
    original = [1, [2, 3]]
    reference = original
    shallow_copy = original.copy()
    
    print("original == reference:", original == reference)
    print("original is reference:", original is reference)
    
    print("\noriginal == shallow_copy:", original == shallow_copy)
    print("original is shallow_copy:", original is shallow_copy)
    
    # But what about the inner list?
    print("\nInner list identity:")
    print("original[1] is shallow_copy[1]:", original[1] is shallow_copy[1])
    # A shallow copy creates a new outer list but references the same inner objects!

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Identity operators (`is`, `is not`) check if two variables point to the same memory location.
# - Use `==` for value comparison and `is` for object identity.
# - Always use `is None` to check for None.
# - Be aware of Python's caching mechanism for small integers and short strings.

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mini_challenge()
