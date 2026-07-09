"""
Topic: Set Practice Exercises
Chapter: 12
Level: Beginner to Intermediate

Description:
    This file contains a series of practical exercises to test and solidify your understanding of Python sets. Working through these exercises will build muscle memory for common set operations and methods.

Real-Life Analogy:
    Like doing drills in a sport. Knowing the rules (syntax) is good, but running drills (practice) is what makes you ready for the game.

Key Concepts:
    - Set creation and mutation
    - Set operations
    - Problem solving with sets
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def ex1_create_and_modify():
    # Task: Create a set of your 3 favorite colors.
    # Add another color, then remove the first one you added.
    colors = {"red", "blue", "green"}
    colors.add("purple")
    colors.remove("red")
    print("Exercise 1:", colors)
    return colors

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def ex2_common_elements():
    # Task: Given two lists of names, find the names that appear in BOTH lists.
    list1 = ["Alice", "Bob", "Charlie", "David"]
    list2 = ["Charlie", "Eve", "Alice", "Frank"]
    
    # Write your logic here
    common = set(list1) & set(list2)
    print("Exercise 2:", common)
    return common

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def ex3_unique_characters():
    # Task: Write a function that takes a sentence and returns the number 
    # of unique alphabetic characters used in it (case-insensitive).
    sentence = "The quick brown fox jumps over the lazy dog"
    
    # Write your logic here
    clean_chars = {char.lower() for char in sentence if char.isalpha()}
    unique_count = len(clean_chars)
    
    print("Exercise 3 - Unique letters:", unique_count)
    return unique_count

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def ex4_find_differences():
    # Task: Given a default config set and a user config set, 
    # find configs that the user is missing, and custom configs the user added.
    default_config = {"dark_mode", "auto_save", "notifications"}
    user_config = {"dark_mode", "sound_on", "auto_save"}
    
    missing = default_config - user_config
    custom = user_config - default_config
    
    print("Exercise 4 - Missing:", missing)
    print("Exercise 4 - Custom:", custom)
    return missing, custom

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: How do you remove an element without raising an error if it doesn't exist?
# A: Use the .discard() method instead of .remove().
#
# Q2: How do you merge multiple sets together?
# A: Use the .union() method or the | operator (e.g., s1 | s2 | s3).

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def ex5_pangram_checker():
    # Task: Check if a string is a pangram (contains every letter of the alphabet).
    import string
    
    def is_pangram(text):
        alphabet = set(string.ascii_lowercase)
        text_letters = {char.lower() for char in text if char.isalpha()}
        return alphabet.issubset(text_letters)
        
    sentence1 = "The quick brown fox jumps over the lazy dog"
    sentence2 = "Hello world"
    
    print(f"Exercise 5 - Is '{sentence1}' a pangram? {is_pangram(sentence1)}")
    print(f"Exercise 5 - Is '{sentence2}' a pangram? {is_pangram(sentence2)}")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    # Task: Given a list of integers, find the length of the longest 
    # consecutive elements sequence.
    # E.g., [100, 4, 200, 1, 3, 2] -> 4 (because of 1, 2, 3, 4)
    # Target time complexity: O(N) using sets.
    
    nums = [100, 4, 200, 1, 3, 2]
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# Practice is essential for mastering sets.
# Focus on identifying when a problem requires finding unique elements
# or doing fast lookups, as these are strong indicators for using a set.

if __name__ == "__main__":
    print("--- Section 1 ---")
    ex1_create_and_modify()
    print("\n--- Section 2 ---")
    ex2_common_elements()
    print("\n--- Section 3 ---")
    ex3_unique_characters()
    print("\n--- Section 4 ---")
    ex4_find_differences()
    print("\n--- Section 6 ---")
    ex5_pangram_checker()
    print("\n--- Section 7 ---")
    print("Longest consecutive sequence length:", mini_challenge())
