from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Define the database URL for SQLAlchemy

# DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/company"
DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Define a Base class for our ORM models
Base = declarative_base()

# Define a simple User model as an example
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    
    
# Create the database tables (if not already created)
Base.metadata.create_all(engine)

# Create a Session class and establish a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Example of adding a user to the database
def add_example_user():
    new_user = User(name="Bob Kelso", email="bk@example.com")
    session.add(new_user)
    session.commit()
    print("Added new user:", new_user)
    
def add_book():
    new_book = Book(name="Foundation")
    session.add(new_book)
    another_new_book = Book(name="Foundation II")
    session.add(another_new_book)
    session.commit()
    print("Added new book: ", new_book)
    print("Added new book: ", another_new_book)

# Main function to run the script
if __name__ == "__main__":
    # Add an example user
    add_example_user()
    add_book()

    # Query and print all users
    users = session.query(User).all()
    for user in users:
        print(f"User {user.id}: {user.name}, {user.email}")
        
    books = session.query(Book).all()
    for book in books:
        print(f"Book {book.name}")
