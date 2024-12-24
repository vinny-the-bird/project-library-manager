print("running app...")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Manager App Online")
        self.setGeometry(600, 200 , 800, 600) # (x, y, width, height)
        self.setWindowIcon(QIcon("img/cup_of_coffee_logo_flat.png"))
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        
        labelTitle = QLabel("Library Manager App Online", self)
        labelTitle.setFont(QFont("Arial", 20))
        labelTitle.setGeometry(0, 0, 800, 0)
        
        labelTitle.setStyleSheet("color: #6a04c9;"
                            # "background-color: #f6f7e9;"
                            "font-weight: bold;")
        
        # labelTitle.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        labelTitle.setAlignment(Qt.AlignCenter) # all center
        
        labelLibImg = QLabel(self)
        labelLibImg.setGeometry(0, 0, 800, 127)
        
        pixmap = QPixmap("img/library_image.jpg")
        # pixmap = QPixmap("img/library_image_resized.jpg")
        labelLibImg.setPixmap(pixmap)
        labelLibImg.setScaledContents(True)
        labelLibImg.setGeometry((self.width() - labelLibImg.width()) // 2,
                          (self.height() - labelLibImg.height()) // 2,
                          labelLibImg.width(), 
                          labelLibImg.height())
        
        labelWelcomeMessage = QLabel("Bienvenue ! Que recherchez vous ?", self)
        labelWelcomeMessage.setFont(QFont("Arial", 10))
        labelWelcomeMessage.setStyleSheet("color: #6a04c9;")
          
        labelWelcomeMessage.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        
        labelSearchInput = QLabel("HERE input field", self)
        labelSearchButton = QLabel("HERE button to click to search", self)
        
        
        vbox = QVBoxLayout()
        vbox.addWidget(labelLibImg)
        vbox.addWidget(labelTitle)
        vbox.addWidget(labelWelcomeMessage)
        vbox.addWidget(labelSearchInput)
        vbox.addWidget(labelSearchButton)
        
        central_widget.setLayout(vbox)
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()