# lib/book.py

class Book:
    def __init__(self, title, author, page_count=0):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.is_checked_out = False  # Default value for the checkout status

    def check_out(self):
        """Mark the book as checked out."""
        self.is_checked_out = True

    def return_book(self):
        """Return the book and mark it as not checked out."""
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}, {self.page_count} pages"


    
        