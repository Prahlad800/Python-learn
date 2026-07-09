"""
Topic: Dictionary Methods
Chapter: 11
Level: Beginner / Intermediate

Description:
    Python provides a rich set of built-in methods for dictionaries to easily manipulate, 
    access, and modify their contents. Understanding these methods is crucial for efficient data handling.

Real-Life Analogy:
    If a dictionary is a filing cabinet, dictionary methods are the specific actions you can perform: 
    fetching a folder (.get()), listing all folders (.keys()), listing all documents inside (.values()), 
    or completely emptying the cabinet (.clear()).

Key Concepts:
    - Access methods: .get(), .keys(), .values(), .items()
    - Modification methods: .update(), .setdefault()
    - Removal methods: .pop(), .popitem(), .clear()
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

user = {
    "id": 101,
    "name": "Jane Doe",
    "role": "Admin"
}

# .keys() - Returns a view object displaying a list of all the keys
print(f"Keys: {user.keys()}")

# .values() - Returns a view object of all values in the dictionary
print(f"Values: {user.values()}")

# .items() - Returns a view object of all (key, value) tuples
print(f"Items: {user.items()}")

# Iterating over items is very common:
for key, value in user.items():
    print(f"{key} -> {value}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Safely getting values with .get()
# .get(key, default) avoids KeyError if the key is missing
settings = {"volume": 80, "brightness": 50}
print(f"Volume: {settings.get('volume')}")
print(f"Contrast (with default): {settings.get('contrast', 100)}")

# Example 2: .update() to merge or update multiple key-value pairs
profile = {"username": "ghost", "level": 5}
# Update with another dictionary
profile.update({"level": 6, "status": "online"})
# Update with keyword arguments
profile.update(last_seen="today", clan="warriors")
print(f"Updated profile: {profile}")

# Example 3: .setdefault()
# Returns the value of a key. If key doesn't exist, inserts the key with a specified value.
inventory = {"apples": 5}
# 'apples' exists, returns 5
apple_count = inventory.setdefault("apples", 0) 
# 'oranges' doesn't exist, inserts 'oranges': 0 and returns 0
orange_count = inventory.setdefault("oranges", 0) 
inventory["oranges"] += 2
print(f"Inventory after setdefault: {inventory}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example 1: .popitem()
# Removes and returns the last inserted key-value pair as a tuple (LIFO order in Python 3.7+)
cache = {"page1": "data1", "page2": "data2"}
last_item = cache.popitem()
print(f"Popped item: {last_item}, Remaining cache: {cache}")

# Advanced Example 2: fromkeys()
# Creates a new dictionary with keys from an iterable and values set to a specified value.
keys = ["name", "email", "phone"]
default_user = dict.fromkeys(keys, "Unknown")
print(f"Dictionary from keys: {default_user}")

# Caution with fromkeys and mutable defaults:
# If you use dict.fromkeys(['a', 'b'], []), both keys point to the SAME list in memory!

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Iterating and modifying size at the same time
# BAD: for k in my_dict.keys(): if k == 'x': del my_dict[k] # RuntimeError
# CORRECTION: Iterate over a copy of the keys or a list of keys
# for k in list(my_dict.keys()): 

# Best Practice: Use .get() instead of try-except KeyError for simple lookups.
# Best Practice: Use dict views (.keys(), .values(), .items()) which are dynamic and reflect changes to the dict immediately.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What does dict.items() return?
A: It returns a dict_items view object, which provides a dynamic view of the dictionary's (key, value) tuple pairs.

Q2: How does dict.setdefault() differ from dict.get()?
A: .get() only retrieves a value (or default) without modifying the dictionary. .setdefault() retrieves the value, but if the key doesn't exist, it also ADDS the key with the default value to the dictionary.

Q3: What is the time complexity of dict.pop(key)?
A: O(1) on average, because dictionary lookups and deletions are O(1) due to the underlying hash table.

Q4: What will dict.fromkeys(['a', 'b'], []) do?
A: It creates {'a': [], 'b': []}, but both keys reference the exact same list object. Appending to dict['a'] will also show up in dict['b'].
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a dictionary. Use .keys() to print all keys and .values() to print all values.
Exercise 2: Use .update() to merge two configuration dictionaries into one.
Exercise 3: Use .pop() to remove a key safely by providing a default value in case it doesn't exist.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Process a stream of votes.
    Use .setdefault() or .get() to count the occurrences of each vote efficiently.
    """
    votes = ["A", "B", "A", "C", "B", "A", "A"]
    vote_counts = {}
    
    for vote in votes:
        # Using .get() approach
        vote_counts[vote] = vote_counts.get(vote, 0) + 1
        
    print("Final Vote Counts:", vote_counts)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- .keys(), .values(), and .items() return view objects for iteration.
- .get(key, default) safely retrieves values.
- .update() merges dictionaries.
- .setdefault(key, default) retrieves and initializes missing keys.
- .pop(key) and .popitem() remove and return items.
- .clear() empties the dictionary.
"""

if __name__ == "__main__":
    mini_challenge()
