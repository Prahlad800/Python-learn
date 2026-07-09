"""
Topic: Advanced Print Function
Chapter: 4
Level: Intermediate

Description:
    Beyond basic output, the `print()` function can be used in advanced ways for debugging, creating command-line interfaces, generating progress bars, and redirecting output streams.

Real-Life Analogy:
    Standard printing is like regular mail. Advanced printing is like using certified mail, express delivery, or redirecting your mail to a different address altogether.

Key Concepts:
    - Overwriting lines in the terminal (\r)
    - Terminal escape codes (colors and styles)
    - Sys.stdout manipulation
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The carriage return character '\r' moves the cursor to the beginning of the line
# without going to the next line. This allows overwriting text.
print("This will be overwritten", end="\r")
print("New Text!") # Overwrites the previous text

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def practical_examples():
    import time
    
    print("--- Simple Timer ---")
    # A simple countdown timer using \r and end=""
    # (Uncomment to see animation)
    # for i in range(3, 0, -1):
    #     print(f"Starting in {i}...", end="\r", flush=True)
    #     time.sleep(1)
    print("Go!                 ") # Extra spaces clear remaining characters from previous print

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def advanced_usage():
    # 1. Basic ANSI Escape Codes for colors
    # Syntax: \033[<style>;<color>m
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    print(f"{RED}This is red text!{RESET}")
    print(f"{GREEN}{BOLD}This is bold green text!{RESET}")
    
    # 2. Redirecting output using context managers (simulated)
    import sys
    import io
    
    # Capture print output into a variable instead of the screen
    captured_output = io.StringIO()
    original_stdout = sys.stdout
    
    sys.stdout = captured_output
    print("This goes to the variable, not the screen.")
    sys.stdout = original_stdout # Restore standard output
    
    print("Captured text was:", captured_output.getvalue().strip())

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Forgetting to reset ANSI colors.
# print("\033[31mRed text")
# print("This will also be red if not reset!")

# Correction: Always append the RESET code.
# print("\033[31mRed text\033[0m")

# Mistake: Using \r without enough padding, leaving trailing characters.
# print("Very long line", end="\r")
# print("Short") -> Output looks like "Shortong line"

# Best Practice: Use libraries like `colorama` or `rich` for terminal colors in production, as ANSI codes don't work natively in all older Windows terminals without setup.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: How do you create a progress bar in the terminal?
A: By using a loop, printing the progress, and ending the print statement with a carriage return (\r) and `flush=True` to overwrite the same line repeatedly.

Q: What does sys.stdout represent?
A: It is the standard output stream, typically the console/terminal. The print function writes to it by default.

Q: How can you write a Python script that prints to a file without opening the file in Python?
A: Run the script from the command line and use the redirection operator: `python script.py > output.txt`.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def practice_exercises():
    # 1. Print a warning message in yellow (ANSI code 33).
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    print(f"{YELLOW}WARNING: Low disk space.{RESET}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Create a fake "downloading" progress bar that updates on a single line.
    (e.g., [===>    ] 50%)
    """
    import time
    print("Downloading...")
    total = 20
    # Uncomment to see animation
    # for i in range(total + 1):
    #     percent = (i / total) * 100
    #     bar = "=" * i + ">" + " " * (total - i)
    #     print(f"\r[{bar}] {percent:.0f}%", end="", flush=True)
    #     time.sleep(0.05)
    # print("\nDownload complete!")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Carriage returns (\r) allow overwriting text on the same line in the terminal.
- Flush parameter is necessary for real-time terminal updates.
- ANSI escape sequences can add color and style to output.
- Print output can be redirected by modifying sys.stdout.
"""

if __name__ == "__main__":
    practical_examples()
    advanced_usage()
    practice_exercises()
    mini_challenge()
