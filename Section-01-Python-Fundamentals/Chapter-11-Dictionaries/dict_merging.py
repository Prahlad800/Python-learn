"""
Topic: Dictionary Merging and Updating
Chapter: 11
Level: Intermediate

Description:
    Combining data from multiple dictionaries is a very common task. Python provides 
    several ways to merge dictionaries, each with slightly different syntax and behaviors.

Real-Life Analogy:
    Imagine two lists of contact details. Your old phone has some contacts, and your new phone has others. 
    Merging them combines all unique contacts. If the same person is in both phones with different numbers, 
    the merge rule decides which number to keep (usually the one from the new phone).

Key Concepts:
    - update() method
    - Dictionary unpacking (** operator)
    - Merge operator (|) in Python 3.9+
    - Update operator (|=) in Python 3.9+
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3} # Note the overlapping key 'b'

# Method 1: Using .update() (In-place modification)
# Modifies dict1 directly. dict2 values overwrite dict1 values for common keys.
dict1.update(dict2)
print(f"Using update(): {dict1}")

# Reset dict1
dict1 = {"a": 1, "b": 2}

# Method 2: Dictionary unpacking (Creates a new dictionary)
# ** unpacks the key-value pairs. Later dictionaries overwrite earlier ones.
merged_unpack = {**dict1, **dict2}
print(f"Using unpacking (**): {merged_unpack}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Merging configurations
default_config = {"theme": "light", "font": "Arial", "size": 12}
user_config = {"theme": "dark", "size": 14}

# We want defaults, overridden by user settings
final_config = {**default_config, **user_config}
print(f"\nFinal Config: {final_config}")

# Example 2: The Python 3.9+ Merge Operator (|)
# This is cleaner and more readable than unpacking
d1 = {"x": 10, "y": 20}
d2 = {"y": 30, "z": 40}

# Creates a new dictionary
merged_pipe = d1 | d2 
print(f"Using merge operator (|): {merged_pipe}")

# Example 3: The Python 3.9+ Update Operator (|=)
# In-place update, equivalent to .update()
d1 |= d2
print(f"Using update operator (|=): {d1}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example 1: Merging with other iterables
# The pipe operator (|) only works between two dicts.
# However, the update operator (|=) and .update() can accept iterables of key-value pairs.

target = {"a": 1}
# target | [("b", 2)]  <-- TypeError!

# But this works:
target |= [("b", 2), ("c", 3)]
print(f"\nUpdated with list of tuples: {target}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Assuming `|` works in older Python versions
# BAD: running d1 | d2 in Python 3.8 will cause a TypeError.
# CORRECTION: Check your environment. If < 3.9, use {**d1, **d2} or .copy() and .update().

# Best Practice: Use `|` (if Python >= 3.9) when you want a *new* dictionary.
# Best Practice: Use `.update()` or `|=` when you want to modify an *existing* dictionary to save memory.
# Best Practice: Remember that the right-most dictionary always "wins" in a key conflict.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What happens if two dictionaries have the same key when merged?
A: The value from the dictionary that is merged last (the one on the right side of `**` or `|`) overwrites the previous value.

Q2: What is the difference between dict1.update(dict2) and dict1 | dict2 ?
A: `.update()` modifies `dict1` in-place and returns None. The `|` operator creates and returns a completely new dictionary, leaving both originals unchanged.

Q3: Can you merge three dictionaries at once using the pipe operator?
A: Yes, you can chain them: d1 | d2 | d3. They are evaluated left to right.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create 3 dictionaries representing different sets of attributes for a character. Merge all 3 into a single `character_sheet` dict.
Exercise 2: Given a `base_prices` dict and a `holiday_discounts` dict, create a new dict containing the final prices, ensuring base prices are kept if no discount exists.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Deep merge.
    Standard merging is shallow. Write a simple function to deeply merge two dictionaries 
    (assuming they only contain nested dictionaries, no lists).
    """
    def deep_merge(d1, d2):
        result = d1.copy()
        for key, value in d2.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_merge(result[key], value)
            else:
                result[key] = value
        return result

    dict_a = {"user": {"name": "John", "age": 30}, "status": "active"}
    dict_b = {"user": {"age": 31, "city": "NY"}, "score": 100}
    
    print("\nDeep Merge Result:")
    print(deep_merge(dict_a, dict_b))
    
    # Compare with shallow merge
    print("Shallow Merge (for comparison):")
    print(dict_a | dict_b) # 'user' gets completely overwritten

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Use `.update()` or `|=` for in-place modification.
- Use `{**d1, **d2}` or `d1 | d2` (Python 3.9+) to create a new merged dictionary.
- In key conflicts, the right-most value overrides the left.
- Standard merge operations are shallow; nested dictionaries are replaced, not merged.
"""

if __name__ == "__main__":
    mini_challenge()
