"""
Topic: Overview of List, Dictionary, and Set Comprehensions
Chapter: 06
Level: Advanced

Description:
    Comprehensions provide a concise and highly optimized way to create new sequences (lists, dictionaries, sets) from existing iterables. 
    They replace multi-line `for` loops that append items to a sequence.

Real-Life Analogy:
    Instead of saying "Get an apple from the basket, wash it, and put it in a new basket, then repeat for all apples", 
    you say "Wash all apples from the basket and put them in the new basket."

Key Concepts:
    - List Comprehensions `[expression for item in iterable if condition]`
    - Dictionary Comprehensions `{key: value for item in iterable}`
    - Set Comprehensions `{expression for item in iterable}`
    - Conditional filtering and expression mapping
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def list_comprehension_basics():
    print("--- Basic List Comprehension ---")
    # Old way
    squares_loop = []
    for i in range(5):
        squares_loop.append(i ** 2)
        
    # Comprehension way
    squares_comp = [i ** 2 for i in range(5)]
    
    print("Loop:", squares_loop)
    print("Comp:", squares_comp)

    print("\n--- Set Comprehension ---")
    # Creates a set of unique lengths of words
    words = ["apple", "bat", "cat", "apple"]
    lengths = {len(word) for word in words}
    print(f"Unique lengths: {lengths}")

    print("\n--- Dictionary Comprehension ---")
    # Maps number to its square
    squares_dict = {i: i**2 for i in range(3)}
    print(f"Squares Map: {squares_dict}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def conditional_comprehensions():
    print("\n--- Filtering with If ---")
    numbers = [1, 2, 3, 4, 5, 6]
    # Keep only even numbers
    evens = [n for n in numbers if n % 2 == 0]
    print(f"Evens: {evens}")

    print("\n--- If-Else Expression Mapping ---")
    # Mark numbers as "Even" or "Odd"
    # Note: When using if-else to change the value, it goes BEFORE the 'for'
    labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
    print(f"Labels: {labels}")

def practical_dict_comprehension():
    print("\n--- Inverting a Dictionary ---")
    employee_ids = {"Alice": 101, "Bob": 102, "Charlie": 103}
    # Swap keys and values
    id_to_name = {v: k for k, v in employee_ids.items()}
    print(f"Inverted Dict: {id_to_name}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def nested_comprehensions():
    print("\n--- Nested List Comprehension ---")
    # Flattening a 2D matrix
    matrix = [[1, 2], [3, 4], [5, 6]]
    # Read as: for row in matrix, then for item in row, return item
    flat = [item for row in matrix for item in row]
    print(f"Flattened matrix: {flat}")

    print("\n--- Matrix Transposition ---")
    matrix = [[1, 2, 3], [4, 5, 6]]
    # Transpose rows and columns
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print(f"Transposed: {transposed}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Creating overly complex nested comprehensions that are impossible to read.
# 2. Putting the `if` condition in the wrong place (after the `for` for filtering, before the `for` if part of a ternary expression).
# 3. Using list comprehensions purely for their side effects (e.g., `[print(x) for x in range(5)]`). This is unpythonic; use a regular for-loop.

# Best Practices:
# 1. Use comprehensions for simple mapping and filtering.
# 2. If a comprehension spans more than two lines or has multiple nested loops, refactor it into a standard `for` loop for readability.
# 3. Use generator expressions `(expr for x in obj)` instead of list comprehensions `[expr for x in obj]` if you are only iterating over it once and want to save memory.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the difference between a list comprehension and a generator expression?
A: List comprehension `[...]` creates the entire list in memory. Generator expression `(...)` creates a generator object that evaluates lazily, saving memory for large datasets.

Q2: How do you add an if-else condition in a list comprehension?
A: The if-else operates as a ternary operator on the output expression, so it goes before the `for`: `[x if x > 0 else 0 for x in nums]`.

Q3: Can you have multiple `if` statements in a comprehension?
A: Yes. `[x for x in nums if x > 0 if x % 2 == 0]` works and acts as an implicit AND.

Q4: Is a list comprehension faster than a for-loop?
A: Generally, yes. It is executed in C under the hood and doesn't require looking up the `.append()` method on every iteration.

Q5: What is tuple comprehension?
A: There is no tuple comprehension. `(x for x in nums)` creates a generator. To create a tuple, use `tuple(x for x in nums)`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Create a list of the first letter of every word in a sentence using comprehension.
    sentence = "Python comprehensions are very powerful"
    pass

    # Exercise 2: Use dictionary comprehension to map numbers 1-5 to their cubes.
    pass

    # Exercise 3: Given a list of strings, create a set comprehension containing all the strings converted to uppercase.
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge:
    Given a dictionary of students and their grades, create a new dictionary 
    containing only the students who scored 80 or above. 
    Also, add a 5-point bonus to their score in the new dictionary.
    """
    students = {"Alice": 75, "Bob": 82, "Charlie": 90, "David": 60, "Eve": 88}
    
    print("\n--- Honors Students Bonus ---")
    
    honors_with_bonus = {name: score + 5 for name, score in students.items() if score >= 80}
    print(f"Original: {students}")
    print(f"Honors with bonus: {honors_with_bonus}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Comprehensions are expressive, readable, and fast.
- They support List `[]`, Set `{}`, and Dict `{k: v}` syntaxes.
- They can include conditionals for filtering (`if` at the end) and mapping (`if-else` at the start).
- Avoid deeply nested comprehensions to maintain readability.
"""

if __name__ == "__main__":
    list_comprehension_basics()
    conditional_comprehensions()
    practical_dict_comprehension()
    nested_comprehensions()
    mini_challenge()
