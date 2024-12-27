print("accessing PublicView.py")
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from src.controllers.book_controller import BookController

class PublicView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Manager App Online")
        self.setGeometry(600, 200 , 800, 600) # (x, y, width, height)
        self.setWindowIcon(QIcon("src/img/cup_of_coffee_logo_flat.png"))
        self.controller = BookController()
        self.buttonSearchBooks = QPushButton("Lancer la recherche", self)
        self.line_edit = QLineEdit(self)
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        labelTitle = QLabel("Library Manager App Online", self)
        labelTitle.setFont(QFont("Arial", 20))
        
        labelTitle.setStyleSheet("color: #6a04c9;"
                            # "background-color: #f6f7e9;"
                            "font-weight: bold;")
        
        labelTitle.setAlignment(Qt.AlignCenter) # all center
    
            # set image
        labelLibImg = QLabel(self)
        pixmap = QPixmap("src/img/library_image.jpg")
        labelLibImg.setPixmap(pixmap)
        labelLibImg.setScaledContents(True)
        
            # Welcome message
        labelWelcomeMessage = QLabel("Bienvenue ! Quel livre recherchez vous ?", self)
        labelWelcomeMessage.setFont(QFont("Arial", 10))
        labelWelcomeMessage.setStyleSheet("color: #6a04c9;")
        labelWelcomeMessage.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
                
            # button searching books
        self.buttonSearchBooks.setStyleSheet("font-size: 20px")
        self.buttonSearchBooks.clicked.connect(self.searchBooks)
        
            # display results area
        self.labelDisplayResults = QLabel("", self)
        self.labelDisplayResults.setStyleSheet("font-size: 15px")
        
            # input
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.line_edit.setPlaceholderText("Entrez votre recherche")
        
            # results display
        self.results_list = QListWidget()
        
            # LAYOUTS
        vbox = QVBoxLayout()
        vbox.addWidget(labelLibImg)
        vbox.addWidget(labelTitle)
        vbox.addWidget(labelWelcomeMessage)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.buttonSearchBooks)
        vbox.addWidget(self.results_list)

        central_widget.setLayout(vbox)
        
    def searchBooks(self): 
        query = self.line_edit.text()
        books = self.controller.search_books(query)
        self.results_list.clear()

        for book in books:
            self.results_list.addItem(f"{book.title} - {book.author} ({book.publication_year})")
        
