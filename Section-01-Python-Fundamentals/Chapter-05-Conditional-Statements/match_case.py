# Topic: match-case Statement
# Explanation: match-case compares a value against multiple patterns.

# Syntax:
# day = "Monday"
match day:
    case "Monday":
        print("Start of week")
    case _:
        print("Other day")

# Examples:
# day = "Monday"
match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("Weekend is near")
    case _:
        print("Other day")

# Practice Programs:
# 1. Match a month name.
2. Build a simple calculator using match-case.

# Interview Questions:
# Q: What is the purpose of match-case?
A: It is a cleaner alternative to many elif blocks.

# Expected Output:
# Start of week

day = "Monday"
match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("Weekend is near")
    case _:
        print("Other day")
