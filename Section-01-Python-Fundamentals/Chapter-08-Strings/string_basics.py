"""
Topic: String Basics
Chapter: 8
Level: Beginner

Description:
    Strings in Python are sequences of characters used to store and manipulate text.
    They are immutable, meaning once created, their contents cannot be changed.

Real-Life Analogy:
    Think of a string like a beaded necklace. Each bead is a character, and the entire necklace is the string.
    You can look at the beads, but you cannot change an individual bead once the necklace is made.

Key Concepts:
    - String literals (single, double, triple quotes)
    - Escape characters
    - Multiline strings
    - Immutability
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Creating strings using single or double quotes
greeting_single = 'Hello, World!'
greeting_double = "Hello, World!"

# Using triple quotes for multiline strings
multiline_string = """This is a
multiline string
in Python."""

def basic_examples():
    """Demonstrates basic string creation."""
    print("Single quotes:", greeting_single)
    print("Double quotes:", greeting_double)
    print("Multiline:\n", multiline_string)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def escape_characters():
    """Examples of common escape characters."""
    # Newline
    newline_str = "Line 1\nLine 2"
    # Tab
    tab_str = "Column1\tColumn2"
    # Quotes inside quotes
    quote_str = "He said, \"Python is awesome!\""
    
    print("Newline example:\n", newline_str)
    print("Tab example:", tab_str)
    print("Quotes example:", quote_str)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def immutability_demo():
    """Demonstrates that strings are immutable."""
    original = "hello"
    # original[0] = "H" # This would raise a TypeError
    # Instead, we create a new string:
    modified = "H" + original[1:]
    print("Original:", original)
    print("Modified:", modified)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to escape characters or mismatching quotes
# Bad: my_str = 'It's a beautiful day' (SyntaxError)
# Correct: my_str = 'It\'s a beautiful day' OR my_str = "It's a beautiful day"

# Best Practice: Use triple quotes for docstrings and long SQL/HTML blocks.
# Best Practice: Choose single or double quotes consistently in your codebase.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: Are strings in Python mutable or immutable?
A: Immutable. Any operation that modifies a string creates a new string object.

Q: How do you include a backslash in a string?
A: By escaping it with another backslash, e.g., "\\".

Q: What is the difference between single and double quotes?
A: There is no functional difference in Python, they can be used interchangeably.

Q: How do you represent a multiline string?
A: Using triple single (''') or triple double (""") quotes.

Q: How would you prevent escape characters from being processed in a string?
A: Prefix the string with 'r' to create a raw string, e.g., r"C:\new\folder".
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Create a variable storing your favorite quote using double quotes.
# 2. Create a variable with a string that contains both single and double quotes correctly.
# 3. Write a multiline string representing a short poem.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create a raw string containing a Windows file path
    and print it. Then create a string representing a JSON object.
    """
    raw_path = r"C:\Users\Name\Documents\new_file.txt"
    json_string = """{
    "name": "Alice",
    "age": 30
}"""
    print("Raw Path:", raw_path)
    print("JSON String:\n", json_string)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Strings represent text data in Python.
- They can be created using single, double, or triple quotes.
- Strings are immutable.
- Escape sequences like \\n and \\t add special formatting.
- Raw strings (prefix 'r') ignore escape sequences.
"""

if __name__ == "__main__":
    basic_examples()
    escape_characters()
    immutability_demo()
    mini_challenge()
