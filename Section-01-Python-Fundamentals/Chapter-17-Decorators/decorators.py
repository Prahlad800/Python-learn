# Topic: Decorators
# Explanation: Decorators wrap functions and modify their behavior.

# Syntax:
# def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    return "hello"

print(greet())

# Examples:
# def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    return "hello"

print(greet())

# Practice Programs:
# 1. Create a decorator that logs function calls.
2. Apply it to a simple function.

# Interview Questions:
# Q: What is a decorator?
A: It is a function that takes another function and extends or changes its behavior.

# Expected Output:
# HELLO

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    return "hello"

print(greet())
