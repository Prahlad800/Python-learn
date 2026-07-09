"""
Topic: Tuple Practice Exercises
Chapter: 10
Level: Intermediate

Description:
    This file contains general practice problems covering all concepts of Python Tuples. 
    It consolidates packing, unpacking, mutability concepts, methods, and real-world 
    use cases into actionable exercises.

Real-Life Analogy:
    This is like a workout circuit at the gym. You've learned how to use the different 
    machines (packing, methods, named tuples); now you'll do a full-body circuit to 
    ensure you know how to combine them effectively.

Key Concepts:
    - Tuple manipulation
    - Nested tuple iteration
    - Data extraction
    - Tuple generation
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def ex1_tuple_creation() -> None:
    # TODO: Create a tuple with the numbers 1 to 5.
    # TODO: Create a tuple with a single string "Solo".
    # TODO: Print the types of both.
    
    # Solution:
    numbers = (1, 2, 3, 4, 5)
    solo = ("Solo",)
    
    print(f"Numbers: {type(numbers)}, Solo: {type(solo)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def ex2_unpacking() -> None:
    # TODO: Given the tuple below, unpack it into variables: name, year, and a list of roles.
    data = ("Leonardo DiCaprio", 1974, "Actor", "Producer", "Environmentalist")
    
    # Solution:
    name, year, *roles = data
    print(f"Name: {name}")
    print(f"Year: {year}")
    print(f"Roles: {roles}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def ex3_nested_search() -> None:
    # TODO: You have a tuple of tuples representing (ID, Username, Active_Status).
    # Write a loop to extract and print only the Usernames of ACTIVE users.
    users = (
        (1, "alice", True),
        (2, "bob", False),
        (3, "charlie", True)
    )
    
    # Solution:
    print("Active Users:")
    for user_id, username, is_active in users:
        if is_active:
            print(f"- {username}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def ex4_modifying_safely() -> None:
    # TODO: Tuples are immutable, but you need to add "Orange" to this tuple.
    # Show the correct way to create a new tuple that includes "Orange" at the end.
    fruits = ("Apple", "Banana", "Cherry")
    
    # Solution:
    fruits = fruits + ("Orange",)
    print(f"Updated fruits: {fruits}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
(Self-Test for the student based on practice)
Q1: Can I use `del fruits[0]` to remove "Apple"?
A: No, tuples do not support item deletion. You must create a new tuple omitting the item.

Q2: How do you convert a list to a tuple and vice versa?
A: Using the `tuple(my_list)` and `list(my_tuple)` constructors.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
def ex5_list_to_tuple_conversion() -> None:
    """
    Given a list of strings, convert it to a tuple. Then find the index of "Python".
    """
    languages = ["C++", "Java", "Python", "Rust"]
    
    # Solution:
    lang_tuple = tuple(languages)
    idx = lang_tuple.index("Python")
    print(f"Python is at index {idx} in the tuple {lang_tuple}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge() -> None:
    """
    Challenge: Write a function `sort_by_last_element(tuples_list)` that takes a list 
    of tuples and returns a new list sorted by the last element of each tuple.
    Example Input: [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
    Expected Output: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    def sort_by_last_element(tuples_list: list) -> list:
        # Sort based on the last element `t[-1]`
        return sorted(tuples_list, key=lambda t: t[-1])
        
    sample = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
    result = sort_by_last_element(sample)
    print(f"Sorted list of tuples: {result}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Unpacking with `*` handles variable-length data gracefully.
- Iterating over tuple collections allows fast multi-variable extraction.
- Converting between lists and tuples is common when you need temporary mutability.
- Tuples can be sorted using `sorted()` and custom `key` functions.
"""

if __name__ == "__main__":
    ex1_tuple_creation()
    ex2_unpacking()
    ex3_nested_search()
    ex4_modifying_safely()
    ex5_list_to_tuple_conversion()
    mini_challenge()
