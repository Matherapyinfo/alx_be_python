# library_system.py

class Book:
    """Base class representing a book"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    """EBook class inheriting from Book with additional file_size attribute"""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

class PrintBook(Book):
    """PrintBook class inheriting from Book with additional page_count attribute"""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """Library class managing a collection of books using composition"""
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """Add any type of book to the library collection"""
        self.books.append(book)
    
    def list_books(self):
        """List all books with type-specific formatting"""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
