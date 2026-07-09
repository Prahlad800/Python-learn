"""
Topic: List Comprehension
Chapter: 9
Level: Intermediate

Description:
    List comprehensions provide a concise way to create lists based on existing iterables. They are often faster and more readable than standard for-loops.

Real-Life Analogy:
    Like an assembly line that applies a specific modification to every item passing through, filtering out the bad ones automatically.

Key Concepts:
    - Syntax of List Comprehensions
    - Adding Conditionals (Filtering)
    - Nested List Comprehensions
    - Performance vs. Standard Loops
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    # Standard way using a for-loop
    squares_loop = []
    for i in range(1, 6):
        squares_loop.append(i ** 2)
    print(f"Squares using loop: {squares_loop}")

    # Pythonic way using list comprehension
    # Syntax: [expression for item in iterable]
    squares_comp = [i ** 2 for i in range(1, 6)]
    print(f"Squares using comprehension: {squares_comp}")

    # Converting strings to uppercase
    words = ["hello", "world", "python"]
    upper_words = [word.upper() for word in words]
    print(f"Uppercase words: {upper_words}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Filtering items using an if-condition
    # Syntax: [expression for item in iterable if condition]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")

    # Applying functions to filter and format data
    raw_data = ["  apple  ", "banana", "  cherry"]
    clean_data = [fruit.strip().capitalize() for fruit in raw_data]
    print(f"Cleaned data: {clean_data}")

    # Using if-else inside list comprehension (ternary operator)
    # Syntax: [expression_if_true else expression_if_false for item in iterable]
    statuses = ["pass" if score >= 50 else "fail" for score in [45, 80, 55, 30]]
    print(f"Exam statuses: {statuses}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Nested list comprehensions (Flattening a 2D list)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # Standard loop approach:
    # flat_list = []
    # for row in matrix:
    #     for num in row:
    #         flat_list.append(num)
    
    flat_list = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flat_list}")

    # Creating a matrix using nested comprehension
    # Creates a 3x3 grid of zeros
    grid = [[0 for _ in range(3)] for _ in range(3)]
    print(f"Generated Grid: {grid}")

    # Complex filtering: Multiple conditions
    nums = range(20)
    div_by_2_and_3 = [x for x in nums if x % 2 == 0 if x % 3 == 0]
    print(f"Numbers divisible by 2 and 3: {div_by_2_and_3}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Writing overly complex list comprehensions
    # While they are powerful, nesting too many loops or conditions makes code unreadable.
    
    # Bad Practice (Hard to read):
    # result = [x*y for x in range(10) for y in range(10) if x > 5 if y < 3 if (x+y) % 2 == 0]
    
    # Best Practice: If it spans more than two lines or is hard to mentally parse, 
    # fall back to standard loops or split it into helper functions.
    
    # Tip: Use list comprehensions primarily for simple mapping and filtering.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What are the advantages of using list comprehensions?
A: They are generally faster than standard for-loops and reduce the number of lines of code, leading to cleaner, more readable Pythonic code.

Q2: How do you include an `else` clause in a list comprehension?
A: The if-else statement must be placed before the `for` keyword. Example: `[x if x > 0 else 0 for x in items]`.

Q3: Can a list comprehension replace every for-loop?
A: Technically yes for list creation, but it shouldn't. If the logic contains side effects (like printing or modifying external state), or is too complex, a standard for-loop is better for readability and maintainability.

Q4: What is the scope of the iteration variable in a list comprehension?
A: In Python 3, the iteration variable (e.g., `i` in `[i for i in range(5)]`) is localized to the comprehension and does not leak into the surrounding scope.

Q5: Is list comprehension memory efficient?
A: It creates the entire list in memory. If dealing with huge datasets, a generator expression `(...)` is more memory-efficient than a list comprehension `[...]`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a list of the first 10 cubes (i**3) using a list comprehension.
Exercise 2: Given the list `words = ["cat", "window", "defenestrate"]`, create a new list containing the lengths of those words.
Exercise 3: Extract all vowels from the string "List Comprehensions are awesome!" using a comprehension.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: Find all the numbers from 1 to 50 that contain the digit '3'.
    Use a list comprehension to solve this.
    """
    numbers_with_3 = [num for num in range(1, 51) if '3' in str(num)]
    print(f"Numbers 1-50 containing '3': {numbers_with_3}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- List comprehensions provide a short syntax for creating lists.
- You can map existing data to new formats `[func(x) for x in list]`.
- You can filter data `[x for x in list if condition]`.
- You can conditionally modify data `[x if cond else y for x in list]`.
- Overusing them can decrease readability; keep them simple.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    common_mistakes()
    mini_challenge()
