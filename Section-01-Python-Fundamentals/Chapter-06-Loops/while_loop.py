"""
Topic: While Loops in Python
Chapter: 6
Level: Beginner

Description:
    A `while` loop repeatedly executes a target statement as long as a given boolean condition evaluates to True.
    It is useful when you do not know beforehand how many times you need to loop.

Real-Life Analogy:
    Think of eating soup. You continue to take spoonfuls (action) *while* there is still soup in the bowl (condition).
    When the bowl is empty, you stop.

Key Concepts:
    - Boolean condition
    - Infinite loops (and how to avoid them)
    - Condition modification within the loop
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    """Demonstrate basic syntax of while loops."""
    print("--- Basic Syntax ---")
    
    # Simple countdown
    count = 5
    print("Countdown started:")
    while count > 0:
        print(f"Count: {count}")
        # ALWAYS update the variable to avoid an infinite loop
        count -= 1
    print("Blast off!")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    """Real-world use cases for 'while' loops."""
    print("\n--- Practical Examples ---")
    
    # 1. Processing a list dynamically
    tasks = ["Wash dishes", "Clean room", "Do laundry"]
    print("Task list execution:")
    while tasks:  # Loops as long as the list is not empty
        current_task = tasks.pop(0)
        print(f"Completing: {current_task}")
    print("All tasks completed.")

    # 2. Reaching a target (e.g., simple savings goal)
    savings = 0
    goal = 100
    months = 0
    while savings < goal:
        savings += 35
        months += 1
    print(f"\nGoal reached in {months} months with ${savings}.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    """Advanced while loop usage."""
    print("\n--- Advanced Usage ---")
    
    # 1. While loop with multiple conditions
    x = 0
    y = 10
    print("Multiple condition loop:")
    while x < 5 and y > 5:
        print(f"x: {x}, y: {y}")
        x += 1
        y -= 1

    # 2. Simulating a do-while loop (Python doesn't have a native one)
    # This ensures the code runs AT LEAST once.
    print("\nSimulated Do-While loop:")
    i = 0
    while True:
        print(f"Running do-while simulation, i={i}")
        i += 1
        if i >= 3:
            break

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_practices():
    """Common pitfalls and best practices."""
    print("\n--- Common Mistakes & Best Practices ---")
    
    # MISTAKE: Infinite loop due to missing update
    # count = 1
    # while count < 5:
    #     print(count)
    #     # Forgot count += 1 here!
    
    # BEST PRACTICE: Ensure the condition will eventually evaluate to False.
    # BEST PRACTICE: Use 'while' only when the number of iterations is unknown. 
    # Use 'for' when iterating over a known sequence.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Q: What is the main difference between a for loop and a while loop?
   A: A `for` loop is typically used when the number of iterations is known (iterating over a sequence). A `while` loop is used when the number of iterations is unknown and depends on a condition.

2. Q: How do you create an infinite loop?
   A: By using `while True:` or having a condition that never becomes False.

3. Q: Does Python have a `do-while` loop?
   A: No. However, you can simulate it by using `while True:` and placing an `if condition: break` at the end of the loop block.

4. Q: How can you break out of a while loop prematurely?
   A: Using the `break` statement.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Write a while loop that asks the user for input until they type 'quit'.
(For the sake of automation in testing, you might mock the input).

Exercise 2: Write a while loop to find the first power of 2 that is greater than 1000.

Exercise 3: Write a program that uses a while loop to reverse a given integer 
(e.g., turn 1234 into 4321) using math operations (% and //).
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Use a while loop to simulate a simple ATM machine's PIN entry.
    The user has a maximum of 3 attempts to enter the correct PIN (1234).
    """
    print("\n--- Mini Challenge (Simulated) ---")
    correct_pin = "1234"
    attempts = 0
    max_attempts = 3
    
    # Simulating user inputs: wrong, wrong, correct
    simulated_inputs = ["1111", "0000", "1234"] 
    
    while attempts < max_attempts:
        entered_pin = simulated_inputs[attempts]
        print(f"Attempt {attempts + 1}: Entered {entered_pin}")
        if entered_pin == correct_pin:
            print("Access Granted!")
            break
        else:
            print("Incorrect PIN.")
            attempts += 1
            
    if attempts == max_attempts:
        print("Account Locked due to too many failed attempts.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `while` loops execute as long as the condition is True.
- Crucial to update the loop variable to avoid infinite loops.
- Can process data dynamically (e.g., emptying lists).
- Useful for event-driven logic (e.g., waiting for specific user input).
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mistakes_and_practices()
    mini_challenge()
