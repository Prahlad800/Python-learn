"""
Topic: Membership Operators
Chapter: 3
Level: Beginner

Description:
    Membership operators are used to test if a sequence (like a string, list, tuple, or set) contains a specific value.

Real-Life Analogy:
    Imagine checking if your name is on a guest list for a party. If it is, you're a member (in). If it's not, you're excluded (not in).

Key Concepts:
    - in
    - not in
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================
def basic_syntax():
    print("--- Section 1: Basic Syntax ---")
    fruits = ["apple", "banana", "cherry"]
    
    # Using 'in'
    print(f"Is 'banana' in fruits? {'banana' in fruits}")
    print(f"Is 'grape' in fruits? {'grape' in fruits}")
    
    # Using 'not in'
    print(f"Is 'orange' not in fruits? {'orange' not in fruits}")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================
def practical_examples():
    print("\n--- Section 2: Practical Examples ---")
    # Example 1: Checking for characters in a string
    vowels = "aeiou"
    letter = 'e'
    if letter in vowels:
        print(f"'{letter}' is a vowel.")

    # Example 2: Validating user input
    valid_commands = ["start", "stop", "pause"]
    command = "jump"
    if command not in valid_commands:
        print(f"Invalid command: {command}")
        
    # Example 3: Dictionary membership (checks keys, not values)
    student_scores = {"Alice": 90, "Bob": 85}
    if "Alice" in student_scores:
        print(f"We have Alice's score: {student_scores['Alice']}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================
def advanced_usage():
    print("\n--- Section 3: Advanced Usage ---")
    # Substring search in strings (very efficient)
    sentence = "The quick brown fox jumps over the lazy dog."
    print(f"Does it contain 'brown fox'? {'brown fox' in sentence}")
    
    # Set membership (O(1) time complexity)
    # Checking membership in a large set is much faster than in a large list (O(n)).
    large_list = list(range(10000))
    large_set = set(large_list)
    
    print(f"9999 in large_list: {9999 in large_list}") # Slower, has to scan
    print(f"9999 in large_set: {9999 in large_set}")   # Instant, hash lookup

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================
# Common Mistakes:
# 1. Using `in` to check for values in a dictionary directly (it checks keys). To check values, use `val in my_dict.values()`.
# 2. Iterating manually to find an element instead of just using `in`.
# 3. Using lists for membership checks with a massive amount of data instead of sets.
#
# Best Practices:
# 1. Convert lists to sets if you need to do many membership tests.
# 2. Use `substring in string` instead of `string.find(substring) != -1`.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
# Q1: What is the time complexity of the `in` operator for a list vs. a set?
# A: O(n) for lists (linear search) and O(1) average case for sets (hash table lookup).
#
# Q2: Can you use `in` on custom objects?
# A: Yes, if the class implements the `__contains__` magic method or is iterable.
#
# Q3: Does `"abc" in "a b c"` evaluate to True?
# A: No, it checks for the exact contiguous substring. Space breaks it.
#
# Q4: How do you check if a value exists in a dictionary?
# A: `value in my_dict.values()`.
#
# Q5: Does `not in` evaluate as `not (x in y)`?
# A: Yes, functionally it is identical, but `x not in y` is more readable and pythonic.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
# 1. Given a list of prohibited words, write a script that checks if a user's comment contains any of them.
# 2. Use `in` to check if the substring "@gmail.com" is present in an email string.
# 3. Create a dictionary and check if a specific key exists using the `in` operator.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
def mini_challenge():
    print("\n--- Section 7: Mini Challenge ---")
    # You are building a spam filter.
    # Given an email body and a list of spam trigger words, 
    # check if the email is spam. It's spam if it contains at least 2 trigger words.
    spam_words = {"free", "winner", "cash", "prize", "urgent"}
    
    email_body = "Congratulations, you are a winner! Claim your free cash prize now. Urgent!"
    
    # Convert email to lowercase and split into words
    words = email_body.lower().replace(",", "").replace("!", "").replace(".", "").split()
    
    spam_count = 0
    for word in words:
        if word in spam_words:
            spam_count += 1
            
    is_spam = spam_count >= 2
    print(f"Spam count: {spam_count}")
    print(f"Is this email spam? {is_spam}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# - `in` and `not in` test for sequence membership.
# - They work with strings, lists, tuples, sets, and dictionary keys.
# - For large datasets, using a set for membership testing is significantly faster than using a list.

if __name__ == "__main__":
    basic_syntax()
    practical_examples()
    advanced_usage()
    mini_challenge()
