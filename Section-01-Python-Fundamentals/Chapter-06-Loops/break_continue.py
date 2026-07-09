"""
Topic: Break and Continue Statements
Chapter: 6
Level: Beginner / Intermediate

Description:
    `break` and `continue` are loop control statements that alter the regular flow of a loop.
    `break` exits the entire loop immediately, while `continue` skips the rest of the current iteration and moves to the next one.

Real-Life Analogy:
    Imagine reading a book page by page:
    - If you find a bookmark saying "Stop reading", you close the book entirely (this is `break`).
    - If you see a page is torn or irrelevant, you skip that specific page and move to the next one (this is `continue`).

Key Concepts:
    - Altering loop execution flow
    - Early exit (`break`)
    - Skipping iterations (`continue`)
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_syntax():
    """Demonstrate basic usage of break and continue."""
    print("--- Break Syntax ---")
    for i in range(1, 6):
        if i == 4:
            print("Breaking the loop at 4")
            break
        print(f"Processing {i}")

    print("\n--- Continue Syntax ---")
    for i in range(1, 6):
        if i == 3:
            print("Skipping 3")
            continue
        print(f"Processing {i}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    """Practical scenarios using break and continue."""
    print("\n--- Practical Examples ---")
    
    # 1. Searching for an item (Break)
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    target = "cherry"
    print(f"Searching for {target}:")
    for item in items:
        print(f"Checking {item}...")
        if item == target:
            print("Found it! Stopping search.")
            break
            
    # 2. Processing only positive numbers (Continue)
    data = [10, -5, 20, -1, 30]
    total = 0
    print("\nSumming only positive numbers:")
    for num in data:
        if num < 0:
            continue  # Skip negative numbers
        total += num
    print(f"Total of positives: {total}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    """Advanced combinations of loop control statements."""
    print("\n--- Advanced Usage ---")
    
    # 1. Break in nested loops
    # Note: 'break' only exits the innermost loop
    print("Nested loop break:")
    for i in range(3):
        for j in range(3):
            if j == 1:
                break
            print(f"i={i}, j={j}")

    # 2. Using continue in a while loop
    # Be careful to update the loop counter BEFORE the continue!
    print("\nWhile loop with continue:")
    x = 0
    while x < 5:
        x += 1
        if x % 2 == 0:
            continue
        print(f"Odd number: {x}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_practices():
    """Common pitfalls when using break and continue."""
    print("\n--- Common Mistakes & Best Practices ---")
    
    # MISTAKE: Placing continue before updating the counter in a while loop
    # i = 0
    # while i < 5:
    #     if i == 2:
    #         continue  # Infinite loop here because 'i' never increments
    #     i += 1
    
    # BEST PRACTICE: Overusing break/continue can make code hard to read.
    # Often, restructuring the 'if' condition is cleaner than using 'continue'.
    # Example (Cleaner without continue):
    # for num in data:
    #     if num >= 0:
    #         total += num

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
1. Q: What is the difference between break and continue?
   A: `break` completely terminates the loop it is inside. `continue` skips the remaining code in the current iteration and jumps to the next iteration.

2. Q: If you use a `break` in a nested loop, does it stop all loops?
   A: No, it only terminates the innermost loop containing the `break` statement.

3. Q: Can `break` or `continue` be used outside of loops?
   A: No, using them outside of loops (like in a standalone `if` statement) will raise a SyntaxError.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

"""
Exercise 1: Write a loop that iterates over a list of strings and stops (breaks) completely if it encounters an empty string.

Exercise 2: Write a loop that iterates from 1 to 20 but uses `continue` to skip any multiples of 3.

Exercise 3: Create a while loop that simulates a login process. Allow 3 attempts. Break out early if successful.
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Process a stream of sensor data.
    - Ignore (continue) any reading below 0 (error code).
    - Stop completely (break) if a reading exceeds 100 (critical danger).
    - Otherwise, sum the readings.
    """
    print("\n--- Mini Challenge ---")
    sensor_data = [45, 60, -1, 55, 105, 70, 80]
    valid_sum = 0
    
    print("Processing sensor data stream:")
    for reading in sensor_data:
        if reading < 0:
            print(f"Ignoring invalid reading: {reading}")
            continue
        if reading > 100:
            print(f"CRITICAL ERROR! Reading {reading} too high. Shutting down.")
            break
        valid_sum += reading
        print(f"Processed {reading}, running total: {valid_sum}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- `break` exits a loop entirely.
- `continue` skips the current iteration and proceeds to the next.
- Both alter the standard loop flow and must be used carefully to maintain code readability.
- In while loops, ensure counters are updated correctly before a `continue` to avoid infinite loops.
"""

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mistakes_and_practices()
    mini_challenge()
