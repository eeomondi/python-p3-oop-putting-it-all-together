#!/usr/bin/env python3

import pytest
from lib.book import Book

def test_book_creation():
    book = Book("1984", "George Orwell", 328)  # Ensure you pass the page_count
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.page_count == 328  # Add this assertion for page_count
    assert book.is_checked_out is False


def test_check_out():
    book = Book("1984", "George Orwell")
    book.check_out()
    assert book.is_checked_out is True

def test_return_book():
    book = Book("1984", "George Orwell")
    book.check_out()
    book.return_book()
    assert book.is_checked_out is False

