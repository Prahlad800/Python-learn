"""
Topic: Set Performance
Chapter: 12
Level: Advanced

Description:
    Sets provide massive performance benefits over lists when it comes to membership testing (`in` operator) because they are implemented as hash tables. However, this speed comes at the cost of higher memory usage.

Real-Life Analogy:
    A list is like a physical book where you must scan page by page to find a word (slow, but takes little space). A set is like a huge index at the back of the book where you can look up the word instantly, but the index itself requires a lot of extra pages.

Key Concepts:
    - Time Complexity (Big O)
    - Memory footprint
    - Hash tables vs. Arrays
"""

import timeit
import sys

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def time_complexity_overview():
    # Set operations average time complexity:
    # - Add: O(1)
    # - Remove: O(1)
    # - Membership (x in s): O(1)
    # - Union: O(len(s1) + len(s2))
    # - Intersection: O(min(len(s1), len(s2)))
    print("Sets offer O(1) time complexity for lookups due to hashing.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def performance_comparison():
    # Comparing membership testing speed
    setup_code = '''
data_list = list(range(10000))
data_set = set(range(10000))
target = 9999
'''
    list_time = timeit.timeit('target in data_list', setup=setup_code, number=10000)
    set_time = timeit.timeit('target in data_set', setup=setup_code, number=10000)
    
    print(f"Time to find element in List: {list_time:.5f} seconds")
    print(f"Time to find element in Set:  {set_time:.5f} seconds")
    print(f"Set is roughly {list_time / set_time:.0f}x faster in this test.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def memory_footprint():
    # Comparing memory usage
    n = 10000
    my_list = list(range(n))
    my_set = set(range(n))
    
    # sys.getsizeof returns size in bytes
    list_size = sys.getsizeof(my_list)
    set_size = sys.getsizeof(my_set)
    
    print(f"Memory used by List: {list_size} bytes")
    print(f"Memory used by Set:  {set_size} bytes")
    print(f"Set uses roughly {set_size / list_size:.1f}x more memory.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake: Converting a list to a set for a single lookup.
    # The cost of creating the set O(N) outweighs the O(1) lookup benefit.
    
    # Bad:
    # if target in set(huge_list): pass
    
    # Best Practice: Only convert to a set if you plan to do MULTIPLE lookups
    # or if the data structure can naturally be a set from the beginning.
    print("Best Practice: Amortize set creation cost across multiple lookups.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why do sets take up more memory than lists?
# A: Sets use hash tables which require sparse arrays (empty slots) to minimize hash collisions, plus they store hash values alongside the objects.
#
# Q2: When is lookup in a set NOT O(1)?
# A: In the worst-case scenario where many elements have hash collisions, lookup degrades to O(N).
#
# Q3: Does creating a set from a list take O(1) time?
# A: No, creating a set takes O(N) time because it must iterate through the list and hash every element.
#
# Q4: Why shouldn't you convert a list to a set for just one lookup?
# A: The conversion takes O(N) time, which makes the whole operation O(N). You might as well just search the list.
#
# Q5: What makes an object unhashable in Python?
# A: An object is unhashable if it is mutable (like lists or dicts), because changing its contents would change its hash value, breaking the hash table structure.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Identify which of these are hashable and can be added to a set
    items = [1, "hello", (1, 2), [3, 4], {"a": 1}]
    
    valid_items = 0
    for item in items:
        try:
            hash(item)
            valid_items += 1
        except TypeError:
            pass
            
    print(f"Number of hashable items: {valid_items} out of {len(items)}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # Demonstrate the crossover point where converting to a set becomes faster
    # than repeatedly searching a list.
    setup_code = '''
data = list(range(1000))
targets = list(range(900, 950)) # 50 lookups
'''
    list_code = '''
for t in targets:
    _ = t in data
'''
    set_code = '''
s_data = set(data)
for t in targets:
    _ = t in s_data
'''
    l_time = timeit.timeit(list_code, setup=setup_code, number=1000)
    s_time = timeit.timeit(set_code, setup=setup_code, number=1000)
    
    return l_time, s_time

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - Sets provide O(1) membership tests vs O(N) for lists.
# - This speed requires significantly more memory.
# - Don't convert list to set for a single lookup; the conversion is O(N).

if __name__ == "__main__":
    print("--- Section 1 ---")
    time_complexity_overview()
    print("\n--- Section 2 ---")
    performance_comparison()
    print("\n--- Section 3 ---")
    memory_footprint()
    print("\n--- Section 4 ---")
    mistakes_and_best_practices()
    print("\n--- Section 6 ---")
    practice()
    print("\n--- Section 7 ---")
    l_time, s_time = mini_challenge()
    print(f"List multiple lookups: {l_time:.4f}s")
    print(f"Set multiple lookups (incl. creation): {s_time:.4f}s")
