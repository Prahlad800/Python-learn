"""
Topic: Functions
Chapter: 7
Level: Beginner

Description:
    Functions are reusable blocks of code designed to perform a single, related action. They help organize code, make it more readable, and reduce repetition.

Real-Life Analogy:
    Think of a function as a coffee machine. You provide the inputs (water and coffee beans), the machine performs a specific process (brewing), and it gives you an output (a cup of coffee).

Key Concepts:
    - Defining functions using 'def'
    - Returning values using 'return'
    - Returning multiple values
    - The 'pass' statement for empty functions
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Basic function definition
def greet_user(name: str) -> None:
    """Prints a greeting message."""
    print(f"Hello, {name}! Welcome to Python programming.")

# Function that returns a value
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

# Function with no parameters and no return
def display_menu() -> None:
    """Displays a simple menu."""
    print("1. Start")
    print("2. Load")
    print("3. Exit")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Calculating area of a rectangle
def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width

# Example 2: Checking if a number is even
def is_even(number: int) -> bool:
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

# Example 3: Returning multiple values (as a tuple)
def get_user_info() -> tuple[str, int, str]:
    """Returns a user's name, age, and occupation."""
    name = "Alice"
    age = 30
    occupation = "Engineer"
    return name, age, occupation

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 1: Functions containing functions (Nested briefly)
def math_operations(a: float, b: float) -> dict[str, float]:
    """Performs multiple math operations and returns a dictionary."""
    def add() -> float:
        return a + b
    
    def multiply() -> float:
        return a * b
        
    return {
        "addition": add(),
        "multiplication": multiply()
    }

# Example 2: Using pass for unimplemented functions
def future_feature() -> None:
    """This function is planned for a future release."""
    pass

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to return a value, which results in returning None
def wrong_add(a: int, b: int) -> None:
    result = a + b
    # Missing 'return result'

# Mistake: Putting code after a return statement
def unreachable_code() -> str:
    return "Done"
    print("This will never be executed") # Unreachable

# Best Practices:
# 1. Functions should do one thing and do it well (Single Responsibility Principle).
# 2. Keep functions short and readable.
# 3. Use descriptive names (verbs are good for functions, e.g., 'calculate_total').
# 4. Use type hints to clarify expected inputs and outputs.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the purpose of the 'return' statement in Python?
# A: It exits the function and optionally passes back an expression to the caller. 
#    If no expression is provided, it returns None.

# Q2: Can a function return multiple values in Python?
# A: Yes, Python can return multiple values separated by commas. These are 
#    automatically packed into a tuple.

# Q3: What happens if a function doesn't have a return statement?
# A: The function implicitly returns the special value 'None'.

# Q4: What is the 'pass' statement used for in functions?
# A: 'pass' is a null operation. It's used as a placeholder when a statement is 
#    syntactically required but no code needs to be executed yet.

# Q5: Are functions objects in Python?
# A: Yes, everything in Python is an object, including functions. They can be 
#    assigned to variables, passed as arguments, and returned from other functions.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a function called `celsius_to_fahrenheit` that takes a temperature 
# in Celsius and returns it in Fahrenheit. (Hint: F = C * 9/5 + 32)
def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32

# Exercise 2: Write a function `find_max` that takes a list of numbers and returns 
# the largest number without using the built-in max() function.
def find_max(numbers: list[int]) -> int | None:
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Exercise 3: Write a function `count_vowels` that takes a string and returns the 
# number of vowels (a, e, i, o, u) in it.
def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Password Validator
# Write a function that checks if a password is valid.
# A valid password must:
# 1. Be at least 8 characters long
# 2. Contain at least one number
# 3. Contain at least one uppercase letter
def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    
    has_num = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    
    return has_num and has_upper

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Functions are defined using the `def` keyword.
# - They encapsulate reusable code blocks.
# - The `return` statement sends data back to the caller.
# - Functions without a return statement implicitly return `None`.
# - Multiple values can be returned as tuples.
# - Type hints make function definitions clearer.

if __name__ == "__main__":
    print("--- Function Execution ---")
    greet_user("Student")
    print(f"5 + 7 = {add_numbers(5, 7)}")
    
    name, age, job = get_user_info()
    print(f"Info: {name}, {age}, {job}")
    
    print(f"Area: {calculate_rectangle_area(10, 5)}")
    print(f"Is 4 even? {is_even(4)}")
    
    print(f"Math operations on 10 and 2: {math_operations(10, 2)}")
    
    print("\n--- Challenge ---")
    pwd1 = "weak"
    pwd2 = "StrongPass1"
    print(f"Password '{pwd1}' valid: {validate_password(pwd1)}")
    print(f"Password '{pwd2}' valid: {validate_password(pwd2)}")
