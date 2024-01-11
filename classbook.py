class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")

class EBook(Book):
    def __init__(self, title, author, file_format):
        super()._init_(title, author)
        self.file_format = file_format

    def display(self):
        super().display()
        print(f"File Format: {self.file_format}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display()

# Testing functionality with exception handling
try:
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook1 = EBook("Python Crash Course", "Eric Matthes", "PDF")

    library = Library()
    library.add_book(book1)
    library.add_book(ebook1)

    library.display_books()

except Exception as e:
    print(f"An error occurred: {e}")
