"""
Topic: List Sorting
Chapter: 9
Level: Intermediate

Description:
    Sorting lists is a common operation in programming. Python provides built-in methods to sort lists in-place or create new sorted lists, using highly optimized sorting algorithms (Timsort).

Real-Life Analogy:
    Imagine having a messy stack of files. Sorting is like organizing them alphabetically by name or numerically by date so you can find what you need instantly.

Key Concepts:
    - .sort() method (In-place)
    - sorted() function (Returns a new list)
    - Sorting with custom keys (the 'key' parameter)
    - Reverse sorting
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    # Using the .sort() method modifies the list IN-PLACE
    numbers = [5, 2, 9, 1, 5, 6]
    numbers.sort()
    print(f"Sorted numbers in-place: {numbers}")

    # Using sorted() returns a NEW sorted list, leaving the original unchanged
    original_letters = ['z', 'b', 'm', 'a']
    sorted_letters = sorted(original_letters)
    print(f"Original letters: {original_letters}")
    print(f"Newly sorted letters: {sorted_letters}")

    # Reverse sorting
    numbers.sort(reverse=True)
    print(f"Reverse sorted numbers: {numbers}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Sorting strings (alphabetical sort, case-sensitive by default)
    words = ["banana", "Apple", "cherry", "date"]
    words.sort() 
    # Notice 'Apple' comes first because uppercase letters have lower ASCII values
    print(f"Case-sensitive sort: {words}")

    # Sorting strings case-insensitively using the 'key' parameter
    words.sort(key=str.lower)
    print(f"Case-insensitive sort: {words}")

    # Sorting by string length
    words_by_len = sorted(words, key=len)
    print(f"Sorted by length: {words_by_len}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Sorting complex data types (e.g., list of tuples or dictionaries)
    students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78)
    ]

    # Sort students by their score (the second element in the tuple)
    # We use a lambda function as the key
    students.sort(key=lambda student: student[1], reverse=True)
    print(f"Students sorted by score (descending): {students}")

    # Sorting objects (assuming dictionaries)
    products = [
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 20},
        {"name": "Keyboard", "price": 80}
    ]
    # Sort by price
    sorted_products = sorted(products, key=lambda p: p["price"])
    print("Products sorted by price:")
    for p in sorted_products:
        print(f" - {p['name']}: ${p['price']}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Assigning the result of .sort() to a variable
    # .sort() returns None because it modifies the list in-place!
    nums = [3, 1, 2]
    result = nums.sort()
    print(f"Mistake - The result of .sort() is: {result}")
    
    # Best Practice: If you need to keep the original list, use sorted()
    unsorted_data = [9, 4, 7]
    sorted_data = sorted(unsorted_data)
    print(f"Original kept safe: {unsorted_data}, Sorted version: {sorted_data}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the difference between `list.sort()` and `sorted(list)`?
A: `list.sort()` modifies the original list in-place and returns None. `sorted()` leaves the original list alone and returns a new sorted list.

Q2: How do you sort a list in descending order?
A: By passing the argument `reverse=True` to either `sort()` or `sorted()`.

Q3: What does the `key` parameter do in sorting functions?
A: It specifies a function to be called on each list element prior to making comparisons. It allows for custom sorting logic (like sorting by length or dictionary value).

Q4: What sorting algorithm does Python use?
A: Python uses Timsort, a hybrid sorting algorithm derived from merge sort and insertion sort, optimized for real-world data.

Q5: Why does 'Zebra' come before 'apple' in a standard alphabetical sort?
A: Because Python sorts strings based on their Unicode/ASCII values, and uppercase letters have lower values than lowercase letters.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Given `nums = [10, 3, 7, 1, 9]`, sort it descending in-place.
Exercise 2: Use `sorted()` to alphabetically sort `['x', 'a', 'c', 'b']` without changing the original list.
Exercise 3: Sort a list of tuples representing (Item, Price) based on Price.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: You have a list of employees represented as dictionaries.
    Sort them primarily by Department (alphabetically), and secondarily by Salary (highest first).
    """
    employees = [
        {"name": "Alice", "dept": "Sales", "salary": 50000},
        {"name": "Bob", "dept": "IT", "salary": 80000},
        {"name": "Charlie", "dept": "Sales", "salary": 60000},
        {"name": "Diana", "dept": "IT", "salary": 75000}
    ]

    # We can return a tuple in the lambda for multi-level sorting.
    # To sort salary descending, we can negate it (since it's a number).
    employees.sort(key=lambda e: (e["dept"], -e["salary"]))
    
    print("Employees sorted by Dept (A-Z) and Salary (High to Low):")
    for emp in employees:
        print(f"{emp['dept']} - {emp['name']}: ${emp['salary']}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Use `.sort()` to modify the list in place (saves memory).
- Use `sorted()` to get a new sorted list (preserves original).
- Use `reverse=True` for descending order.
- Use the `key` argument with functions or lambdas for custom sorting logic.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    common_mistakes()
    mini_challenge()
