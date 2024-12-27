from sqlalchemy.orm import Session
from src.db.session import SessionLocal
from src.entities.book import Book

class BookRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def fetch_all_books(self):
        return self.db.query(Book).all()

    def fetch_books_by_title(self, title: str):
        return self.db.query(Book).filter(Book.title.like(f"%{title}%")).all()
