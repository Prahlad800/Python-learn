"""
Topic: Tuple Mini Project
Chapter: 10
Level: Advanced

Description:
    This file contains a comprehensive mini-project that utilizes all the tuple 
    concepts discussed in this chapter. We will build an immutable Student Record 
    Management System using standard tuples and Named Tuples.

Real-Life Analogy:
    Imagine managing a school registry where once a semester's final grades are posted, 
    the records become immutable to prevent tampering. Tuples are the perfect data 
    structure for this read-only archive.

Key Concepts:
    - typing.NamedTuple for structure
    - Tuple packing and unpacking
    - Tuples as Dictionary keys
    - Searching and filtering immutable collections
"""

from typing import NamedTuple

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# Define the structure for a Course and a Student Record
class Course(NamedTuple):
    course_id: str
    course_name: str
    credits: int

class StudentRecord(NamedTuple):
    student_id: int
    name: str
    major: str
    # 'grades' will be a tuple of tuples: ((Course, grade), (Course, grade))
    grades: tuple 

# ============================================================
# SECTION 2: PRACTICAL EXAMPLES (Project Setup)
# ============================================================

def setup_database() -> tuple:
    """Initialize the immutable database."""
    # Courses
    cs101 = Course("CS101", "Intro to CS", 3)
    math201 = Course("MATH201", "Calculus I", 4)
    eng105 = Course("ENG105", "Literature", 3)
    
    # Students
    s1 = StudentRecord(1001, "Alice Smith", "Computer Science", 
                       ((cs101, "A"), (math201, "B")))
                       
    s2 = StudentRecord(1002, "Bob Jones", "Mathematics", 
                       ((math201, "A"), (eng105, "C")))
                       
    s3 = StudentRecord(1003, "Charlie Brown", "Engineering", 
                       ((cs101, "B"), (math201, "C"), (eng105, "B")))
                       
    # The database itself is a tuple of StudentRecords
    return (s1, s2, s3)

# ============================================================
# SECTION 3: ADVANCED USAGE (GPA Calculation)
# ============================================================

def calculate_gpa(student: StudentRecord) -> float:
    """Calculates the GPA based on the grades tuple."""
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    total_points = 0.0
    total_credits = 0
    
    # Unpack the nested tuple structure
    for course, grade in student.grades:
        points = grade_points.get(grade, 0.0)
        total_points += points * course.credits
        total_credits += course.credits
        
    return total_points / total_credits if total_credits > 0 else 0.0

# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def generate_transcript(student: StudentRecord) -> None:
    """Generates a formatted text transcript."""
    print(f"\n{'='*40}")
    print(f"TRANSCRIPT: {student.name.upper()} (ID: {student.student_id})")
    print(f"MAJOR: {student.major}")
    print(f"{'-'*40}")
    
    for course, grade in student.grades:
        print(f"{course.course_id:8} | {course.course_name:15} | {course.credits}CR | Grade: {grade}")
        
    print(f"{'-'*40}")
    print(f"CUMULATIVE GPA: {calculate_gpa(student):.2f}")
    print(f"{'='*40}")

# ============================================================
# SECTION 5: INTERVIEW QUESTIONS (Contextual)
# ============================================================
"""
Q: Why use Named Tuples instead of standard classes for StudentRecord?
A: Since the data represents historical, read-only grades, immutability ensures data integrity. Named Tuples provide this immutability while maintaining lightweight memory footprints and clean attribute access.

Q: How is the 'grades' attribute structured?
A: It is a nested tuple. A tuple containing tuples of (Course(NamedTuple), String).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES (Integrated into project)
# ============================================================

def get_students_by_major(db: tuple, search_major: str) -> tuple:
    """Returns a tuple of students matching the major."""
    # Using generator expression converted to tuple
    return tuple(s for s in db if s.major.lower() == search_major.lower())

def get_course_roster(db: tuple, search_course_id: str) -> list:
    """Finds all students who took a specific course."""
    roster = []
    for student in db:
        # Check if course is in student's grades
        for course, _ in student.grades:
            if course.course_id == search_course_id:
                roster.append(student.name)
                break
    return roster

# ============================================================
# SECTION 7: MINI CHALLENGE (Running the Project)
# ============================================================

def mini_challenge() -> None:
    """
    Execute the project functions to demonstrate a working system.
    """
    print("Initializing Student Database...")
    db = setup_database()
    
    print(f"\nDatabase loaded. Total students: {len(db)}")
    
    # 1. Print a transcript
    generate_transcript(db[0])  # Alice
    
    # 2. Filter by major
    cs_students = get_students_by_major(db, "Computer Science")
    print(f"\nCS Students: {[s.name for s in cs_students]}")
    
    # 3. Get Course Roster
    math_roster = get_course_roster(db, "MATH201")
    print(f"\nStudents who took MATH201: {math_roster}")

# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- Real-world applications of tuples often revolve around data integrity (read-only state).
- `NamedTuple` makes accessing complex structured data easy and readable.
- Aggregation functions (like GPA calculation) can iterate easily over nested tuples.
- Combining tuples and lists strategically (e.g., building a roster list from tuple data) 
  is a standard Pythonic pattern.
"""

if __name__ == "__main__":
    mini_challenge()
