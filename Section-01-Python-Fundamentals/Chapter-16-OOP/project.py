"""Learning file for OOP Mini Project."""

# Topic Name: OOP Mini Project
# Level: Advanced
# An OOP mini project combines classes, encapsulation, methods, and object collaboration.
# Read the theory first, then run this file and modify examples.

# Theory
# An OOP mini project combines classes, encapsulation, methods, and object collaboration.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# class Task:
# class TodoList:
# todo.add_task(...)

# Practice Programs
# 1. Model a bank account class.
# 2. Use inheritance for different employee types.
# 3. Build a small task manager project.

# Mini Project
# Build a tiny program that uses oop mini project
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What is self?
# A1. self is the instance being operated on by an instance method.
# Q2. What is encapsulation?
# A2. Keeping data and behavior together while controlling access to internal state.

# Examples and practice implementations start below.
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "done" if self.completed else "pending"
        return f"{self.title} [{status}]"


class TodoList:
    def __init__(self):
        self._tasks = []

    def add_task(self, title):
        task = Task(title)
        self._tasks.append(task)
        return task

    def complete_task(self, title):
        for task in self._tasks:
            if task.title == title:
                task.mark_done()
                return task
        raise ValueError("Task not found.")

    def pending_tasks(self):
        return [task for task in self._tasks if not task.completed]


def main():
    print("--- OOP Mini Project ---")
    todo = TodoList()
    todo.add_task("Read OOP chapter")
    todo.add_task("Build project")
    todo.complete_task("Read OOP chapter")
    print("Pending:", [str(task) for task in todo.pending_tasks()])


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- OOP Mini Project ---
# Pending: ['Build project [pending]']
# End Expected Output
