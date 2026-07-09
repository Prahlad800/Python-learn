"""
Topic: General String Practice
Chapter: 8
Level: Intermediate

Description:
    A collection of common string manipulation problems to test understanding of string basics, slicing, methods, and formatting.

Real-Life Analogy:
    Like a driving test after learning the controls of a car. Now you have to combine steering, braking, and signaling to navigate a course.

Key Concepts:
    - Reversing strings
    - Palindromes
    - Anagrams
    - Vowel counting
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def reverse_string(s: str) -> str:
    """Reverse a string using slicing."""
    return s[::-1]

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def is_palindrome(s: str) -> bool:
    """Check if a string reads the same forwards and backwards."""
    # Clean string: remove spaces, lowercase
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def are_anagrams(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams of each other."""
    # Clean and sort both strings
    clean_s1 = sorted(s1.replace(" ", "").lower())
    clean_s2 = sorted(s2.replace(" ", "").lower())
    return clean_s1 == clean_s2

def run_length_encoding(s: str) -> str:
    """Basic run length encoding compression (e.g., AAAABBB -> A4B3)."""
    if not s:
        return ""
    
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(f"{s[i - 1]}{count}")
            count = 1
    encoded.append(f"{s[-1]}{count}")
    return "".join(encoded)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to handle case sensitivity and spaces when checking palindromes or anagrams.
# Best Practice: Normalize data (e.g., `.lower()`, `.strip()`) before processing strings.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: How do you check if a string is a palindrome in Python?
A: `return s == s[::-1]`

Q: What is the time complexity of reversing a string using slicing?
A: O(N), where N is the length of the string.

Q: How can you reverse the words in a sentence, not the letters?
A: `sentence.split()`, reverse the list, then `' '.join()` it. `return ' '.join(sentence.split()[::-1])`
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Write a function to capitalize the first letter of every word (without using `.title()`).
# 2. Write a function to find the most frequent character in a string.
# 3. Write a function to remove duplicate characters from a string while preserving order.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def reverse_words_in_sentence(sentence: str) -> str:
    """Reverse words in a sentence."""
    words = sentence.split()
    return " ".join(words[::-1])

def mini_challenge():
    """Test all practice functions."""
    print("Reversed 'hello':", reverse_string("hello"))
    print("Is 'race car' palindrome?", is_palindrome("race car"))
    print("Vowels in 'hello world':", count_vowels("hello world"))
    print("Are 'listen' and 'silent' anagrams?", are_anagrams("listen", "silent"))
    print("RLE of 'AABBBCCCC':", run_length_encoding("AABBBCCCC"))
    print("Reversed sentence:", reverse_words_in_sentence("Python is fun"))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Slicing `[::-1]` is the pythonic way to reverse a string.
- Normalizing string case is crucial for algorithms like Palindromes and Anagrams.
- `join()` and `split()` work perfectly together for word-level manipulations.
"""

if __name__ == "__main__":
    mini_challenge()
