# Topic: Custom Exceptions
# Explanation: You can create custom exception classes for domain-specific errors.

# Syntax:
# class InvalidAgeError(Exception):
    pass

try:
    raise InvalidAgeError("Age is not valid")
except InvalidAgeError as error:
    print(error)

# Examples:
# class InvalidAgeError(Exception):
    pass

try:
    raise InvalidAgeError("Age is not valid")
except InvalidAgeError as error:
    print(error)

# Practice Programs:
# 1. Create a custom exception for invalid password.
2. Raise it in a function.

# Interview Questions:
# Q: Why use custom exceptions?
A: They make code more expressive and easier to debug.

# Expected Output:
# Age is not valid

class InvalidAgeError(Exception):
    pass

try:
    raise InvalidAgeError("Age is not valid")
except InvalidAgeError as error:
    print(error)
