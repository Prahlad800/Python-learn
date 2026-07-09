"""
Topic: Frozensets
Chapter: 12
Level: Advanced

Description:
    A frozenset is an immutable version of a Python set. Because it is immutable, it is hashable and can be used as a key in a dictionary or as an element in another set.

Real-Life Analogy:
    If a regular set is a whiteboard where you can write and erase names, a frozenset is like a stone tablet with names carved into it. You can read it, but you can't change it.

Key Concepts:
    - Immutability
    - Hashable sets
    - Frozensets as dictionary keys
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    # Creating a frozenset
    normal_set = {1, 2, 3}
    f_set = frozenset(normal_set)
    print("Frozenset:", f_set)
    
    # Attempting to modify a frozenset raises an AttributeError
    try:
        f_set.add(4)
    except AttributeError as e:
        print("Error on add:", e)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    # Using frozensets as dictionary keys
    # Imagine a distance dictionary where distance A->B is same as B->A
    distances = {
        frozenset(["New York", "Boston"]): 215,
        frozenset(["New York", "Chicago"]): 790
    }
    
    # We can query it regardless of order
    route = frozenset(["Boston", "New York"])
    print("Distance NY to Boston:", distances.get(route))

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    # Frozensets inside a set
    set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
    print("Set containing frozensets:", set_of_sets)
    
    # Set operations work between sets and frozensets
    f_set = frozenset([1, 2, 3])
    n_set = {3, 4, 5}
    
    # The result type depends on the left operand
    print("frozenset | set:", type(f_set | n_set))
    print("set | frozenset:", type(n_set | f_set))

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Mistake: Trying to use a normal set as a dictionary key
    try:
        invalid_dict = {{1, 2}: "value"}
    except TypeError as e:
        print("TypeError for normal set key:", e)
        
    # Best Practice: Use frozensets when you need a set of unique items 
    # to be guaranteed unchanged throughout the program's lifecycle.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the main difference between set and frozenset?
# A: set is mutable and unhashable. frozenset is immutable and hashable.
#
# Q2: Can you perform union and intersection on frozensets?
# A: Yes, they support all non-mutating set operations.
#
# Q3: Are elements inside a frozenset mutable?
# A: No, a frozenset can only contain hashable (immutable) elements.
#
# Q4: Why would you use a frozenset over a tuple?
# A: When you need fast membership testing (O(1)) and uniqueness, but still need immutability.
#
# Q5: What is the time complexity to create a frozenset from a list?
# A: O(N) where N is the length of the list.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice():
    # Create a list of frozensets representing pairs of colleagues
    pairs = [frozenset(["Alice", "Bob"]), frozenset(["Charlie", "David"])]
    # Check if a specific pair is in the list
    search_pair = frozenset(["Bob", "Alice"])
    print("Is Alice and Bob pair present?", search_pair in pairs)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # Given a list of transactions where each transaction is a list of items,
    # count the frequency of unique item sets using a dictionary.
    transactions = [
        ["apple", "banana"],
        ["banana", "apple"], # Same as above
        ["orange", "apple"]
    ]
    
    freq = {}
    for t in transactions:
        f_set = frozenset(t)
        freq[f_set] = freq.get(f_set, 0) + 1
        
    return freq

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - frozenset is an immutable, hashable set.
# - It can be used as a dictionary key or an element in another set.
# - It supports all read-only set operations.

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
    print("Frequencies:", mini_challenge())
