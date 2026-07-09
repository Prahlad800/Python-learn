"""
Topic: Set Basics
Chapter: 12
Level: Beginner

Description:
    Sets are unordered, mutable collections of unique elements in Python. They are primarily used for mathematical operations like union, intersection, and for removing duplicate elements from other iterables.

Real-Life Analogy:
    Think of a set like a club with a strict guest list where no one is allowed to enter twice. Even if your name is called multiple times, you only get one entry tag.

Key Concepts:
    - Unordered collection
    - Unique elements only
    - Mutable (for normal sets)
    - Elements must be hashable
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    # Creating an empty set (Note: {} creates an empty dict)
    empty_set = set()
    print("Empty set:", empty_set)
    
    # Creating a set with elements
    fruits = {"apple", "banana", "orange"}
    print("Fruits set:", fruits)
    
    # Automatic duplicate removal
    numbers = {1, 2, 2, 3, 3, 3, 4}
    print("Unique numbers:", numbers)
    
    # Creating a set from a list
    char_list = ['a', 'b', 'c', 'a']
    char_set = set(char_list)
    print("Set from list:", char_set)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    # Example 1: Finding unique items from user input
    user_tags = ["python", "coding", "python", "dev"]
    unique_tags = set(user_tags)
    print("Unique tags:", unique_tags)

    # Example 2: Checking membership (O(1) time complexity)
    allowed_roles = {"admin", "editor", "moderator"}
    user_role = "viewer"
    print(f"Is {user_role} allowed? {user_role in allowed_roles}")
    
    # Example 3: Adding and removing elements
    allowed_roles.add("viewer")
    allowed_roles.remove("editor") # Raises KeyError if not found
    allowed_roles.discard("guest") # Does not raise error if not found
    print("Updated roles:", allowed_roles)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    # Sets can only contain hashable types (tuples, strings, ints, etc.)
    # valid_set = {1, "two", (3, 4)} # This works
    
    # Attempting to add a list will raise TypeError
    try:
        invalid_set = {1, 2, [3, 4]}
    except TypeError as e:
        print(f"Error: {e}")
        
    # Unpacking sets (order is not guaranteed)
    items = {"laptop", "mouse", "keyboard"}
    a, b, c = items
    print(f"Unpacked: {a}, {b}, {c}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake 1: Using {} to create an empty set (creates dict instead).
    # Correction: Use set()
    my_empty_set = set()
    my_dict = {}
    print("Type of set():", type(my_empty_set))
    print("Type of {}:", type(my_dict))

    # Best Practice: Use sets instead of lists for membership testing (`in` operator) 
    # because sets provide O(1) lookups on average.
    data_list = list(range(10000))
    data_set = set(data_list)
    # Using 'in data_set' is significantly faster than 'in data_list'

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How does a set enforce uniqueness?
# A: It uses a hash table internally. Before inserting, it hashes the element and checks if it already exists.
#
# Q2: Can a set contain a dictionary?
# A: No, dictionaries are mutable and therefore unhashable.
#
# Q3: What is the time complexity of 'x in my_set'?
# A: O(1) on average.
#
# Q4: How do you clear all elements from a set?
# A: Using the clear() method.
#
# Q5: Can sets be nested?
# A: Normal sets cannot be nested because sets are mutable and unhashable. Use frozensets instead.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Exercise 1: Create a set of first 5 even numbers.
    evens = {2, 4, 6, 8, 10}
    # Exercise 2: Add the number 12 to the set.
    evens.add(12)
    # Exercise 3: Remove the number 2 using discard().
    evens.discard(2)
    print("Practice result:", evens)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge(text):
    # Write a function that takes a string and returns a set of unique characters in it, excluding spaces.
    return set(char for char in text if char != ' ')

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Sets are unordered and mutable.
# - They contain only unique, hashable elements.
# - Created using {} or set().
# - Ideal for removing duplicates and fast membership testing.

if __name__ == "__main__":
    print("--- Section 1 ---")
    basic_syntax()
    print("\n--- Section 2 ---")
    practical_examples()
    print("\n--- Section 3 ---")
    advanced_usage()
    print("\n--- Section 4 ---")
    mistakes_and_best_practices()
    print("\n--- Section 6 ---")
    practice()
    print("\n--- Section 7 ---")
    print("Mini challenge ('hello world'):", mini_challenge("hello world"))
