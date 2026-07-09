"""
Topic: *args and **kwargs
Chapter: 7
Level: Intermediate

Description:
    *args and **kwargs allow a function to accept an arbitrary number of arguments. 
    *args collects positional arguments into a tuple, while **kwargs collects keyword arguments into a dictionary.

Real-Life Analogy:
    Imagine an all-you-can-eat buffet plate. *args is when you grab a random number of different food items (positional). **kwargs is when you make custom requests like "sauce: extra, spice: mild, temperature: hot" (keyword mappings).

Key Concepts:
    - *args for variable-length positional arguments
    - **kwargs for variable-length keyword arguments
    - Unpacking arguments using * and **
    - Order of parameters in function signatures
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# *args: Collects extra positional arguments into a tuple named 'args'
def print_all_items(*args) -> None:
    """Prints all positional arguments passed to the function."""
    print("Items:", args)

# **kwargs: Collects extra keyword arguments into a dictionary named 'kwargs'
def print_all_properties(**kwargs) -> None:
    """Prints all keyword arguments passed to the function."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Summing any number of values using *args
def sum_all(*numbers: float) -> float:
    """Returns the sum of all provided numbers."""
    return sum(numbers)

# Example 2: Creating a dynamic HTML tag using **kwargs
def create_html_tag(tag: str, text: str, **attributes: str) -> str:
    """Generates an HTML tag with arbitrary attributes."""
    attr_str = "".join([f' {k}="{v}"' for k, v in attributes.items()])
    return f"<{tag}{attr_str}>{text}</{tag}>"

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 1: Using both *args and **kwargs together
def log_request(method: str, url: str, *args, **kwargs) -> None:
    """Simulates a network request logger."""
    print(f"[{method}] {url}")
    if args:
        print(f"  Positional Data: {args}")
    if kwargs:
        print(f"  Keyword Data: {kwargs}")

# Example 2: Unpacking arguments from iterables and dictionaries
def calculate_box_volume(length: float, width: float, height: float) -> float:
    return length * width * height

# We can unpack a list or tuple using *
box_dims = (10, 5, 2)
# volume = calculate_box_volume(*box_dims)

# We can unpack a dictionary using **
box_dict = {"length": 10, "width": 5, "height": 2}
# volume = calculate_box_volume(**box_dict)

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Incorrect parameter order
# The order must be: standard params, *args, default params, **kwargs
# def bad_func(*args, name, **kwargs):  # 'name' becomes a keyword-only argument
#     pass

# Best Practices:
# 1. You don't have to name them 'args' and 'kwargs' (the magic is in the * and **), 
#    but it's a strong community convention. Stick to it.
# 2. Use them when you design APIs or wrapper functions where the exact number 
#    of arguments isn't known in advance.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What type of object is `args` inside a function defined with `*args`?
# A: It is a tuple.

# Q2: What type of object is `kwargs` inside a function defined with `**kwargs`?
# A: It is a dictionary.

# Q3: If a function has `def func(a, b, *args, **kwargs)`, what gets assigned to what in `func(1, 2, 3, 4, x=5)`?
# A: a=1, b=2, args=(3, 4), kwargs={'x': 5}.

# Q4: Can you use names other than 'args' and 'kwargs'?
# A: Yes, `*values` or `**options` are perfectly valid. The `*` and `**` operators 
#    do the work.

# Q5: How do you unpack a dictionary to pass it as keyword arguments?
# A: Prepend the dictionary variable with `**` when calling the function, e.g., `func(**my_dict)`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function `multiply_all` that takes any number of arguments 
# and returns their product. (Return 1 if no args).
def multiply_all(*args: float) -> float:
    result = 1.0
    for num in args:
        result *= num
    return result

# Exercise 2: Write a function `build_profile` that takes `first_name` and `last_name`, 
# and any number of keyword arguments representing profile details.
def build_profile(first_name: str, last_name: str, **user_info) -> dict:
    profile = {"first_name": first_name, "last_name": last_name}
    profile.update(user_info)
    return profile

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: The Ultimate Wrapper
# Write a function `timing_wrapper` that accepts a function name as a string, 
# and any combination of *args and **kwargs. It should print that the function is starting, 
# print the provided arguments, and then say the function is done.
def timing_wrapper(func_name: str, *args, **kwargs) -> None:
    print(f"Starting execution of '{func_name}'...")
    print(f"Arguments: {args}")
    print(f"Keyword Arguments: {kwargs}")
    print(f"Execution of '{func_name}' complete.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `*args` allows passing a variable number of positional arguments (packed into a tuple).
# - `**kwargs` allows passing a variable number of keyword arguments (packed into a dict).
# - The correct order of parameters is: positional, `*args`, keyword-only (or defaults), `**kwargs`.
# - You can also use `*` and `**` to unpack lists and dictionaries into function calls.

if __name__ == "__main__":
    print_all_items(1, 2, "hello", True)
    print_all_properties(color="red", size="large", weight=10.5)
    
    print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
    
    html = create_html_tag("a", "Click Here", href="https://example.com", target="_blank")
    print(f"Generated HTML: {html}")
    
    print("\n--- Logging Request ---")
    log_request("POST", "/api/users", 123, 456, timeout=30, retry=True)
    
    print("\n--- Unpacking ---")
    dims = (5, 5, 5)
    print(f"Volume: {calculate_box_volume(*dims)}")
    
    print("\n--- Exercises & Challenge ---")
    print(f"Product: {multiply_all(2, 3, 4)}")
    print(build_profile("Jane", "Doe", occupation="Engineer", city="Seattle"))
    
    timing_wrapper("process_data", 1, 2, 3, mode="async", verbose=True)
