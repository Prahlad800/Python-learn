"""
Topic: Data Types
Chapter: 2
Level: Beginner

Description:
    Data types represent the kind of value that tells what operations can be performed on a particular data. 
    Since everything is an object in Python, data types are actually classes and variables are instances (objects) of these classes.
    Python has various standard data types that are used to define the operations possible on them.

Real-Life Analogy:
    Imagine a filing cabinet. You wouldn't store a glass bottle of water in a folder meant for paper documents. 
    Similarly, data types define the "container type" for information. A string (text) is handled differently 
    than an integer (whole number) when we process them.

Key Concepts:
    - Numeric Types: int, float, complex
    - Sequence Types: str, list, tuple
    - Mapping Type: dict
    - Set Types: set, frozenset
    - Boolean Type: bool
    - None Type: NoneType
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def explore_basic_data_types() -> None:
    """Demonstrates creating variables of different basic data types."""
    print("--- Basic Data Types ---")
    
    # Integer
    age = 30
    print(f"Age: {age}, Type: {type(age)}")
    
    # Float
    temperature = 98.6
    print(f"Temperature: {temperature}, Type: {type(temperature)}")
    
    # String
    greeting = "Hello, World!"
    print(f"Greeting: {greeting}, Type: {type(greeting)}")
    
    # Boolean
    is_sunny = True
    print(f"Is sunny: {is_sunny}, Type: {type(is_sunny)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def complex_data_types() -> None:
    """Shows practical use cases of compound data types (collections)."""
    print("\n--- Collections / Sequence Types ---")
    
    # List (Mutable)
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    print(f"Fruits List: {fruits}, Type: {type(fruits)}")
    
    # Tuple (Immutable)
    coordinates = (10.0, 20.0)
    print(f"Coordinates Tuple: {coordinates}, Type: {type(coordinates)}")
    
    # Dictionary (Key-Value mappings)
    person = {"name": "John", "age": 28, "city": "New York"}
    print(f"Person Dictionary: {person}, Type: {type(person)}")
    
    # Set (Unique unordered items)
    unique_numbers = {1, 2, 3, 3, 2, 1}
    print(f"Unique Numbers Set: {unique_numbers}, Type: {type(unique_numbers)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_types() -> None:
    """Demonstrates complex numbers and frozenset."""
    print("\n--- Advanced Data Types ---")
    
    # Complex numbers
    complex_num = 3 + 4j
    print(f"Complex Number: {complex_num}, Type: {type(complex_num)}")
    print(f"Real part: {complex_num.real}, Imaginary part: {complex_num.imag}")
    
    # Frozenset (Immutable set)
    frozen_items = frozenset([1, 2, 3, 4])
    print(f"Frozenset: {frozen_items}, Type: {type(frozen_items)}")
    # frozen_items.add(5)  # This would raise an AttributeError

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Highlights common pitfalls regarding data types."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    # Pitfall: Assuming list and tuple are interchangeable
    # lists are mutable, tuples are immutable. Use tuples for fixed data to save memory and ensure safety.
    
    # Pitfall: Mixing incompatible types without casting
    # Example: print("Age: " + 25) # TypeError!
    # Correction: Use f-strings or type casting
    print(f"Correct way to mix types in strings using f-strings: Age is {25}")
    
    # Best Practice: Use the `type()` or `isinstance()` function to check variable types
    val = [1, 2, 3]
    if isinstance(val, list):
        print("Confirmed: val is a list.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. What is the difference between a list and a tuple?
   Answer: Lists are mutable (can be changed), whereas tuples are immutable (cannot be changed after creation).

2. How do you check the data type of a variable in Python?
   Answer: You can use the built-in type() function or isinstance().

3. Is a Python string mutable?
   Answer: No, strings are immutable. Operations that modify strings actually create a new string object.

4. What is a dictionary?
   Answer: A dictionary is an unordered collection of data values used to store data in key:value pairs.

5. What is the difference between a set and a list?
   Answer: A set contains unique, unordered elements and does not support indexing, whereas a list is ordered, allows duplicates, and supports indexing.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a dictionary storing information about a book (title, author, year published, and a boolean indicating if you've read it).
Exercise 2: Create a list with duplicate numbers, convert it to a set to remove duplicates, and print the set.
Exercise 3: Write a program that checks if a given variable is a float using isinstance().
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Mini challenge involving various data types."""
    print("\n--- Mini Challenge ---")
    
    # Model a student's profile
    student_profile = {
        "student_id": 101,                  # int
        "name": "Emma",                     # str
        "grades": [85.5, 92.0, 88.5],       # list of floats
        "is_enrolled": True,                # bool
        "subjects": {"Math", "Science"}     # set of str
    }
    
    # Process some data
    avg_grade = sum(student_profile["grades"]) / len(student_profile["grades"])
    
    print(f"Student: {student_profile['name']} (ID: {student_profile['student_id']})")
    print(f"Enrolled: {student_profile['is_enrolled']}")
    print(f"Subjects: {', '.join(student_profile['subjects'])}")
    print(f"Average Grade: {avg_grade:.2f}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Python provides numerous built-in data types: numeric, sequence, mapping, set, and boolean.
- Mutability is a key concept: lists and dictionaries are mutable, while strings and tuples are immutable.
- Understanding and using the correct data type is critical for efficiency and logical correctness.
"""

if __name__ == "__main__":
    explore_basic_data_types()
    complex_data_types()
    advanced_types()
    common_mistakes()
    mini_challenge()
