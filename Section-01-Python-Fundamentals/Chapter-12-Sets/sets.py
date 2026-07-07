"""Learning file for Sets."""

# Topic Name: Sets
# Level: Beginner
# Sets store unique unordered values and are perfect for deduplication and fast membership checks.
# Read the theory first, then run this file and modify examples.

# Theory
# Sets store unique unordered values and are perfect for deduplication and fast membership checks.
# Good Python code favors clear names, small functions, and
# predictable behavior that can be tested.

# Syntax
# unique = {1, 2, 3}
# empty = set()
# unique.add(4)

# Practice Programs
# 1. Find common students between two clubs.
# 2. Remove duplicate emails from a list.
# 3. Compare required and submitted documents.

# Mini Project
# Build a tiny program that uses sets
# with realistic sample data, validation, and printed output.

# Interview Questions
# Q1. What are sets optimized for?
# A1. Uniqueness and fast membership tests.
# Q2. Do sets preserve order?
# A2. Do not rely on set ordering; use a list when order matters.

# Examples and practice implementations start below.
def example_unique_values():
    numbers = [1, 2, 2, 3, 3, 3]
    unique_numbers = set(numbers)
    print("Unique:", unique_numbers)


def example_membership():
    blocked_users = {"spam1", "spam2"}
    print("spam1 blocked:", "spam1" in blocked_users)


def practice_unique_emails(emails):
    return set(email.lower().strip() for email in emails)


def main():
    print("--- Sets ---")
    example_unique_values()
    example_membership()
    print("Emails:", practice_unique_emails(["A@X.COM", "a@x.com", " b@y.com "]))


if __name__ == "__main__":
    main()

# Expected Output (sample):
# Run this file with Python to reproduce the lesson output.
# --- Sets ---
# Unique: {1, 2, 3}
# spam1 blocked: True
# Emails: {'a@x.com', 'b@y.com'}
# End Expected Output
