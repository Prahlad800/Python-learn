"""
Topic: Variables and Data Types Practice 1
Chapter: 2
Level: Beginner

Description:
    This file contains basic practice exercises focusing on variables and basic data types.
    It combines declaration, assignment, dynamic typing, and checking types.

Real-Life Analogy:
    Like organizing a toolbox, here you are practicing putting different tools (data) 
    into their correct compartments (variables) and identifying what tool you are holding (type checking).

Key Concepts:
    - Variable assignment
    - Type identification
    - Dynamic typing
    - Basic operations
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def declare_and_inspect() -> None:
    """Practice declaring variables of different types."""
    print("--- Exercise 1: Declare and Inspect ---")
    
    # 1. Create a variable for a book title (String)
    title = "Python Crash Course"
    
    # 2. Create a variable for the number of pages (Integer)
    pages = 544
    
    # 3. Create a variable for the price (Float)
    price = 29.99
    
    # 4. Create a variable for whether it's available (Boolean)
    is_available = True
    
    print(f"Book: {title} | Type: {type(title)}")
    print(f"Pages: {pages} | Type: {type(pages)}")
    print(f"Price: ${price} | Type: {type(price)}")
    print(f"Available: {is_available} | Type: {type(is_available)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def swap_practice() -> None:
    """Practice swapping variables."""
    print("\n--- Exercise 2: Swapping Data ---")
    
    cup_a = "Coffee"
    cup_b = "Tea"
    
    print(f"Before Swap -> Cup A: {cup_a}, Cup B: {cup_b}")
    
    # Swap logic
    cup_a, cup_b = cup_b, cup_a
    
    print(f"After Swap  -> Cup A: {cup_a}, Cup B: {cup_b}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def multiple_assignments() -> None:
    """Practice unpacking and multiple assignment."""
    print("\n--- Exercise 3: Multiple Assignments ---")
    
    # Initializing coordinates to zero
    x = y = z = 0
    print(f"Initial coordinates: x={x}, y={y}, z={z}")
    
    # Unpacking a tuple
    color_data = (255, 128, 0)
    red, green, blue = color_data
    
    print(f"Unpacked Colors -> Red: {red}, Green: {green}, Blue: {blue}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def variable_reassignment() -> None:
    """Demonstrating dynamic typing reassignments."""
    print("\n--- Exercise 4: Dynamic Typing ---")
    
    # Best Practice: Avoid changing a variable's type unless intentionally required.
    # Python allows it, but it can confuse other developers.
    mystery_box = "I contain a string"
    print(f"Mystery box currently holds: {mystery_box}")
    
    mystery_box = 42
    print(f"Mystery box now holds: {mystery_box}")
    
    mystery_box = ["Now", "a", "list"]
    print(f"Mystery box finally holds: {mystery_box}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Can you change the type of a variable in Python after it's declared?
   Answer: Yes, Python is dynamically typed. A variable that points to an int can later point to a string.

2. Is a string mutable or immutable?
   Answer: Immutable.

3. How do you find out the type of a variable dynamically?
   Answer: Using the built-in `type()` function.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Practice on your own:
1. Create a dictionary that stores the properties of a car (make, model, year, is_electric).
2. Unpack a list of 4 names into 4 separate variables.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Calculate BMI using variables."""
    print("\n--- Mini Challenge: BMI Calculator ---")
    
    weight_kg = 70.5
    height_m = 1.75
    
    # BMI formula: weight / (height ^ 2)
    bmi = weight_kg / (height_m ** 2)
    
    print(f"Weight: {weight_kg} kg")
    print(f"Height: {height_m} m")
    print(f"Calculated BMI: {bmi:.2f}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Variables hold data of various types.
- Multiple variables can be assigned at once using unpacking.
- Python variables are dynamically typed.
"""

if __name__ == "__main__":
    declare_and_inspect()
    swap_practice()
    multiple_assignments()
    variable_reassignment()
    mini_challenge()
