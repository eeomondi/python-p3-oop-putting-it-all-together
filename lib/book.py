# lib/book.py
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # Add this line
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False


    
        