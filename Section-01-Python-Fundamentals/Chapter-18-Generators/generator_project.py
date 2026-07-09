"""
Topic: Generator Data Processing Project
Chapter: 18
Level: Advanced

Description:
    This project combines all generator concepts into a comprehensive data processing 
    pipeline. We will simulate reading a large CSV file of sales data, filtering invalid 
    records, converting data types, calculating revenue, and aggregating results—all 
    using memory-efficient generator pipelines and `yield from`.

Real-Life Analogy:
    Building a water purification plant. Raw, dirty water enters (raw CSV data). 
    It passes through a filter (generator 1), gets chemically treated (generator 2), 
    and is finally stored as clean drinking water (aggregation dictionary).

Key Concepts:
    - Combining multiple generators
    - ETL (Extract, Transform, Load) pipelines
    - Memory efficiency applied
"""
from typing import Iterator, Dict, Any

# ============================================================
# SECTION 1: EXTRACT (Reading Data)
# ============================================================

# Simulating a massive CSV file using a list of strings.
MOCK_CSV_DATA = [
    "transaction_id,product,price,quantity,status",
    "101,Laptop,1200.50,2,Completed",
    "102,Mouse,-25.00,5,Completed",          # Invalid price
    "103,Keyboard,75.00,0,Completed",        # Invalid quantity
    "104,Monitor,300.00,1,Cancelled",        # Cancelled
    "105,Laptop,1200.50,1,Completed",
    "106,Headphones,150.00,3,Completed",
    "107,Mouse,25.00,a,Completed",           # Corrupt quantity data
]

def read_data(data_source: list[str]) -> Iterator[str]:
    """Yields rows from the data source one by one."""
    for row in data_source:
        yield row

# ============================================================
# SECTION 2: TRANSFORM (Pipelines)
# ============================================================

def split_rows(rows: Iterator[str]) -> Iterator[list[str]]:
    """Splits CSV string rows into lists."""
    for row in rows:
        yield row.split(",")

def dictify(rows: Iterator[list[str]], header: list[str]) -> Iterator[Dict[str, str]]:
    """Converts lists into dictionaries mapped to headers."""
    for row in rows:
        if len(row) == len(header):
            yield dict(zip(header, row))

def filter_completed(records: Iterator[Dict[str, str]]) -> Iterator[Dict[str, str]]:
    """Filters out non-completed transactions."""
    for record in records:
        if record.get("status") == "Completed":
            yield record

def clean_data(records: Iterator[Dict[str, str]]) -> Iterator[Dict[str, Any]]:
    """Cleans and converts data types. Yields valid records only."""
    for record in records:
        try:
            price = float(record["price"])
            quantity = int(record["quantity"])
            
            if price > 0 and quantity > 0:
                record["price"] = price
                record["quantity"] = quantity
                yield record
        except ValueError:
            # Skip rows with corrupt data (like 'a' for quantity)
            continue

def calculate_revenue(records: Iterator[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """Calculates total revenue per transaction."""
    for record in records:
        record["revenue"] = record["price"] * record["quantity"]
        yield record

# ============================================================
# SECTION 3: DELEGATION (yield from)
# ============================================================

def process_chunk(chunk: list[str]) -> Iterator[Dict[str, Any]]:
    """Demonstrates yield from by delegating to the pipeline."""
    # Setup pipeline
    rows = read_data(chunk)
    header_str = next(rows) # Extract header
    header = header_str.split(",")
    
    parsed_rows = split_rows(rows)
    dicts = dictify(parsed_rows, header)
    completed = filter_completed(dicts)
    cleaned = clean_data(completed)
    with_revenue = calculate_revenue(cleaned)
    
    yield from with_revenue

# ============================================================
# SECTION 4: LOAD (Aggregation)
# ============================================================

def aggregate_sales_by_product(records: Iterator[Dict[str, Any]]) -> Dict[str, float]:
    """Consumes the pipeline and aggregates revenue by product."""
    report = {}
    for record in records:
        product = record["product"]
        revenue = record["revenue"]
        report[product] = report.get(product, 0.0) + revenue
    return report

# ============================================================
# SECTION 5: PROJECT EXECUTION
# ============================================================

def main():
    print("Starting ETL Pipeline...")
    
    # 1. Initialize the pipeline generator
    pipeline = process_chunk(MOCK_CSV_DATA)
    
    # 2. Consume the pipeline and generate report
    sales_report = aggregate_sales_by_product(pipeline)
    
    # 3. Output results
    print("\n--- Final Sales Report ---")
    for product, revenue in sales_report.items():
        print(f"{product}: ${revenue:,.2f}")
        
    print("\nPipeline executed successfully with O(1) memory footprint per row!")

if __name__ == "__main__":
    main()
