 class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print(f"Book '{title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

    def search_book(self, title):
        if title in self.books:
            print(f"Book '{title}' is available in the library.")
        else:
            print(f"Book '{title}' not found in the library.")

library = Library()
library.add_book("The Catcher in the Rye")
library.add_book("To Kill a Mockingbird")
library.display_books()
library.search_book("To Kill a Mockingbird")
library.search_book("1984")
