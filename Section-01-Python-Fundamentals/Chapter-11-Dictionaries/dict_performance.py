"""
Topic: Dictionary Performance and Memory
Chapter: 11
Level: Advanced

Description:
    Dictionaries in Python are highly optimized, utilizing hash tables under the hood. 
    This provides incredibly fast average-case O(1) time complexity for lookups, inserts, and deletes. 
    Understanding how this works helps write high-performance Python code.

Real-Life Analogy:
    Think of a dictionary like a library with an index catalog. Instead of searching shelf by shelf (a list), 
    you calculate exactly which shelf a book is on using its title (hashing). You walk straight to that shelf.

Key Concepts:
    - Time complexity (Big O notation)
    - Hash tables and the hash() function
    - Key collisions
    - Dictionary memory footprint
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
import time
import sys

# The magic behind dictionaries is the hash() function
print(f"Hash of 'apple': {hash('apple')}")
print(f"Hash of 42: {hash(42)}")
# Lists cannot be hashed!
# hash([1, 2, 3]) # TypeError: unhashable type: 'list'

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (PERFORMANCE COMPARISON)
# ============================================================

# Let's compare searching in a List vs searching in a Dictionary
def benchmark_search():
    size = 1_000_000
    
    # Setup data
    my_list = list(range(size))
    my_dict = {i: True for i in range(size)}
    
    target = 999_999 # Element at the very end
    
    # List search (O(n) - must scan elements)
    start_time = time.time()
    _ = target in my_list
    list_time = time.time() - start_time
    
    # Dict search (O(1) - instant hash lookup)
    start_time = time.time()
    _ = target in my_dict
    dict_time = time.time() - start_time
    
    print("\n--- Performance Comparison ---")
    print(f"List Search Time: {list_time:.6f} seconds")
    print(f"Dict Search Time: {dict_time:.6f} seconds")
    if dict_time > 0:
        print(f"Dict is ~{list_time/dict_time:.0f}x faster for lookups at this size.")

benchmark_search()

# ============================================================
# SECTION 3: ADVANCED USAGE (MEMORY PROFILING)
# ============================================================

# Because dictionaries use hash tables, they require extra memory to maintain 
# sparseness (empty slots) to avoid hash collisions.

def benchmark_memory():
    size = 10_000
    my_list = list(range(size))
    my_dict = {i: i for i in range(size)}
    
    list_size = sys.getsizeof(my_list)
    dict_size = sys.getsizeof(my_dict)
    
    print("\n--- Memory Comparison ---")
    print(f"List memory usage: {list_size} bytes")
    print(f"Dict memory usage: {dict_size} bytes")
    print("Dictionaries consume more memory to provide O(1) speed.")

benchmark_memory()

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a list to check for membership in large datasets.
# BAD: `if item in large_list:` (O(N) time)
# CORRECTION: Convert the list to a set (which uses a dict under the hood) or use a dict. 
# `if item in large_set:` (O(1) time)

# Best Practice: If you only need to store unique items and check for membership (but don't need values), use a `set`. Sets are implemented similarly to dictionaries but use slightly less memory since they only store keys.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the time complexity of looking up a key in a Python dictionary?
A: The average time complexity is O(1). In the worst-case scenario (severe hash collisions), it can degrade to O(N), but Python's hash functions make this extremely rare.

Q2: Why must dictionary keys be immutable?
A: Dictionaries rely on the key's hash value to determine where to store it in memory. If a key is mutable (like a list) and changes after insertion, its hash value would change, making it impossible to find it in the dictionary later.

Q3: Explain what a "hash collision" is.
A: A hash collision occurs when two different keys generate the exact same hash value. Python handles this internally using open addressing (probing) to find the next available empty slot.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a large list of 10,000 random strings. Time how long it takes to find a specific string.
Exercise 2: Convert that list to a dictionary (where keys are the strings) and time the same lookup.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Find duplicates fast.
    Given a large list of numbers, find the first duplicate number.
    Do this in O(N) time using a dictionary (or set).
    """
    numbers = [1, 5, 8, 3, 9, 2, 5, 8, 10]
    seen = {}
    
    first_duplicate = None
    for num in numbers:
        if num in seen: # O(1) lookup
            first_duplicate = num
            break
        seen[num] = True
        
    print(f"\nFirst duplicate found: {first_duplicate}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Dictionaries provide O(1) average time complexity for lookups, insertions, and deletions.
- They achieve this using Hash Tables.
- Keys must be hashable (immutable) types.
- The speed tradeoff is memory: dictionaries use more RAM than lists.
- For large datasets where membership checking is frequent, always prefer dictionaries or sets over lists.
"""

if __name__ == "__main__":
    mini_challenge()
