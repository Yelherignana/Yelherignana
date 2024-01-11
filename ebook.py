class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(f"Book Title: {self.title}")

class EBook(Book):
    def __init__(self, title, file_format):
        super().__init__(title)
        self.file_format = file_format

    def display(self):
        super().display()
        print(f"File Format: {self.file_format}")
book1 = Book("The Great Gatsby")
book1.display()

ebook1 = EBook("Python","PDF")
ebook1.display()

