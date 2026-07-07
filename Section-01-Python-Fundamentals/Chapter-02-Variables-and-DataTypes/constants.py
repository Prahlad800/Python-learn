"""Learning file for Constants."""

# Topic Name: Constants
# Level: Beginner
# Python constants are a naming convention; uppercase names signal values that should not change.
# Read the theory first, then run this file and modify examples.

# Theory
# Python constants are a naming convention; uppercase names signal values that should not change.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# PI = 3.14159
# MAX_LOGIN_ATTEMPTS = 3
# @dataclass(frozen=True)

# Practice Programs
# 1. Store a student's details using suitable data types.
# 2. Convert numeric strings into numbers and calculate a total.
# 3. Validate a piece of text before converting it.

# Mini Project
# Build a tiny program that uses constants
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. Is Python statically typed?
# A1. No. Python is dynamically typed; names can refer to objects of different types over time.
# Q2. What is the difference between mutable and immutable types?
# A2. Mutable objects can change in place; immutable objects create new values when changed.

# Examples and practice implementations start below.
from dataclasses import dataclass


PI = 3.14159
MAX_LOGIN_ATTEMPTS = 3


@dataclass(frozen=True)
class AppConfig:
    app_name: str
    version: str


def example_constants():
    radius = 2
    area = PI * radius ** 2
    print("Circle area:", round(area, 2))
    print("Max attempts:", MAX_LOGIN_ATTEMPTS)


def practice_config():
    return AppConfig(app_name="Python Learn", version="1.0")


def main():
    print("--- Constants ---")
    example_constants()
    print("Config:", practice_config())


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Constants ---
# Circle area: 12.57
# Max attempts: 3
# Config: AppConfig(app_name='Python Learn', version='1.0')
# End Expected Output
