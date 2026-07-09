"""
Topic: Basic Input (input function)
Chapter: 4
Level: Beginner

Description:
    The `input()` function is used to take user input from the keyboard. It pauses program execution until the user types something and presses Enter. The input is always returned as a string.

Real-Life Analogy:
    It's like a drive-thru window speaker. The cashier (program) asks you for your order, waits for you to speak (user input), and then takes what you said to process the order.

Key Concepts:
    - input() function
    - Providing a prompt string
    - Data type conversion (casting)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Basic usage of input()
# Note: Uncomment to run interactive prompts
# user_name = input("Please enter your name: ")
# print(f"Hello, {user_name}!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("--- Practical Examples (Simulated) ---")
    # Taking string input
    # city = input("Which city do you live in? ")
    # print(f"Wow, {city} is a beautiful place!")
    
    # Input is ALWAYS a string. If we want a number, we must cast it.
    # age_str = input("Enter your age: ")
    # age = int(age_str)
    # print(f"You will be {age + 1} next year.")
    print("Remember: input() returns a string. You must use int() or float() to convert it.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("--- Advanced Usage (Simulated) ---")
    # Taking multiple inputs in one line using split()
    # data = input("Enter your first and last name separated by a space: ")
    # first, last = data.split()
    # print(f"First Name: {first}, Last Name: {last}")
    
    # Handling specific data types directly
    # price = float(input("Enter the price of the item: "))
    # print(f"Price with tax: {price * 1.05}")
    print("Advanced usage often involves chaining methods like input().strip().lower()")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to convert numeric input.
# num = input("Enter number: ")
# print(num * 2) # If user enters "5", this prints "55", not 10.

# Correction: Use int() or float()
# num = int(input("Enter number: "))
# print(num * 2) # Now correctly prints 10.

# Best Practice: Always provide a clear and descriptive prompt.
# Best Practice: Handle potential errors when casting (e.g., user types "five" instead of "5").

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: What data type does the input() function return?
A: A string (str).

Q: How do you get an integer input from a user?
A: By wrapping the input() function with int(), e.g., int(input("Enter: ")).

Q: What happens if a user inputs a letter when you try to cast it to an int?
A: Python will raise a ValueError.

Q: Can you pass multiple arguments to the input() function?
A: No, input() takes exactly zero or one argument (the prompt string).

Q: How do you read a password securely without displaying it?
A: By using the getpass module: getpass.getpass("Password: ")
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    pass
    # 1. Write code to ask the user for their favorite color.
    # color = input("Favorite color: ")
    
    # 2. Ask the user for two numbers and print their sum.
    # num1 = float(input("Number 1: "))
    # num2 = float(input("Number 2: "))
    # print(num1 + num2)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create a simple calculator that asks the user for a width and height,
    and then prints the area and perimeter of a rectangle.
    """
    print("--- Rectangle Calculator ---")
    # width = float(input("Enter width: "))
    # height = float(input("Enter height: "))
    # area = width * height
    # perimeter = 2 * (width + height)
    # print(f"Area: {area}, Perimeter: {perimeter}")
    print("Implementation commented out to prevent execution hang.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- input() is used to gather information from the user.
- It always returns a string, regardless of what the user types.
- Type casting (int(), float()) is required for numeric operations.
- Always provide a clear prompt so the user knows what to type.
"""

if __name__ == "__main__":
    practical_examples()
    advanced_usage()
    practice_exercises()
    mini_challenge()
