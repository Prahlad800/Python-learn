"""
Topic: Namespace and Scope in Modules
Chapter: 13
Level: Intermediate

Description:
    A namespace is a system that has a unique name for each and every object in Python. 
    Scope refers to the coding region from which a particular Python object is accessible. 
    Modules act as distinct namespaces, preventing naming conflicts between different parts of a program.

Real-Life Analogy:
    Imagine two different schools. Both have a student named "John Smith". Inside School A (Module A), 
    saying "John Smith" refers to their student. Inside School B (Module B), it refers to someone else. 
    To specify, you say "School A's John Smith". Modules keep variable names separated just like schools do.

Key Concepts:
    - LEGB Rule (Local, Enclosing, Global, Built-in)
    - Module namespace
    - `globals()` and `locals()`
    - Naming conflicts
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Every module has its own global namespace.
# Variables defined at the top level of a module are in that module's global namespace.

module_variable = "I am global to this module."

def show_module_variable():
    print(module_variable)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# The LEGB Rule:
# Local -> Enclosing -> Global -> Built-in

# 1. Built-in
# print, len, Exception

# 2. Global (Module Level)
x = "Global X"

def outer_function():
    # 3. Enclosing
    x = "Enclosing X"
    
    def inner_function():
        # 4. Local
        x = "Local X"
        print(f"Inside inner: {x}")
        
    inner_function()
    print(f"Inside outer: {x}")

print(f"Module level: {x}")
outer_function()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# globals() and locals()
# These functions return dictionaries representing the current namespaces.

def examine_namespaces():
    local_var = 42
    
    print("--- Locals ---")
    local_dict = locals()
    print(f"local_var exists in locals: {'local_var' in local_dict}")
    
    print("--- Globals ---")
    global_dict = globals()
    print(f"module_variable exists in globals: {'module_variable' in global_dict}")

# Modifying globals from within a function requires the `global` keyword.
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
print(f"Counter is now: {counter}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Modifying global variables extensively.
# It makes code hard to test and reason about because state can change from anywhere.
# Best Practice: Avoid global variables. Pass variables as arguments and return results.

# Mistake 2: Shadowing built-ins.
# Example: `list = [1, 2, 3]`. Now you can't use the `list()` constructor in that namespace.
# Best Practice: Never use built-in names (str, list, dict, type, id) as variable names.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a namespace in Python?
# A: A mapping from names to objects, implemented as dictionaries under the hood.

# Q2: Explain the LEGB rule.
# A: It defines the order in which Python resolves names: Local, Enclosing (non-local), Global, Built-in.

# Q3: If you import `math`, does it merge its namespace with yours?
# A: No. `import math` creates a single name `math` in your namespace. You access its contents via `math.pi`.
#    However, `from math import pi` brings `pi` directly into your namespace.

# Q4: What happens if two modules define the same variable name and you import both?
# A: If you use `import moduleA` and `import moduleB`, there is no conflict (`moduleA.var` vs `moduleB.var`). 
#    If you use `from moduleA import var` and `from moduleB import var`, the second one overwrites the first.

# Q5: What does the `global` keyword do?
# A: It allows a function to modify a variable defined at the module's global scope, rather than creating a new local variable.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Define a global variable `theme = 'light'`. 
# Create a function that attempts to change it to 'dark' without the `global` keyword (shadowing).
# Create another function that actually changes it using the `global` keyword.

theme = 'light'

def shadow_theme():
    theme = 'dark' # Local variable
    print(f"Inside shadow_theme: {theme}")

def update_theme():
    global theme
    theme = 'dark' # Modifies global
    print(f"Inside update_theme: {theme}")

print(f"Initial theme: {theme}")
shadow_theme()
print(f"After shadow_theme: {theme}")
update_theme()
print(f"After update_theme: {theme}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Write a script that deliberately creates a name collision by redefining a built-in function locally, 
# then uses the `builtins` module to access the original function.

def run_namespace_challenge():
    import builtins
    
    # Shadowing the built-in len
    def len(item):
        return "Haha, nope!"
        
    my_list = [1, 2, 3]
    
    print(f"Using shadowed len: {len(my_list)}")
    print(f"Using original len: {builtins.len(my_list)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Namespaces map names to objects, keeping modules isolated.
# - Python resolves names using the LEGB rule (Local, Enclosing, Global, Built-in).
# - Avoid extensive use of global variables.
# - Be careful not to shadow built-in functions or variables.

if __name__ == "__main__":
    show_module_variable()
    examine_namespaces()
    run_namespace_challenge()
