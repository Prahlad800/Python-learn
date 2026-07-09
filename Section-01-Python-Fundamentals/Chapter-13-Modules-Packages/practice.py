"""
Topic: Modules and Packages Practice
Chapter: 13
Level: Beginner to Advanced

Description:
    This file serves as a comprehensive practice ground combining concepts of standard libraries, 
    custom module simulation, namespace understanding, and dunder attributes.

Real-Life Analogy:
    This is the final exam or the capstone project. You've learned about all the different tools 
    (modules), how to organize them (packages), and how they interact (namespaces). Now you build 
    a small machine using all of them together.

Key Concepts:
    - Standard library integration
    - Modular architecture thinking
    - Path manipulation
    - System level interactions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import os
import sys
import datetime
import random
import math

def system_info_report():
    """Generates a basic report using standard library modules."""
    print("--- System Info Report ---")
    print(f"OS Platform: {sys.platform}")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 26)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Simulating a math module utility that might exist in a separate package.

class GeometryLib:
    """Mock library for geometry calculations."""
    
    @staticmethod
    def circle_area(radius: float) -> float:
        return math.pi * (radius ** 2)
        
    @staticmethod
    def hypotenuse(a: float, b: float) -> float:
        return math.sqrt(a**2 + b**2)

def use_geometry_lib():
    print(f"Area of circle (r=5): {GeometryLib.circle_area(5):.2f}")
    print(f"Hypotenuse (3, 4): {GeometryLib.hypotenuse(3, 4):.2f}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Safe dynamic execution context (simulating a plugin system)
# Warning: In real life, `eval` or `exec` with untrusted input is dangerous.

def execute_plugin(plugin_code: str):
    """Executes a string of code in an isolated namespace dictionary."""
    plugin_namespace = {}
    try:
        exec(plugin_code, {}, plugin_namespace)
        if 'run' in plugin_namespace:
            print("Executing plugin run() function:")
            plugin_namespace['run']()
        else:
            print("Plugin loaded but no run() function found.")
    except Exception as e:
        print(f"Plugin execution failed: {e}")

plugin_str = """
def run():
    print("Hello from the dynamic plugin!")
"""

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Catching generalized Exceptions when importing.
# If you do `except Exception: pass` around an import, you might hide real SyntaxErrors or NameErrors.
# Best Practice: Catch `ImportError` specifically.

def safe_import_example():
    try:
        import non_existent_module
    except ImportError as e:
        print(f"Caught an import error gracefully: {e}")
    except Exception as e:
        print("This shouldn't happen for a simple import failure.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How do you check which modules are built into the Python interpreter?
# A: By checking `sys.builtin_module_names`.

# Q2: Can you have a package and a module with the same name in the same directory?
# A: The OS won't allow a file (module.py) and a folder (module/) to share the exact same name without extension issues, 
#    but if `foo.py` and `foo/` exist, Python prioritizes the package (`foo/`) if it has `__init__.py`.

# Q3: What is Monkey Patching?
# A: Dynamically modifying a class or module at runtime (e.g., replacing a function in an imported module with your own).

# Q4: How do you prevent a module from being imported?
# A: You can't strictly prevent it, but you can raise an exception at the top of the file, or not distribute it.

# Q5: Is there a performance penalty for importing a module multiple times?
# A: No, Python caches it in `sys.modules`. Subsequent imports are essentially just dictionary lookups.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Create a function that shuffles a list using `random` and measures the time it takes using `time`.
import time

def performance_test():
    data = list(range(100000))
    start_time = time.time()
    random.shuffle(data)
    end_time = time.time()
    
    print(f"Shuffled 100,000 items in {end_time - start_time:.4f} seconds.")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Create a "Module Analyzer" function.
# It takes a module object as an argument and prints:
# 1. The module's name
# 2. The module's file path (if available)
# 3. The number of functions/classes defined in it.

def module_analyzer(mod):
    import inspect
    print(f"--- Analyzing Module: {mod.__name__} ---")
    
    if hasattr(mod, '__file__'):
        print(f"File Path: {mod.__file__}")
    else:
        print("File Path: Built-in or dynamic")
        
    members = inspect.getmembers(mod)
    functions = [m for m in members if inspect.isfunction(m[1])]
    classes = [m for m in members if inspect.isclass(m[1])]
    
    print(f"Number of Functions: {len(functions)}")
    print(f"Number of Classes: {len(classes)}")

def run_challenge():
    module_analyzer(math)
    module_analyzer(os)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Mastering modules and packages is key to building scalable Python applications.
# - Standard libraries provide immense power out of the box.
# - Understanding import mechanics, namespaces, and paths prevents frustrating bugs.
# - Keep code organized, avoid global state, and document your public APIs.

if __name__ == "__main__":
    system_info_report()
    use_geometry_lib()
    execute_plugin(plugin_str)
    safe_import_example()
    performance_test()
    run_challenge()
