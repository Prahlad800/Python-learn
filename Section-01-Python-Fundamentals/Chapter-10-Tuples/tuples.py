"""
Topic: Introduction to Tuples
Chapter: 10
Level: Beginner

Description:
    Tuples are ordered, immutable collections of items in Python. Once a tuple is created, 
    its elements cannot be changed, added, or removed. They are useful for storing 
    fixed data structures and heterogeneous data.

Real-Life Analogy:
    Think of a tuple like a printed book. You can read the pages in order, but you cannot 
    edit the text, add new pages, or remove existing ones without creating a completely new book.

Key Concepts:
    - Creation (parentheses vs comma)
    - Immutability
    - Indexing and Slicing
    - Heterogeneous data storage
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax() -> None:
    # Creating empty tuple
    empty_tuple: tuple = ()
    print(f"Empty tuple: {empty_tuple}")

    # Creating a single-element tuple requires a trailing comma
    single_tuple = (42,)
    not_a_tuple = (42)  # This is just an integer in parentheses
    print(f"Single tuple type: {type(single_tuple)}")
    print(f"Not a tuple type: {type(not_a_tuple)}")

    # Creating tuples with multiple elements
    coordinates = (10, 20)
    print(f"Coordinates: {coordinates}")

    # Parentheses are optional (tuple packing)
    colors = "red", "green", "blue"
    print(f"Colors tuple: {colors}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples() -> None:
    # Tuples are often used to represent a single entity with multiple properties
    # Example: A user record (ID, Username, Email, IsActive)
    user_record = (101, "johndoe", "john@example.com", True)
    
    # Accessing elements via indexing
    user_id = user_record[0]
    username = user_record[1]
    
    print(f"User ID: {user_id}, Username: {username}")
    
    # Slicing tuples (works exactly like lists)
    contact_info = user_record[1:3]
    print(f"Contact Info: {contact_info}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage() -> None:
    # Immutability nuance: Tuples can contain mutable objects
    # You cannot change the tuple itself, but you CAN modify mutable elements inside it
    hybrid_tuple = (1, 2, [3, 4, 5])
    print(f"Original hybrid tuple: {hybrid_tuple}")
    
    # This is allowed because we are mutating the list, not the tuple's reference to the list
    hybrid_tuple[2].append(6)
    print(f"Mutated hybrid tuple: {hybrid_tuple}")
    
    # However, this will raise a TypeError:
    # hybrid_tuple[0] = 10

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    # Mistake 1: Forgetting the comma for single-element tuples
    # Correct: t = (1,)
    # Wrong: t = (1)
    
    # Mistake 2: Trying to modify an element
    t = (1, 2, 3)
    try:
        t[0] = 99
    except TypeError as e:
        print(f"Caught expected error: {e}")

    # Best Practice: Use tuples for heterogeneous data (different types)
    # and lists for homogeneous data (same types).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the main difference between a list and a tuple?
A: Lists are mutable (can be changed), while tuples are immutable (cannot be changed after creation).

Q2: How do you create a tuple with a single element?
A: By adding a trailing comma, e.g., `t = (42,)`.

Q3: Can a tuple be used as a dictionary key?
A: Yes, because tuples are immutable and hashable, unlike lists.

Q4: Are tuples faster than lists?
A: Yes, generally. Because they are immutable, Python optimizes their memory usage and iteration speed.

Q5: Can you change a list inside a tuple?
A: Yes, you can modify mutable objects (like lists) that are elements of a tuple.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def practice_exercises() -> None:
    """
    Exercise 1: Create a tuple containing your first name, last name, and age.
    Exercise 2: Extract the last name from the tuple using indexing.
    Exercise 3: Try to change your age in the tuple and observe the error.
    """
    # Solution 1
    my_info = ("Jane", "Doe", 28)
    
    # Solution 2
    last_name = my_info[1]
    print(f"Last name is: {last_name}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: You are given a tuple of file metadata: (filename, size_in_bytes, is_executable).
    Write code to format this into a readable string: "File [name] is [size] bytes. Executable: [Yes/No]"
    """
    file_metadata = ("script.py", 1024, True)
    
    name = file_metadata[0]
    size = file_metadata[1]
    is_exec = "Yes" if file_metadata[2] else "No"
    
    print(f"File {name} is {size} bytes. Executable: {is_exec}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Tuples are created using parentheses `()` or just comma-separated values.
- They are immutable: elements cannot be reassigned.
- Single-element tuples must have a trailing comma `(x,)`.
- They support indexing and slicing just like lists.
- Mutable objects inside a tuple can still be modified.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    common_mistakes()
    practice_exercises()
    mini_challenge()
