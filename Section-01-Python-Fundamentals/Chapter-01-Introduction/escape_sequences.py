"""
Topic: Escape Sequences
Chapter: 01
Level: Beginner

Description:
    Escape sequences allow you to include special characters in strings that would otherwise 
    be difficult or impossible to type, such as newlines, tabs, or quote marks themselves. 
    They always begin with a backslash `\`.

Real-Life Analogy:
    Imagine writing a letter and needing a special symbol to tell the reader to 
    "turn the page" or "pause." Escape sequences are those hidden symbols that tell 
    the computer how to format the text output rather than just printing the letter exactly.

Key Concepts:
    - The backslash `\` escape character
    - Newline `\n`
    - Tab `\t`
    - Escaping quotes `\'` and `\"`
    - Escaping the backslash `\\`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_escapes():
    # Newline character
    print("Line 1\nLine 2")
    
    # Tab character
    print("Column A\tColumn B")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_escaping():
    # Escaping quotes so they don't prematurely end the string
    print("They said, \"Python is awesome!\"")
    print('It\'s a wonderful day to code.')
    
    # Escaping the backslash itself (e.g., file paths)
    print("C:\\Users\\Admin\\Documents")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_sequences():
    # Carriage return (\r) moves the cursor to the beginning of the line
    # (Note: behaves differently in various terminals; here it overwrites)
    print("Hello World\rPython")
    
    # Raw strings (prefixing with 'r') ignore escape sequences completely.
    # Highly useful for regular expressions and Windows file paths.
    print(r"Raw string: C:\Users\Admin\Documents\new_file.txt")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Using a single backslash in a file path without making it a raw string.
#   e.g., path = "C:\new_folder" (The \n becomes a newline!)
# - Forgetting that escape sequences count as a single character in string length.

# Best Practices:
# - Use raw strings (r"") for regular expressions and Windows paths.
# - If your string contains many double quotes, wrap the whole string in single quotes 
#   (or vice versa) to avoid excessive escaping. e.g., 'He said "Hello"'

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does `\n` do inside a string?
# A: It inserts a newline, moving the subsequent text to the next line.
#
# Q2: How do you print a literal backslash `\`?
# A: By escaping it with another backslash: `\\`.
#
# Q3: What is a raw string in Python?
# A: A string prefixed with `r` or `R` that treats backslashes as literal characters, ignoring escape sequences.
#
# Q4: If `s = "a\nb"`, what is `len(s)`?
# A: 3 (The 'a', the newline character '\n', and the 'b').
#
# Q5: Why is `\t` useful?
# A: It inserts a horizontal tab, useful for aligning text columns in the console.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a print statement that outputs a 2x2 grid using \t and \n.
# Exercise 2: Print the phrase: The symbol for a backslash is \.
# Exercise 3: Create a raw string containing a hypothetical file path.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create a formatted receipt using escape sequences.
    """
    receipt = "RECEIPT\n-------\nItem\t\tPrice\nApple\t\t$1.00\nBanana\t\t$0.50\n-------\nTotal\t\t$1.50"
    print(receipt)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The backslash `\` is the escape character.
# - `\n` creates a new line, `\t` creates a tab.
# - `\"` and `\'` allow quotes inside strings.
# - Raw strings `r"text"` prevent escape sequence evaluation.

if __name__ == "__main__":
    print("--- Basic Escapes ---")
    basic_escapes()
    print("\n--- Practical Escaping ---")
    practical_escaping()
    print("\n--- Advanced Sequences ---")
    advanced_sequences()
    print("\n--- Mini Challenge ---")
    mini_challenge()
