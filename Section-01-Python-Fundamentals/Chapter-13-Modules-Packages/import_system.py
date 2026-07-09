"""
Topic: Python Import System
Chapter: 13
Level: Advanced

Description:
    The Python import system is the mechanism by which Python locates, loads, and initializes modules.
    Understanding `sys.path`, module caching in `sys.modules`, and how the interpreter searches for 
    files allows you to debug "ModuleNotFoundError" and structure complex projects properly.

Real-Life Analogy:
    When you search for a book in a library, you check specific aisles in a specific order (catalogue, 
    reference, fiction). Python's import system checks a specific list of directories (sys.path) 
    in a specific order to find the module you asked for.

Key Concepts:
    - sys.path
    - sys.modules
    - PYTHONPATH environment variable
    - Built-in vs third-party vs local resolution order
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import sys
import pprint

# sys.path is a list of strings that specifies the search path for modules.
# When you say `import foo`, Python looks for `foo.py` in these directories in order.
def show_sys_path():
    """Prints the current module search paths."""
    print("Module Search Path (sys.path):")
    for path in sys.path[:5]: # Show first 5 for brevity
        print(f" - {path}")
    print("...")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# sys.modules is a dictionary that maps module names to modules which have already been loaded.
# This acts as a cache.

def check_loaded_modules(module_name: str):
    """Checks if a module is currently cached in sys.modules."""
    if module_name in sys.modules:
        print(f"'{module_name}' is currently loaded in memory.")
        print(f"Module object: {sys.modules[module_name]}")
    else:
        print(f"'{module_name}' is NOT loaded.")

import math
check_loaded_modules('math')
check_loaded_modules('random') # Might not be loaded unless imported earlier

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Manipulating sys.path dynamically
# Sometimes, you need to import a module from a directory not currently in sys.path.
import os

def dynamic_path_modification():
    """Temporarily adds a directory to sys.path to load a module."""
    custom_dir = os.path.abspath(os.path.join(os.getcwd(), 'my_custom_lib_folder'))
    
    # Check if we should add it
    if custom_dir not in sys.path:
        sys.path.insert(0, custom_dir) # Insert at beginning to prioritize
        print(f"Added {custom_dir} to sys.path")
    
    # Now you could hypothetically `import custom_module` located in that folder
    
    # Cleanup
    if custom_dir in sys.path:
        sys.path.remove(custom_dir)
        print("Restored sys.path")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Naming your local file the same as a standard library module (e.g., email.py, math.py).
# Because the current directory is often first in sys.path, Python will load YOUR file instead of the standard one, 
# breaking standard library imports elsewhere.

# Mistake 2: Hacking sys.path permanently in production code.
# Avoid manipulating sys.path dynamically if possible. It makes code hard to follow.
# Best Practice: Use proper packaging and installation (`pip install -e .`) instead of sys.path hacks.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the order in which Python searches for modules?
# A: 1. Built-in modules, 2. Directories in sys.path (current directory first, then PYTHONPATH, then standard library, then site-packages).

# Q2: How does Python prevent loading the same module multiple times?
# A: It caches loaded modules in `sys.modules`. If an import request is made, it checks this dictionary first.

# Q3: What happens if you modify `sys.modules`?
# A: You can force Python to reload a module by deleting its entry from `sys.modules` and re-importing, 
#    or use `importlib.reload()`.

# Q4: How does PYTHONPATH affect imports?
# A: PYTHONPATH is an environment variable containing a list of paths. Python adds these paths to `sys.path` on startup.

# Q5: What is a Namespace Package?
# A: A package spread across multiple directories on disk, without an `__init__.py`, allowing multiple packages 
#    to share a single namespace.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a function that finds the absolute file path of an imported module.

def find_module_path(module_name: str) -> str:
    """Returns the file path of a loaded module."""
    mod = sys.modules.get(module_name)
    if mod:
        # built-in modules might not have __file__
        return getattr(mod, '__file__', 'Built-in or dynamically generated (no __file__)')
    return "Module not loaded."

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Write a script that checks if a specific directory is in `sys.path`.
# If not, add it, simulate an import by adding a dummy entry to `sys.modules`, 
# prove it's loaded, and then clean everything up.

def run_import_simulation():
    fake_path = "/fake/custom/path"
    fake_module_name = "super_custom_module"
    
    print("--- Starting Simulation ---")
    sys.path.append(fake_path)
    print(f"Added path. sys.path contains fake_path: {fake_path in sys.path}")
    
    # Simulate loading
    sys.modules[fake_module_name] = "This is a mock module object"
    
    # Simulate import
    print(f"Is {fake_module_name} imported? {fake_module_name in sys.modules}")
    
    # Cleanup
    sys.path.remove(fake_path)
    del sys.modules[fake_module_name]
    print("Cleanup complete.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The import system relies heavily on `sys.path` for discovery and `sys.modules` for caching.
# - Name shadowing (naming a file math.py) is a common beginner error caused by sys.path resolution order.
# - Try to rely on standard project structures rather than hacking sys.path.

if __name__ == "__main__":
    show_sys_path()
    dynamic_path_modification()
    import json
    print(f"Path to json module: {find_module_path('json')}")
    run_import_simulation()
