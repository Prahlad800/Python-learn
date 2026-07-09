"""
Topic: Dunder Attributes in Modules
Chapter: 13
Level: Intermediate

Description:
    "Dunder" stands for "Double Underscore". Modules in Python have several built-in attributes 
    surrounded by double underscores (e.g., `__name__`, `__file__`, `__doc__`). These attributes 
    store metadata about the module.

Real-Life Analogy:
    Think of a dunder attribute like the manufacturer's tag on a piece of clothing. 
    It's not the main part of the shirt, but it tells you the brand, the size, and washing instructions. 
    Dunder attributes tell Python (and you) metadata about the file.

Key Concepts:
    - __name__
    - __file__
    - __doc__
    - __all__
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The most famous dunder attribute is __name__.
# It evaluates to the name of the module as a string.

def print_name():
    print(f"The __name__ of this module is: {__name__}")

# The __doc__ attribute holds the docstring of the module (the large comment at the top).
def print_doc():
    print("Module Docstring Snippet:")
    print(__doc__[:100] + "...")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Using __file__ to find paths
# __file__ gives the absolute path to the module's file on disk.
import os

def find_sibling_file(filename: str) -> str:
    """Finds a file in the same directory as this module."""
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, filename)

print(f"Path to this file: {__file__}")
print(f"Path to sibling 'config.json': {find_sibling_file('config.json')}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# The __all__ attribute
# It is a list of strings defining what symbols are exported when someone does `from module import *`.

__all__ = ["public_function", "PublicClass"]

def public_function():
    return "I am public"

def _private_function():
    # The leading underscore suggests this is internal, 
    # and it won't be exported by `import *` anyway.
    return "I am private"

class PublicClass:
    pass

class SecretClass:
    pass

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Executing code during import because of missing `if __name__ == "__main__":`
# If you run `print("Hello")` outside a function, it runs when imported.
# Best Practice: Always gate your execution block.

# Mistake 2: Hardcoding file paths instead of using `__file__`.
# If you hardcode `C:/Users/...`, your code will break on another machine.
# Best Practice: Use `os.path.dirname(__file__)` to build paths relative to the current script.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What does `if __name__ == "__main__":` do?
# A: It checks if the script is being run directly by the Python interpreter. If it is being imported 
#    by another script, `__name__` will be the module's name, so the block won't execute.

# Q2: What is the `__file__` attribute used for?
# A: It contains the path to the file from which the module was loaded. Useful for finding data files 
#    stored relative to the Python script.

# Q3: What is the `__doc__` attribute?
# A: It contains the documentation string of the module, class, or function. It's used by the `help()` function.

# Q4: What is the purpose of `__all__`?
# A: It explicitly defines the public API of a module. It restricts what is imported when using `from module import *`.

# Q5: Why are they called "dunder" attributes?
# A: It's an abbreviation for "Double Under(score)", used to avoid saying "underscore underscore name underscore underscore".

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a function that prints all the attributes of the current module that start with `__`.

def list_dunder_attributes():
    print("Dunder Attributes in this module:")
    for key in globals():
        if key.startswith("__") and key.endswith("__"):
            print(f"- {key}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Create a mock dictionary representing a module's dictionary.
# Write a function that mimics `from module import *`. 
# It should respect the `__all__` list if it exists; otherwise, it imports everything not starting with an underscore.

def simulate_star_import(module_dict: dict) -> list:
    imported = []
    if "__all__" in module_dict:
        # Respect __all__
        imported = module_dict["__all__"]
    else:
        # Default behavior
        for key in module_dict.keys():
            if not key.startswith("_"):
                imported.append(key)
    return imported

def run_challenge():
    mod1 = {
        "__all__": ["func_a"],
        "func_a": "A",
        "func_b": "B",
        "_func_c": "C"
    }
    
    mod2 = {
        "func_x": "X",
        "func_y": "Y",
        "_func_z": "Z"
    }
    
    print(f"Importing from mod1 (has __all__): {simulate_star_import(mod1)}")
    print(f"Importing from mod2 (no __all__): {simulate_star_import(mod2)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Dunder attributes provide metadata about a module.
# - `__name__` is crucial for writing scripts that can be imported or run directly.
# - `__file__` is essential for constructing robust, relative file paths.
# - `__all__` helps you control your module's public interface.

if __name__ == "__main__":
    print_name()
    print_doc()
    list_dunder_attributes()
    run_challenge()
