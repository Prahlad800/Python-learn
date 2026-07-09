"""
Topic: Dictionary Practice Exercises
Chapter: 11
Level: Intermediate

Description:
    This file contains comprehensive practice exercises to reinforce dictionary concepts,
    including creation, methods, iteration, and comprehensions.

Real-Life Analogy:
    Practice is like going to the gym. You've learned the theory of how the machines work, 
    but you need to put in the reps to build the muscle memory for solving real-world problems.

Key Concepts:
    - Applying dictionary methods
    - Data transformation
    - Nested data processing
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Practice sets up various basic data structures to work with.

student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95
}

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (SOLUTIONS TO COMMON PROBLEMS)
# ============================================================

# Problem 1: Find the student with the highest score
def find_top_student(scores):
    top_student = None
    highest_score = -1
    for student, score in scores.items():
        if score > highest_score:
            highest_score = score
            top_student = student
    return top_student, highest_score

print(f"Top student: {find_top_student(student_scores)}")

# Problem 2: Grouping items
# Group words by their starting letter
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
def group_by_first_letter(word_list):
    grouped = {}
    for word in word_list:
        first_char = word[0]
        if first_char not in grouped:
            grouped[first_char] = []
        grouped[first_char].append(word)
    return grouped

print(f"Grouped words: {group_by_first_letter(words)}")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Problem 3: Frequency counter
def count_characters(text):
    # Ignoring spaces and making lowercase
    cleaned_text = text.replace(" ", "").lower()
    freq = {}
    for char in cleaned_text:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(f"Character frequencies: {count_characters('Hello World')}")

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Modifying dictionary while iterating over it in a practice problem
# BAD: for k, v in my_dict.items(): if v == 0: del my_dict[k]
# GOOD: 
def remove_zeros(d):
    # Create a new dictionary using comprehension
    return {k: v for k, v in d.items() if v != 0}

test_dict = {"a": 1, "b": 0, "c": 3, "d": 0}
print(f"Without zeros: {remove_zeros(test_dict)}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q1: How do you sort a dictionary by its values?
A: You can use the built-in sorted() function on dict.items() with a custom lambda key.
   Example: dict(sorted(my_dict.items(), key=lambda item: item[1]))

Q2: Write a function to merge two dictionaries, summing the values of common keys.
A: 
def merge_and_sum(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

Q3: How do you check if two dictionaries have the exact same key-value pairs?
A: You can simply use the equality operator: dict1 == dict2.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# EXERCISE 1: Dictionary to List of Tuples
# Write a function that converts a dictionary into a list of (key, value) tuples.
def dict_to_tuples(d):
    return list(d.items())

# EXERCISE 2: List of Tuples to Dictionary
# Write a function that converts a list of (key, value) tuples back into a dictionary.
def tuples_to_dict(t_list):
    return dict(t_list)

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """
    Challenge: Anagram Grouper
    Given a list of strings, group anagrams together.
    An anagram is a word formed by rearranging the letters of a different word.
    Example Input: ["eat","tea","tan","ate","nat","bat"]
    """
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagrams = {}
    
    for word in words:
        # Sort the word to create a unique key for anagrams
        sorted_word = "".join(sorted(word))
        
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
        
    # Print the grouped anagrams as a list of lists
    print("Grouped Anagrams:", list(anagrams.values()))

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Practice combines methods like .get(), .items(), and loops.
- Grouping, counting, and transforming are common real-world dictionary operations.
- Remember to avoid modifying a dictionary size during iteration.
- Comprehensions are powerful tools for creating new filtered/transformed dictionaries.
"""

if __name__ == "__main__":
    mini_challenge()
