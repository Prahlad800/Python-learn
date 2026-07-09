"""
Topic: Variables
Chapter: 2
Level: Beginner

Description:
    Variables are fundamental building blocks in Python used to store data values. They act as named 
    containers that hold information, which can be referenced and manipulated throughout your code.
    In Python, variables are created dynamically when you assign a value to them.

Real-Life Analogy:
    Think of a variable as a labeled storage box. The label is the variable name, and what you 
    put inside the box is the value. You can change the contents of the box whenever you want, 
    but the label remains the same, helping you find it easily.

Key Concepts:
    - Variable Declaration and Assignment
    - Dynamic Typing
    - Naming Conventions (Snake Case)
    - Multiple Assignments
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_variables() -> None:
    """Demonstrates basic variable creation and assignment."""
    print("--- Basic Variables ---")
    
    # Declaring an integer variable
    user_age: int = 25
    print(f"Age: {user_age}")
    
    # Declaring a string variable
    user_name: str = "Alice"
    print(f"Name: {user_name}")
    
    # Python is dynamically typed; you don't need to specify the type
    score = 98.5
    print(f"Score: {score} (Type: {type(score).__name__})")
    
    # Variables can be updated with new values
    score = 100.0
    print(f"Updated Score: {score}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples() -> None:
    """Shows practical use cases of variables in calculations."""
    print("\n--- Practical Examples ---")
    
    # Calculating the area of a rectangle
    length: float = 10.5
    width: float = 5.0
    area: float = length * width
    print(f"Rectangle with length {length} and width {width} has an area of {area}")
    
    # Multiple assignment
    x, y, z = 1, 2, 3
    print(f"Coordinates: x={x}, y={y}, z={z}")
    
    # Assigning the same value to multiple variables
    a = b = c = 0
    print(f"Initialized multiple variables to zero: a={a}, b={b}, c={c}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage() -> None:
    """Demonstrates advanced variable concepts like swapping and global variables."""
    print("\n--- Advanced Usage ---")
    
    # Swapping variables without a temporary variable
    first_val = 10
    second_val = 20
    print(f"Before Swap: first={first_val}, second={second_val}")
    
    first_val, second_val = second_val, first_val
    print(f"After Swap: first={first_val}, second={second_val}")
    
    # Unpacking a list or tuple into variables
    user_info = ["Bob", 30, "Developer"]
    name, age, profession = user_info
    print(f"Unpacked Data -> Name: {name}, Age: {age}, Profession: {profession}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes_and_best_practices() -> None:
    """Highlights variable naming pitfalls and best practices."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    # Pitfall: Starting with a number (e.g., 1st_place = "John") - SyntaxError
    # Correction: Use letters or underscores first
    first_place = "John"
    
    # Pitfall: Using reserved keywords as variable names (e.g., class = 5) - SyntaxError
    # Correction: Append an underscore if necessary
    class_ = 5
    
    # Best Practice: Use snake_case for variable names
    is_user_active = True
    
    # Best Practice: Use descriptive names rather than vague ones
    # Bad: d = 5
    # Good: days_until_deadline = 5
    
    print("Variables should be descriptive and use snake_case formatting.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Are variables in Python statically typed or dynamically typed?
   Answer: Python variables are dynamically typed. The type of a variable is inferred at runtime and can change if reassigned.

2. How do you swap the values of two variables in a single line?
   Answer: a, b = b, a

3. What are the rules for naming a variable in Python?
   Answer: Must start with a letter or underscore, cannot start with a number, can only contain alphanumeric characters and underscores, and cannot be a reserved keyword.

4. How can you unpack a tuple containing 3 elements into variables?
   Answer: var1, var2, var3 = my_tuple

5. What happens if you try to use a variable before assigning a value to it?
   Answer: Python raises a NameError.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Create variables for your favorite movie, its release year, and its IMDb rating. Print them in a single formatted string.
Exercise 2: Swap the values of three variables a, b, c such that a gets b, b gets c, and c gets a.
Exercise 3: Extract the first and last name from a list ["Jane", "Doe"] using unpacking.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Mini challenge combining multiple concepts."""
    print("\n--- Mini Challenge ---")
    
    # Simulate a shopping cart item setup using variable unpacking and calculation
    item_data = ("Wireless Mouse", 25.99, 2)
    item_name, item_price, item_quantity = item_data
    
    total_cost = item_price * item_quantity
    print(f"Purchased {item_quantity}x {item_name}(s) at ${item_price} each.")
    print(f"Total Cost: ${total_cost:.2f}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Variables are named containers for storing data.
- Python is dynamically typed; types are inferred at runtime.
- Variable names must follow specific rules and conventions (snake_case).
- Multiple assignment and unpacking are powerful Python features.
"""

if __name__ == "__main__":
    basic_variables()
    practical_examples()
    advanced_usage()
    common_mistakes_and_best_practices()
    mini_challenge()
