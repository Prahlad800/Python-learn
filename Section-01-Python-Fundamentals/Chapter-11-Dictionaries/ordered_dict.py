"""
Topic: OrderedDict (collections module)
Chapter: 11
Level: Intermediate

Description:
    `OrderedDict` is a dictionary subclass that remembers the order in which its contents were added.
    While standard dicts in Python 3.7+ also guarantee insertion order, OrderedDict offers additional 
    methods specific to ordering and has slightly different equality semantics.

Real-Life Analogy:
    Imagine a waiting list at a restaurant. It's a list of names (keys) and party sizes (values), 
    but the *order* in which they arrived is critically important. An OrderedDict guarantees 
    you process the first arrivals first.

Key Concepts:
    - collections.OrderedDict
    - OrderedDict vs Standard Dict (in Python 3.7+)
    - .move_to_end() method
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
from collections import OrderedDict

# Creating an OrderedDict
ordered_data = OrderedDict()
ordered_data["apple"] = 1
ordered_data["banana"] = 2
ordered_data["cherry"] = 3

print("OrderedDict iteration:")
for key, value in ordered_data.items():
    print(f"  {key}: {value}")

# Note: In Python 3.7+, a normal dict behaves exactly the same way when iterating!
normal_dict = {}
normal_dict["apple"] = 1
normal_dict["banana"] = 2
normal_dict["cherry"] = 3
# normal_dict will also print in insertion order.

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Reordering with move_to_end()
tasks = OrderedDict()
tasks["task1"] = "Pending"
tasks["task2"] = "Pending"
tasks["task3"] = "Pending"

# Oh, task2 is high priority, move it to the front (or back)
# move_to_end(key, last=True) moves to right end. last=False moves to left end.
tasks.move_to_end("task2", last=False) 

print("\nTasks after moving task2 to front:")
for task in tasks:
    print(f"  {task}")

# Example 2: Equality comparison
# Two normal dicts are equal if they have the same items, regardless of order.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(f"\nNormal dict equality: {dict1 == dict2}") # True

# Two OrderedDicts are ONLY equal if they have the same items AND the same order.
od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
print(f"OrderedDict equality: {od1 == od2}") # False

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example 1: Popping items
# popitem(last=True) pops from the right (LIFO). last=False pops from the left (FIFO).
queue = OrderedDict([("first", 1), ("second", 2), ("third", 3)])

# Process first in, first out (FIFO)
item = queue.popitem(last=False)
print(f"\nPopped from left (FIFO): {item}")
print(f"Remaining queue: {queue}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using OrderedDict in new code unnecessarily.
# Since Python 3.7, standard dictionaries guarantee insertion order.
# Using OrderedDict just for ordering uses more memory and is slower.

# Best Practice: Only use OrderedDict if you specifically need:
# 1. To use .move_to_end()
# 2. Strict order-sensitive equality testing (od1 == od2)
# 3. Compatibility with older Python versions (< 3.7) where dict order is not guaranteed.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: If regular dicts maintain insertion order in Python 3.7+, why does OrderedDict still exist?
A: OrderedDict has extra features like `move_to_end()` and `popitem(last=False)`, and its equality `==` operator considers order, whereas regular dict equality ignores order.

Q2: Is OrderedDict more memory-efficient than a regular dict?
A: No, OrderedDict actually consumes more memory because it maintains a doubly-linked list internally to track the order.

Q3: How do you implement an LRU (Least Recently Used) cache using OrderedDict?
A: You store items. When an item is accessed, use `move_to_end(key)` to mark it recently used. When the cache is full, use `popitem(last=False)` to remove the least recently used item from the front.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create an OrderedDict and add 5 elements. Move the 3rd element to the very end.
Exercise 2: Create a simple function that takes a standard dict, sorts its keys, and returns an OrderedDict.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Implement a very basic LRU Cache wrapper structure.
    Max capacity = 3.
    """
    class SimpleLRUCache:
        def __init__(self, capacity):
            self.cache = OrderedDict()
            self.capacity = capacity
            
        def get(self, key):
            if key not in self.cache:
                return -1
            # Move to end as it was recently accessed
            self.cache.move_to_end(key)
            return self.cache[key]
            
        def put(self, key, value):
            self.cache[key] = value
            self.cache.move_to_end(key)
            # Evict if over capacity
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False) # Remove oldest

    lru = SimpleLRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"\nLRU state: {list(lru.cache.items())}")
    lru.get(1) # Access 1, makes it newest
    lru.put(3, 3) # Evicts 2
    print(f"LRU state after putting 3: {list(lru.cache.items())}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- OrderedDict remembers the exact insertion order of items.
- In Python 3.7+, standard dicts also remember insertion order.
- Use OrderedDict for its unique methods: `move_to_end()` and `popitem(last=False)`.
- Use OrderedDict when you need order-sensitive equality comparisons.
"""

if __name__ == "__main__":
    mini_challenge()
