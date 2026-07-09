"""
Topic: Variables and Data Types Practice 2
Chapter: 2
Level: Beginner

Description:
    This file contains practice exercises focusing on Type Casting and User Input processing.
    It combines string parsing, type conversion, and handling possible errors.

Real-Life Analogy:
    Like a translator taking a document written in one language and carefully converting it 
    into another so the machinery (your code logic) can read and process it.

Key Concepts:
    - input() function simulation
    - int(), float(), and str() conversions
    - String splitting and list conversion
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_casting_practice() -> None:
    """Practice converting strings to numbers."""
    print("--- Exercise 1: String to Numbers ---")
    
    # Simulated input data
    input_distance = "150.5"
    input_time = "2"
    
    # Conversion
    distance_km = float(input_distance)
    time_hours = int(input_time)
    
    speed = distance_km / time_hours
    print(f"Distance: {distance_km} km")
    print(f"Time: {time_hours} hours")
    print(f"Speed: {speed} km/h")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def input_processing() -> None:
    """Simulate processing a single line of input with multiple values."""
    print("\n--- Exercise 2: Processing Split Input ---")
    
    # Simulate: user types "10 20 30"
    raw_input = "10 20 30"
    
    # Split string into a list of strings
    str_list = raw_input.split()
    
    # Convert list of strings to list of integers
    int_list = [int(num) for num in str_list]
    
    total = sum(int_list)
    print(f"Raw Input: '{raw_input}'")
    print(f"Converted List: {int_list}")
    print(f"Sum of List: {total}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def safe_casting() -> None:
    """Handling errors gracefully during type casting."""
    print("\n--- Exercise 3: Safe Casting ---")
    
    bad_data = "forty-two"
    
    try:
        numeric_val = int(bad_data)
        print(f"Success! Value is {numeric_val}")
    except ValueError:
        print(f"Failed to cast '{bad_data}' to an integer. Please provide a valid number.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def formatting_output() -> None:
    """Best practices for casting numbers back to strings for display."""
    print("\n--- Exercise 4: Output Formatting ---")
    
    score = 95
    # Pitfall: print("Score is " + score) # TypeError
    
    # Correction 1: explicit str()
    print("Score is " + str(score))
    
    # Correction 2: f-strings (Preferred)
    print(f"Score is {score}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. How do you take two space-separated integers as input on a single line?
   Answer: a, b = map(int, input().split())

2. Why is type casting important when taking input in Python?
   Answer: Because input() always returns a string, and mathematical operations require numeric types.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Practice on your own:
1. Write code to take a comma-separated string of names (e.g., "Alice,Bob,Charlie"), split it, and print the number of names.
2. Attempt to cast the float 3.99 to an integer. Note what happens to the decimal part.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Receipt generator challenge."""
    print("\n--- Mini Challenge: Receipt Generator ---")
    
    # Simulated input
    item = "Notebook"
    price_str = "4.50"
    quantity_str = "3"
    
    # Processing
    price = float(price_str)
    quantity = int(quantity_str)
    subtotal = price * quantity
    tax = subtotal * 0.08
    grand_total = subtotal + tax
    
    # Output formatting
    print(f"Item: {item}")
    print(f"Qty:  {quantity}")
    print(f"Sub:  ${subtotal:.2f}")
    print(f"Tax:  ${tax:.2f}")
    print("-" * 15)
    print(f"Tot:  ${grand_total:.2f}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- Type casting bridges the gap between text input and mathematical processing.
- Using split() is an effective way to parse string inputs.
- Always handle ValueErrors when converting strings to numbers.
"""

if __name__ == "__main__":
    basic_casting_practice()
    input_processing()
    safe_casting()
    formatting_output()
    mini_challenge()
