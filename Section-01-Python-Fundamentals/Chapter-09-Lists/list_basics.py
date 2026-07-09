"""
Topic: List Basics
Chapter: 9
Level: Beginner

Description:
    Lists in Python are ordered, mutable collections of items. They allow you to store multiple items, even of different types, in a single variable.

Real-Life Analogy:
    Think of a list as a shopping list where you can add, remove, and reorder items as you go through the store.

Key Concepts:
    - Creating Lists
    - Indexing and Accessing Elements
    - Mutability (Changing Elements)
    - Heterogeneous Elements (Different Data Types)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    # Creating an empty list
    empty_list = []
    print(f"Empty list: {empty_list}")

    # Creating a list with initial values
    fruits = ["apple", "banana", "cherry"]
    print(f"Fruits list: {fruits}")

    # Accessing elements using positive indexing (0-based)
    print(f"First fruit: {fruits[0]}")
    print(f"Second fruit: {fruits[1]}")

    # Accessing elements using negative indexing (starts from -1)
    print(f"Last fruit: {fruits[-1]}")
    
    # Lists are mutable (we can change their contents)
    fruits[1] = "blueberry"
    print(f"Modified fruits list: {fruits}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Lists can store different data types (Heterogeneous)
    user_info = ["John Doe", 28, True, 175.5]
    print(f"User Info: {user_info}")

    # Adding elements to a list (appending at the end)
    tasks = ["Wake up", "Drink coffee"]
    tasks.append("Write code")
    print(f"Daily tasks: {tasks}")

    # Checking if an item exists in a list
    if "Drink coffee" in tasks:
        print("Don't forget your coffee!")

    # Getting the length of a list
    num_tasks = len(tasks)
    print(f"Number of tasks today: {num_tasks}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # List multiplication and addition (concatenation)
    zero_list = [0] * 5
    print(f"List with five zeros: {zero_list}")

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined_list = list1 + list2
    print(f"Combined list: {combined_list}")

    # Unpacking lists into variables
    coordinates = [10.5, 20.3, 5.0]
    x, y, z = coordinates
    print(f"Unpacked coordinates - X: {x}, Y: {y}, Z: {z}")

    # Using enumerate to get index and value simultaneously
    animals = ["cat", "dog", "bird"]
    for index, animal in enumerate(animals):
        print(f"Index {index}: {animal}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Index out of range
    colors = ["red", "green", "blue"]
    try:
        print(colors[5])  # This will raise an IndexError
    except IndexError as e:
        print(f"Mistake caught: {e}")

    # Best Practice: Always check list length or use safe access methods
    # when you are unsure if an index exists.
    if len(colors) > 5:
        print(colors[5])
    else:
        print("Index 5 is out of bounds for the colors list.")

    # Mistake: Iterating and modifying the same list simultaneously
    # Best Practice: Iterate over a copy of the list if you plan to remove items
    numbers = [1, 2, 3, 4, 5]
    for num in numbers.copy():
        if num % 2 == 0:
            numbers.remove(num)
    print(f"List after removing even numbers safely: {numbers}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the difference between a list and a tuple in Python?
A: Lists are mutable (can be changed after creation), whereas tuples are immutable (cannot be changed). Lists use square brackets [], tuples use parentheses ().

Q2: How do you find the length of a list?
A: By using the built-in len() function, e.g., len(my_list).

Q3: What happens if you try to access an index that doesn't exist?
A: Python raises an IndexError: list index out of range.

Q4: Can a Python list contain different data types?
A: Yes, Python lists are heterogeneous and can store integers, strings, objects, or even other lists simultaneously.

Q5: How does negative indexing work in lists?
A: Negative indexing starts from the end of the list. -1 refers to the last element, -2 to the second to last, and so on.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a list of your 3 favorite movies. Change the second movie to something else.
Exercise 2: Write a script that checks if the number 10 is in the list `[1, 5, 8, 10, 15]`.
Exercise 3: Use a loop and `enumerate()` to print out a numbered list of groceries.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: Create a simple inventory system.
    1. Start with an inventory list: ["Sword", "Shield", "Potion"]
    2. Add "Bow" to the inventory.
    3. Check if "Potion" is in the inventory. If so, print "You have a potion!"
    4. Print the total number of items in the inventory.
    """
    inventory = ["Sword", "Shield", "Potion"]
    inventory.append("Bow")
    if "Potion" in inventory:
        print("You have a potion!")
    print(f"Total items in inventory: {len(inventory)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Lists are created using square brackets [] or the list() constructor.
- Elements are accessed using 0-based indexing or negative indexing for reverse order.
- Lists are mutable, meaning their elements can be updated, added, or removed.
- Lists can hold elements of various data types.
- Be cautious of IndexError when accessing elements outside the valid range.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    common_mistakes()
    mini_challenge()
