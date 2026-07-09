"""
Topic: Guard Clauses (Early Returns)
Chapter: 5
Level: Intermediate

Description:
    A guard clause is a conditional statement at the top of a function that handles an edge case 
    or invalid condition by exiting the function early (using `return`). This technique replaces 
    deeply nested `if-else` blocks and makes code more readable.

Real-Life Analogy:
    A bouncer at a club. "If you don't have ID, go away immediately." 
    They don't take you inside, show you the dance floor, and THEN say you can't stay.

Key Concepts:
    - Early Return: Exiting a function as soon as a failure state is detected.
    - Flattening Code: Removing levels of indentation caused by nested `if`s.
    - Precondition Checking: Verifying data validity before doing the main work.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def without_guard_clause(user, age):
    # Deeply nested, harder to read
    if user:
        if age >= 18:
            print("Access granted to the system.")
            return True
        else:
            print("User is underage.")
            return False
    else:
        print("User not found.")
        return False

def basic_guard_examples():
    print("--- Section 1: Basic Guard Clauses ---")
    
    # Applying Guard Clauses to flatten the logic
    def process_user(user, age):
        # Guard 1
        if not user:
            print("User not found.")
            return False
            
        # Guard 2
        if age < 18:
            print("User is underage.")
            return False
            
        # Main Logic (no indentation needed!)
        print("Access granted to the system.")
        return True

    process_user("Alice", 20)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: File processing
    def read_config_file(filepath):
        if not filepath:
            print("Error: No filepath provided.")
            return None
            
        if not filepath.endswith(".json"):
            print("Error: Only JSON files supported.")
            return None
            
        # Actual work happens here safely
        print(f"Reading configuration from {filepath}...")
        return {"status": "success"}

    read_config_file("")
    read_config_file("config.txt")
    read_config_file("config.json")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")

    # Example: Raising Exceptions in Guard Clauses
    # Instead of just returning, guard clauses often raise explicit errors.
    
    def divide_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers.")
        if b == 0:
            raise ValueError("Cannot divide by zero.")
            
        return a / b

    try:
        print(f"10 / 2 = {divide_numbers(10, 2)}")
        # This will trigger a guard clause
        divide_numbers(10, 0)
    except ValueError as e:
        print(f"Caught exception: {e}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Putting the main logic inside the `else` block of a guard clause. 
#    The whole point is to avoid the `else` and keep the main logic un-indented.
# 2. Checking for too many complex things in a single guard clause, making it hard to read.

# Best Practices:
# - Put guard clauses at the very beginning of the function.
# - Use them to assert preconditions (e.g., checking for None, empty strings, invalid types).
# - Return early or raise exceptions to halt execution immediately.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a guard clause?
# A1: A check at the beginning of a function that returns early or raises an exception if preconditions aren't met, flattening code structure.

# Q2: How do guard clauses improve code readability?
# A2: They eliminate the need for deeply nested `if-else` blocks (the "Arrow Anti-pattern"), allowing the main logic to sit at the base indentation level.

# Q3: Should a guard clause use an `else` block?
# A3: No. If the condition is met, it returns/raises. Therefore, an `else` is redundant and defeats the purpose of flattening the code.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Refactor a nested `if` statement that checks if a list is empty and if its first element is > 0 into a function using guard clauses.
# Exercise 2: Write a function `calculate_discount` that applies guard clauses for negative prices and negative discount percentages.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Write a function `update_profile` that takes `username` and `email`.
    # Use guard clauses to:
    # 1. Ensure username is at least 3 chars.
    # 2. Ensure email contains an '@' symbol.
    # If valid, print "Profile updated."
    
    def update_profile(username, email):
        if len(username) < 3:
            print("Failed: Username too short.")
            return
        if "@" not in email:
            print("Failed: Invalid email address.")
            return
            
        print(f"Profile updated for {username} ({email}).")

    update_profile("ab", "test@test.com")
    update_profile("alice", "testtest.com")
    update_profile("alice", "alice@domain.com")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Guard clauses handle edge cases and invalid data by exiting early.
# - They replace complex nested conditionals.
# - Code becomes flatter, easier to read, and places the "happy path" front and center.

if __name__ == "__main__":
    basic_guard_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
