import sys
from PyQt5.QtWidgets import QApplication
from src.views.public_view import PublicView

def main():
    app = QApplication(sys.argv)
    main_window = PublicView()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()