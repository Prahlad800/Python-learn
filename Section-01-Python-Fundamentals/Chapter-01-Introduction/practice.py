"""Learning file for Introduction Practice Programs."""

# Topic Name: Introduction Practice Programs
# Level: Beginner
# Introduction Practice Programs reinforces the chapter with runnable examples.
# Read the theory first, then run this file and modify examples.

# Theory
# Introduction Practice Programs reinforces the chapter with runnable examples.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# # See the runnable examples below for the topic syntax.

# Practice Programs
# 1. Print your name, city, and learning goal.
# 2. Create a short script with a main() function.
# 3. Add comments that explain the purpose of each line.

# Mini Project
# Build a tiny program that uses introduction practice programs
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why is Python popular?
# A1. It is readable, versatile, has a huge ecosystem, and supports many programming styles.
# Q2. What does the main guard do?
# A2. It lets code run only when the file is executed directly, not when imported.

# Examples and practice implementations start below.
def print_profile(name, city, goal):
    return f"{name} from {city} wants to learn {goal}."


def repeat_message(message, times):
    return [message for _ in range(times)]


def practice_ascii_banner(text):
    border = "=" * len(text)
    return f"{border}\n{text}\n{border}"


def main():
    print("--- Introduction Practice Programs ---")
    print(print_profile("Asha", "Delhi", "Python"))
    print("Messages:", repeat_message("Practice daily", 3))
    print(practice_ascii_banner("PYTHON"))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Introduction Practice Programs ---
# Asha from Delhi wants to learn Python.
# Messages: ['Practice daily', 'Practice daily', 'Practice daily']
# ======
# PYTHON
# ======
# End Expected Output
