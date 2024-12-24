print("running app...")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Manager App Online")
        self.setGeometry(700, 300 , 500, 500) # (x, y, width, height)
        self.setWindowIcon(QIcon("img/cup_of_coffee_logo_flat.png"))
        
        
        labelTitle = QLabel("Library Manager App Online", self)
        labelTitle.setFont(QFont("Arial", 20))
        labelTitle.setGeometry(0, 0, 500, 100)
        labelTitle.setStyleSheet("color: #05a660;"
                            "background-color: #f6f7e9;"
                            "font-weight: bold;")
        
        labelTitle.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # label.setAlignment(Qt.AlignCenter) # all center
        
        labelLibImg = QLabel(self)
        labelLibImg.setGeometry(0, 0, 600, 250)
        
        pixmap = QPixmap("img/library_image.jpg")
        labelLibImg.setPixmap(pixmap)
        labelLibImg.setScaledContents(True)
        labelLibImg.setGeometry((self.width() - labelLibImg.width()) // 2,
                          (self.height() - labelLibImg.height()) // 2,
                          labelLibImg.width(), 
                          labelLibImg.height())
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()