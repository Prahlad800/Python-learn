"""
Topic: Advanced Conditional Logic Practice
Chapter: 5
Level: Intermediate / Advanced

Description:
    This file focuses on more advanced scenarios, including structural pattern matching (match-case), 
    guard clauses, and complex nested conditions.

Real-Life Analogy:
    Like an escape room, these exercises require combining multiple tools and rules to find the 
    most efficient and readable solution.

Key Concepts:
    - Match-Case structural extraction.
    - Refactoring nested logic to guard clauses.
    - Evaluating complex data structures.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def practice_match_case():
    print("--- Practice: Match-Case ---")
    # Task 1: Parse API response
    response = {"status": 200, "data": ["item1", "item2"]}
    
    match response:
        case {"status": 200, "data": data}:
            print(f"Success! Data received: {data}")
        case {"status": 404}:
            print("Error: Resource not found.")
        case {"status": status_code}:
            print(f"Error with status code: {status_code}")
        case _:
            print("Invalid response format.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practice_guard_clauses(user_role, is_active, balance):
    print(f"\n--- Practice: Guard Clauses (Role: {user_role}) ---")
    # Task 2: Validate a user purchase
    
    if not is_active:
        print("Account is inactive.")
        return False
        
    if balance <= 0:
        print("Insufficient funds.")
        return False
        
    if user_role not in ["admin", "premium_user"]:
        print("You do not have permission to buy this item.")
        return False
        
    print("Purchase successful!")
    return True

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def practice_complex_nesting():
    print("\n--- Practice: Complex Conditionals ---")
    # Evaluate a password's strength
    password = "Secure!Pass1"
    
    strength = "Weak"
    if len(password) >= 8:
        if any(char.isdigit() for char in password):
            if any(char.isupper() for char in password):
                if any(char in "!@#$%^&*" for char in password):
                    strength = "Strong"
                else:
                    strength = "Moderate (Missing special char)"
            else:
                strength = "Moderate (Missing uppercase)"
    
    print(f"Password Strength: {strength}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Best Practices for Advanced Conditionals:
# - If a function contains a massive block of nested conditionals (like Task 3), 
#   it's a sign it should be broken down into smaller helper functions.
# - Use match-case when inspecting the structure/keys of dictionaries, not just exact values.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# (Refer to specific feature files for Q&A)

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Refactoring Challenge:
# Try rewriting `practice_complex_nesting` logic using multiple separate `if` statements 
# updating a score, rather than deeply nested conditionals.

def calculate_score(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(char.isdigit() for char in password): score += 1
    if any(char.isupper() for char in password): score += 1
    if any(char in "!@#$%^&*" for char in password): score += 1
    return score

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    practice_guard_clauses("basic_user", True, 50)
    practice_guard_clauses("premium_user", True, 100)
    
    score = calculate_score("Secure!Pass1")
    print(f"Refactored password score: {score}/4")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Match-case provides elegant ways to parse JSON/Dictionaries.
# - Guard clauses significantly reduce nesting.
# - Complex nested logic is a code smell that often requires refactoring.

if __name__ == "__main__":
    practice_match_case()
    practice_guard_clauses("admin", True, 500)
    practice_complex_nesting()
    mini_challenge()
