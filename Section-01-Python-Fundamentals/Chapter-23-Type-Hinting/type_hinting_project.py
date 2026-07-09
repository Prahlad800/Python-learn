"""
Topic: Type Hinting Capstone Project
Chapter: 23
Level: Advanced

Description:
    This file brings together all the type hinting concepts we've learned into a 
    miniature, realistic application: A Library Management System. 

Real-Life Analogy:
    Building a house using all the blueprints. You are combining basic variables, 
    complex collections, Protocols, TypeVars, and Aliases to build a strictly typed system.

Key Concepts:
    - Combining basic types, Collections, and Unions
    - Using NewType for IDs
    - Using Protocols for interfaces
    - Using Generics for data structures
"""

from typing import TypeAlias, NewType, Protocol, TypeVar, Generic, Optional

# ============================================================
# TYPES AND ALIASES
# ============================================================

BookId = NewType('BookId', str)
UserId = NewType('UserId', str)
ISBN: TypeAlias = str

# ============================================================
# PROTOCOLS
# ============================================================

class Searchable(Protocol):
    """
    Any object that can be searched by a query string.
    """
    def matches_query(self, query: str) -> bool:
        ...

# ============================================================
# DATA MODELS
# ============================================================

class Book:
    def __init__(self, book_id: BookId, title: str, author: str, isbn: ISBN) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out: bool = False

    def matches_query(self, query: str) -> bool:
        """Satisfies the Searchable protocol."""
        query = query.lower()
        return query in self.title.lower() or query in self.author.lower()

class User:
    def __init__(self, user_id: UserId, name: str) -> None:
        self.user_id = user_id
        self.name = name
        self.borrowed_books: list[Book] = []

# ============================================================
# GENERICS
# ============================================================

T_Searchable = TypeVar('T_Searchable', bound=Searchable)

class SearchIndex(Generic[T_Searchable]):
    """
    A generic searchable index that can store Books, Users, or anything 
    else that implements the Searchable protocol.
    """
    def __init__(self) -> None:
        self.items: list[T_Searchable] = []

    def add(self, item: T_Searchable) -> None:
        self.items.append(item)

    def search(self, query: str) -> list[T_Searchable]:
        return [item for item in self.items if item.matches_query(query)]

# ============================================================
# MAIN APPLICATION LOGIC
# ============================================================

class LibrarySystem:
    def __init__(self) -> None:
        self.books: dict[BookId, Book] = {}
        self.users: dict[UserId, User] = {}
        self.book_index: SearchIndex[Book] = SearchIndex()

    def add_book(self, title: str, author: str, isbn: ISBN) -> BookId:
        """Adds a book to the library."""
        new_id = BookId(f"B-{len(self.books) + 1:04d}")
        new_book = Book(new_id, title, author, isbn)
        self.books[new_id] = new_book
        self.book_index.add(new_book)
        return new_id

    def add_user(self, name: str) -> UserId:
        """Adds a user to the library system."""
        new_id = UserId(f"U-{len(self.users) + 1:04d}")
        self.users[new_id] = User(new_id, name)
        return new_id

    def checkout_book(self, user_id: UserId, book_id: BookId) -> bool:
        """
        Allows a user to check out a book. Returns True if successful.
        """
        user: Optional[User] = self.users.get(user_id)
        book: Optional[Book] = self.books.get(book_id)

        if user is None or book is None:
            print("Error: User or Book not found.")
            return False

        if book.is_checked_out:
            print(f"Error: '{book.title}' is already checked out.")
            return False

        book.is_checked_out = True
        user.borrowed_books.append(book)
        print(f"Success: {user.name} checked out '{book.title}'.")
        return True

    def search_books(self, query: str) -> list[Book]:
        """Searches the library via the Generic SearchIndex."""
        return self.book_index.search(query)

# ============================================================
# EXECUTION
# ============================================================

if __name__ == "__main__":
    library = LibrarySystem()
    
    # Add Books
    b1 = library.add_book("1984", "George Orwell", "978-0451524935")
    b2 = library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0060935467")
    b3 = library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    
    # Add Users
    u1 = library.add_user("Alice Smith")
    u2 = library.add_user("Bob Johnson")
    
    # Perform Actions
    library.checkout_book(u1, b1)
    
    # This would be caught by mypy if we tried to pass a BookId to a UserId!
    # library.checkout_book(b1, u1) # type checker ERROR
    
    # Try to checkout an already checked out book
    library.checkout_book(u2, b1)
    
    # Search
    print("\nSearch results for 'Orwell':")
    results = library.search_books("Orwell")
    for b in results:
        print(f" - {b.title}")
