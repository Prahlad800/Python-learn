"""
Topic: Infinite Loops and their Management
Chapter: 06
Level: Intermediate

Description:
    An infinite loop is a loop whose condition never becomes false, meaning it will run forever unless manually interrupted.
    While often caused by bugs, infinite loops are also intentionally used in server polling, game loops, and UI event loops.

Real-Life Analogy:
    A clock ticking. It never stops automatically. It requires external intervention (battery dying, someone stopping it) to halt.

Key Concepts:
    - `while True:` structure
    - Controlling loops with `break`
    - Handling external interruptions (Ctrl+C / KeyboardInterrupt)
    - Accidental vs Intentional infinite loops
"""

import time

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def accidental_infinite_loop():
    # DO NOT RUN this without understanding it will freeze the console.
    """
    count = 0
    while count < 5:
        print("Hello!")
        # Missing count += 1 here creates an infinite loop
    """
    print("--- Accidental Infinite Loop Example Documented ---")
    print("A missing state update in a while loop is the most common cause.")

def intentional_infinite_loop():
    print("\n--- Intentional Infinite Loop with Break ---")
    counter = 1
    while True:
        print(f"Tick {counter}")
        if counter >= 3:
            print("Condition met, breaking out!")
            break
        counter += 1

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def user_input_loop():
    print("\n--- Prompting User Until Valid ---")
    # Simulated input mechanism for example
    simulated_inputs = ["invalid", "bad", "quit"]
    input_index = 0
    
    while True:
        # In reality, this would be: user_input = input("Enter 'quit' to exit: ")
        user_input = simulated_inputs[input_index]
        print(f"User typed: {user_input}")
        
        if user_input.lower() == 'quit':
            print("Exiting loop.")
            break
            
        print("Invalid command. Try again.")
        input_index += 1

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def polling_loop():
    print("\n--- Server Polling Simulation ---")
    # Simulating checking a server status every second
    polls = 0
    try:
        while True:
            # Simulate a status check
            polls += 1
            if polls > 2: # Automatically break after 2 for safety in this script
                print("Server online! Stopping poll.")
                break
                
            print(f"Polling server... (Poll {polls})")
            time.sleep(0.1) # Pauses execution for 0.1 seconds (usually 1+ seconds)
            
    except KeyboardInterrupt:
        # This triggers if the user presses Ctrl+C in the terminal
        print("\nPolling interrupted by user.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Forgetting to increment the counter in a `while` loop.
# 2. Writing a `while True:` loop without any `break` statement inside it.
# 3. Not utilizing `time.sleep()` in polling loops, causing the CPU to hit 100% usage while doing nothing.

# Best Practices:
# 1. If an infinite loop is intentional, explicitly use `while True:` for readability.
# 2. Always ensure there is a clear, reachable exit path (`break` or `return`).
# 3. If the loop is waiting for an external event, incorporate `time.sleep()` to yield CPU resources.
# 4. Use `try...except KeyboardInterrupt:` to gracefully handle user termination (Ctrl+C).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: What is the most common use case for an intentional infinite loop?
A: Event listeners in UI applications, game engine loops, and server daemons listening for requests.

Q2: How do you stop a runaway infinite loop in the terminal?
A: By pressing `Ctrl + C`, which sends a SIGINT (KeyboardInterrupt) signal to the Python interpreter.

Q3: Why is `while True:` preferred over `while 1 == 1:`?
A: `while True:` is slightly faster and much more readable. Python explicitly optimizes `while True:`.

Q4: What happens if a server polling loop lacks a `sleep()` function?
A: It will cause a "busy wait," consuming 100% of the CPU core executing the loop and slowing down the whole system.

Q5: Can a `for` loop be infinite?
A: Typically no, since `for` iterates over a finite sequence. However, if it iterates over a custom generator that yields infinitely, it can be.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # Exercise 1: Write a while loop that keeps generating random numbers between 1 and 10 until it generates a 7, then breaks.
    pass

    # Exercise 2: Create a simple text-menu loop that runs indefinitely until the user selects option "3" to exit.
    pass

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: 
    Implement a loop that simulates a retry mechanism for connecting to a database.
    It should try up to 3 times, with a 0.1 second delay between attempts.
    If it fails 3 times, print an error. (Simulate failure by always assuming connection fails).
    """
    print("\n--- Database Connection Retry Simulation ---")
    max_retries = 3
    attempt = 1
    
    while attempt <= max_retries:
        print(f"Connecting to database... (Attempt {attempt}/{max_retries})")
        # Simulating connection failure
        time.sleep(0.1)
        
        # If connection succeeded, we would break here
        
        attempt += 1
    else:
        # Using loop-else from previous concepts!
        print("CRITICAL: Failed to connect to database after maximum retries.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Infinite loops run continuously because their condition is always truthy.
- They are created using `while True:`.
- Essential tools for intentional infinite loops: `break`, `time.sleep()`, and handling `KeyboardInterrupt`.
- Accidental infinite loops are usually logic errors involving loop variables.
"""

if __name__ == "__main__":
    accidental_infinite_loop()
    intentional_infinite_loop()
    user_input_loop()
    polling_loop()
    mini_challenge()
