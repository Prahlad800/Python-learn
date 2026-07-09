"""
Topic: Enumerate and Zip Functions
Chapter: 06
Level: Intermediate

Description:
    `enumerate()` adds a counter to an iterable and returns it in a form of an enumerate object (yielding index-value pairs). 
    `zip()` takes iterables (can be zero or more), aggregates them in a tuple, and returns it. Both are incredibly useful for clean, "Pythonic" loops.

Real-Life Analogy:
    Enumerate: A teacher pointing at students in a row, giving them a number (1st, 2nd, 3rd) along with their name.
    Zip: Zipping a jacket where you perfectly align teeth from the left side with teeth from the right side.

Key Concepts:
    - Index tracking with enumerate
    - Parallel iteration with zip
    - Unpacking tuples in loops
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_enumerate():
    print("--- Enumerate Basic Syntax ---")
    fruits = ["apple", "banana", "cherry"]
    
    # Instead of doing: for i in range(len(fruits)):
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Fruit: {fruit}")
        
    print("\n--- Enumerate with Custom Start ---")
    for index, fruit in enumerate(fruits, start=1):
        print(f"Rank {index}: {fruit}")

def basic_zip():
    print("\n--- Zip Basic Syntax ---")
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    
    # Iterating over two lists in parallel
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Dictionary from Zip ---")
    # Quick way to create a dictionary from two lists
    keys = ["id", "username", "role"]
    values = [101, "admin_jane", "SuperAdmin"]
    user_dict = dict(zip(keys, values))
    print(user_dict)

    print("\n--- Filtering with Enumerate ---")
    # Finding indices of all even numbers
    numbers = [10, 15, 20, 25, 30]
    even_indices = [idx for idx, num in enumerate(numbers) if num % 2 == 0]
    print(f"Even numbers found at indices: {even_indices}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Unzipping ---")
    # Zipping
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    
    # Unzipping using the * operator
    letters, numbers = zip(*pairs)
    print("Letters:", letters)
    print("Numbers:", numbers)

    print("\n--- Zip with Enumerate ---")
    names = ["X", "Y", "Z"]
    ages = [20, 25, 30]
    
    # Combining both
    for idx, (name, age) in enumerate(zip(names, ages)):
        print(f"Person #{idx}: {name} is {age} years old.")
        
    print("\n--- Zip with Different Lengths (zip_longest) ---")
    from itertools import zip_longest
    list1 = [1, 2, 3]
    list2 = ['a', 'b']
    # Standard zip stops at the shortest list.
    # zip_longest fills the missing values with None (or a specified fillvalue).
    for num, char in zip_longest(list1, list2, fillvalue='?'):
        print(f"{num} -> {char}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Using `range(len(lst))` to track the index. This is an anti-pattern in Python; use `enumerate()`.
# 2. Expecting `zip` to pad uneven lists automatically. Standard `zip` stops when the shortest iterable is exhausted.
# 3. Forgetting to unpack the tuple yielded by `enumerate` or `zip`.

# Best Practices:
# 1. Always use `enumerate()` if you need the index inside a loop.
# 2. Use `zip()` to iterate over multiple lists in lock-step.
# 3. Use `itertools.zip_longest` when dealing with lists of unequal lengths and no data loss is required.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What happens if you pass lists of different lengths to `zip()`?
A: `zip` will stop generating tuples as soon as the shortest iterable is exhausted.

Q2: Can `zip()` take more than two iterables?
A: Yes, `zip` can take arbitrary number of iterables. e.g., `zip(l1, l2, l3)`.

Q3: What does `enumerate()` return?
A: An enumerate object, which is an iterator yielding tuples containing a count (from start, which defaults to 0) and the values obtained from iterating over the iterable.

Q4: How do you perform the reverse operation of `zip()`?
A: Using the unpack operator `*` with `zip()`: `zip(*zipped_list)`.

Q5: Why is `enumerate()` preferred over `range(len())`?
A: It is more readable, idiomatic (Pythonic), and slightly faster as it handles tracking the index natively.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Given a list of words, print the word only if its index is an odd number.
    pass

    # Exercise 2: Given lists `questions = ['name', 'color']` and `answers = ['Lancelot', 'blue']`, 
    # use zip to format and print: "What is your name? It is Lancelot." etc.
    pass

    # Exercise 3: Use zip and map to calculate the sum of elements from two lists of equal size, element by element.
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: 
    You have lists of product names, prices, and quantities.
    Calculate the total cost for each product (price * quantity) and print an itemized bill
    with the item number (starting from 1).
    """
    products = ["Laptop", "Mouse", "Keyboard"]
    prices = [1000, 20, 50]
    quantities = [2, 5, 3]
    
    print("\n--- Itemized Bill ---")
    grand_total = 0
    
    for idx, (prod, price, qty) in enumerate(zip(products, prices, quantities), start=1):
        total_cost = price * qty
        grand_total += total_cost
        print(f"{idx}. {prod} x{qty}: ${total_cost}")
        
    print(f"Grand Total: ${grand_total}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `enumerate(iterable, start=0)` is the Pythonic way to keep a count of iterations.
- `zip(*iterables)` is the best way to iterate through multiple sequences in parallel.
- Both functions return iterators, saving memory.
- `itertools.zip_longest` is available for un-even parallel iterations.
"""

if __name__ == "__main__":
    basic_enumerate()
    basic_zip()
    practical_examples()
    advanced_usage()
    mini_challenge()
