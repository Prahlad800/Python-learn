"""
Topic: Lambda Functions
Chapter: 7
Level: Beginner / Intermediate

Description:
    Lambda functions, also known as anonymous functions, are small, unnamed functions defined using the `lambda` keyword. They are typically used for short, throwaway operations where a full `def` statement would be overkill.

Real-Life Analogy:
    Think of a lambda function like a disposable paper cup. You use it once or twice for a quick drink and then throw it away, whereas a regular function is like a sturdy ceramic mug you keep in your cupboard for repeated use.

Key Concepts:
    - Anonymous functions
    - The `lambda` keyword
    - Single expression limitation
    - Use with `map()`, `filter()`, and `sorted()`
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The syntax is: lambda arguments: expression
# Here is a regular function:
def add_ten(x: int) -> int:
    return x + 10

# Here is the equivalent lambda function:
add_ten_lambda = lambda x: x + 10

# Let's see them in action
regular_result = add_ten(5)
lambda_result = add_ten_lambda(5)

print(f"Regular function result: {regular_result}")
print(f"Lambda function result: {lambda_result}")

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(f"Multiplying 4 and 5 gives: {multiply(4, 5)}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Sorting a list of tuples by the second element
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
print(f"Students sorted by grade: {sorted_students}")

# Example 2: Using filter() to get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Example 3: Using map() to square numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Example 4: Extracting specific data from dictionaries
users = [
    {"name": "John", "age": 28},
    {"name": "Jane", "age": 22},
    {"name": "Doe", "age": 35}
]
# Sort users by age
users_by_age = sorted(users, key=lambda u: u["age"])
print(f"Users sorted by age: {users_by_age}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 1: IIFE (Immediately Invoked Function Expression)
# You can define and call a lambda in the same line
iife_result = (lambda x, y: x**2 + y**2)(3, 4)
print(f"Result of IIFE (3^2 + 4^2): {iife_result}")

# Example 2: Lambda returning another lambda (Closure-like)
def power_factory(n: int):
    return lambda x: x ** n

square = power_factory(2)
cube = power_factory(3)
print(f"Square of 5: {square(5)}")
print(f"Cube of 5: {cube(5)}")

# Example 3: Conditional expressions within a lambda
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"Is 4 even or odd? {is_even(4)}")
print(f"Is 7 even or odd? {is_even(7)}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Trying to use multiple statements
# INCORRECT: lambda x: print(x); return x + 1 (SyntaxError)
# BEST PRACTICE: Keep lambdas strictly to a single expression.

# Mistake 2: Assigning lambdas to names unnecessarily
# INCORRECT (violates PEP 8): 
# my_func = lambda x: x * 2
# BEST PRACTICE: If you are assigning it to a name, use 'def'.
def my_func(x):
    return x * 2

# Mistake 3: Overusing lambdas for complex logic
# If the logic is hard to read, write a proper function instead.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a lambda function in Python?
# A: It is a small, anonymous function defined with the `lambda` keyword. It can take any number of arguments but can only have one expression.

# Q2: Why would you use a lambda function?
# A: They are ideal for short, throwaway functions, especially as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

# Q3: Can a lambda function contain a return statement?
# A: No. The expression evaluated by the lambda function is automatically returned.

# Q4: Are lambda functions faster than regular functions?
# A: No. They run at the same speed. The only difference is in their syntax and anonymity.

# Q5: Can lambda functions have type hints?
# A: Technically yes, but it is highly unconventional and generally unsupported by typical type checkers directly in the lambda syntax. It's better to use `def` if type hints are needed.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Write a lambda function that takes a string and returns it in uppercase.
to_upper = lambda s: s.upper()

# Exercise 2: Use `filter` and a lambda to extract words longer than 5 characters from a list.
words = ["apple", "banana", "kiwi", "strawberry", "grape"]
long_words = list(filter(lambda w: len(w) > 5, words))

# Exercise 3: Use `map` and a lambda to convert a list of temperatures in Celsius to Fahrenheit.
# Formula: (C * 9/5) + 32
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Given a list of dictionaries representing products with 'name' and 'price',
# write code to find the name of the most expensive product using `max()` and a lambda.
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300}
]

# Solution:
most_expensive = max(products, key=lambda p: p["price"])
print(f"The most expensive product is: {most_expensive['name']}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Lambda functions are anonymous, single-expression functions.
# - They are defined using the `lambda` keyword.
# - Best used for short operations, often passed to `map`, `filter`, or `sorted`.
# - Avoid naming lambdas; use `def` instead if you need a named function.
# - They support conditionals but not multiple statements.

if __name__ == "__main__":
    pass
