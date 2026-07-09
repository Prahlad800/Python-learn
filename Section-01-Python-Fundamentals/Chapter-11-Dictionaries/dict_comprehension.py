"""
Topic: Dictionary Comprehension
Chapter: 11
Level: Intermediate

Description:
    Dictionary comprehension is an elegant and concise way to create dictionaries in Python.
    It follows a similar syntax to list comprehensions but constructs key-value pairs instead of single items.

Real-Life Analogy:
    Imagine taking a list of prices in dollars and quickly writing down a new list with the same items but 
    prices converted to euros. Dictionary comprehension is the mental shortcut to do this translation rapidly.

Key Concepts:
    - Comprehension syntax: {key: value for item in iterable}
    - Conditional dictionary comprehension
    - Transforming existing dictionaries
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Syntax: {key_expression: value_expression for item in iterable}

# Creating a dictionary from a range of numbers (number: square)
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares}")
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Creating a dictionary from a list of strings (word: length)
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Inverting a dictionary (swapping keys and values)
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(f"Inverted dict: {inverted_dict}")

# Example 2: Converting temperatures
celsius_temps = {"New York": 15, "London": 12, "Tokyo": 20}
# Formula: (C * 9/5) + 32 = F
fahrenheit_temps = {city: (temp * 9/5) + 32 for city, temp in celsius_temps.items()}
print(f"Temperatures in Fahrenheit: {fahrenheit_temps}")

# Example 3: Filtering with if-condition
# Creating a dictionary with only even squares
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Advanced Example 1: Dictionary comprehension with if-else in value expression
numbers = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# Classify numbers as 'even' or 'odd'
classification = {k: ("even" if v % 2 == 0 else "odd") for k, v in numbers.items()}
print(f"Number classification: {classification}")

# Advanced Example 2: Nested dictionary comprehension
# Creating a multiplication table (1 to 3)
multiplication_table = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print("Multiplication table:")
for k, v in multiplication_table.items():
    print(f"  {k}: {v}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Overcomplicating comprehensions. 
# If it's too hard to read, use a standard for-loop instead.
# BAD (Too complex): 
# complex_dict = {k: v for k, v in data.items() if some_complex_condition(k, v) and another_condition(v)}

# Best Practice: Use dictionary comprehensions for simple transformations and filtering.
# Best Practice: Ensure that the new keys you generate will be unique, otherwise later values will overwrite earlier ones.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is a dictionary comprehension?
A: It's a syntactic construct that allows you to build a dictionary from an iterable in a single, readable line of code.

Q2: How do you filter items in a dictionary comprehension?
A: By adding an `if` clause at the end of the comprehension, e.g., {k: v for k, v in my_dict.items() if v > 10}.

Q3: Can you have an if-else statement in a dictionary comprehension?
A: Yes, but it goes in the value expression part before the `for` loop, e.g., {k: (v if v > 0 else 0) for k, v in items}.

Q4: What happens if your comprehension generates duplicate keys?
A: The dictionary will only keep the last generated value for that key, as keys must be unique.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Given a list of names `['Alice', 'Bob', 'Charlie']`, create a dict where keys are names and values are uppercase names.
Exercise 2: Given `prices = {'apple': 0.5, 'banana': 0.25, 'mango': 1.5}`, create a new dict with items costing more than 0.4.
Exercise 3: Given `ascii_chars = ['A', 'B', 'C']`, create a dict mapping the char to its ASCII value using `ord()`.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Process a list of student scores and create a dictionary mapping student 
    names to 'Pass' or 'Fail' (Pass if score >= 50).
    """
    scores = {"John": 45, "Emma": 82, "Sam": 50, "Lisa": 39}
    
    # Dictionary comprehension with if-else
    results = {name: ("Pass" if score >= 50 else "Fail") for name, score in scores.items()}
    
    print("Student Results:", results)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Dictionary comprehension provides a concise way to create dictionaries.
- Syntax: {key: value for item in iterable}.
- You can filter elements by appending an `if` condition.
- You can transform values conditionally using `value1 if condition else value2`.
- Keep comprehensions readable; avoid overly nested or complex logic.
"""

if __name__ == "__main__":
    mini_challenge()
