"""
Topic: Mini Project - String Parsing
Chapter: 8
Level: Intermediate

Description:
    A comprehensive mini-project that combines slicing, formatting, regex, and string methods to parse a raw text log file into structured data.

Real-Life Analogy:
    Imagine receiving a messy, unformatted spreadsheet. This script is like applying a set of rules to clean it up and organize it neatly into columns and rows.

Key Concepts:
    - Log parsing
    - Data extraction
    - String formatting for output
    - Regex pattern matching
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import re

# Simulated raw log data
RAW_LOGS = """
[2023-10-01 10:15:30] ERROR User 'alice' failed to login from IP 192.168.1.10. Code: 403
[2023-10-01 10:16:05] INFO User 'bob' logged in successfully from IP 10.0.0.5. Code: 200
[2023-10-01 10:20:11] WARNING High memory usage detected on server 'web-01'. Code: 500
[2023-10-01 10:25:40] ERROR User 'charlie' failed to login from IP 172.16.0.4. Code: 403
"""

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

def parse_logs(log_data: str) -> list:
    """Parse raw log text into a list of dictionaries."""
    parsed_entries = []
    
    # Split logs into lines, ignore empty lines
    lines = [line.strip() for line in log_data.strip().split("\n") if line.strip()]
    
    # Regex to extract Date, Level, Message, Code
    # Example format: [DATE] LEVEL MESSAGE Code: CODE
    pattern = re.compile(r"\[(.*?)\]\s+(\w+)\s+(.*?)\.\s+Code:\s+(\d+)")
    
    for line in lines:
        match = pattern.search(line)
        if match:
            entry = {
                "timestamp": match.group(1),
                "level": match.group(2),
                "message": match.group(3),
                "code": match.group(4)
            }
            parsed_entries.append(entry)
            
    return parsed_entries

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

def format_report(entries: list):
    """Format parsed log entries into a neat report table."""
    print("=" * 80)
    print(f"{'TIMESTAMP':<22} | {'LEVEL':<8} | {'CODE':<5} | {'MESSAGE'}")
    print("-" * 80)
    
    for entry in entries:
        # Highlight errors
        level = entry['level']
        if level == 'ERROR':
            level_str = f"!! {level} !!"
        else:
            level_str = level
            
        print(f"{entry['timestamp']:<22} | {level_str:<8} | {entry['code']:<5} | {entry['message']}")
    print("=" * 80)

def count_errors(entries: list) -> int:
    """Count how many ERROR level logs exist."""
    count = 0
    for entry in entries:
        if entry['level'] == 'ERROR':
            count += 1
    return count

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Using basic `split()` to parse complex logs, which can break if the message contains commas or varying spaces.
# Best Practice: Use Regex (`re`) to parse complex strings with a predictable pattern.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

"""
Q: Why parse raw strings into a list of dictionaries?
A: Dictionaries provide structured key-value pairs, making it easier to filter, search, and manipulate the data programmatically compared to raw text.

Q: In the regex pattern, what does `(.*?)` do?
A: It is a non-greedy capture group. It matches any character, but captures as few characters as possible until the next part of the pattern matches.
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# 1. Modify the `parse_logs` function to extract the IP address if it exists in the message.
# 2. Write a function to filter logs by a specific date.
# 3. Export the formatted report to a CSV file.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def mini_challenge():
    """Run the log parsing project."""
    print("Parsing logs...")
    parsed_data = parse_logs(RAW_LOGS)
    
    print(f"\nFound {len(parsed_data)} log entries.")
    print(f"Total Errors: {count_errors(parsed_data)}")
    
    print("\nGenerating Report:")
    format_report(parsed_data)

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

"""
- Combining string methods like `split()` and `strip()` cleans raw data.
- Regex is the best tool for extracting structured fields from unstructured text.
- f-strings with alignment (`:<20`) are perfect for generating text-based tables and reports.
"""

if __name__ == "__main__":
    mini_challenge()
