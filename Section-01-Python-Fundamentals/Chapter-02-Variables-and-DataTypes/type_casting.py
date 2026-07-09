"""
Topic: Type Casting
Chapter: 2
Level: Beginner

Description:
    Type casting (or type conversion) is the process of converting a value from one data type to another. 
    In Python, this can be done implicitly by the interpreter or explicitly by the programmer using built-in 
    functions like int(), float(), str(), etc.

Real-Life Analogy:
    Imagine you have a price tag written in Euros (String), but your cash register only calculates in Dollars (Float). 
    You need a currency exchange service to "convert" the Euros into a usable Dollar amount before you can do math on it. 
    Type casting is that exchange service for data.

Key Concepts:
    - Implicit Type Conversion (Automatic)
    - Explicit Type Conversion (Manual)
    - Functions: int(), float(), str(), bool(), list(), tuple(), set()
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def explicit_casting() -> None:
    """Demonstrates explicit type conversion using built-in functions."""
    print("--- Explicit Type Casting ---")
    
    # String to Integer
    str_num = "42"
    int_num = int(str_num)
    print(f"String '{str_num}' to Integer: {int_num}, Type: {type(int_num)}")
    
    # Integer to Float
    float_num = float(int_num)
    print(f"Integer {int_num} to Float: {float_num}, Type: {type(float_num)}")
    
    # Float to String
    str_val = str(float_num)
    print(f"Float {float_num} to String: '{str_val}', Type: {type(str_val)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_casting() -> None:
    """Shows practical uses of type casting, especially with user input simulations."""
    print("\n--- Practical Examples ---")
    
    # Simulating reading an age from a text file or input (which is always a string)
    input_age_str = "25"
    
    # We must cast it to an int to perform math
    age_next_year = int(input_age_str) + 1
    print(f"Age next year will be: {age_next_year}")
    
    # Converting a string of numbers separated by space to a list of integers
    numbers_str = "10 20 30"
    string_list = numbers_str.split()
    # Using list comprehension for bulk casting
    int_list = [int(num) for num in string_list]
    print(f"String '{numbers_str}' converted to int list: {int_list}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_casting() -> None:
    """Demonstrates boolean casting and sequence conversions."""
    print("\n--- Advanced Usage ---")
    
    # Truthiness / Boolean Casting
    # Any non-zero number or non-empty string is True. 0, None, and empty collections are False.
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool('Hello'): {bool('Hello')}")
    print(f"bool(''): {bool('')}")
    print(f"bool([]): {bool([])}")
    
    # Sequence Conversions
    my_list = [1, 2, 2, 3]
    # List to Set (removes duplicates automatically)
    my_set = set(my_list)
    print(f"List {my_list} to Set: {my_set}")
    
    # Set to Tuple
    my_tuple = tuple(my_set)
    print(f"Set {my_set} to Tuple: {my_tuple}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Discusses ValueError and data loss during casting."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    # Pitfall: Attempting to cast non-numeric strings to int
    try:
        invalid_int = int("Hello")
    except ValueError as e:
        print(f"Error caught: Cannot cast non-numeric string to int -> {e}")
        
    # Pitfall: Losing precision when casting float to int
    pi_val = 3.14159
    pi_int = int(pi_val) # Truncates the decimal
    print(f"Casting float {pi_val} to int results in {pi_int} (Data Loss!)")
    
    # Best Practice: Always wrap user-input casting in a try-except block to handle ValueErrors safely.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. What is the difference between implicit and explicit type conversion in Python?
   Answer: Implicit conversion is handled automatically by Python (e.g., int + float = float). Explicit conversion is done manually by the programmer using functions like int() or str().

2. What does int("10.5") produce?
   Answer: It raises a ValueError. You must cast it to a float first: int(float("10.5")).

3. What does bool("False") evaluate to?
   Answer: True. Any non-empty string evaluates to True, even if its content is the word "False".

4. How do you convert a tuple into a list?
   Answer: By using the list() constructor, e.g., my_list = list(my_tuple).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Convert the float 99.99 to an integer. What happens to the decimal part?
Exercise 2: Write a program that converts the boolean True to an integer and prints it.
Exercise 3: Convert the string "123" and the string "456" to integers, add them, and print the result.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Challenge to cast and calculate user data."""
    print("\n--- Mini Challenge ---")
    
    # Simulated input strings
    price_input = "19.99"
    quantity_input = "5"
    
    # Convert inputs to appropriate types
    price = float(price_input)
    quantity = int(quantity_input)
    
    # Calculate total
    total = price * quantity
    
    # Convert total back to string for concatenation (or just use f-strings)
    print("Total cost is: $" + str(total))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Type casting converts data from one type to another.
- Functions like int(), float(), and str() are used for explicit conversion.
- Casting can sometimes result in data loss (e.g., float to int) or raise exceptions (e.g., invalid string to int).
- Boolean casting evaluates the "truthiness" of a value.
"""

if __name__ == "__main__":
    explicit_casting()
    practical_casting()
    advanced_casting()
    common_mistakes()
    mini_challenge()
