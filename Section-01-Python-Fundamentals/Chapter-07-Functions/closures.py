"""
Topic: Closures
Chapter: 7
Level: Intermediate / Advanced

Description:
    A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Closures occur when a nested function references a value in its enclosing environment.

Real-Life Analogy:
    Imagine a backpack. A factory function creates the backpack and packs it with certain items (variables). When the factory gives you the backpack (the inner function), you can open it later and still access the items inside, even though you left the factory a long time ago.

Key Concepts:
    - Nested functions
    - Enclosing scope
    - Data hiding and encapsulation
    - Function factories
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def outer_function(msg: str):
    # msg is an enclosing variable
    
    def inner_function():
        # inner_function remembers 'msg' even after outer_function finishes
        print(f"The message is: {msg}")
        
    return inner_function  # Returning the function object, not calling it

# Creating a closure
my_closure = outer_function("Hello from Closure!")

# Calling the closure later
print("--- Section 1 ---")
my_closure()

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

print("\n--- Section 2 ---")

# Example 1: Multiplier Factory
def multiplier_factory(n: int):
    def multiplier(x: int) -> int:
        return x * n
    return multiplier

times_two = multiplier_factory(2)
times_five = multiplier_factory(5)

print(f"10 times 2: {times_two(10)}")
print(f"10 times 5: {times_five(10)}")

# Example 2: HTML Tag Generator
def html_tag(tag: str):
    def wrap_text(msg: str):
        return f"<{tag}>{msg}</{tag}>"
    return wrap_text

print_h1 = html_tag("h1")
print_p = html_tag("p")

print(print_h1("Welcome to Closures"))
print(print_p("This is a paragraph inside a closure."))

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

print("\n--- Section 3 ---")

# Example 1: Stateful Closures using `nonlocal`
def make_averager():
    count = 0
    total = 0
    
    def averager(new_value: float) -> float:
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
        
    return averager

avg = make_averager()
print(f"Avg of 10: {avg(10)}")
print(f"Avg of 20 (now 10+20): {avg(20)}")
print(f"Avg of 30 (now 10+20+30): {avg(30)}")

# Inspecting closure contents
print("Closure variables:", avg.__code__.co_freevars)
print("Closure cell contents:", [cell.cell_contents for cell in avg.__closure__])

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Late Binding in Loops
# Creating closures inside a loop without binding the loop variable properly.
def create_multipliers():
    # This will NOT work as expected; all functions will use the final value of i (which is 4)
    return [lambda x: i * x for i in range(5)]

bad_mults = create_multipliers()
print("Late binding issue:", bad_mults[2](10)) # Returns 40, not 20!

# Correct way using default arguments to force early binding:
def create_multipliers_correct():
    return [lambda x, i=i: i * x for i in range(5)]

good_mults = create_multipliers_correct()
print("Correct binding:", good_mults[2](10)) # Returns 20

# Best Practice: Use closures for data hiding instead of classes if you only have one method.
# It uses less memory and keeps code concise.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What defines a closure in Python?
# A: A closure is a nested function that captures and remembers variables from its enclosing scope, even after the outer function has returned.

# Q2: How does Python implement closures internally?
# A: Python stores captured variables in an attribute called `__closure__` which contains a tuple of cell objects.

# Q3: When should you use a closure instead of a class?
# A: When you need to maintain state but only require a single method (like a callback or factory). If you need multiple methods, a class is better.

# Q4: What does the `nonlocal` keyword do in the context of a closure?
# A: It allows the inner function to reassign or modify a variable defined in the enclosing scope, making the closure stateful.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a closure `make_counter` that starts at a given value and increments by 1 each time it's called.
def make_counter(start: int = 0):
    count = start
    def increment():
        nonlocal count
        current = count
        count += 1
        return current
    return increment

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Build a "logger" closure. 
# `setup_logger(level)` should take a level string (e.g., "INFO", "ERROR")
# and return a function that takes a message and prints "[LEVEL]: message".
def setup_logger(level: str):
    def log_message(msg: str):
        print(f"[{level.upper()}]: {msg}")
    return log_message

print("\n--- Mini Challenge ---")
info_logger = setup_logger("info")
error_logger = setup_logger("error")

info_logger("System booted successfully.")
error_logger("Failed to connect to database.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Closures are nested functions that remember their enclosing scope.
# - They are useful for function factories and data encapsulation.
# - They can replace simple classes by keeping state in enclosing variables.
# - Use the `nonlocal` keyword if the inner function needs to modify the captured state.
# - Beware of late binding when creating closures inside loops.

if __name__ == "__main__":
    pass
