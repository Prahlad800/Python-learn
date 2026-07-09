"""
Topic: Match-Case Statements (Structural Pattern Matching)
Chapter: 5
Level: Intermediate / Advanced

Description:
    Introduced in Python 3.10, the `match-case` statement provides structural pattern matching. 
    It allows you to compare a variable against a series of patterns and execute code based on the first match. 
    It is much more powerful than traditional `switch` statements found in other languages.

Real-Life Analogy:
    Sorting mail at the post office. "If the package is shaped like a tube, put it in bin A. 
    If it's a flat envelope, put it in bin B. If it's anything else, put it in the miscellaneous bin."

Key Concepts:
    - Pattern Matching: Matching exact values, shapes of data (like lists/dicts), and object types.
    - `_` (Wildcard): Acts as the default case if no other patterns match.
    - Extraction: Extracting variables directly from the matched structure.
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def basic_match_examples():
    print("--- Section 1: Basic Match-Case ---")
    
    # Syntax:
    # match subject:
    #     case pattern1:
    #         # execute
    #     case pattern2:
    #         # execute
    #     case _:
    #         # default

    # Example 1: Simple value matching (like a switch statement)
    status_code = 404
    
    match status_code:
        case 200:
            print("OK - Request successful.")
        case 404:
            print("Not Found - Resource missing.")
        case 500:
            print("Server Error.")
        case _:
            print("Unknown status code.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    print("\n--- Section 2: Practical Examples ---")

    # Example 1: Matching multiple values with OR (|)
    command = "quit"
    
    match command:
        case "start" | "run":
            print("Starting the engine...")
        case "stop" | "halt":
            print("Stopping...")
        case "quit" | "exit":
            print("Exiting program.")
        case _:
            print("Command not recognized.")

    # Example 2: Matching Data Structures (Lists/Tuples)
    # Extracting variables during the match
    point = (0, 5)
    
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y-axis, at y={y}")
        case (x, 0):
            print(f"X-axis, at x={x}")
        case (x, y):
            print(f"Point at ({x}, {y})")
        case _:
            print("Not a 2D point.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")

    # Example 1: Matching Dictionaries and adding Guards (if conditions)
    user = {"name": "Alice", "role": "admin", "age": 30}
    
    match user:
        case {"name": name, "role": "admin"} if user.get("age", 0) > 18:
            print(f"Welcome Admin {name}, you have full access.")
        case {"name": name, "role": "user"}:
            print(f"Welcome User {name}.")
        case _:
            print("Invalid user format or permissions.")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Common Mistakes:
# 1. Running match-case on older Python versions (requires 3.10+). It will cause a SyntaxError.
# 2. Forgetting the `_` (wildcard) case, which can lead to silent failures if no case matches.
# 3. Confusing `|` (OR) in a case statement with the boolean `or`. You must use `|` in patterns.

# Best Practices:
# - Use match-case when dealing with complex data structures (JSON, nested dictionaries, ASTs).
# - For simple exact-value checks, a dictionary lookup might still be faster and cleaner.
# - Always include a default `case _:` to handle unexpected data.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: In which Python version was `match-case` introduced?
# A1: Python 3.10.

# Q2: Is `match-case` just a `switch` statement?
# A2: No. While it can act like a switch statement for simple values, it is a structural pattern matching tool that can unpack data structures and bind variables.

# Q3: What does `case _:` do?
# A3: It acts as the wildcard or default case. It matches anything that hasn't been matched by prior cases.

# Q4: Can you use conditions within a `case` statement?
# A4: Yes, using "guards". You can append an `if` condition to a case, e.g., `case [x, y] if x == y:`.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a match-case that takes a string day of the week and prints if it's a weekday or weekend.
# Exercise 2: Use match-case to process a list representing an action. `["move", 10]` should print "Moving 10 spaces", `["jump"]` should print "Jumping".

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # Parse events from a simple game engine.
    # Event types: {"type": "click", "coords": (x, y)}, {"type": "keypress", "key": key}
    
    events = [
        {"type": "click", "coords": (100, 250)},
        {"type": "keypress", "key": "Enter"},
        {"type": "unknown"}
    ]
    
    for event in events:
        match event:
            case {"type": "click", "coords": (x, y)}:
                print(f"Mouse clicked at X:{x} Y:{y}")
            case {"type": "keypress", "key": key}:
                print(f"Key pressed: {key}")
            case _:
                print("Unknown event ignored.")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - `match-case` is a powerful tool for structural pattern matching (Python 3.10+).
# - It allows for unpacking and checking data structures cleanly.
# - Guards (`if`) and the wildcard (`_`) provide flexibility and safety.

if __name__ == "__main__":
    basic_match_examples()
    practical_examples()
    advanced_usage()
    mini_challenge()
