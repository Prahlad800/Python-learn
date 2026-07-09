"""
Topic: String Slicing and Indexing
Chapter: 8
Level: Beginner

Description:
    String slicing allows you to extract specific parts of a string by specifying a range of indices.
    Indexing retrieves a single character from a string.

Real-Life Analogy:
    Imagine a train with numbered carriages. Indexing is picking a specific carriage.
    Slicing is selecting a continuous sequence of carriages to form a shorter train.

Key Concepts:
    - Zero-based indexing
    - Negative indexing
    - Slicing syntax: [start:stop:step]
    - Reversing strings
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

sample_text = "Python Programming"

def indexing_examples():
    """Demonstrates accessing individual characters."""
    first_char = sample_text[0]
    last_char = sample_text[-1]
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")

def slicing_basics():
    """Demonstrates basic slicing."""
    first_word = sample_text[0:6]
    print(f"First word: {first_word}")
    
    # Omitting start defaults to 0
    same_first_word = sample_text[:6]
    print(f"Omitting start: {same_first_word}")
    
    # Omitting stop defaults to end of string
    second_word = sample_text[7:]
    print(f"Second word: {second_word}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_slicing():
    """Extracting data from fixed-format strings."""
    date_str = "2023-10-15"
    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:]
    print(f"Year: {year}, Month: {month}, Day: {day}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_slicing():
    """Using the step parameter."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Every second character
    every_second = alphabet[::2]
    # Reversing a string
    reversed_alpha = alphabet[::-1]
    print(f"Every second char: {every_second}")
    print(f"Reversed: {reversed_alpha}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: IndexError when accessing out-of-bounds index
# char = sample_text[100]  # Raises IndexError

# Best Practice: Slicing handles out-of-bounds gracefully.
# slice_safe = sample_text[0:100] # Works fine without error, returns whole string

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: What happens if you specify a stop index larger than the string length in a slice?
A: Python gracefully stops at the end of the string without raising an error.

Q: How do you reverse a string using slicing?
A: Using the slice `string[::-1]`.

Q: What does a negative step in slicing do?
A: It iterates through the string backwards.

Q: Is `string[0]` the same as `string[0:1]`?
A: Value-wise they are the same (both return a 1-character string), but `string[0]` can raise IndexError for an empty string, whereas `string[0:1]` returns an empty string.

Q: Can you change a character using indexing, e.g., `s[0] = 'a'`?
A: No, strings are immutable.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Given the string "DataScience", extract the word "Data".
# 2. Extract the word "Science" using negative indexing.
# 3. Return every 3rd character from the string "ABCDEFGHIJKLMNOPQRSTUVWXYZ".

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge(url: str):
    """
    Challenge: Extract the domain name from a URL format like "https://www.example.com"
    """
    # Assuming standard format
    start = url.find("www.") + 4
    end = url.find(".com")
    domain = url[start:end]
    print(f"Domain extracted: {domain}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Strings are indexed starting from 0.
- Negative indices count from the end (-1 is the last character).
- Syntax for slicing is `[start:stop:step]`.
- Start is inclusive, stop is exclusive.
- Slicing out of bounds does not raise errors, but indexing does.
"""

if __name__ == "__main__":
    indexing_examples()
    slicing_basics()
    practical_slicing()
    advanced_slicing()
    mini_challenge("https://www.openai.com")
