"""Learning file for Magic Methods."""

# Topic Name: Magic Methods
# Level: Advanced
# Magic methods customize how objects behave with built-in Python operations.
# Read the theory first, then run this file and modify examples.

# Theory
# Magic methods customize how objects behave with built-in Python operations.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# __str__
# __repr__
# __len__
# __add__

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses magic methods
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Rs.{self.amount:.2f}"

    def __repr__(self):
        return f"Money(amount={self.amount!r})"

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __len__(self):
        return len(str(int(self.amount)))


def example_magic_methods():
    wallet = Money(150.5)
    bonus = Money(49.5)
    print("Wallet:", wallet)
    print("Total:", wallet + bonus)
    print("Digits:", len(wallet))


def main():
    print("--- Magic Methods ---")
    example_magic_methods()


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Magic Methods ---
# Wallet: Rs.150.50
# Total: Rs.200.00
# Digits: 3
# End Expected Output
