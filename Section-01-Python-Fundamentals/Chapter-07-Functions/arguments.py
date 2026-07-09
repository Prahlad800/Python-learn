"""
Topic: Function Arguments
Chapter: 7
Level: Beginner

Description:
    Arguments (or parameters) allow you to pass data into functions. Python supports multiple ways to pass arguments, including positional arguments, keyword arguments, and a mix of both.

Real-Life Analogy:
    If a function is a blender, arguments are the ingredients you put into it. Positional arguments are like throwing ingredients in order, while keyword arguments are like explicitly labeling "milk = 1 cup, bananas = 2".

Key Concepts:
    - Parameters vs Arguments
    - Positional Arguments
    - Keyword Arguments
    - Mixing positional and keyword arguments
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Parameters are defined in the function signature
def display_profile(name: str, age: int, city: str) -> None:
    """Displays a user profile."""
    print(f"Name: {name}, Age: {age}, City: {city}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Positional Arguments
# Arguments are mapped to parameters based on their position
def calculate_salary(hours: float, rate: float) -> float:
    return hours * rate

# Example 2: Keyword Arguments
# Arguments are mapped by parameter name, order doesn't matter
def create_booking(hotel: str, nights: int, guest_name: str) -> str:
    return f"Booking for {guest_name} at {hotel} for {nights} nights."

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 1: Mixing positional and keyword arguments
# Positional arguments MUST come before keyword arguments
def configure_server(hostname: str, port: int, os_type: str) -> None:
    print(f"Server {hostname} running {os_type} on port {port}")

# Example 2: Keyword-only arguments (using *)
# Any argument after * MUST be passed as a keyword argument
def secure_login(username: str, *, token: str, require_mfa: bool) -> bool:
    print(f"Authenticating {username} with token {token[:3]}... MFA: {require_mfa}")
    return True

# Example 3: Positional-only arguments (using /) (Python 3.8+)
def power(base: int, exponent: int, /) -> int:
    return base ** exponent

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Putting keyword arguments before positional arguments
# def example_func(a, b): pass
# example_func(a=1, 2)  # SyntaxError: positional argument follows keyword argument

# Mistake: Providing multiple values for the same parameter
# display_profile("Alice", 25, name="Bob") # TypeError

# Best Practices:
# 1. Use keyword arguments when calling functions with many parameters to improve readability.
# 2. Use positional-only or keyword-only arguments to enforce how a function should be called.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between a parameter and an argument?
# A: A parameter is the variable listed inside the parentheses in the function 
#    definition. An argument is the actual value passed to the function when it is called.

# Q2: Can you mix positional and keyword arguments? What is the rule?
# A: Yes, but positional arguments must always precede keyword arguments in the function call.

# Q3: How do you enforce an argument to be passed only as a keyword argument?
# A: By placing a single asterisk `*` before it in the function signature.

# Q4: What does the `/` operator do in a function signature?
# A: Introduced in Python 3.8, it specifies that all parameters before the `/` 
#    are positional-only arguments and cannot be passed as keyword arguments.

# Q5: Why might you want to use keyword-only arguments?
# A: To make code more explicit and readable, especially for boolean flags or 
#    optional parameters where the meaning might not be obvious from position alone.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a function `build_url` with parameters `protocol`, `domain`, and `path`.
# Call it once using only positional arguments, and once using only keyword arguments.
def build_url(protocol: str, domain: str, path: str) -> str:
    return f"{protocol}://{domain}/{path}"

# Exercise 2: Write a function `describe_pet` that takes `animal_type` and `pet_name`.
# Make `pet_name` a keyword-only argument.
def describe_pet(animal_type: str, *, pet_name: str) -> str:
    return f"I have a {animal_type} named {pet_name}."

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Shopping Cart Item Builder
# Create a function that accepts `item_id` (positional only), `name` (standard), 
# and `price` & `quantity` (keyword only).
def add_to_cart(item_id: int, /, name: str, *, price: float, quantity: int) -> dict:
    return {
        "id": item_id,
        "name": name,
        "total": price * quantity
    }

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Arguments provide data to functions.
# - Positional arguments rely on the order in which they are passed.
# - Keyword arguments explicitly name the parameter, ignoring order.
# - Positional arguments must appear before keyword arguments in calls.
# - Python supports positional-only (`/`) and keyword-only (`*`) parameters.

if __name__ == "__main__":
    # Positional
    display_profile("John", 28, "New York")
    
    # Keyword
    print(create_booking(guest_name="Sarah", nights=3, hotel="Grand Plaza"))
    
    # Mixed
    configure_server("db-01", os_type="Linux", port=5432)
    
    # Keyword only
    secure_login("admin", token="abc123xyz", require_mfa=True)
    
    # Positional only
    print(f"2^3 = {power(2, 3)}")
    
    # Exercises & Challenge
    print(build_url("https", "example.com", "about"))
    print(build_url(domain="example.com", path="contact", protocol="https"))
    print(describe_pet("dog", pet_name="Buddy"))
    print(add_to_cart(101, "Laptop", price=999.99, quantity=2))
