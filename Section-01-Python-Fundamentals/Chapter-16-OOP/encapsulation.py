# Topic: Encapsulation
# Explanation: Encapsulation hides internal details and exposes safe methods.

# Syntax:
# class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())

# Examples:
# class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())

# Practice Programs:
# 1. Create a class with a private attribute.
2. Access it via a method.

# Interview Questions:
# Q: What does encapsulation protect?
A: It protects data by controlling access.

# Expected Output:
# 100

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())
