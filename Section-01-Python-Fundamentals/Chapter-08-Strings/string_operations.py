"""
Topic: String Operations (Concatenation, Repetition, Membership)
Chapter: 8
Level: Beginner

Description:
    String operations allow combining multiple strings, repeating them, or checking if a substring exists within them.
    These are fundamental tools for basic string manipulation.

Real-Life Analogy:
    Concatenation is like joining train cars together. Repetition is like copying a flyer multiple times.
    Membership testing is like checking if a specific ingredient is listed in a recipe.

Key Concepts:
    - Concatenation (+)
    - Repetition (*)
    - Membership testing (in, not in)
    - Lexicographical comparison (==, <, >)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_operations():
    """Demonstrates fundamental string operations."""
    str1 = "Hello"
    str2 = "World"
    
    # Concatenation
    joined = str1 + " " + str2
    print(f"Concatenation: {joined}")
    
    # Repetition
    repeated = "Echo! " * 3
    print(f"Repetition: {repeated}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def membership_testing():
    """Checking for substrings inside strings."""
    sentence = "The quick brown fox jumps over the lazy dog."
    
    word_to_find = "fox"
    if word_to_find in sentence:
        print(f"Found '{word_to_find}' in the sentence.")
        
    absent_word = "cat"
    if absent_word not in sentence:
        print(f"'{absent_word}' is not in the sentence.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def string_comparison():
    """Comparing strings lexicographically (alphabetical order)."""
    word1 = "apple"
    word2 = "banana"
    
    print(f"Is '{word1}' equal to '{word2}'? {word1 == word2}")
    # Compares ASCII values character by character
    print(f"Does '{word1}' come before '{word2}'? {word1 < word2}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Trying to concatenate a string with a non-string without conversion.
# result = "Age: " + 25  # Raises TypeError
# Fix: result = "Age: " + str(25)

# Best Practice: Avoid heavy string concatenation in loops with `+`.
# Use `"".join(list)` instead for better memory performance.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: How does the `in` operator work on strings?
A: It checks if the left operand (substring) exists within the right operand (string) and returns a boolean.

Q: What happens when you multiply a string by 0 or a negative number?
A: It returns an empty string.

Q: How do string comparisons (<, >) work in Python?
A: They compare strings lexicographically based on their Unicode code points character by character.

Q: Why is concatenating strings in a large loop bad practice?
A: Because strings are immutable, every `+` creates a new string object, leading to quadratic time complexity. `str.join()` is linear and preferred.

Q: Can you subtract strings in Python?
A: No, the `-` operator is not supported for strings.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Ask the user for their first name and last name, then concatenate them with a space.
# 2. Print a horizontal divider using string repetition (e.g., "-" repeated 50 times).
# 3. Write a function that returns True if a given string contains all the vowels (a, e, i, o, u).

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def contains_all_vowels(text: str) -> bool:
    """Check if all vowels are present in a string, case-insensitive."""
    vowels = "aeiou"
    text = text.lower()
    for v in vowels:
        if v not in text:
            return False
    return True

def mini_challenge():
    """Test the vowel function."""
    test_str = "Education"
    print(f"Does '{test_str}' contain all vowels? {contains_all_vowels(test_str)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `+` operator joins strings.
- `*` operator repeats a string a given number of times.
- `in` and `not in` are used to check for substrings.
- Strings can be compared using relational operators (==, <, >), which rely on Unicode values.
"""

if __name__ == "__main__":
    basic_operations()
    membership_testing()
    string_comparison()
    mini_challenge()
