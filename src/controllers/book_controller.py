from src.managers.book_manager import BookManager

class BookController:
    def __init__(self):
        self.manager = BookManager()

    def search_books(self, query: str = ""):
        if query.strip():
            return self.manager.get_books_by_title(query)
        else:
            return self.manager.get_all_books()
