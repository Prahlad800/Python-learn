"""
Topic: User Input
Chapter: 2
Level: Beginner

Description:
    Python allows for user input directly from the console using the built-in `input()` function. 
    This allows programs to be interactive, taking data from the user and processing it dynamically.
    Importantly, the `input()` function ALWAYS returns a string, regardless of what the user types.

Real-Life Analogy:
    Think of a barista asking for your name for a coffee order. They wait for you to speak, 
    write exactly what you said on the cup (as text/string), and then continue processing the order.

Key Concepts:
    - The input() function
    - Prompting the user
    - Converting input types (Casting)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_input() -> None:
    """Demonstrates basic usage of the input() function."""
    print("--- Basic User Input ---")
    
    # In a real scenario, this pauses execution and waits for the user.
    # We will simulate the input for the sake of making this script non-blocking during automated runs.
    # user_name = input("Please enter your name: ")
    user_name = "Simulated User"  # Simulated input
    
    print(f"Hello, {user_name}! Welcome to Python.")
    print(f"The data type of user_name is: {type(user_name)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_input() -> None:
    """Shows how to take input and cast it to numeric types for calculations."""
    print("\n--- Practical Examples ---")
    
    # Simulating input of a number
    # age_str = input("How old are you? ")
    age_str = "25"  # Simulated input
    
    # We MUST convert the string to an integer before doing math
    age = int(age_str)
    
    years_to_retire = 65 - age
    print(f"You have {years_to_retire} years until retirement.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_input() -> None:
    """Handling multiple inputs and using split()."""
    print("\n--- Advanced Usage ---")
    
    # Simulating multiple inputs on a single line
    # raw_input = input("Enter your first and last name separated by a space: ")
    raw_input = "John Doe"  # Simulated input
    
    # split() divides the string into a list based on spaces
    first_name, last_name = raw_input.split()
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    """Highlights issues with forgetting to cast and handling invalid input."""
    print("\n--- Common Mistakes and Best Practices ---")
    
    # Pitfall: Forgetting to cast numerical input
    # num = input("Enter a number: ") # Let's say user enters 5
    # print(num * 2) # Output would be "55", not 10!
    
    # Best Practice: Always handle potential ValueError when casting input
    simulated_bad_input = "twenty"
    try:
        val = int(simulated_bad_input)
    except ValueError:
        print(f"Error: '{simulated_bad_input}' is not a valid integer. Please enter digits only.")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. What data type does the input() function return?
   Answer: It always returns a string (str).

2. How do you take an integer input from the user?
   Answer: Wrap the input() function in an int() cast: num = int(input("Enter number: "))

3. How can you take multiple inputs on a single line?
   Answer: Use the split() string method: a, b = input("Enter two values: ").split()

4. What happens if you try to cast user input "10.5" using int()?
   Answer: It throws a ValueError. You should cast it to float() first.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Write a program that asks the user for the length and width of a rectangle, then prints the area.
Exercise 2: Ask the user for their birth year and calculate their current age.
Exercise 3: Ask the user to input three numbers separated by commas, split them, convert to floats, and find their sum.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge() -> None:
    """Mini challenge to build a simple interactive calculator (simulated)."""
    print("\n--- Mini Challenge ---")
    
    # Simulated inputs
    num1_str = "15"
    num2_str = "5.5"
    operation = "+"
    
    try:
        n1 = float(num1_str)
        n2 = float(num2_str)
        
        if operation == "+":
            print(f"Result: {n1} + {n2} = {n1 + n2}")
        elif operation == "-":
            print(f"Result: {n1} - {n2} = {n1 - n2}")
        else:
            print("Unsupported operation.")
            
    except ValueError:
        print("Invalid numbers provided.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
Summary:
- The input() function makes Python programs interactive.
- Input is always captured as a string.
- Explicit type casting (e.g., int(), float()) is required for mathematical operations.
- Always anticipate user error and handle exceptions appropriately.
"""

if __name__ == "__main__":
    basic_input()
    practical_input()
    advanced_input()
    common_mistakes()
    mini_challenge()
