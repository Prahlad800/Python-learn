"""Learning file for Abstraction."""

# Topic Name: Abstraction
# Level: Intermediate
# Abstraction hides implementation details behind a simple interface.
# Read the theory first, then run this file and modify examples.

# Theory
# Abstraction hides implementation details behind a simple interface.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# from abc import ABC, abstractmethod
# @abstractmethod

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses abstraction
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        """Process a payment and return a status message."""


class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid Rs.{amount} by card"


def checkout(payment_method, amount):
    return payment_method.pay(amount)


def main():
    print("--- Abstraction ---")
    payment = CardPayment()
    print(checkout(payment, 500))
    print("Concrete class:", isinstance(payment, Payment))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Abstraction ---
# Paid Rs.500 by card
# Concrete class: True
# End Expected Output
