"""Learning file for Introduction to Python."""

# Topic Name: Introduction to Python
# Level: Beginner
# Python is a readable, general-purpose language used for automation, web apps, data, AI, scripting, and testing.
# Read the theory first, then run this file and modify examples.

# Theory
# Python is a readable, general-purpose language used for automation, web apps, data, AI, scripting, and testing.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# print('Python is running')
# name = 'Learner'
# if __name__ == '__main__': main()

# Practice Programs
# 1. Print your name, city, and learning goal.
# 2. Create a short script with a main() function.
# 3. Add comments that explain the purpose of each line.

# Mini Project
# Build a tiny program that uses introduction to python
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Why is Python popular?
# A1. It is readable, versatile, has a huge ecosystem, and supports many programming styles.
# Q2. What does the main guard do?
# A2. It lets code run only when the file is executed directly, not when imported.

# Examples and practice implementations start below.
def example_python_uses():
    uses = ["automation", "web development", "data analysis", "AI"]
    for index, use in enumerate(uses, start=1):
        print(f"{index}. {use}")


def example_readability():
    learner = "Asha"
    hours = 2
    print(f"{learner} studies Python for {hours} hours daily.")


def practice_learning_plan(days):
    return [f"Day {day}: practice Python" for day in range(1, days + 1)]


def main():
    print("--- Introduction to Python ---")
    example_python_uses()
    example_readability()
    print("Plan:", practice_learning_plan(3))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Introduction to Python ---
# 1. automation
# 2. web development
# 3. data analysis
# 4. AI
# Asha studies Python for 2 hours daily.
# Plan: ['Day 1: practice Python', 'Day 2: practice Python', 'Day 3: practice Python']
# End Expected Output
