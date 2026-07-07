"""Learning file for Polymorphism."""

# Topic Name: Polymorphism
# Level: Intermediate
# Polymorphism lets different object types respond to the same interface in their own way.
# Read the theory first, then run this file and modify examples.

# Theory
# Polymorphism lets different object types respond to the same interface in their own way.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# def draw(shape):
#     shape.draw()

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses polymorphism
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
class EmailNotification:
    def send(self):
        return "Email sent"


class SmsNotification:
    def send(self):
        return "SMS sent"


def notify(channel):
    return channel.send()


def example_polymorphism():
    for channel in [EmailNotification(), SmsNotification()]:
        print(notify(channel))


def practice_send_all(channels):
    return [notify(channel) for channel in channels]


def main():
    print("--- Polymorphism ---")
    example_polymorphism()
    print("All:", practice_send_all([EmailNotification(), SmsNotification()]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Polymorphism ---
# Email sent
# SMS sent
# All: ['Email sent', 'SMS sent']
# End Expected Output
