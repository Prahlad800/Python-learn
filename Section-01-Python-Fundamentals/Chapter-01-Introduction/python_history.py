"""
Topic: History of Python
Chapter: 01
Level: Beginner

Description:
    Understanding the origins of Python helps contextualize its design philosophy. 
    Created by Guido van Rossum and first released in 1991, Python was designed 
    to be a successor to the ABC programming language.

Real-Life Analogy:
    Knowing the history of a programming language is like knowing the history of your hometown. 
    It explains why the roads (or code structures) are built the way they are.

Key Concepts:
    - Guido van Rossum
    - Python 2 vs Python 3
    - The "Benevolent Dictator For Life" (BDFL)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_history():
    print("Python was conceived in the late 1980s.")
    print("Its implementation began in December 1989 by Guido van Rossum at CWI in the Netherlands.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def python_versions():
    # Demonstrating the major releases
    releases = {
        "Python 1.0": 1994,
        "Python 2.0": 2000,
        "Python 3.0": 2008
    }
    print("Major Python Releases:")
    for version, year in releases.items():
        print(f"{version} was released in {year}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def python_2_vs_3():
    # Python 3 was a major backwards-incompatible release.
    print("\nKey Difference Between Python 2 and 3:")
    print("In Python 2: print 'Hello'")
    print("In Python 3: print('Hello')")
    
    # Division difference
    print("In Python 2: 5 / 2 = 2 (integer division)")
    print("In Python 3: 5 / 2 = 2.5 (true division)")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Looking at Python 2 tutorials when trying to learn Python 3.
# - Assuming 'Python' refers to Python 2. Since 2020, Python 2 is officially end-of-life.

# Best Practices:
# - Always ensure you are running and learning Python 3.x.
# - Keep your Python version updated to benefit from new features and security patches.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Who created Python?
# A: Guido van Rossum.
#
# Q2: Why is it called Python?
# A: Guido was reading the published scripts from "Monty Python's Flying Circus" while developing the language.
#
# Q3: What is the significance of the year 2008 in Python's history?
# A: Python 3.0 was released, introducing major changes to fix fundamental design flaws.
#
# Q4: Is Python 2 still supported?
# A: No, Python 2 reached its end of life on January 1, 2020.
#
# Q5: What does BDFL stand for?
# A: Benevolent Dictator For Life, a title given to Guido van Rossum (he stepped down in 2018).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Create a print statement that outputs the creator of Python.
# Exercise: Write a dictionary that stores your birth year and Python's release year (1991), then print the difference.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Calculate how old Python is right now.
    """
    current_year = 2024
    release_year = 1991
    age = current_year - release_year
    print(f"As of {current_year}, Python is {age} years old!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Python was created by Guido van Rossum and released in 1991.
# - Named after "Monty Python's Flying Circus".
# - Python 3 is the modern, supported version of the language.

if __name__ == "__main__":
    basic_history()
    print()
    python_versions()
    python_2_vs_3()
    print()
    mini_challenge()
