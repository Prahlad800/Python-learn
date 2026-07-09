"""
Topic: Advanced Dictionary Methods
Chapter: 11
Level: Advanced

Description:
    Beyond basic retrieval and modification, Python's dictionaries offer powerful methods 
    for dynamic views, copying, and iteration control. Understanding these allows for elegant 
    and highly efficient data manipulation.

Real-Life Analogy:
    Think of standard methods as reading a book. Advanced methods are like a smart index 
    that automatically updates while you write, or a copy machine that lets you make 
    exact duplicates (or deep clones) of your documents.

Key Concepts:
    - View objects (dynamic updating)
    - Shallow vs Deep copy
    - Reversed iteration
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# View Objects: .keys(), .values(), .items() return dynamic views, not static lists.
data = {"a": 1, "b": 2}
keys_view = data.keys()

print(f"Original keys view: {keys_view}")
# If we modify the dictionary...
data["c"] = 3
# The view updates automatically!
print(f"Updated keys view (without re-calling .keys()): {keys_view}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Set operations on dictionary views
# Dictionary keys (and items) behave like sets, allowing set operations!
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 3, "d": 4}

# Find common keys using intersection (&)
common_keys = dict1.keys() & dict2.keys()
print(f"\nCommon keys: {common_keys}")

# Find keys only in dict1 using difference (-)
unique_to_d1 = dict1.keys() - dict2.keys()
print(f"Keys only in dict1: {unique_to_d1}")

# Find common (key, value) pairs exactly
common_items = dict1.items() & dict2.items()
print(f"Common exact items: {common_items}") # Only ('c', 3)

# Example 2: Reversed Iteration (Python 3.8+)
# Since dicts maintain insertion order, you can iterate in reverse.
history = {"login": "10:00", "view": "10:05", "logout": "10:30"}
print("\nReversed history:")
for action in reversed(history):
    print(f"  {action}: {history[action]}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
import copy

# Advanced Example: Shallow vs Deep Copy
original = {"name": "System", "settings": {"theme": "dark"}}

# Shallow copy (using .copy() or dict())
shallow = original.copy()
# Deep copy (using copy module)
deep = copy.deepcopy(original)

# Modify a nested mutable object in the copy
shallow["settings"]["theme"] = "light"
deep["settings"]["theme"] = "blue"

print(f"\nOriginal after copies modified: {original}") 
# Notice original theme became 'light' because shallow copy shares nested dicts!
print(f"Shallow copy: {shallow}")
print(f"Deep copy: {deep}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Assuming .keys() returns a list and trying to index it.
# BAD: my_dict.keys()[0] # TypeError: 'dict_keys' object is not subscriptable
# CORRECTION: Convert to list first if you need indexing: list(my_dict.keys())[0]

# Best Practice: Use set operations (&, |, -, ^) on dictionary views to quickly find intersections or differences without writing slow loops.
# Best Practice: Always use `copy.deepcopy()` if you need to copy a dictionary that contains other dictionaries or lists, to prevent unintended side effects.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the difference between dict.copy() and copy.deepcopy(dict)?
A: `dict.copy()` creates a shallow copy; it duplicates the top-level keys and values, but nested objects (like lists or other dicts) are passed by reference. `copy.deepcopy()` recursively creates completely independent copies of all nested objects.

Q2: How do you find keys that are present in `dictA` but missing in `dictB` efficiently?
A: By using set difference on the view objects: `dictA.keys() - dictB.keys()`.

Q3: Can you perform set operations on `dict.values()`?
A: Generally no. Unlike keys (which are unique and hashable) and items (which are hashable if the values are hashable), values are not guaranteed to be unique or hashable, so they do not support set operations.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create two dicts representing users who completed Part 1 and Part 2 of a course. Use set operations to find users who completed both.
Exercise 2: Create a nested dictionary. Make a shallow copy. Modify a nested value in the copy and verify the original changed.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Config Diff Tool
    Given old_config and new_config dictionaries, output three things:
    1. Added keys (in new, not in old)
    2. Removed keys (in old, not in new)
    3. Modified keys (in both, but values differ)
    """
    old_config = {"host": "localhost", "port": 8080, "debug": True}
    new_config = {"host": "127.0.0.1", "port": 8080, "workers": 4}
    
    # 1. Added
    added = new_config.keys() - old_config.keys()
    # 2. Removed
    removed = old_config.keys() - new_config.keys()
    # 3. Modified
    common = old_config.keys() & new_config.keys()
    modified = {k for k in common if old_config[k] != new_config[k]}
    
    print("\nConfig Diff:")
    print(f"Added keys: {added}")
    print(f"Removed keys: {removed}")
    print(f"Modified keys: {modified}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `keys()`, `values()`, and `items()` return dynamic views that update automatically.
- Views on keys and items support fast set operations (intersection, difference).
- Use `reversed(dict)` to iterate in LIFO order (Python 3.8+).
- Understand shallow vs deep copying to avoid corrupting nested dictionary data.
"""

if __name__ == "__main__":
    mini_challenge()
