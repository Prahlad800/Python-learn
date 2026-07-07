# Topic: Abstraction
# Explanation: Abstraction focuses on essential behavior and hides implementation details.

# Syntax:
# from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print(Rectangle(3, 4).area())

# Examples:
# from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print(Rectangle(3, 4).area())

# Practice Programs:
# 1. Create an abstract class.
2. Implement it in a subclass.

# Interview Questions:
# Q: What is abstraction?
A: It exposes only what is necessary and hides complexity.

# Expected Output:
# 12

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print(Rectangle(3, 4).area())
