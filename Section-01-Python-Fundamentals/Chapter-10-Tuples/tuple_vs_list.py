"""
Topic: Tuples vs Lists
Chapter: 10
Level: Intermediate

Description:
    Tuples and Lists are both sequence data types in Python that store collections of items. 
    However, they have key differences in mutability, performance, and use cases. Understanding 
    when to use which is a fundamental skill in Python programming.

Real-Life Analogy:
    A List is like a whiteboard: you can write things down, erase them, and add new things at will.
    A Tuple is like a printed document: once printed, the text is fixed and cannot be changed, 
    but it's much faster to distribute and read.

Key Concepts:
    - Mutability vs Immutability
    - Memory footprint (sys.getsizeof)
    - Performance (timeit)
    - Semantic differences (Heterogeneous vs Homogeneous)
"""

import sys
import timeit

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_comparison() -> None:
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    
    print(f"List type: {type(my_list)}")
    print(f"Tuple type: {type(my_tuple)}")
    
    # Mutability check
    my_list[0] = 99
    print(f"List after modification: {my_list}")
    
    # Tuple modification will fail
    try:
        my_tuple[0] = 99
    except TypeError as e:
        print(f"Tuple modification failed: {e}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def memory_comparison() -> None:
    # Memory footprint comparison
    list_data = [1, 2, 3, 4, 5]
    tuple_data = (1, 2, 3, 4, 5)
    
    # Lists require more memory because they need dynamic resizing capabilities
    print(f"Size of list: {sys.getsizeof(list_data)} bytes")
    print(f"Size of tuple: {sys.getsizeof(tuple_data)} bytes")
    
    # Even empty lists are larger than empty tuples
    print(f"Size of empty list: {sys.getsizeof([])} bytes")
    print(f"Size of empty tuple: {sys.getsizeof(())} bytes")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def performance_comparison() -> None:
    # Instantiation speed
    list_time = timeit.timeit("x = [1, 2, 3, 4, 5]", number=1_000_000)
    tuple_time = timeit.timeit("x = (1, 2, 3, 4, 5)", number=1_000_000)
    
    print(f"Time to create 1M lists: {list_time:.4f} seconds")
    print(f"Time to create 1M tuples: {tuple_time:.4f} seconds")
    
    # Tuples are generally faster to instantiate because Python does constant folding
    # and caches small tuples.

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def best_practices() -> None:
    # Best Practice 1: Use Lists for homogeneous data (same type of items)
    # e.g., a list of usernames
    usernames = ["alice", "bob", "charlie"]
    
    # Best Practice 2: Use Tuples for heterogeneous data (related items of different types)
    # e.g., a single user record
    user_record = ("alice", 28, "admin@site.com")
    
    # Best Practice 3: Use Tuples as Dictionary keys (Lists cannot be keys)
    locations = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles"
    }
    print(f"Dictionary with tuple keys: {locations}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the primary difference between a list and a tuple?
A: Lists are mutable (can change), tuples are immutable (cannot change).

Q2: Why do lists consume more memory than tuples?
A: Lists maintain additional internal structures (like over-allocating capacity) to allow for efficient dynamic resizing and appending.

Q3: Which one is faster to create, a list or a tuple?
A: A tuple. Python optimizes tuple creation; literal tuples are evaluated at compile time.

Q4: Can a list be used as a dictionary key? Why or why not?
A: No, because dictionary keys must be hashable. Lists are unhashable because their contents can change, which would break the hash table.

Q5: When would you strictly choose a list over a tuple?
A: When you have a collection of items that might grow, shrink, or require modification during the program's execution.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Create a collection to store the days of the week. Should it be a list or tuple?
    Exercise 2: Create a collection to store a user's active shopping cart items. List or tuple?
    """
    # Days of the week shouldn't change -> Tuple
    days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    
    # Shopping cart items will change (add/remove) -> List
    shopping_cart = ["Apple", "Milk"]
    shopping_cart.append("Bread")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: Write a function that takes a list of numbers. 
    Return a tuple containing the sum, the maximum, and the minimum of the list.
    """
    def analyze_numbers(nums: list) -> tuple:
        if not nums:
            return (0, None, None)
        return (sum(nums), max(nums), min(nums))
        
    stats = analyze_numbers([10, 5, 20, 15])
    print(f"Stats (Sum, Max, Min): {stats}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- **Lists** `[]`: Mutable, dynamic size, slower, more memory. Good for homogeneous data that changes.
- **Tuples** `()`: Immutable, fixed size, faster, less memory. Good for heterogeneous data, constants, and dictionary keys.
- Choose tuples for structural data (like a database row).
- Choose lists for sequences of similar objects.
"""

if __name__ == "__main__":
    basic_comparison()
    memory_comparison()
    performance_comparison()
    best_practices()
    practice_exercises()
    mini_challenge()
