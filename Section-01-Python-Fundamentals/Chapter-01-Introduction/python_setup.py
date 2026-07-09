"""
Topic: Python Setup and Execution
Chapter: 01
Level: Beginner

Description:
    This file explains how Python scripts are executed and the different ways 
    you can run Python code (e.g., interactive shell vs. script file).
    It also introduces the __name__ == "__main__" idiom.

Real-Life Analogy:
    Setting up Python is like setting up a new kitchen. The interactive shell is like 
    tasting ingredients straight from the jar, while a script file is like following 
    a full recipe from start to finish.

Key Concepts:
    - Interactive shell (REPL)
    - Script execution
    - Main entry point (`if __name__ == "__main__":`)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def explain_execution():
    print("Python code can be run in two main ways:")
    print("1. Interactive Shell (REPL - Read, Eval, Print, Loop)")
    print("2. Script Files (.py extension)")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def explain_repl():
    # The REPL is great for quick tests.
    print("\nIn the REPL, you can type '2 + 2' and hit Enter to immediately see '4'.")
    print("In a script, you must use 'print(2 + 2)' to see the output.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def explain_main_idiom():
    print("\nUnderstanding: if __name__ == '__main__':")
    print("This idiom checks if the script is being run directly or imported as a module.")
    print("If run directly, __name__ is set to '__main__'.")
    print("If imported, __name__ is set to the filename.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistakes:
# - Writing an entire application in the REPL (it doesn't save!).
# - Forgetting to save the .py file before running it in the terminal.
# - Putting execution code directly in the global scope instead of using the main block.

# Best Practices:
# - Use the REPL for quick experimentation.
# - Use a proper IDE or text editor for writing scripts.
# - Always use `if __name__ == "__main__":` to protect execution code.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does REPL stand for?
# A: Read, Eval, Print, Loop.
#
# Q2: Why is `if __name__ == "__main__":` used?
# A: To prevent code from being executed automatically when the module is imported into another script.
#
# Q3: How do you run a Python script from the command line?
# A: By typing `python filename.py` (or `python3 filename.py`).
#
# Q4: What extension do Python scripts use?
# A: .py
#
# Q5: What is a virtual environment?
# A: An isolated environment that allows you to install packages for a specific project without affecting the global Python installation.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Open your terminal, type `python`, and run a simple calculation in the REPL.
# Exercise: Create a new file, write a print statement, save it, and run it from the terminal.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Print a message indicating whether this file is being run directly or imported.
    """
    # Note: Because this function is called inside the main block below, 
    # it will typically print the first option when this script is run.
    if __name__ == "__main__":
        print("This script is running directly as the main program!")
    else:
        print("This script was imported as a module!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Python has an interactive shell for quick testing.
# - Scripts are saved as .py files and run via the interpreter.
# - The `if __name__ == "__main__":` block is essential for modular, reusable code.

if __name__ == "__main__":
    explain_execution()
    explain_repl()
    explain_main_idiom()
    print()
    mini_challenge()
