"""
Topic: List Methods
Chapter: 9
Level: Beginner

Description:
    Python lists come with built-in methods that allow you to easily modify, search, and manage list elements without writing complex loops.

Real-Life Analogy:
    Built-in tools in a Swiss army knife; each method has a specific purpose like cutting, opening, or adjusting items inside your container.

Key Concepts:
    - Adding elements (append, extend, insert)
    - Removing elements (remove, pop, clear)
    - Searching and info (index, count)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    cart = ["apple", "milk"]
    print(f"Initial cart: {cart}")

    # .append() adds an item to the end of the list
    cart.append("bread")
    print(f"After append: {cart}")

    # .insert() adds an item at a specific index
    cart.insert(1, "eggs") # Inserts "eggs" at index 1
    print(f"After insert: {cart}")

    # .remove() deletes the first occurrence of a specific value
    cart.remove("milk")
    print(f"After remove: {cart}")

    # .pop() removes and returns the item at the given index (default is the last item)
    last_item = cart.pop()
    print(f"Popped item: {last_item}")
    print(f"After pop: {cart}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # .extend() adds multiple elements from another iterable to the end
    team_a = ["Alice", "Bob"]
    team_b = ["Charlie", "Diana"]
    team_a.extend(team_b)
    print(f"Team A after extending with Team B: {team_a}")

    # .index() returns the index of the first occurrence of a value
    letters = ['a', 'b', 'c', 'b']
    b_index = letters.index('b')
    print(f"The first 'b' is at index: {b_index}")

    # .count() returns how many times a value appears in the list
    b_count = letters.count('b')
    print(f"The letter 'b' appears {b_count} times.")

    # .clear() empties the entire list
    temp_list = [1, 2, 3]
    temp_list.clear()
    print(f"Cleared list: {temp_list}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Combining methods for complex logic
    # Suppose we want to safely remove an item if it exists multiple times
    inventory = ["sword", "shield", "potion", "potion", "bow"]
    
    item_to_remove = "potion"
    # Remove all potions
    while item_to_remove in inventory:
        inventory.remove(item_to_remove)
    print(f"Inventory after removing all potions: {inventory}")

    # Popping from the beginning of the list (Not highly efficient for lists, but possible)
    # A deque is usually better for this, but list.pop(0) works.
    queue = ["Customer 1", "Customer 2", "Customer 3"]
    served = queue.pop(0)
    print(f"Served: {served}, Remaining queue: {queue}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Using append instead of extend for multiple items
    nums = [1, 2]
    # nums.append([3, 4])  # This creates [1, 2, [3, 4]]
    nums.extend([3, 4])    # This correctly makes [1, 2, 3, 4]
    print(f"Correctly extended nums: {nums}")

    # Mistake: Removing an item that doesn't exist raises a ValueError
    animals = ["dog", "cat"]
    try:
        animals.remove("bird")
    except ValueError as e:
        print(f"Mistake caught: {e}")

    # Best Practice: Check if an item is in the list before calling .remove()
    if "bird" in animals:
        animals.remove("bird")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the difference between append() and extend()?
A: append() adds its argument as a single element to the end of the list. extend() iterates over its argument and adds each element to the list.

Q2: What is the difference between remove() and pop()?
A: remove() deletes the first matching *value*. pop() removes the element at a specific *index* and returns it.

Q3: What does the clear() method do?
A: It removes all elements from the list, leaving it completely empty ([]).

Q4: What happens if you call pop() on an empty list?
A: Python raises an IndexError.

Q5: Does index() return all indices if the item appears multiple times?
A: No, index() only returns the index of the first occurrence. You would need a loop or list comprehension to find all indices.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a list `[10, 20, 30]`. Insert `15` between 10 and 20.
Exercise 2: Create a list with duplicate values. Use `count()` to find how many times a specific duplicate appears.
Exercise 3: Remove the last item from a list using `pop()` and print the removed item.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: Create a simple waiting list manager.
    1. Start with a list: ["Alice", "Bob", "Charlie"]
    2. A new person "David" arrives, add him to the end.
    3. The VIP "Eve" arrives, insert her at the very front of the list.
    4. "Alice" gets tired of waiting and leaves (remove her).
    5. The first person is served (pop them out and print their name).
    """
    wait_list = ["Alice", "Bob", "Charlie"]
    wait_list.append("David")
    wait_list.insert(0, "Eve")
    wait_list.remove("Alice")
    served = wait_list.pop(0)
    print(f"Served: {served}")
    print(f"Remaining wait list: {wait_list}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Use .append() to add a single item, .extend() to merge iterables.
- Use .insert() to add an item at a specific position.
- Use .remove() to delete by value, .pop() to delete by index and retrieve it.
- Use .index() to find the position of a value, and .count() to count occurrences.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    common_mistakes()
    mini_challenge()
