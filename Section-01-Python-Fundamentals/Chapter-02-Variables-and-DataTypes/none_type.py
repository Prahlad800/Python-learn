"""
Topic: None Type
Chapter: 2
Level: Beginner

Description:
    The `None` keyword in Python is used to define a null value, or no value at all.
    None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) 
    and only None can be None. It is often used as a placeholder or a default value for function arguments.

Real-Life Analogy:
    Imagine filling out a form. If a question asks for your "Middle Name" and you don't have one, 
    you leave it blank. You didn't answer "0" or "False", you simply provided 'nothing'. 
    In Python, that concept of 'nothingness' or 'absence of a value' is represented by `None`.

Key Concepts:
    - The None keyword
    - NoneType
    - Checking for None using `is`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_none() -> None:
    """Demonstrates basic usage of None."""
    print("--- Basic NoneType ---")
    
    # Assigning None to a variable
    user_middle_name = None
    
    print(f"Middle Name: {user_middle_name}")
    print(f"Type of user_middle_name: {type(user_middle_name)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def none_as_placeholder() -> None:
    """Shows how None is used as an initial placeholder for data yet to be retrieved."""
    print("\n--- Practical Examples ---")
    
    # We might not know the user's score until they finish a game
    final_score = None
    
    # Game completes...
    final_score = 95
    
    if final_score is not None:
        print(f"Game over! Your score is: {final_score}")
    else:
        print("Game still in progress...")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def function_returns_none() -> None:
    """Demonstrates that functions return None implicitly if no return statement is given."""
    print("\n--- Advanced Usage ---")
    
    # A function that performs an action but doesn't return data
    def log_message(msg: str):
        print(f"LOG: {msg}")
        # Implicitly returns None at the end
        
    result = log_message("System started.")
    print(f"The function returned: {result}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Discusses the difference between == and is when checking for None."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    val = None
    
    # Pitfall: Using == to check for None
    # While `val == None` works, it is discouraged because custom objects can override __eq__ 
    # to return True even if they aren't actually None.
    
    # Best Practice: Always use the `is` operator to check for None.
    # The `is` operator checks for object identity (memory address). 
    # Since None is a singleton (only one exists in memory), `is` is the safest and most Pythonic way.
    if val is None:
        print("Correct way to check for None.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. What is `None` in Python?
   Answer: `None` represents the absence of a value. It is an object of its own datatype, `NoneType`.

2. Is `None` equal to False or 0?
   Answer: No. `None == False` is False, and `None == 0` is False. However, `None` evaluates to False in a boolean context (it is "falsy").

3. Why should you use `is None` instead of `== None`?
   Answer: `is` checks for object identity. Because there is only one `None` object in a Python process (it's a singleton), `is` guarantees an accurate check, bypassing any custom equality logic (`__eq__`) an object might have.

4. What does a function return if there is no `return` statement?
   Answer: It returns `None`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create a variable `winner` set to None. Write an if-statement checking if `winner is None` and print a message if true.
Exercise 2: Write a function `greet(name)` that prints "Hello, [name]". Assign its result to a variable and print the variable to see that it is None.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Mini challenge using None for optional parameters."""
    print("\n--- Mini Challenge ---")
    
    # Using None to handle optional configurations
    def connect_to_server(ip: str, port=None):
        if port is None:
            port = 80 # Default to 80 if no port provided
        print(f"Connecting to {ip} on port {port}...")
        
    connect_to_server("192.168.1.1")
    connect_to_server("10.0.0.5", 8080)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- `None` represents the absence of a value or a null value.
- It is of type `NoneType` and evaluates to False in logical conditions.
- Always use `is None` or `is not None` when checking variables against None.
- Functions without an explicit return statement will implicitly return None.
"""

if __name__ == "__main__":
    basic_none()
    none_as_placeholder()
    function_returns_none()
    common_mistakes()
    mini_challenge()
