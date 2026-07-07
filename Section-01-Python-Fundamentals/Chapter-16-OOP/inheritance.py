# Topic: Inheritance
# Explanation: Inheritance allows one class to reuse another class.

# Syntax:
# class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    pass

my_dog = Dog()
my_dog.speak()

# Examples:
# class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    pass

my_dog = Dog()
my_dog.speak()

# Practice Programs:
# 1. Create a parent class and child class.
2. Call a parent method from the child.

# Interview Questions:
# Q: What is inheritance?
A: It enables code reuse through parent-child relationships.

# Expected Output:
# Animal

class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    pass

my_dog = Dog()
my_dog.speak()
