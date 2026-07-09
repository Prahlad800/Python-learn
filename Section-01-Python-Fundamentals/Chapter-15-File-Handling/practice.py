"""
Topic: Chapter 15 Practice & Exercises
Chapter: 15
Level: Intermediate

Description:
    This file combines the concepts learned in Chapter 15: File I/O, `pathlib`, `os`, `tempfile`, and `zipfile`.

Instructions:
    Implement the functions according to their docstrings. Ensure your code cleans up any temporary files or directories it creates (or use context managers that do it automatically).
"""

from pathlib import Path
import os
import tempfile
import zipfile

# ============================================================
# EXERCISE 1: Pathlib Basics
# ============================================================

def get_file_extension(filepath_str: str) -> str:
    """
    Given a string representing a file path, return the file extension
    (including the dot). Use `pathlib`.
    
    Example: "data/images/photo.jpg" -> ".jpg"
    """
    return Path(filepath_str).suffix

# ============================================================
# EXERCISE 2: OS Walk and Filtering
# ============================================================

def count_files_by_extension(directory_path: str, extension: str) -> int:
    """
    Given a directory path and an extension (e.g., ".txt"), use `os.walk`
    to traverse the directory (and all subdirectories) and return the 
    total number of files that end with that extension.
    """
    count = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count

# ============================================================
# EXERCISE 3: Tempfile
# ============================================================

def write_and_read_temp(data: str) -> str:
    """
    Create a NamedTemporaryFile. Write the `data` string to it.
    Seek back to the beginning, read the data, and return it.
    The file should automatically delete when the function finishes.
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp:
        temp.write(data)
        temp.seek(0)
        return temp.read()

# ============================================================
# EXERCISE 4: Zipfile Manipulation
# ============================================================

def extract_specific_file(zip_path: str, filename_to_extract: str, extract_to: str) -> bool:
    """
    Open the zip file at `zip_path`. Check if `filename_to_extract` exists inside it.
    If it does, extract just that file to the `extract_to` directory and return True.
    If it does not exist in the zip, return False.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            if filename_to_extract in zipf.namelist():
                zipf.extract(filename_to_extract, path=extract_to)
                return True
            return False
    except FileNotFoundError:
        return False
    except zipfile.BadZipFile:
        return False

# ============================================================
# TESTING BLOCK
# ============================================================

if __name__ == "__main__":
    print("--- Testing Exercise 1 ---")
    print(f"Extension of report.pdf: {get_file_extension('report.pdf')}") # Expected: .pdf
    
    print("\n--- Testing Exercise 2 ---")
    # Setup dummy env
    os.makedirs("test_ex2/sub", exist_ok=True)
    Path("test_ex2/a.txt").touch()
    Path("test_ex2/b.csv").touch()
    Path("test_ex2/sub/c.txt").touch()
    
    print(f"TXT files count: {count_files_by_extension('test_ex2', '.txt')}") # Expected: 2
    
    # Cleanup
    import shutil
    shutil.rmtree("test_ex2")
    
    print("\n--- Testing Exercise 3 ---")
    print(f"Temp read: {write_and_read_temp('Secret Temp Data')}")
    
    print("\n--- Testing Exercise 4 ---")
    # Setup dummy zip
    with zipfile.ZipFile("test.zip", "w") as zf:
        zf.writestr("target.txt", "found me")
        zf.writestr("ignore.txt", "ignore me")
        
    os.makedirs("output_ex4", exist_ok=True)
    success = extract_specific_file("test.zip", "target.txt", "output_ex4")
    print(f"Extraction successful: {success}") # Expected: True
    print(f"File exists: {os.path.exists('output_ex4/target.txt')}") # Expected: True
    
    # Cleanup
    os.remove("test.zip")
    shutil.rmtree("output_ex4")
