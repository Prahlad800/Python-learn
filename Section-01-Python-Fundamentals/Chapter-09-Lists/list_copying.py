"""
Topic: List Copying (Shallow vs Deep Copies)
Chapter: 9
Level: Advanced

Description:
    Copying lists in Python is trickier than it seems due to how Python handles memory references. Understanding the difference between assignment, shallow copies, and deep copies is crucial for avoiding subtle bugs.

Real-Life Analogy:
    Assignment is giving a friend a spare key to your house (you both share the same house).
    Shallow copy is building an identical house, but sharing the same movable furniture.
    Deep copy is building an identical house AND buying entirely new identical furniture.

Key Concepts:
    - Reference Assignment (`=`)
    - Shallow Copy (`.copy()`, `list()`, slicing `[:]`)
    - Deep Copy (`copy.deepcopy()`)
"""

import copy

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def reference_assignment():
    print("--- Section 1: Reference Assignment ---")
    # Creating a list
    original = [1, 2, 3]
    
    # Assigning it to a new variable does NOT copy it.
    # It just creates a new "tag" pointing to the SAME list in memory.
    alias = original
    
    # Changing the alias changes the original!
    alias[0] = 99
    print(f"Original list: {original}")
    print(f"Alias list: {alias}")
    print(f"Are they the exact same object? {original is alias}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (SHALLOW COPIES)
# ============================================================

def shallow_copies():
    print("\n--- Section 2: Shallow Copies ---")
    # A shallow copy creates a new list object, but it references the same elements.
    list_a = [10, 20, 30]
    
    # Method 1: The .copy() method
    list_b = list_a.copy()
    
    # Method 2: Slicing
    list_c = list_a[:]
    
    # Modifying the shallow copy does NOT affect the original (for flat lists)
    list_b[0] = 100
    print(f"Original list_a: {list_a}")
    print(f"Modified copy list_b: {list_b}")
    print(f"Are they the same object? {list_a is list_b}")

# ============================================================
# SECTION 3: ADVANCED USAGE (DEEP COPIES)
# ============================================================

def deep_copies():
    print("\n--- Section 3: Deep Copies (The Nested Problem) ---")
    # The problem with shallow copies arises with NESTED lists
    nested_original = [[1, 2], [3, 4]]
    
    # Create a shallow copy
    shallow_nested = nested_original.copy()
    
    # If we modify an INNER list, BOTH the original and the copy change!
    # Because the inner lists are just referenced.
    shallow_nested[0][0] = 99
    print(f"Original after shallow copy modification: {nested_original}")
    
    print("\n--- Fixing with Deep Copy ---")
    # We must use the 'copy' module for a deep copy
    # This recursively copies everything, creating entirely new objects.
    true_original = [[1, 2], [3, 4]]
    deep_nested = copy.deepcopy(true_original)
    
    deep_nested[0][0] = 99
    print(f"True Original: {true_original}")
    print(f"Deep Copy (Modified): {deep_nested}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Assuming `list2 = list1` creates a backup of data.
    # If you need to modify a list while keeping the original safe, ALWAYS use .copy().
    
    # Best Practice: Default to shallow copy `[:]` or `.copy()` for flat lists 
    # because it is faster and uses less memory.
    # Only use `copy.deepcopy()` when dealing with nested lists or complex objects
    # where you specifically need complete independence.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What happens when you use the assignment operator (=) with lists?
A: It copies the reference to the list, not the list itself. Both variables point to the same object in memory.

Q2: What is a shallow copy?
A: A shallow copy creates a new list object, but inserts references into it to the objects found in the original list.

Q3: What is a deep copy?
A: A deep copy creates a new list object and then, recursively, inserts copies into it of the objects found in the original.

Q4: How do you create a shallow copy of a list?
A: Using `list.copy()`, slicing `list[:]`, or the `list()` constructor.

Q5: When would you need to import the `copy` module?
A: When you need to use `copy.deepcopy()` to safely copy a list containing nested lists or dictionaries.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a list `a = [1, 2, 3]`. Create a variable `b` assigned to `a`. Change `b[0]` to 10. Print `a` and see the result.
Exercise 2: Create a flat list, make a shallow copy, modify the copy, and verify the original is untouched.
Exercise 3: Create a 2D matrix, make a deep copy, modify a nested element in the copy, and verify the original is untouched.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: You are building a game where you need to reset the board.
    You have a `master_board` setup.
    Create a `current_board` that starts as an exact replica.
    Make a move on the `current_board` (modify a nested element).
    Ensure the `master_board` remains pristine.
    """
    master_board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    
    # Must use deepcopy to avoid altering master_board when a move is made
    current_board = copy.deepcopy(master_board)
    
    # Make a move
    current_board[1][1] = "X"
    
    print(f"Master Board middle row: {master_board[1]}")
    print(f"Current Board middle row: {current_board[1]}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `=` assigns a reference.
- `.copy()` or `[:]` creates a shallow copy (safe for flat lists).
- `copy.deepcopy()` creates a deep copy (necessary for nested lists).
- Understanding memory referencing prevents critical data mutation bugs.
"""

if __name__ == "__main__":
    reference_assignment()
    shallow_copies()
    deep_copies()
    common_mistakes()
    mini_challenge()
