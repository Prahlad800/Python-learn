"""
Topic: Nested Dictionaries
Chapter: 11
Level: Advanced

Description:
    A nested dictionary is a dictionary that contains other dictionaries as values. 
    This allows you to represent complex, hierarchical data structures, very similar 
    to JSON objects used in web APIs and configuration files.

Real-Life Analogy:
    Think of a company's organizational chart. The company (main dictionary) has departments 
    (keys). Inside each department (nested dictionary), there are managers (keys) and 
    employees (nested lists/dicts).

Key Concepts:
    - Creating nested dictionaries
    - Accessing nested values
    - Iterating through hierarchies
    - Updating nested structures
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Creating a nested dictionary
school = {
    "class_a": {
        "teacher": "Mr. Smith",
        "students": 30
    },
    "class_b": {
        "teacher": "Ms. Jones",
        "students": 25
    }
}

# Accessing a nested value (Chaining square brackets)
# Get the teacher for class_a
teacher_a = school["class_a"]["teacher"]
print(f"Class A teacher: {teacher_a}")

# Modifying a nested value
school["class_b"]["students"] = 28
print(f"Updated Class B students: {school['class_b']['students']}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Iterating through a nested dictionary
print("\nSchool Roster:")
for class_name, details in school.items():
    print(f"- {class_name.upper()}:")
    for key, value in details.items():
        print(f"    {key}: {value}")

# Example 2: Adding a new nested dictionary dynamically
school["class_c"] = {} # Initialize empty dict first
school["class_c"]["teacher"] = "Dr. Brown"
school["class_c"]["students"] = 20

# Example 3: Storing tabular data
employees = {
    101: {"name": "Alice", "role": "Engineer", "salary": 90000},
    102: {"name": "Bob", "role": "Manager", "salary": 110000}
}
print(f"\nEmployee 101 Name: {employees[101]['name']}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example: Flattening a nested dictionary
# Sometimes you need to convert a nested dict into a flat dict (e.g., for CSV export)
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            # Recursively flatten
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

nested_config = {"db": {"host": "localhost", "port": 5432}, "debug": True}
flat_config = flatten_dict(nested_config)
print(f"\nFlattened dict: {flat_config}") 
# Output: {'db_host': 'localhost', 'db_port': 5432, 'debug': True}

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to initialize the inner dictionary before assignment
# BAD: my_dict = {}; my_dict["parent"]["child"] = 1 # KeyError: 'parent'
# CORRECTION: my_dict = {"parent": {}}; my_dict["parent"]["child"] = 1

# Best Practice: Use `defaultdict(dict)` if you know you will be building deeply nested structures dynamically.
# Best Practice: For highly complex hierarchical data, consider creating dedicated Python Classes instead of massive nested dictionaries for better readability and validation.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: How do you safely access `dict['A']['B']['C']` without throwing a KeyError if 'B' doesn't exist?
A: Use chained `.get()` methods: `dict.get('A', {}).get('B', {}).get('C')`.

Q2: What is the risk of doing a shallow copy `dict.copy()` on a nested dictionary?
A: The inner dictionaries are NOT copied; they are passed by reference. Modifying the inner dictionary in the copy will accidentally modify the original dictionary as well.

Q3: Write a recursive function to search for a specific key in a nested dictionary of unknown depth.
A: (See Mini Challenge for an implementation concept)
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a nested dict representing a menu. 'Breakfast' and 'Lunch' as main keys, containing items and prices.
Exercise 2: Write a loop that applies a 10% discount to all prices in your nested menu.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Recursive Key Search
    Write a function that searches a deeply nested dictionary for a specific key 
    and returns its value. Return None if not found.
    """
    def find_key(d, target_key):
        if target_key in d:
            return d[target_key]
            
        for k, v in d.items():
            if isinstance(v, dict):
                # Recursively search the sub-dictionary
                result = find_key(v, target_key)
                if result is not None:
                    return result
        return None

    data = {
        "level1": {
            "level2": {
                "level3": {
                    "secret_code": 42
                }
            }
        }
    }
    
    print("\nRecursive Search Result:")
    print(f"Found secret_code: {find_key(data, 'secret_code')}")
    print(f"Found missing_key: {find_key(data, 'missing_key')}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Nested dictionaries allow for multi-dimensional data representation (like JSON).
- Access values by chaining bracket notation `dict[key1][key2]`.
- Always ensure inner dictionaries are initialized before assigning values to them.
- Recursion is a powerful tool for traversing and manipulating nested dictionaries.
"""

if __name__ == "__main__":
    mini_challenge()
