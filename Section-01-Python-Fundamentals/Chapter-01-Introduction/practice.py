"""
Topic: Chapter 1 Practice and Overview
Chapter: 01
Level: Beginner

Description:
    This file serves as a consolidated practice ground for all the fundamental concepts 
    covered in Chapter 1: Syntax, Printing, Comments, and overall setup.
    It combines various elements to ensure a solid grasp of the basics.

Real-Life Analogy:
    Like a comprehensive driving test at the end of learning the basics. 
    You have to steer (syntax), use blinkers (comments), and communicate (print) 
    all at the same time to prove you are ready for the road.

Key Concepts:
    - Combining comments, prints, and syntax
    - Ensuring error-free code
    - Basic code organization
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Proper syntax ensures the code runs without errors.
# Let's set up some foundational variables.

def setup_environment():
    """Initializes basic variables for the practice session."""
    user = "Student"
    status = "Active"
    return user, status

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def display_status(user: str, status: str):
    # Using multiple print parameters
    print("User Profile Info")
    print("-----------------")
    print("Name:", user)
    print("Current Status:", status)

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_greeting():
    # Combining sep, end, and f-strings
    day = "Monday"
    print("System starting on", day, end=". ")
    print("Have a", "great", "day", sep="-", end="!\n")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Mixing up variable types when concatenating.
# - Forgetting colons after function definitions.

# Best Practices:
# - Run code frequently while writing it to catch syntax errors early.
# - Comment heavily when practicing to reinforce your own understanding.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why is practicing basic syntax important?
# A: Muscle memory for syntax prevents frustrating bugs later on when dealing with complex logic.
#
# Q2: Can you put a comment at the end of a print statement line?
# A: Yes, inline comments are supported.
#
# Q3: What is the main entry point idiom in Python scripts?
# A: `if __name__ == "__main__":`

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Modify the variables in setup_environment to reflect your details.
# Exercise: Add a new print statement using both `sep` and `end`.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Write a mini diagnostic script.
    - Print a header.
    - Print checking steps on the same line using `end`.
    - Print a final success message.
    """
    print("--- Diagnostic Tool ---")
    print("Checking memory", end="... ")
    print("OK")
    print("Checking disk", end="... ")
    print("OK")
    print("All systems operational.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Mastering basics is critical.
# - Combining `print()`, variables, and comments is the first step to writing robust scripts.
# - Practice builds confidence for the next chapters.

if __name__ == "__main__":
    u, s = setup_environment()
    display_status(u, s)
    print()
    advanced_greeting()
    print()
    mini_challenge()
