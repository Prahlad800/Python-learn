"""
Topic: Scope and Namespaces
Chapter: 7
Level: Beginner / Intermediate

Description:
    Scope defines the visibility and lifetime of a variable in your code. Python uses the LEGB rule (Local, Enclosing, Global, Built-in) to resolve names. Understanding scope prevents variable shadowing and unintended side effects.

Real-Life Analogy:
    Think of variables like people with the same name. If you yell "John!" in your house (Local Scope), your brother John answers. If there's no John in your house, you might look in your neighborhood (Global Scope) to find a neighbor named John.

Key Concepts:
    - Local Scope
    - Enclosing (Nonlocal) Scope
    - Global Scope
    - Built-in Scope
    - The `global` and `nonlocal` keywords
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Global Scope: defined at the top level of the script
global_var = "I am global"

def show_scopes():
    # Local Scope: defined inside the function
    local_var = "I am local"
    print(local_var)
    print(global_var) # We can read global variables inside a function

print("--- Section 1 ---")
show_scopes()
# print(local_var) # This would raise a NameError because local_var is not visible here.

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (LEGB RULE)
# ============================================================

print("\n--- Section 2 ---")

# 1. Local (L)
def my_func():
    x = 10 # Local
    print(f"Local x: {x}")

my_func()

# 2. Enclosing (E)
def outer_func():
    y = 20 # Enclosing for inner_func
    def inner_func():
        print(f"Enclosing y read from inner: {y}")
    inner_func()

outer_func()

# 3. Global (G)
z = 30
def another_func():
    print(f"Global z read from func: {z}")

another_func()

# 4. Built-in (B)
# Python has built-in names like `len`, `print`, `Exception`.
# They are always available.
print(f"Built-in len function: {len('hello')}")

# ============================================================
# SECTION 3: ADVANCED USAGE (GLOBAL AND NONLOCAL)
# ============================================================

print("\n--- Section 3 ---")

# Using the `global` keyword to modify a global variable inside a function
counter = 0

def increment_global():
    global counter  # Tells Python we want to modify the global 'counter'
    counter += 1
    print(f"Counter modified inside function: {counter}")

increment_global()
increment_global()
print(f"Counter outside function: {counter}")

# Using the `nonlocal` keyword to modify an enclosing variable
def outer_counter():
    count = 0
    def inner_increment():
        nonlocal count # Modifies the 'count' from outer_counter
        count += 1
        return count
    return inner_increment

my_counter = outer_counter()
print(f"Nonlocal count 1: {my_counter()}")
print(f"Nonlocal count 2: {my_counter()}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Variable Shadowing
x = "Global String"
def shadow_example():
    x = "Local String" # This shadows the global x
    print(x) # Prints "Local String"
# It's best to avoid naming local variables the same as global ones to prevent confusion.

# Mistake 2: Modifying globals without `global` keyword
# count = 0
# def add_count():
#     count += 1  # Raises UnboundLocalError!
# You must declare `global count` first.

# Best Practice: Avoid global variables when possible. Pass values as arguments
# and return results. It makes functions pure and easier to test.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the LEGB rule in Python?
# A: It's the order Python searches for variable names: Local, Enclosing, Global, Built-in.

# Q2: When do you use the `global` keyword?
# A: When you need to reassign or modify a globally scoped immutable variable from within a local scope.

# Q3: What is the difference between `global` and `nonlocal`?
# A: `global` targets variables at the module level. `nonlocal` targets variables in an outer enclosing function's scope (but not global).

# Q4: What happens if you read a global variable without the `global` keyword?
# A: It works perfectly fine. You only need `global` if you want to reassign it.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Fix the code below so it prints 5 instead of raising an error.
total = 0
def add_to_total(amount):
    global total
    total += amount

add_to_total(5)
print(f"Total is: {total}")

# Exercise 2: Use nonlocal to maintain state.
def make_multiplier(factor):
    current = 1
    def multiply():
        nonlocal current
        current *= factor
        return current
    return multiply

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Create a simple bank account using closures and scope.
# Write a function `create_account(initial_balance)` that returns two functions: `deposit(amount)` and `withdraw(amount)`.
# They should modify the `initial_balance` using `nonlocal`.

def create_account(initial_balance):
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
        
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        return "Insufficient funds"
        
    return deposit, withdraw

print("\n--- Mini Challenge ---")
dep, wdraw = create_account(100)
print(f"Deposited 50: {dep(50)}")
print(f"Withdrew 30: {wdraw(30)}")
print(f"Withdrew 200: {wdraw(200)}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Python uses the LEGB rule to resolve variable scopes.
# - Functions create a local scope. Variables defined inside are not visible outside.
# - You can read outer variables freely, but modifying them requires `global` or `nonlocal`.
# - Use `global` to change module-level variables.
# - Use `nonlocal` to change variables in an enclosing function.
# - Overusing globals makes code harder to maintain; prefer passing arguments.

if __name__ == "__main__":
    pass
