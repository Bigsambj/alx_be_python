#!/usr/bin/python3
"""
Module: library_management
Defines Book and Library classes for a simple library management system.
"""

class Book:
    """Represents a book with a title, author, and checked-out status."""

    def __init__(self, title, author):
        """
        Initialize a new Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute for availability tracking

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initialize an empty list to store Book instances."""
        self._books = []

    def add_book(self, book):
        """
        Add a new Book instance to the library.
        Args:
            book (Book): The book object to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book instances can be added.")

    def check_out_book(self, title):
        """
        Check out a book from the library by title.
        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """
        Return a book to the library by title.
        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """
        List all books currently available in the library.
        This method prints each book's title and author.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
