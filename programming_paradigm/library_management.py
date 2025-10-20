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
        self._is_checked_out = False  # Private attribute to track availability

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
    """Represents a collection of books and provides methods to manage them."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Add a Book instance to the library collection.
        Args:
            book (Book): The Book object to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book instances can be added to the library.")

    def check_out_book(self, title):
        """
        Check out a book by its title.
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
        Return a checked-out book to the library.
        Args:
            title (str): The title of the book to return.
        """

