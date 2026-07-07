# Topic: Recursion
# Explanation: Recursion solves a problem by calling itself with a smaller input.

# Syntax:
# def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Examples:
# def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Practice Programs:
# 1. Write a recursive function for Fibonacci.
2. Write a recursive function for sum of 1..n.

# Interview Questions:
# Q: What must recursion include?
A: A base case to stop calling itself.

# Expected Output:
# 120

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
