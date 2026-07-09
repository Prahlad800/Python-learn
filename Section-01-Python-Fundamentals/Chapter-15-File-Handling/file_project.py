"""
Topic: File Handling Mini-Project
Chapter: 15
Level: Intermediate

Description:
    This project ties together reading/writing files, parsing CSV data, using `pathlib` for paths, and generating an output report. It acts as a realistic scenario you might encounter in a data processing job.

Real-Life Analogy:
    Imagine you receive a messy spreadsheet of monthly expenses from different departments. Your job is to extract the raw data, calculate total expenditures per department, and save a clean, summarized report into a new file.

Key Concepts:
    - pathlib for directory management
    - csv module for reading data
    - Dictionary aggregation
    - Formatting and writing output
"""

import csv
import json
from pathlib import Path

# ============================================================
# SECTION 1: SETUP AND DATA GENERATION
# ============================================================

# We will create a dummy CSV file so the script is self-contained.
def generate_sample_data(filepath: Path):
    """Creates a sample CSV file with sales data."""
    data = [
        ["Date", "Department", "Amount"],
        ["2023-10-01", "IT", "1500.50"],
        ["2023-10-02", "HR", "350.00"],
        ["2023-10-02", "IT", "200.00"],
        ["2023-10-03", "Marketing", "800.75"],
        ["2023-10-04", "HR", "150.25"],
        ["2023-10-05", "IT", "45.00"],
        ["2023-10-05", "Marketing", "1200.00"]
    ]
    
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"Sample data generated at: {filepath}")

# ============================================================
# SECTION 2: DATA PROCESSING (The Core Logic)
# ============================================================

def process_sales_data(filepath: Path) -> dict:
    """
    Reads the CSV and aggregates the total amount spent per department.
    """
    department_totals = {}
    
    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # reader automatically uses the first row as keys (Date, Department, Amount)
            for row in reader:
                dept = row["Department"]
                # Convert string amount to float
                amount = float(row["Amount"])
                
                # Aggregate
                if dept in department_totals:
                    department_totals[dept] += amount
                else:
                    department_totals[dept] = amount
                    
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    except Exception as e:
        print(f"An error occurred during processing: {e}")
        
    return department_totals

# ============================================================
# SECTION 3: GENERATING THE REPORT
# ============================================================

def generate_report(data: dict, output_path: Path):
    """
    Writes the aggregated data into a clean JSON report.
    """
    # Let's add some metadata to our report
    total_spent = sum(data.values())
    
    report_content = {
        "summary": {
            "total_departments": len(data),
            "grand_total": round(total_spent, 2)
        },
        "department_breakdown": data
    }
    
    with open(output_path, mode='w', encoding='utf-8') as f:
        json.dump(report_content, f, indent=4)
        
    print(f"Report generated successfully at: {output_path}")

# ============================================================
# SECTION 4: MAIN EXECUTION
# ============================================================

def main():
    # 1. Setup paths using pathlib
    base_dir = Path("project_data")
    base_dir.mkdir(exist_ok=True) # Create directory if it doesn't exist
    
    input_file = base_dir / "raw_sales.csv"
    output_file = base_dir / "sales_report.json"
    
    # 2. Generate dummy data
    generate_sample_data(input_file)
    
    # 3. Process the data
    print("Processing data...")
    totals = process_sales_data(input_file)
    
    # Print to console to verify
    for dept, amount in totals.items():
        print(f"  - {dept}: ${amount:.2f}")
        
    # 4. Generate the final report
    generate_report(totals, output_file)
    
    # Note: We are leaving the files on disk so you can inspect them!

if __name__ == "__main__":
    main()
