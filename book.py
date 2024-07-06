import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Track availability

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "available": self.available}

class BookManager:
    def __init__(self, storage_file='books.json'):
        self.storage_file = storage_file
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.storage_file, 'r') as file:
                books_data = json.load(file)
                books = []
                for book_data in books_data:
                    book = Book(book_data['title'], book_data['author'], book_data['isbn'])
                    book.available = book_data['available']  # Set availability separately
                    books.append(book)
                return books
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.storage_file, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file)

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_books()

    def list_books(self):
        for book in self.books:
            availability = "Available" if book.available else "Checked out"
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Availability: {availability}")

    def search_books(self, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key) == value]
        return results

    def update_book_availability(self, isbn, available):
        for book in self.books:
            if book.isbn == isbn:
                book.available = available
                self.save_books()
                return True
        return False
