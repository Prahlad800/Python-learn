"""
Topic: Indentation and Block Structure
Chapter: 01
Level: Beginner

Description:
    Unlike many other programming languages that use curly braces {} to define code blocks, 
    Python uses indentation (whitespace at the beginning of a line). This enforces readable 
    and structurally clean code.

Real-Life Analogy:
    Indentation is like an outline or table of contents. Just as sub-points are indented 
    under main points to show they belong together, Python code is indented to show which 
    statements belong to a specific block (like a function or a loop).

Key Concepts:
    - Whitespace matters
    - 4 spaces standard
    - `IndentationError`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_indentation():
    # This print is inside the function because it's indented.
    print("I am inside the function.")
    
# This print is outside because it's flush left.
# print("I am outside.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def nested_blocks():
    print("Start of function")
    if True:
        # We indent again to go inside the 'if' block
        print("  Inside the if block")
    # Un-indenting brings us back to the function block
    print("Back in the function block")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def multi_level_nesting():
    # Deeply nested code can become hard to read, but Python requires it to be strict.
    for i in range(1):
        if True:
            try:
                print("Deeply nested code block")
            except:
                pass

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Mixing tabs and spaces. This will cause an IndentationError or TabError.
# - Inconsistent indentation (e.g., 3 spaces on one line, 4 on the next).

# Best Practices:
# - Always use 4 spaces per indentation level.
# - Configure your text editor to convert Tabs to Spaces automatically.
# - Keep your code shallow (avoid excessive nesting) to maintain readability.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How does Python define code blocks?
# A: Using indentation (whitespace at the start of lines).
#
# Q2: What happens if you mix tabs and spaces in Python 3?
# A: It will raise a TabError, preventing the script from running.
#
# Q3: How many spaces is standard for a single level of indentation?
# A: 4 spaces, according to PEP 8.
#
# Q4: Why did Python's creator choose indentation over braces?
# A: To enforce readable code and eliminate clutter. Code is read more often than written.
#
# Q5: What is an IndentationError?
# A: An error raised when the interpreter finds inconsistent or unexpected whitespace at the start of a line.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write an `if` statement and intentionally misalign the indentation inside it. Run it to see the error.
# Exercise 2: Write a nested structure (a function containing an if statement) with perfect 4-space indentation.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Fix the indentation (conceptually)
    Imagine the following code was unindented. It is fixed here.
    """
    is_raining = True
    if is_raining:
        print("Take an umbrella")
        print("Wear a raincoat")
    print("Leave the house")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Indentation defines the grouping of statements.
# - 4 spaces is the industry standard.
# - Never mix tabs and spaces.
# - Clean indentation means fewer bugs and easier reading.

if __name__ == "__main__":
    basic_indentation()
    print("\n--- Nested Blocks ---")
    nested_blocks()
    print("\n--- Mini Challenge ---")
    mini_challenge()
