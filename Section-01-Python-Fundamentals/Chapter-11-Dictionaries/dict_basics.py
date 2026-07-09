"""
Topic: Dictionary Basics
Chapter: 11
Level: Beginner

Description:
    Dictionaries in Python are unordered (in Python < 3.7) but ordered by insertion (Python 3.7+), mutable collections of key-value pairs. 
    They allow you to store and retrieve data quickly by uniquely identifying values with a key.

Real-Life Analogy:
    Think of a physical dictionary book or a contact list on your phone. You look up a word or name (the key) 
    to find its definition or phone number (the value).

Key Concepts:
    - Key-value pairs
    - Creating dictionaries
    - Accessing and modifying values
    - Dictionary mutability
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Creating an empty dictionary
empty_dict = {}
another_empty = dict()

# Creating a dictionary with initial values
# Keys must be immutable types (strings, numbers, tuples)
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Accessing values using keys
print(f"Student's name is {student['name']}")

# Adding a new key-value pair
student["major"] = "Computer Science"
print(f"Added major: {student}")

# Modifying an existing value
student["age"] = 21
print(f"Updated age: {student}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Storing configurations
app_config = {
    "theme": "dark",
    "version": "1.0.4",
    "debug_mode": False
}

def setup_app(config):
    print(f"Setting up app. Theme: {config['theme']}, Debug: {config['debug_mode']}")

setup_app(app_config)

# Example 2: Counting items (histogram)
fruit_basket = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_counts = {}

for fruit in fruit_basket:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

print(f"Fruit counts: {fruit_counts}")

# Example 3: Storing user details from a web form
user_input = {
    "username": "coder123",
    "email": "coder@example.com",
    "is_active": True
}
print(f"User {user_input['username']} registered with email {user_input['email']}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example 1: Using tuples as keys
# Tuples are immutable, so they can be dictionary keys. Lists cannot.
locations = {
    (40.7128, 74.0060): "New York",
    (34.0522, 118.2437): "Los Angeles"
}
print(f"Location at (40.7128, 74.0060): {locations[(40.7128, 74.0060)]}")

# Advanced Example 2: Deleting items
item_prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
del item_prices["banana"] # Raises KeyError if key doesn't exist
print(f"Prices after deleting banana: {item_prices}")

# Using pop to remove and get the value
removed_price = item_prices.pop("cherry")
print(f"Removed cherry with price {removed_price}, remaining: {item_prices}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using a mutable object (like a list) as a key
# BAD: my_dict = {[1, 2, 3]: "numbers"} # TypeError: unhashable type: 'list'

# Mistake: Accessing a non-existent key directly
# BAD: print(student["address"]) # KeyError: 'address'
# CORRECTION: Use .get() or check if key in dict
print("Address:", student.get("address", "Not Found"))

# Best Practice: Use meaningful keys
# Best Practice: Prefer .get() when you are unsure if a key exists to avoid exceptions

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is a dictionary in Python?
A: A dictionary is a mutable, iterable collection of key-value pairs where keys must be unique and immutable.

Q2: How is a dictionary implemented internally in Python?
A: Python dictionaries are implemented using hash tables, which allows for fast O(1) average time complexity for lookups, insertions, and deletions.

Q3: Can a list be used as a dictionary key? Why or why not?
A: No, a list cannot be a key because lists are mutable and therefore unhashable. Keys must be immutable types like strings, numbers, or tuples.

Q4: What happens if you assign a value to an existing key?
A: The old value is overwritten by the new value.

Q5: What is the difference between dict[key] and dict.get(key)?
A: dict[key] raises a KeyError if the key doesn't exist. dict.get(key) returns None (or a specified default value) without raising an error.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a dictionary representing a car with keys 'brand', 'model', and 'year'.
Exercise 2: Add a new key 'color' to the car dictionary.
Exercise 3: Update the 'year' to the current year.
Exercise 4: Safely try to retrieve the 'price' key, returning 'Unknown' if not found.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create a simple inventory system.
    1. Start with an empty inventory dict.
    2. Add 'apples': 10, 'bananas': 5.
    3. Sell 3 apples (decrease count).
    4. Print the final inventory.
    """
    inventory = {}
    inventory["apples"] = 10
    inventory["bananas"] = 5
    
    # Sell 3 apples
    if "apples" in inventory and inventory["apples"] >= 3:
        inventory["apples"] -= 3
        
    print("Final Inventory:", inventory)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Dictionaries store data in key-value pairs.
- Keys must be unique and immutable (strings, ints, tuples).
- Values can be of any data type and can be duplicated.
- They are mutable, allowing additions, modifications, and deletions.
- Use square brackets [] or .get() to access values.
"""

if __name__ == "__main__":
    mini_challenge()
