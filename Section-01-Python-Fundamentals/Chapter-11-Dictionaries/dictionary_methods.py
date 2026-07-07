# Topic: Dictionary Methods
# Explanation: Dictionaries provide methods like keys(), values(), get(), and update().

# Syntax:
# student = {"name": "Asha", "age": 20}
print(student.get("name"))

# Examples:
# student = {"name": "Asha", "age": 20}
print(student.keys())
print(student.get("name"))

# Practice Programs:
# 1. Print all keys.
2. Update a value.

# Interview Questions:
# Q: What is get() useful for?
A: It safely returns a value even if the key is missing.

# Expected Output:
# dict_keys(['name', 'age'])
Asha

student = {"name": "Asha", "age": 20}
print(student.keys())
print(student.get("name"))
