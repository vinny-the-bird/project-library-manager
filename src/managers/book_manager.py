from src.repositories.book_repository import BookRepository

class BookManager:
    def __init__(self):
        self.repository = BookRepository()

    def get_all_books(self):
        return self.repository.fetch_all_books()

    def get_books_by_title(self, title: str):
        return self.repository.fetch_books_by_title(title)
