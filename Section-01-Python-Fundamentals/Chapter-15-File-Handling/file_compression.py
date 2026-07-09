"""
Topic: File Compression (zipfile and tarfile)
Chapter: 15
Level: Intermediate

Description:
    Python provides built-in modules to handle archiving and compressing files. The `zipfile` module is used for standard ZIP files (common on Windows), while `tarfile` handles TAR archives (common on Unix/Linux, often compressed with gzip as .tar.gz).

Real-Life Analogy:
    Compression is like vacuum-sealing a stack of clothes before putting them in a suitcase. It takes up less space (compression), and it groups multiple items together into one package (archiving).

Key Concepts:
    - zipfile.ZipFile
    - tarfile.open
    - Reading, writing, and extracting archives
    - shutil.make_archive
"""

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION (ZIPFILE)
# ============================================================
import zipfile
import os

print("--- Section 1: zipfile ---")
# Setup: Create some dummy files to zip
os.makedirs("zip_demo", exist_ok=True)
with open("zip_demo/file1.txt", "w") as f: f.write("Hello ZIP 1")
with open("zip_demo/file2.txt", "w") as f: f.write("Hello ZIP 2")

# Creating a ZIP file
# 'w' mode overwrites, 'a' mode appends, 'x' creates new (fails if exists)
zip_path = "demo_archive.zip"
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    # Add files. arcname determines the name inside the zip
    zipf.write("zip_demo/file1.txt", arcname="file1.txt")
    zipf.write("zip_demo/file2.txt", arcname="file2.txt")

print(f"Created ZIP archive: {zip_path}")

# Reading a ZIP file without extracting
with zipfile.ZipFile(zip_path, 'r') as zipf:
    print("Files inside the ZIP:")
    print(zipf.namelist())
    
    # Read specific file content directly from the zip
    content = zipf.read("file1.txt")
    print(f"Content of file1.txt inside zip: {content.decode('utf-8')}")

# Extracting a ZIP file
with zipfile.ZipFile(zip_path, 'r') as zipf:
    zipf.extractall("extracted_zip")
print("Extracted ZIP to 'extracted_zip' folder.")

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (TARFILE)
# ============================================================
import tarfile

print("\n--- Section 2: tarfile ---")

tar_path = "demo_archive.tar.gz"

# Creating a tar.gz archive
# 'w:gz' means write using gzip compression
with tarfile.open(tar_path, 'w:gz') as tar:
    # Adding an entire directory is very easy with tarfile
    tar.add("zip_demo", arcname="zipped_data")

print(f"Created TAR.GZ archive: {tar_path}")

# Extracting a tar.gz archive
# A safety check is often required in modern Python to avoid extracting outside target directory
with tarfile.open(tar_path, 'r:gz') as tar:
    # For newer Python versions (3.11+), tarfile has a 'filter' argument for security
    try:
        tar.extractall("extracted_tar", filter='data') 
    except TypeError:
        # Fallback for older Python versions
        tar.extractall("extracted_tar")
print("Extracted TAR.GZ to 'extracted_tar' folder.")

# ============================================================
# SECTION 3: ADVANCED USAGE (SHUTIL)
# ============================================================
import shutil

print("\n--- Section 3: shutil ---")

# The easiest way to archive an entire directory is using shutil.make_archive
# It creates demo_shutil.zip from the contents of the 'zip_demo' folder.
shutil.make_archive(base_name="demo_shutil", format="zip", root_dir="zip_demo")
print("Created archive using shutil.make_archive().")

# The easiest way to unpack an archive
shutil.unpack_archive(filename="demo_shutil.zip", extract_dir="shutil_extracted")
print("Unpacked archive using shutil.unpack_archive().")

# Cleanup
import time
time.sleep(0.1) # small delay for Windows file locks
try:
    shutil.rmtree("zip_demo")
    shutil.rmtree("extracted_zip")
    shutil.rmtree("extracted_tar")
    shutil.rmtree("shutil_extracted")
    os.remove(zip_path)
    os.remove(tar_path)
    os.remove("demo_shutil.zip")
except OSError:
    pass

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

# Mistake 1: Not specifying compression in zipfile
# By default, `zipfile` only stores files; it doesn't compress them.
# You must specify `compression=zipfile.ZIP_DEFLATED`.

# Mistake 2: Extracting untrusted archives without checking paths
# Malicious archives can contain paths like `../../../etc/passwd`.
# Best Practice: Always validate `namelist()` or use safe extraction mechanisms (like the `filter='data'` in modern `tarfile`).

# Best Practice: Use `shutil.make_archive` for simple directory backups. Use `zipfile`/`tarfile` for fine-grained control over individual files.

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================

# Q1: What is the difference between `zipfile` and `shutil.make_archive`?
# A: `zipfile` gives you fine-grained control (adding specific files, reading without extracting). `shutil.make_archive` is a high-level utility for zipping entire directories in one line of code.

# Q2: How do you compress files when using the `zipfile` module?
# A: By passing the argument `compression=zipfile.ZIP_DEFLATED` when creating the `ZipFile` object.

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================

# Exercise: Write a function that takes a zip file path and prints the total
# uncompressed size of all files inside it (without extracting them).

def print_zip_size(zip_path: str):
    if not os.path.exists(zip_path):
        return
    total_size = 0
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        for info in zipf.infolist():
            total_size += info.file_size
    print(f"Total uncompressed size: {total_size} bytes")

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================

# Challenge:
# Write a function that creates a zip file containing ONLY the .py files from a given directory.

def backup_python_files(source_dir: str, zip_name: str):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in os.listdir(source_dir):
            if filename.endswith('.py'):
                file_path = os.path.join(source_dir, filename)
                zipf.write(file_path, arcname=filename)
    print(f"Backed up Python files to {zip_name}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================

# - Python has built-in support for ZIP (`zipfile`) and TAR (`tarfile`) archives.
# - You can read files inside archives without extracting them to disk.
# - `shutil.make_archive` and `shutil.unpack_archive` are the easiest tools for full directories.
# - Always use context managers (`with` statements) to ensure archives are properly closed.

if __name__ == "__main__":
    pass
