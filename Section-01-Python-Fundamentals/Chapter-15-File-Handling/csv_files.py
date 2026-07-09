"""
Topic: CSV Files
Chapter: 15
Level: Intermediate

Description:
    CSV (Comma-Separated Values) files are a common format for storing tabular data. Python's built-in `csv` module allows you to easily read from and write to CSV files, handling delimiters, quotes, and line terminators seamlessly.

Real-Life Analogy:
    A CSV file is like a plain-text version of a spreadsheet. Each line is a row, and the commas act like the vertical lines dividing the columns.

Key Concepts:
    - csv.reader and csv.writer
    - csv.DictReader and csv.DictWriter
    - Delimiters and quoting
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

import csv

# Writing to a CSV file using csv.writer
data = [
    ["Name", "Age", "City"],
    ["Alice", 28, "New York"],
    ["Bob", 34, "San Francisco"],
    ["Charlie", 22, "London"]
]

# Important: newline='' is required in Python 3 to prevent extra blank lines
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading from a CSV file using csv.reader
print("Basic CSV Reading:")
with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Example 1: Using DictWriter to write dictionaries
dict_data = [
    {"Name": "David", "Age": 45, "City": "Berlin"},
    {"Name": "Eva", "Age": 31, "City": "Paris"}
]

with open("people_dict.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()  # Writes the column names
    writer.writerows(dict_data)

# Example 2: Using DictReader (Highly Recommended)
# DictReader automatically uses the first row as dictionary keys
print("\nReading with DictReader:")
with open("people_dict.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} lives in {row['City']} and is {row['Age']} years old.")

# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Example 1: Custom Delimiters (e.g., TSV - Tab Separated Values)
tsv_data = [["Item", "Price"], ["Apple", "1.20"], ["Banana", "0.80"]]
with open("products.tsv", "w", newline="", encoding="utf-8") as f:
    # Use delimiter='\t' for tabs
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(tsv_data)

print("\nReading TSV file:")
with open("products.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(" | ".join(row))

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Forgetting `newline=''` when opening a file for writing CSV in Python 3.
# Correction: Always include `newline=''` to avoid alternating blank rows in Windows.

# Mistake 2: Parsing CSV manually using split(',').
# Correction: Always use the `csv` module because it correctly handles commas inside quoted fields (e.g., "Smith, John").

# Best Practice: Use DictReader and DictWriter. They make the code more robust against changes in column order.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: Why should you use the `csv` module instead of string.split(',')?
# A: The `csv` module correctly handles edge cases, such as fields that contain commas enclosed in quotes.

# Q2: What does `csv.DictReader` do?
# A: It reads the CSV file and maps each row to a dictionary, using the first row as the keys.

# Q3: Why do we pass `newline=''` when writing a CSV file?
# A: To prevent the `csv` module and the OS from adding duplicate newline characters, which creates empty rows.

# Q4: How do you read a file where fields are separated by pipes ('|')?
# A: Pass the argument `delimiter='|'` to the csv.reader.

# Q5: What is `writeheader()` used for?
# A: It writes a row containing the field names specified in `csv.DictWriter` to the CSV file.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create a list of dictionaries containing book details (Title, Author, Year). Write them to 'books.csv'.

# Exercise 2: Read 'books.csv' using DictReader and print only the Titles.

# Exercise 3: Read 'books.csv', add a new book to the list, and write the updated list back to the file.

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

def process_sales(input_csv, output_csv):
    """
    Mini Challenge: Read a CSV of sales (Item, Price, Quantity).
    Calculate the Total for each row (Price * Quantity).
    Write the data to a new CSV including the new "Total" column.
    """
    # Setup dummy data
    with open(input_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([["Item", "Price", "Quantity"], ["Pen", 1.5, 10], ["Notebook", 5.0, 3]])

    # Process
    with open(input_csv, "r", encoding="utf-8") as infile, \
         open(output_csv, "w", newline="", encoding="utf-8") as outfile:
         
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["Total"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in reader:
            row["Total"] = float(row["Price"]) * int(row["Quantity"])
            writer.writerow(row)
            
    # Verify
    print("\nProcessed Sales:")
    with open(output_csv, "r", encoding="utf-8") as f:
        print(f.read().strip())

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - The `csv` module parses tabular data effectively.
# - Use csv.reader/writer for list-based data.
# - Use csv.DictReader/DictWriter for dictionary-based data (more readable).
# - Always open CSV files with `newline=''` to avoid formatting issues.
# - The module easily handles custom delimiters like tabs and pipes.

if __name__ == "__main__":
    process_sales("sales.csv", "sales_summary.csv")
