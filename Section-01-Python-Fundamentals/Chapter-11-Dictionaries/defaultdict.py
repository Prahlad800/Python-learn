"""
Topic: defaultdict (collections module)
Chapter: 11
Level: Intermediate / Advanced

Description:
    `defaultdict` is a subclass of the built-in dict class. It overrides one method and adds one writable 
    instance variable. Its primary function is to provide a default value for a key that does not exist, 
    preventing KeyError exceptions without needing manual checks or `.get()` / `.setdefault()`.

Real-Life Analogy:
    Imagine an automated storage facility. If you ask for a box number that doesn't exist yet, 
    instead of throwing an error saying "Box not found", the system automatically creates a brand new, 
    empty box at that number and hands it to you.

Key Concepts:
    - collections.defaultdict
    - Default factory functions (list, int, dict, custom functions)
    - Avoiding KeyErrors
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
from collections import defaultdict

# Normal dictionary behavior (Raises KeyError)
normal_dict = {}
# normal_dict["missing_key"] += 1  # Raises KeyError!

# Using defaultdict with 'int' as the default_factory
# If a key is missing, int() is called, which returns 0.
int_default = defaultdict(int)
int_default["missing_key"] += 1
print(f"defaultdict(int) after increment: {int_default}")

# Using 'list' as the default_factory
# If a key is missing, list() is called, returning an empty list []
list_default = defaultdict(list)
list_default["fruits"].append("apple")
list_default["fruits"].append("banana")
print(f"defaultdict(list): {list_default}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Grouping items (Much cleaner than normal dict)
animals = [("mammal", "dog"), ("bird", "eagle"), ("mammal", "cat"), ("fish", "shark"), ("bird", "sparrow")]

# Group by category using defaultdict
grouped_animals = defaultdict(list)
for category, name in animals:
    grouped_animals[category].append(name) # No need to check if category exists!

print("\nGrouped Animals:")
for cat, names in grouped_animals.items():
    print(f"  {cat}: {names}")

# Example 2: Counting character frequencies
word = "mississippi"
char_counts = defaultdict(int)

for char in word:
    char_counts[char] += 1

print(f"\nCharacter counts in '{word}': {dict(char_counts)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example 1: Using a custom default_factory
def default_status():
    return "Pending"

status_tracker = defaultdict(default_status)
status_tracker["task_1"] = "Completed"

print(f"\nTask 1 Status: {status_tracker['task_1']}")
# task_2 doesn't exist, so default_status() is called
print(f"Task 2 Status (auto-generated): {status_tracker['task_2']}") 

# Advanced Example 2: defaultdict of defaultdicts (Tree structure)
def tree():
    return defaultdict(tree)

taxonomy = tree()
taxonomy["Animalia"]["Chordata"]["Mammalia"]["Carnivora"] = "Dog"
# We can just access it deeply.
print(f"\nTaxonomy tree leaf: {taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Passing the result of a function instead of the function itself
# BAD: my_dd = defaultdict(list()) # TypeError: first argument must be callable or None
# GOOD: my_dd = defaultdict(list) # Note the missing parentheses!

# Best Practice: Use defaultdict when accumulating, grouping, or counting data.
# It makes the code cleaner and often slightly faster than using .setdefault() or .get().

# Best Practice: Remember that reading a missing key WILL add it to the dictionary.
# test = defaultdict(int)
# if test['missing'] == 0: # This just added 'missing': 0 to the dict!
# Use 'if key in test' to check for existence without adding.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: Why use defaultdict instead of dict.setdefault()?
A: defaultdict is generally faster and makes the code cleaner because you set the default behavior once at creation time, rather than every time you access/modify a key.

Q2: What happens if you try to access a non-existent key in a defaultdict?
A: The default_factory function is called to create a default value, the new key-value pair is inserted into the dictionary, and the default value is returned.

Q3: Can default_factory be None?
A: Yes, if default_factory is None, defaultdict behaves exactly like a normal dictionary and raises a KeyError for missing keys.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Given a list of words, use defaultdict(list) to group them by their length.
Exercise 2: Given a list of tuples (student_name, grade), use defaultdict(list) to map grades to a list of students who achieved that grade.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Graph Adjacency List
    Represent an undirected graph using an adjacency list.
    Edges: (A, B), (B, C), (A, C), (C, D)
    """
    edges = [("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")]
    
    # Create the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u) # Since it's undirected
        
    print("\nGraph Adjacency List:")
    for node, neighbors in graph.items():
        print(f"  Node {node} is connected to: {neighbors}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `defaultdict` is a subclass of `dict` from the `collections` module.
- It requires a callable (like `int`, `list`, or a custom function) as a `default_factory`.
- It automatically creates missing keys with a default value, preventing KeyError.
- Highly useful for grouping, counting, and nested dictionary structures.
"""

if __name__ == "__main__":
    mini_challenge()
