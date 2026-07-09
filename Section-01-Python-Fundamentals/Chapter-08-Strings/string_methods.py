"""
Topic: Built-in String Methods
Chapter: 8
Level: Intermediate

Description:
    Python strings come with a rich set of built-in methods for manipulation, searching, replacing, and case conversion.
    Since strings are immutable, these methods always return a new string.

Real-Life Analogy:
    Think of string methods like tools in a text editor. You have a tool to uppercase everything, a tool to find a word, and a tool to replace words.

Key Concepts:
    - Case conversions: lower(), upper(), title(), capitalize()
    - Searching: find(), index(), count(), startswith(), endswith()
    - Modification: replace(), strip(), split(), join()
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def case_methods():
    """Demonstrates case conversion methods."""
    text = "python PROGRAMMING is fun"
    print("Original:", text)
    print("Upper:", text.upper())
    print("Lower:", text.lower())
    print("Title:", text.title())
    print("Capitalize:", text.capitalize())

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def modification_methods():
    """Demonstrates stripping, replacing, splitting, and joining."""
    # Stripping whitespace
    messy = "   some user input   "
    clean = messy.strip()
    print(f"Stripped: '{clean}'")
    
    # Replacing
    sentence = "I like apples."
    new_sentence = sentence.replace("apples", "oranges")
    print("Replaced:", new_sentence)
    
    # Splitting and Joining
    csv_data = "apple,banana,cherry"
    fruits_list = csv_data.split(",")
    print("Split list:", fruits_list)
    
    joined_data = " | ".join(fruits_list)
    print("Joined string:", joined_data)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def search_methods():
    """Searching within strings."""
    filepath = "report_2023.pdf"
    
    print("Starts with 'report':", filepath.startswith("report"))
    print("Ends with '.pdf':", filepath.endswith(".pdf"))
    
    # find vs index
    text = "Where's Waldo?"
    print("Find Waldo:", text.find("Waldo")) # Returns index
    print("Find missing:", text.find("Carmen")) # Returns -1
    
    # text.index("Carmen") # Would raise ValueError!
    
    print("Count 'W':", text.count("W"))

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Expecting a method to modify the string in-place.
# text = "hello"
# text.upper()
# print(text) # Still prints "hello"
# Fix: text = text.upper()

# Best Practice: Use `startswith` or `endswith` instead of slicing or regex for simple prefix/suffix checks.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: What is the difference between `find()` and `index()`?
A: `find()` returns -1 if the substring is not found, whereas `index()` raises a ValueError.

Q: How do you remove punctuation from the beginning and end of a string?
A: `string.strip(punctuation_characters)`

Q: Does `split()` with no arguments split by commas?
A: No, it splits by any whitespace (spaces, tabs, newlines) and discards empty strings.

Q: How can you count non-overlapping occurrences of a substring?
A: Using the `string.count(substring)` method.

Q: What does `title()` do? Is it flawless?
A: `title()` capitalizes the first letter of every word. However, it can mess up apostrophes (e.g., "they're" -> "They'Re").
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Given a string with leading and trailing dots, strip them out.
# 2. Replace all spaces in a string with underscores.
# 3. Take a sentence, split it into words, and join it back using dashes.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """Clean and normalize a list of user inputs."""
    raw_inputs = ["   john doe  ", "ALICE", "bOb SMITH   "]
    cleaned = []
    
    for name in raw_inputs:
        cleaned.append(name.strip().title())
        
    print("Original:", raw_inputs)
    print("Cleaned:", cleaned)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- String methods always return new string objects.
- Case conversions: `lower()`, `upper()`, `title()`, `capitalize()`, `swapcase()`.
- Search: `find()`, `index()`, `count()`, `startswith()`, `endswith()`.
- Modification: `strip()`, `replace()`, `split()`, `join()`.
"""

if __name__ == "__main__":
    case_methods()
    modification_methods()
    search_methods()
    mini_challenge()
