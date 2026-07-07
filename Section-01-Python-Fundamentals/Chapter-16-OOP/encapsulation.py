"""Learning file for Encapsulation."""

# Topic Name: Encapsulation
# Level: Intermediate
# Encapsulation protects object state behind methods and properties.
# Read the theory first, then run this file and modify examples.

# Theory
# Encapsulation protects object state behind methods and properties.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# self._protected
# self.__private
# @property

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses encapsulation
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount


def example_encapsulation():
    account = BankAccount("Asha", 1000)
    account.deposit(500)
    print(account.owner, account.balance)


def practice_account(owner, balance):
    return BankAccount(owner, balance)


def main():
    print("--- Encapsulation ---")
    example_encapsulation()
    print("Practice balance:", practice_account("Ravi", 300).balance)


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Encapsulation ---
# Asha 1500
# Practice balance: 300
# End Expected Output
