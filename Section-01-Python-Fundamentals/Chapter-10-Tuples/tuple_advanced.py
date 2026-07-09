"""
Topic: Advanced Tuple Concepts
Chapter: 10
Level: Advanced

Description:
    Dive deeper into how tuples function in Python. This file covers nested tuples, 
    tuples containing mutable objects (and the implications thereof), hashing 
    rules, and advanced unpacking tricks.

Real-Life Analogy:
    A nested tuple is like a Matryoshka doll (Russian nesting dolls) where you can 
    have tuples inside tuples. A tuple containing a list is like a locked safe 
    containing a transparent box; you can't replace the box, but you can put things 
    into the box.

Key Concepts:
    - Nested Tuples
    - Immutability caveats (Mutable items inside tuples)
    - Hashing and Hashability
    - Advanced Unpacking
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def advanced_nesting() -> None:
    # Tuples can contain other tuples (Nested Tuples)
    matrix = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    
    # Accessing elements in a nested tuple
    row = matrix[1]
    cell = matrix[1][2]
    
    print(f"Second row: {row}")
    print(f"Value at row 1, col 2: {cell}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def mutable_inside_immutable() -> None:
    # A tuple is immutable, meaning its references cannot change.
    # However, if it references a mutable object, that object can change.
    company = ("TechCorp", [10, 20, 30])  # List represents revenue
    print(f"Original company tuple: {company}")
    
    # We cannot do: company[1] = [10, 20, 30, 40] -> TypeError
    # But we can mutate the list inplace:
    company[1].append(40)
    print(f"Modified company tuple: {company}")
    
    # Tricky edge case (The += operator on a mutable object inside a tuple)
    try:
        company[1] += [50]
    except TypeError as e:
        print(f"Caught TypeError: {e}")
        # Surprisingly, the list ACTUALLY GOT UPDATED before the error was thrown!
        print(f"Tuple after += error: {company}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def hashability() -> None:
    # In Python, an object is hashable if it has a hash value which never changes.
    # Tuples are hashable ONLY IF all their contents are hashable.
    
    hashable_tuple = (1, 2, "hello")
    print(f"Hash of hashable_tuple: {hash(hashable_tuple)}")
    
    # This tuple contains a list (unhashable)
    unhashable_tuple = (1, 2, ["hello"])
    
    try:
        hash(unhashable_tuple)
    except TypeError as e:
        print(f"Cannot hash tuple with list: {e}")
        
    # Why this matters? Only hashable objects can be Dictionary Keys or Set items.

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    # Mistake: Using nested unpacking incorrectly
    record = ("Alice", ("Developer", "Senior"), 100)
    
    try:
        # Fails if structure doesn't match
        name, role, salary = record
        # 'role' is now a tuple ("Developer", "Senior")
    except ValueError as e:
        pass
        
    # Best Practice: Match the unpacking structure perfectly
    name, (job_title, seniority), salary = record
    print(f"{name} is a {seniority} {job_title}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: Can a tuple be used as a key in a dictionary?
A: Only if all elements inside the tuple are immutable (hashable). If the tuple contains a list or dictionary, it cannot be used as a key.

Q2: What happens when you do `t[0].append(x)` where `t` is a tuple and `t[0]` is a list?
A: The list is mutated in place, and the operation succeeds because the tuple's reference to the list object did not change.

Q3: Explain the += behavior with lists inside tuples.
A: `t[0] += [1]` evaluates to `t[0] = t[0].__iadd__([1])`. The `__iadd__` extends the list successfully, but the subsequent assignment back to `t[0]` raises a TypeError because tuples are immutable. Result: list changes, but an error is thrown.

Q4: What is a nested tuple?
A: A tuple that contains one or more tuples as its elements.

Q5: How do you unpack nested structures?
A: By mirroring the nested structure in your assignment target, e.g., `a, (b, c) = (1, (2, 3))`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Create a tuple containing a string and a dictionary.
    Exercise 2: Add a new key-value pair to the dictionary inside the tuple.
    """
    data = ("config", {"timeout": 30})
    data[1]["retries"] = 3
    print(f"Updated data tuple: {data}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: You are given a list of tuples representing (Person, (X, Y_coords)).
    Sort the list based on the Y coordinate in descending order.
    """
    people = [
        ("Alice", (10, 50)),
        ("Bob", (20, 30)),
        ("Charlie", (5, 90))
    ]
    
    # Sort by nested element
    people.sort(key=lambda item: item[1][1], reverse=True)
    print(f"Sorted people: {people}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Tuples can be nested infinitely.
- Tuples are only hashable (usable as dict keys) if all nested items are hashable.
- Mutable objects inside tuples CAN be modified in-place (like `.append()`).
- Avoid `+=` on mutable items inside tuples due to confusing partial execution behavior.
- Advanced unpacking allows extracting variables directly from nested tuples.
"""

if __name__ == "__main__":
    advanced_nesting()
    mutable_inside_immutable()
    hashability()
    common_mistakes()
    practice_exercises()
    mini_challenge()
