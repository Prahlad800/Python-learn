# Topic: OOP Mini Project
# Explanation: Build a small class-based project such as a bank account.

# Syntax:
# class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount("Asha", 100)
print(account.deposit(50))

# Examples:
# class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount("Asha", 100)
print(account.deposit(50))

# Practice Programs:
# 1. Add methods for deposit and withdraw.
2. Store multiple accounts.

# Interview Questions:
# Q: Why is OOP useful in projects?
A: It organizes code into reusable components.

# Expected Output:
# 150

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount("Asha", 100)
print(account.deposit(50))
