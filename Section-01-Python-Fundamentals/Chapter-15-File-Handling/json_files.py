"""
Topic: JSON Files
Chapter: 15
Level: Intermediate

Description:
    JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write and easy for machines to parse. Python's built-in `json` module makes it trivial to convert Python dictionaries and lists into JSON strings, and vice versa.

Real-Life Analogy:
    JSON is like a universal translation dictionary. If a Python program and a JavaScript web app want to exchange data, they can both read and speak "JSON" as their common language.

Key Concepts:
    - json.dump() and json.dumps()
    - json.load() and json.loads()
    - Serialization (Python to JSON)
    - Deserialization (JSON to Python)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import json

# Data to be serialized (Python Dictionary)
user_data = {
    "name": "Alice",
    "age": 30,
    "is_active": True,
    "skills": ["Python", "Machine Learning"]
}

# json.dumps() converts a Python object to a JSON string (Serialization)
json_string = json.dumps(user_data)
print("JSON String:", json_string)

# json.loads() converts a JSON string back to a Python dictionary (Deserialization)
parsed_data = json.loads(json_string)
print("Parsed Data Type:", type(parsed_data))
print("Parsed Name:", parsed_data["name"])

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Writing JSON to a file (json.dump)
with open("user.json", "w", encoding="utf-8") as f:
    # indent=4 makes the JSON file human-readable (pretty printing)
    json.dump(user_data, f, indent=4)

# Example 2: Reading JSON from a file (json.load)
print("\nReading from user.json:")
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(f"Loaded User: {loaded_data['name']}, Skills: {', '.join(loaded_data['skills'])}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Custom object serialization
# JSON doesn't know how to handle complex Python objects like datetime or custom classes.

from datetime import datetime

class User:
    def __init__(self, name):
        self.name = name

# We must provide a custom encoder or convert to a dict first.
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, User):
        return {"name": obj.name}
    raise TypeError("Type not serializable")

complex_data = {
    "timestamp": datetime.now(),
    "user": User("Bob")
}

advanced_json = json.dumps(complex_data, default=custom_serializer, indent=2)
print("\nAdvanced Serialization with custom types:")
print(advanced_json)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Confusing load/dump with loads/dumps.
# Correction: 'load'/'dump' deal with files (file objects). 'loads'/'dumps' deal with Strings. (The 's' stands for string).

# Mistake 2: Trying to serialize non-standard Python objects (like sets or custom classes) without a custom encoder.
# Correction: Convert them to standard types (lists, dicts) before serializing, or use the `default` parameter in dumps().

# Best Practice: Use `indent=4` during development for readable JSON files, but omit it for production files to save space.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does JSON stand for?
# A: JavaScript Object Notation.

# Q2: What is the difference between json.dump and json.dumps?
# A: json.dump writes directly to a file, whereas json.dumps returns a JSON formatted string.

# Q3: Can JSON store Python tuples?
# A: Yes, but they are converted to JSON arrays (which turn into Python lists when loaded back). JSON has no concept of a tuple.

# Q4: How do you handle a TypeError when dumping a Python object to JSON?
# A: You can pass a custom function to the `default` parameter of json.dumps() to handle the conversion of unsupported types.

# Q5: Is JSON only used in Python?
# A: No, it is a language-independent data format widely used in APIs and web development across many languages.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a dictionary with info about a car. Save it to 'car.json' with an indent of 2.

# Exercise 2: Read 'car.json' back into a Python script and print the car's model.

# Exercise 3: Take a JSON string `{"x": 10, "y": 20}` and convert it to a Python dict. Sum x and y.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def update_config(config_file, key, value):
    """
    Mini Challenge: Write a function that reads a JSON configuration file,
    updates a specific key with a new value, and writes it back to the file.
    If the file doesn't exist, create it.
    """
    import os
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        config = {}
        
    config[key] = value
    
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
        
    print(f"\nUpdated {config_file}:")
    with open(config_file, "r") as f:
        print(f.read())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - JSON is a lightweight format for data exchange.
# - json.dumps() / json.loads() for strings.
# - json.dump() / json.load() for files.
# - Use `indent` for pretty-printing.
# - Tuples become lists, and custom objects require custom serialization.

if __name__ == "__main__":
    update_config("settings.json", "theme", "dark")
    update_config("settings.json", "version", "1.1")
