"""
Topic: Generator Pipelines
Chapter: 18
Level: Intermediate

Description:
    Generator pipelines are created by chaining multiple generators together. Each generator
    takes an iterator as input and yields its output to the next generator in the chain.
    This creates an efficient, memory-friendly data processing pipeline akin to Unix pipes.

Real-Life Analogy:
    Think of an assembly line in a factory. One worker extracts raw materials (generator 1),
    the next worker cleans them (generator 2), and the final worker packages them (generator 3).
    Items move through the line one by one, rather than stockpiling between steps.

Key Concepts:
    - Chaining generators
    - Unix-like data pipelines
    - Memory efficiency in large data processing
"""
from typing import Iterator, Iterable

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

def generate_numbers(n: int) -> Iterator[int]:
    """First stage: generate numbers."""
    for i in range(n):
        yield i

def square_numbers(numbers: Iterable[int]) -> Iterator[int]:
    """Second stage: square the numbers."""
    for num in numbers:
        yield num * num

def stringify_numbers(numbers: Iterable[int]) -> Iterator[str]:
    """Third stage: convert to string."""
    for num in numbers:
        yield f"Number: {num}"

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Simulating log file processing
def read_log_lines(logs: list[str]) -> Iterator[str]:
    for line in logs:
        yield line

def filter_error_logs(lines: Iterable[str]) -> Iterator[str]:
    for line in lines:
        if "ERROR" in line:
            yield line

def extract_error_messages(lines: Iterable[str]) -> Iterator[str]:
    for line in lines:
        # Assuming format: "[DATE] ERROR: message"
        yield line.split("ERROR: ")[-1].strip()

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# We can use generator expressions for cleaner pipeline syntax
def process_pipeline_with_expressions(raw_data: list[str]) -> Iterator[str]:
    """A pipeline built entirely out of generator expressions."""
    # Step 1: Strip whitespace
    stripped = (line.strip() for line in raw_data)
    # Step 2: Remove empty lines
    non_empty = (line for line in stripped if line)
    # Step 3: Capitalize
    capitalized = (line.upper() for line in non_empty)
    return capitalized

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake: Converting intermediate generators to lists (e.g. `list(filter_errors(...))`).
# Correction: Keep data as iterators throughout the pipeline to maintain memory efficiency.
# Only convert to a list at the very end, if necessary.

# Best Practice: Keep each generator function small and focused on a single responsibility
# (Single Responsibility Principle).

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is a generator pipeline?
# A1: A series of generators where the output of one becomes the input to the next.
#
# Q2: Why are generator pipelines beneficial?
# A2: They allow processing of infinite or extremely large datasets with constant, 
#     minimal memory usage.
#
# Q3: Does data flow through a pipeline all at once, or one item at a time?
# A3: One item at a time. The entire pipeline pulls one item from the source to the end.
#
# Q4: How do generator pipelines compare to Unix pipes ( | )?
# A4: They are conceptually identical. Both pull data stream item-by-item through transformations.
#
# Q5: Can you reuse a generator pipeline?
# A5: No, because the iterators inside it get exhausted. You must rebuild the pipeline to reuse it.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a 3-stage pipeline: generate words -> filter words starting with 'a' -> convert to uppercase.
# Exercise 2: Build a pipeline that takes a list of paths, reads file sizes, and yields only those > 1MB.
# Exercise 3: Use a pipeline to flatten a 2D list and then filter out negative numbers.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge: Write a pipeline to parse a CSV-like list of strings.
# Data: ["id,name,age", "1,Alice,30", "2,Bob,25", "3,Charlie,35"]
# Pipeline stages: 
# 1. Skip header
# 2. Split by comma
# 3. Extract ages as integers
# 4. Calculate and return the average age (not a generator, consumes the pipeline)

def average_age_pipeline(csv_lines: list[str]) -> float:
    """Calculates the average age from CSV data using a pipeline."""
    lines_gen = (line for line in csv_lines)
    next(lines_gen)  # 1. Skip header
    split_lines = (line.split(",") for line in lines_gen)  # 2. Split
    ages = (int(row[2]) for row in split_lines)  # 3. Extract age
    
    # Consume pipeline
    total_age = 0
    count = 0
    for age in ages:
        total_age += age
        count += 1
    return total_age / count if count > 0 else 0.0

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Pipelines chain multiple generators.
# - They act lazily; execution is driven by the final consumer.
# - They are ideal for parsing logs, processing streams, and ETL tasks.
# - intermediate stages remain memory efficient.

if __name__ == "__main__":
    print("--- Basic Pipeline ---")
    nums = generate_numbers(5)
    squares = square_numbers(nums)
    strings = stringify_numbers(squares)
    for s in strings:
        print(s)
        
    print("\n--- Log Processing Pipeline ---")
    mock_logs = [
        "[2024-01-01] INFO: App started",
        "[2024-01-01] ERROR: Connection timeout",
        "[2024-01-01] DEBUG: Retrying...",
        "[2024-01-01] ERROR: Database disconnected"
    ]
    log_stream = read_log_lines(mock_logs)
    errors_only = filter_error_logs(log_stream)
    messages = extract_error_messages(errors_only)
    print(list(messages))
    
    print("\n--- Pipeline with Expressions ---")
    raw = ["  hello\n", "", "world  ", " ", "python"]
    print(list(process_pipeline_with_expressions(raw)))
    
    print("\n--- Mini Challenge ---")
    csv_data = ["id,name,age", "1,Alice,30", "2,Bob,25", "3,Charlie,35"]
    print(f"Average age: {average_age_pipeline(csv_data)}")
