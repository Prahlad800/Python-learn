"""Learning file for Bitwise Operators."""

# Topic Name: Bitwise Operators
# Level: Intermediate
# Bitwise operators work on individual bits and are useful for flags, masks, permissions, and low-level algorithms.
# Read the theory first, then run this file and modify examples.

# Theory
# Bitwise operators work on individual bits and are useful for flags, masks, permissions, and low-level algorithms.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# a & b
# a | b
# a ^ b
# ~a
# a << 1
# a >> 1

# Practice Programs
# 1. Build a calculator for two numbers.
# 2. Check whether a number is even, positive, and inside a range.
# 3. Use membership and comparison operators to validate a role.

# Mini Project
# Build a tiny program that uses bitwise operators
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is operator precedence?
# A1. It is the order in which Python evaluates operators in an expression.
# Q2. What is short-circuit evaluation?
# A2. and/or stop evaluating as soon as the final boolean result is known.

# Examples and practice implementations start below.
def example_operations():
    a = 10
    b = 3
    print("and:", a & b)
    print("or:", a | b)
    print("xor:", a ^ b)
    print("left_shift:", a << 1)
    print("right_shift:", a >> 1)

def practice_has_permission(flags, permission):
    return (flags & permission) == permission


def main():
    print("--- Bitwise Operators ---")
    example_operations()
    read_permission = 0b001
    write_permission = 0b010
    user_flags = read_permission | write_permission
    print("Can write:", practice_has_permission(user_flags, write_permission))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Bitwise Operators ---
# and: 2
# or: 11
# xor: 9
# left_shift: 20
# right_shift: 5
# Can write: True
# End Expected Output
