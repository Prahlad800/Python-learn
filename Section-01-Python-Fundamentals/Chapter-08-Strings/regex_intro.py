"""
Topic: Introduction to Regular Expressions
Chapter: 8
Level: Advanced

Description:
    Regular expressions (Regex) are powerful tools for pattern matching within text.
    The `re` module in Python provides full support for regex.

Real-Life Analogy:
    Regex is like a highly advanced "Find and Replace" tool on steroids. Instead of finding a specific word, you can find a "pattern", like "any word that starts with A, has a number in it, and ends with Z".

Key Concepts:
    - re.search(), re.match(), re.findall()
    - Metacharacters (. ^ $ * + ? { } [ ] \ | ( ))
    - Character classes (\d, \w, \s)
    - Groups and capturing
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import re

def basic_regex():
    """Introduction to the re module."""
    text = "The quick brown fox jumps over 42 hurdles."
    
    # Search for a literal
    match = re.search(r"fox", text)
    if match:
        print("Found:", match.group())
        
    # Search for digits
    match_num = re.search(r"\d+", text)
    if match_num:
        print("Found number:", match_num.group())

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_regex():
    """Extracting emails and phone numbers."""
    text = "Contact us at info@example.com or support@test.org. Phone: 123-456-7890."
    
    # Find all emails
    emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
    print("Emails found:", emails)
    
    # Find all phone numbers matching pattern ddd-ddd-dddd
    phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
    print("Phones found:", phones)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def regex_substitution():
    """Using re.sub for replacing patterns."""
    text = "My secret pin is 1234 and my zip code is 56789."
    # Hide all numbers
    redacted = re.sub(r"\d+", "[REDACTED]", text)
    print("Redacted text:", redacted)
    
    # Grouping and backreferences
    date = "2023-10-15" # YYYY-MM-DD
    # Convert to DD/MM/YYYY
    formatted_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", date)
    print("Formatted date:", formatted_date)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Not using raw strings (r"") for regex patterns.
# Normal strings process escape sequences, making regex like \b (word boundary) become backspace.
# Always use r"\bword\b".

# Best Practice: Compile regex patterns using `re.compile()` if they are used repeatedly inside a loop.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: What is the difference between `re.match()` and `re.search()`?
A: `re.match()` checks for a match only at the beginning of the string, while `re.search()` checks anywhere in the string.

Q: What does `re.findall()` return?
A: A list of all non-overlapping matches in the string. If there are groups, it returns a list of tuples.

Q: What do `^` and `$` signify in regex?
A: `^` matches the start of the string, and `$` matches the end of the string.

Q: What does `\d`, `\w`, and `\s` stand for?
A: `\d` = digit, `\w` = word character (alphanumeric + underscore), `\s` = whitespace.

Q: How do you make a pattern case-insensitive?
A: By passing the flag `re.IGNORECASE` (or `re.I`) to the regex function.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Write a regex to validate if a string contains only letters and numbers.
# 2. Use `re.findall` to extract all hashtags from a tweet (e.g., "#python is #awesome").
# 3. Replace multiple spaces in a string with a single space using `re.sub`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """Validate a strong password."""
    # Requirements: At least 8 chars, 1 uppercase, 1 lowercase, 1 digit
    passwords = ["weak", "AlmostThere1", "StrongPass123!"]
    
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$")
    
    for pwd in passwords:
        if pattern.match(pwd):
            print(f"'{pwd}' is a valid password.")
        else:
            print(f"'{pwd}' is invalid.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `re` module provides regex operations.
- Use raw strings `r""` for patterns.
- `re.search()` finds the first match; `re.findall()` finds all matches.
- `re.sub()` is used for pattern-based string replacement.
- Groups `()` capture specific parts of a match.
"""

if __name__ == "__main__":
    basic_regex()
    practical_regex()
    regex_substitution()
    mini_challenge()
