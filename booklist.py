class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
book1.display_info()

