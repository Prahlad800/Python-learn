"""
Topic: Basic Output (print function)
Chapter: 4
Level: Beginner

Description:
    The `print()` function is the primary way to output text and data to the console in Python. It can handle multiple arguments, different data types, and allows customization of how items are separated and how the output ends.

Real-Life Analogy:
    Printing is like writing a message on a whiteboard for everyone to see. You can write single words, full sentences, or multiple distinct items spaced out.

Key Concepts:
    - print() function
    - comma-separated arguments
    - the 'sep' parameter
    - the 'end' parameter
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Printing a single string
print("Hello, World!")

# Printing multiple items
# Python automatically adds a space between them by default
print("The answer is", 42)

# Printing variables
name = "Charlie"
print("My name is", name)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    # Using the 'sep' parameter to change the separator
    print("apple", "banana", "cherry", sep=", ")
    
    # Formatting a date using sep
    print("12", "05", "2024", sep="/")
    
    # Using the 'end' parameter to avoid a newline
    print("This is line one. ", end="")
    print("This is still line one.")
    
    # Combining sep and end
    print("A", "B", "C", sep="-", end="***\n")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    import sys
    
    # Printing to a file (simulated by standard error here)
    print("This is an error message!", file=sys.stderr)
    
    # The flush parameter forces the output to be written immediately,
    # which is useful in long-running loops or animations.
    import time
    print("Loading", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        # time.sleep(0.5) # Uncomment to see the effect
    print(" Done!")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting parentheses in Python 3.
# print "Hello" # SyntaxError in Python 3

# Mistake: Concatenating non-strings without casting.
# print("Age: " + 25) # TypeError
# Correction: Use commas or type casting
print("Age: " + str(25))
print("Age:", 25)

# Best Practice: Use f-strings for complex formatting instead of many commas.
# Best Practice: Use 'end=" "' when looping to print items on the same line.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: Is print a statement or a function in Python 3?
A: It is a function. (In Python 2, it was a statement).

Q: What is the default separator (sep) in the print function?
A: A single space (" ").

Q: What is the default end character in the print function?
A: A newline character ("\n").

Q: How can you output to stderr instead of stdout?
A: By using the `file` parameter: print("Error", file=sys.stderr).

Q: What does the `flush` parameter do?
A: It forces the output buffer to be written to the terminal immediately.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # 1. Print three words separated by asterisks (*).
    print("One", "Two", "Three", sep="*")
    
    # 2. Print two statements on the same line using the 'end' parameter.
    print("Statement 1.", end=" ")
    print("Statement 2.")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Using a loop and a single print function with customized parameters,
    print the numbers 1 to 5 separated by arrows (->), and ending with "GO!".
    Expected: 1 -> 2 -> 3 -> 4 -> 5 -> GO!
    """
    for i in range(1, 6):
        print(i, end=" -> ")
    print("GO!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- print() outputs data to the console.
- Accepts multiple arguments and converts them to strings automatically.
- `sep` controls what goes between items (default is space).
- `end` controls what goes at the end (default is newline).
- `file` allows redirecting output to files or streams.
"""

if __name__ == "__main__":
    practical_examples()
    advanced_usage()
    practice_exercises()
    mini_challenge()
