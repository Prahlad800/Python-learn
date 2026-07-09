"""
Topic: Set Mini Project
Chapter: 12
Level: Intermediate

Description:
    This mini-project synthesizes the set concepts learned in this chapter. We will build a simple "Spell Checker and Text Analyzer". It will analyze a block of text, find misspelled words based on a dictionary, and provide statistics about unique word usage.

Real-Life Analogy:
    Like a teacher grading an essay. The teacher has a mental dictionary of correct words (a set). They read the essay, identify words not in their dictionary (difference), and count how varied the student's vocabulary is (length of unique words).

Key Concepts:
    - Text parsing and sanitization
    - Set differences for spell checking
    - Set intersections for overlap analysis
"""

import re

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Mock Dictionary Data
VALID_WORDS = {
    "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", 
    "hello", "world", "python", "is", "awesome", "coding", "fun"
}

def clean_text(text):
    # Convert to lowercase and remove punctuation
    # Using regex to extract just alphabetic words
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return words

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def spell_check(words_list):
    # Convert input text to a set of unique words
    unique_words = set(words_list)
    
    # Misspelled words are those in the text but NOT in the dictionary
    misspelled = unique_words - VALID_WORDS
    
    return misspelled

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def analyze_vocabulary(words_list):
    unique_words = set(words_list)
    total_words = len(words_list)
    unique_count = len(unique_words)
    
    # Lexical richness: ratio of unique words to total words
    if total_words == 0:
        return 0
    richness = (unique_count / total_words) * 100
    
    return unique_count, richness

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def mistakes_and_best_practices():
    # Best Practice: Notice how we load VALID_WORDS as a set globally.
    # If VALID_WORDS were a list, checking `word in VALID_WORDS` for a 
    # large text would be very slow (O(N*M)). Using a set makes it O(M).
    pass

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why use a set for a spell checker dictionary?
# A: For O(1) membership testing, which is crucial when checking thousands of words.
#
# Q2: How did we find misspelled words in one line?
# A: By using set difference: text_words - valid_words.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

def suggest_corrections(misspelled_word):
    # A naive suggestion generator: finding valid words with similar length
    length = len(misspelled_word)
    suggestions = {word for word in VALID_WORDS if abs(len(word) - length) <= 1}
    return suggestions

# ============================================================
# SECTION 7: MINI CHALLENGE (THE PROJECT)
# ============================================================

def run_project(text):
    print("--- Text Analyzer & Spell Checker ---")
    print(f"Original Text: '{text}'\n")
    
    # 1. Clean the text
    words_list = clean_text(text)
    
    # 2. Analyze vocabulary
    unique_count, richness = analyze_vocabulary(words_list)
    print(f"Total words: {len(words_list)}")
    print(f"Unique words: {unique_count}")
    print(f"Lexical richness: {richness:.1f}%\n")
    
    # 3. Spell check
    misspelled = spell_check(words_list)
    
    if not misspelled:
        print("Spell Check: Perfect! No errors found.")
    else:
        print(f"Spell Check: Found {len(misspelled)} misspelled word(s):")
        for word in misspelled:
            suggestions = suggest_corrections(word)
            print(f" - '{word}' (Suggestions: {', '.join(suggestions) if suggestions else 'None'})")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
# By combining string manipulation with set operations (difference and comprehensions),
# we can build efficient and powerful text analysis tools.

if __name__ == "__main__":
    sample_text = "The quik brown fox jumps over the lazi dog! Python is awesom."
    run_project(sample_text)
