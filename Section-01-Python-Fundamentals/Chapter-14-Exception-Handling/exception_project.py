"""
Topic: Comprehensive Exception Handling Project
Chapter: 14
Level: Advanced

Description:
    This project integrates all concepts from the Exception Handling chapter.
    We will build a simple robust "Data Loader" that reads JSON files, validates the data,
    handles various failure points using custom exceptions, and logs everything safely using context managers.

Real-Life Analogy:
    Building a commercial airplane. You don't just hope the engines work. You install sensors (logging), backup systems (except blocks), strict safety rules (assertions and custom errors), and guaranteed protocols for landing safely even in an emergency (finally blocks and context managers).

Key Concepts:
    - Try/except/else/finally
    - Exception chaining
    - Custom exceptions
    - Context managers
    - Logging
"""

import json
import logging
import os

# ============================================================
# LOGGING CONFIGURATION
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ============================================================
# CUSTOM EXCEPTIONS
# ============================================================

class DataLoaderError(Exception):
    """Base exception for the Data Loader project."""
    pass

class FileFormatError(DataLoaderError):
    """Raised when the file is not valid JSON."""
    pass

class DataValidationError(DataLoaderError):
    """Raised when the data is logically invalid (e.g., negative age)."""
    pass

# ============================================================
# CONTEXT MANAGER
# ============================================================

class TemporaryFileLock:
    """Simulates locking a file while reading to prevent concurrent edits."""
    def __init__(self, filename):
        self.filename = filename
        self.lock_file = filename + ".lock"

    def __enter__(self):
        logging.debug(f"Acquiring lock for {self.filename}")
        with open(self.lock_file, "w") as f:
            f.write("LOCKED")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.debug(f"Releasing lock for {self.filename}")
        if os.path.exists(self.lock_file):
            os.remove(self.lock_file)
        if exc_type:
            logging.error(f"Error occurred during lock period: {exc_type.__name__}")
        return False # Let exceptions propagate

# ============================================================
# CORE LOGIC
# ============================================================

def process_user_data(user):
    """Validates individual user records."""
    assert isinstance(user, dict), "User data must be a dictionary."
    
    if "name" not in user or "age" not in user:
        raise DataValidationError("Missing required fields: 'name' or 'age'")
    
    age = user["age"]
    if not isinstance(age, int) or age < 0:
        raise DataValidationError(f"Invalid age provided for user {user.get('name', 'Unknown')}: {age}")
    
    logging.info(f"Successfully processed user: {user['name']}")
    return True

def load_data(filepath):
    """Main function to load and process data robustly."""
    logging.info(f"Attempting to load data from {filepath}")
    
    try:
        with TemporaryFileLock(filepath):
            with open(filepath, 'r') as file:
                content = file.read()
                
            try:
                data = json.loads(content)
            except json.JSONDecodeError as e:
                # Exception chaining
                raise FileFormatError("The file does not contain valid JSON.") from e
            
            # Process data
            valid_count = 0
            for item in data:
                try:
                    process_user_data(item)
                    valid_count += 1
                except DataValidationError as e:
                    logging.warning(f"Validation failed for an item: {e}")
                except Exception as e:
                    # Catch unforeseen errors to prevent complete failure
                    logging.exception(f"Unexpected error processing item: {item}")
            
    except FileNotFoundError:
        logging.error(f"Failed to locate file: {filepath}")
    except FileFormatError as e:
        logging.error(f"File Format Error: {e} (Cause: {e.__cause__})")
    except Exception as e:
        logging.critical(f"A critical system error occurred: {e}")
    else:
        logging.info(f"Data loading complete. Valid records processed: {valid_count}")
    finally:
        logging.info("Load operation finished. Cleaning up temporary states.")

# ============================================================
# SETUP AND EXECUTION
# ============================================================

def setup_test_files():
    """Create some dummy files for testing."""
    valid_data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": -5}, {"name": "Charlie"}]
    with open("valid_users.json", "w") as f:
        json.dump(valid_data, f)
        
    with open("broken_users.json", "w") as f:
        f.write("{ invalid json formatting")

def cleanup_test_files():
    for f in ["valid_users.json", "broken_users.json"]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == "__main__":
    print("--- Setting up test environment ---")
    setup_test_files()
    
    print("\n--- Test 1: Valid File with some invalid records ---")
    load_data("valid_users.json")
    
    print("\n--- Test 2: Broken JSON File ---")
    load_data("broken_users.json")
    
    print("\n--- Test 3: Missing File ---")
    load_data("missing_file.json")
    
    print("\n--- Cleaning up ---")
    cleanup_test_files()
