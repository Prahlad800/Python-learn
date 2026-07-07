# Topic: Constructors
# Explanation: The __init__ method initializes object attributes.

# Syntax:
# class Student:
    def __init__(self, name):
        self.name = name

student = Student("Asha")
print(student.name)

# Examples:
# class Student:
    def __init__(self, name):
        self.name = name

student = Student("Asha")
print(student.name)

# Practice Programs:
# 1. Create a class with a constructor.
2. Initialize name and age.

# Interview Questions:
# Q: What is a constructor?
A: It initializes an object at creation time.

# Expected Output:
# Asha

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Asha")
print(student.name)
