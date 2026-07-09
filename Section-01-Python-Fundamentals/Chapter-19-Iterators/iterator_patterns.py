"""
Topic: Iterator Patterns
Chapter: 19
Level: Advanced

Description:
    The Iterator Pattern is a behavioral design pattern that allows sequential traversal through a complex data structure without exposing its internal representation. While Python's built-in iterators handle most basic needs, custom iterator patterns allow you to traverse trees, graphs, or composite objects in specific ways (e.g., depth-first, breadth-first, or custom filtering).

Real-Life Analogy:
    Think of a museum tour guide. The museum has a complex layout of rooms and floors. The guide (the iterator) takes you through a specific route (e.g., chronologically, or by art style) without you needing to memorize the building's floor plan.

Key Concepts:
    - Hiding internal data structures
    - Providing multiple traversal algorithms (e.g., Forward, Backward, Filtered)
    - Separating the traversal logic from the collection logic
"""

from typing import Any, List, Iterator, Optional

# ============================================================
# SECTION 1: BASIC SYNTAX AND INTRODUCTION
# ============================================================

# The Collection Component
class BookCollection:
    def __init__(self):
        self._books: List[str] = []
        
    def add_book(self, book: str) -> None:
        self._books.append(book)
        
    def __iter__(self) -> Iterator[str]:
        # Default iteration behavior
        return iter(self._books)

def basic_pattern_demo() -> None:
    print("--- Section 1: Basic Iterator Pattern ---")
    library = BookCollection()
    library.add_book("1984")
    library.add_book("Brave New World")
    
    # We don't access library._books directly; the iterator abstracts it.
    for book in library:
        print(book)


# ============================================================
# SECTION 2: PRACTICAL EXAMPLES
# ============================================================

# Extending the pattern to provide MULTIPLE ways to traverse the same collection

class Employee:
    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department

class Organization:
    def __init__(self):
        self.employees: List[Employee] = []
        
    def add(self, emp: Employee):
        self.employees.append(emp)
        
    def iter_by_dept(self, dept: str) -> Iterator[Employee]:
        """A specific traversal strategy."""
        for emp in self.employees:
            if emp.department == dept:
                yield emp
                
    def iter_alphabetical(self) -> Iterator[Employee]:
        """Another traversal strategy."""
        sorted_emps = sorted(self.employees, key=lambda e: e.name)
        return iter(sorted_emps)

def multiple_traversals_demo() -> None:
    print("\n--- Section 2: Multiple Traversal Strategies ---")
    org = Organization()
    org.add(Employee("Alice", "Engineering"))
    org.add(Employee("Bob", "HR"))
    org.add(Employee("Charlie", "Engineering"))
    
    print("Engineering Team:")
    for emp in org.iter_by_dept("Engineering"):
        print(f" - {emp.name}")


# ============================================================
# SECTION 3: ADVANCED USAGE
# ============================================================

# Traversing a complex data structure (A Tree)

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        
    def __iter__(self):
        """In-order traversal iterator pattern"""
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

def tree_traversal_demo() -> None:
    print("\n--- Section 3: Advanced Usage (Tree Traversal) ---")
    # Build a simple tree
    #      5
    #     / \
    #    3   7
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    
    # The iterator pattern hides the recursive tree traversal logic
    print("Tree in-order traversal:")
    for val in root:
        print(val, end=" ")
    print()


# ============================================================
# SECTION 4: COMMON MISTAKES AND BEST PRACTICES
# ============================================================

def common_mistakes() -> None:
    print("\n--- Section 4: Common Mistakes ---")
    
    # Mistake: Exposing the internal structure to the client
    # class BadLibrary:
    #     def __init__(self):
    #         self.books = []  # Public list
    #
    # # Client code directly manipulates the list
    # lib = BadLibrary()
    # lib.books.append("X") 
    
    # Best Practice: Keep internals private (`_books`) and provide an `__iter__` method 
    # so the client interacts with the iterator, not the underlying data structure.
    print("Best Practice: Encapsulate data structures and expose iterators.")


# ============================================================
# SECTION 5: INTERVIEW QUESTIONS
# ============================================================
"""
Q1: What is the main purpose of the Iterator Design Pattern?
A1: To provide a way to access the elements of an aggregate object (like a list, tree, or graph) sequentially without exposing its underlying representation.

Q2: How does Python simplify the classic Gang of Four Iterator Pattern?
A2: Instead of creating a separate Iterator class interface with `hasNext()` and `next()`, Python has the built-in `__iter__()` and `__next__()` protocol. Furthermore, `yield` (generators) makes creating iterators trivial without needing a dedicated class.

Q3: Can a collection have multiple iterators?
A3: Yes. You can define methods on a collection that return different iterator objects (e.g., `forward_iterator()`, `backward_iterator()`, `filtered_iterator()`).
"""

# ============================================================
# SECTION 6: PRACTICE EXERCISES
# ============================================================
"""
Exercise 1:
Expand the `TreeNode` class to include a `pre_order_iter()` method that yields values in pre-order (Root, Left, Right).

Exercise 2:
Create a `Playlist` class containing songs. Implement an iterator that yields songs in a shuffled order (use random.shuffle on a copy of the list internally).
"""

# ============================================================
# SECTION 7: MINI CHALLENGE
# ============================================================
"""
Challenge: Build a 2D Grid collection (matrix). 
Implement two iteration patterns:
1. Row-major (default `__iter__`): Yields items left-to-right, top-to-bottom.
2. Column-major (`iter_cols`): Yields items top-to-bottom, left-to-right.
"""

class Grid:
    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        
    def __iter__(self) -> Iterator[int]:
        # Row-major
        for row in self._matrix:
            for item in row:
                yield item
                
    def iter_cols(self) -> Iterator[int]:
        # Column-major
        if not self._matrix: return
        cols = len(self._matrix[0])
        rows = len(self._matrix)
        for c in range(cols):
            for r in range(rows):
                yield self._matrix[r][c]

def mini_challenge() -> None:
    print("\n--- Section 7: Mini Challenge Demo ---")
    data = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    grid = Grid(data)
    
    print("Row-major:")
    print(list(grid))
    
    print("Column-major:")
    print(list(grid.iter_cols()))


# ============================================================
# SECTION 8: SUMMARY
# ============================================================
"""
- The Iterator Pattern abstracts the traversal logic away from the client.
- Python handles this elegantly via the `__iter__` protocol and generators (`yield`).
- You can provide multiple specific traversal methods (e.g., `iter_by_department`, `iter_cols`).
- It is crucial for traversing complex data structures like Trees and Graphs safely.
"""

if __name__ == "__main__":
    basic_pattern_demo()
    multiple_traversals_demo()
    tree_traversal_demo()
    common_mistakes()
    mini_challenge()
