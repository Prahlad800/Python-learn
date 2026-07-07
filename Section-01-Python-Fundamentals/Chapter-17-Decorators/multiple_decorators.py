# Topic: Multiple Decorators
# Explanation: You can apply more than one decorator to a function.

# Syntax:
# def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def message():
    return "Python"

print(message())

# Examples:
# def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def message():
    return "Python"

print(message())

# Practice Programs:
# 1. Apply two simple decorators.
2. Show the order of execution.

# Interview Questions:
# Q: How do multiple decorators work?
A: They are applied from the bottom up.

# Expected Output:
# <b><i>Python</i></b>

def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def message():
    return "Python"

print(message())
