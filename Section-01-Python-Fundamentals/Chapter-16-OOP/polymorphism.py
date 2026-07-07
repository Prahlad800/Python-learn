# Topic: Polymorphism
# Explanation: Polymorphism allows different classes to respond to the same method name.

# Syntax:
# class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

for animal in (Cat(), Dog()):
    animal.speak()

# Examples:
# class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

for animal in (Cat(), Dog()):
    animal.speak()

# Practice Programs:
# 1. Create two classes with the same method name.
2. Call the method on both objects.

# Interview Questions:
# Q: What is polymorphism?
A: It lets different objects respond to the same method call differently.

# Expected Output:
# Meow
Woof

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

for animal in (Cat(), Dog()):
    animal.speak()
