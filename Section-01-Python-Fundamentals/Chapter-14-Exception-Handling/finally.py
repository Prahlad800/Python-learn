"""Learning file for finally Block."""

# Topic Name: finally Block
# Level: Beginner
# finally runs cleanup code whether an exception happens or not.
# Read the theory first, then run this file and modify examples.

# Theory
# finally runs cleanup code whether an exception happens or not.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# try:
#     open_resource()
# finally:
#     close_resource()

# Practice Programs
# 1. Handle invalid integer input.
# 2. Raise an error for negative age.
# 3. Create a custom exception for low account balance.

# Mini Project
# Build a tiny program that uses finally block
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Should you catch bare Exception everywhere?
# A1. No. Catch specific exceptions so unrelated bugs are not hidden.
# Q2. When should you raise exceptions?
# A2. Raise when a function cannot complete its contract with the given data.

# Examples and practice implementations start below.
def example_finally():
    events = []
    try:
        events.append("open")
        events.append("work")
    finally:
        events.append("close")
    print("Events:", events)


def example_finally_with_error():
    try:
        int("bad")
    except ValueError:
        print("Handled ValueError")
    finally:
        print("Cleanup completed")


def practice_resource_log():
    log = []
    try:
        log.append("resource acquired")
    finally:
        log.append("resource released")
    return log


def main():
    print("--- finally Block ---")
    example_finally()
    example_finally_with_error()
    print("Log:", practice_resource_log())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- finally Block ---
# Events: ['open', 'work', 'close']
# Handled ValueError
# Cleanup completed
# Log: ['resource acquired', 'resource released']
# End Expected Output
