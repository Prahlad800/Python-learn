"""
Topic: List Filtering and Mapping (filter/map functions)
Chapter: 9
Level: Intermediate

Description:
    While list comprehensions are highly popular, Python also offers functional programming tools like `map()` and `filter()` to process lists. They apply a function to every item in an iterable.

Real-Life Analogy:
    `map()` is like putting every item on a conveyor belt through a painting machine (transforming them).
    `filter()` is like a quality control scanner that only lets valid items pass through.

Key Concepts:
    - The `map()` function
    - The `filter()` function
    - Using `lambda` (anonymous functions) with map/filter
    - Comparing with List Comprehensions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_map():
    print("--- Section 1: The map() Function ---")
    # map(function, iterable)
    # Applies a function to all the items in an input list.
    
    def square(x):
        return x ** 2

    numbers = [1, 2, 3, 4, 5]
    
    # map() returns a map object (an iterator), so we must convert it to a list to see it
    squared_nums = list(map(square, numbers))
    print(f"Squared numbers using map: {squared_nums}")

    # Using map with built-in functions
    string_nums = ["10", "20", "30"]
    integers = list(map(int, string_nums))
    print(f"Converted to integers: {integers}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (FILTER)
# ============================================================

def basic_filter():
    print("\n--- Section 2: The filter() Function ---")
    # filter(function, iterable)
    # Creates a list of elements for which the function returns True.
    
    def is_even(x):
        return x % 2 == 0

    numbers = [1, 2, 3, 4, 5, 6]
    
    # filter() returns a filter object, must be converted to a list
    even_nums = list(filter(is_even, numbers))
    print(f"Filtered even numbers: {even_nums}")

    # Filtering out empty strings or None values
    # Passing None as the function filters out falsy values
    mixed_data = ["hello", "", "world", None, "python", False]
    truthy_data = list(filter(None, mixed_data))
    print(f"Filtered truthy data: {truthy_data}")

# ============================================================
# SECTION 3: ADVANCED USAGE (LAMBDAS)
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Using Lambda Functions ---")
    # It is common to use small, inline, anonymous functions (lambdas) with map/filter
    # rather than formally defining a function with 'def' if it's only used once.
    
    prices = [10, 20, 30]
    # Apply a 10% discount using map + lambda
    discounted = list(map(lambda p: p * 0.9, prices))
    print(f"Discounted prices: {discounted}")

    # Filter out words shorter than 4 characters using filter + lambda
    words = ["cat", "dog", "elephant", "bird"]
    long_words = list(filter(lambda w: len(w) > 4, words))
    print(f"Words longer than 4 chars: {long_words}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes():
    print("\n--- Section 4: Common Mistakes & Best Practices ---")
    # Mistake: Forgetting to convert the map/filter object back to a list
    nums = [1, 2, 3]
    result = map(lambda x: x*2, nums)
    print(f"Mistake (printing map object): {result}")
    
    # Best Practice: While map() and filter() are great, List Comprehensions 
    # are generally considered more "Pythonic" and often more readable.
    
    # Map equivalent
    # list(map(lambda x: x*2, nums))
    comp_map = [x*2 for x in nums]
    
    # Filter equivalent
    # list(filter(lambda x: x>1, nums))
    comp_filter = [x for x in nums if x > 1]
    print(f"Pythonic alternatives (Comprehensions): {comp_map}, {comp_filter}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What does the `map()` function return in Python 3?
A: It returns a map object (an iterator). You usually need to wrap it in `list()` to evaluate and store the results.

Q2: How does `filter()` decide which elements to keep?
A: It applies a provided function to each element. If the function evaluates to True, the element is kept.

Q3: What happens if you pass `None` as the function to `filter()`?
A: It removes all "falsy" values from the iterable (e.g., False, 0, "", None, []).

Q4: When should you use list comprehensions vs map/filter?
A: Generally, list comprehensions are preferred in Python due to readability. However, `map()` is cleaner when you are just applying an existing function (like `map(int, list)`).

Q5: Can `map()` take multiple iterables?
A: Yes! If you provide multiple lists, the function must take that many arguments, and `map` applies it to items from the lists in parallel.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Given `temps_c = [0, 20, 37, 100]`, use `map()` and a lambda to convert them to Fahrenheit `(C * 9/5) + 32`.
Exercise 2: Given a list of mixed numbers `[-5, 3, -2, 8]`, use `filter()` to extract only the positive numbers.
Exercise 3: Combine both: filter out negative numbers, then square the remaining positive numbers using map().
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    """
    Challenge: You have a list of email addresses, some of which are poorly formatted 
    (missing the '@' symbol).
    1. Filter out the invalid emails.
    2. Convert all valid emails to lowercase using map.
    """
    emails = ["User1@GMAIL.com", "bademail.com", "Admin@Corp.org", "no_at_symbol"]
    
    # 1. Filter
    valid_emails = filter(lambda e: "@" in e, emails)
    
    # 2. Map
    clean_emails = list(map(lambda e: e.lower(), valid_emails))
    
    print(f"Clean, valid emails: {clean_emails}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `map(func, list)` applies a function to every element.
- `filter(func, list)` keeps only elements where the function returns True.
- Both return iterators, requiring conversion to a list `list()`.
- They are often paired with `lambda` functions for quick, inline operations.
"""

if __name__ == "__main__":
    basic_map()
    basic_filter()
    advanced_usage()
    common_mistakes()
    mini_challenge()
