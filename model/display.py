import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QSize


class ShowData(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(QSize(1240, 640))
        #self.setWindowIcon(QIcon('data/favicon.png'))
        self.title = "Atom Login"
        self.left = 10
        self.top = 10
        self.width = 1240
        self.height = 640
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create widget image
        label = QLabel(self)
        #pixmap = QPixmap("data/image/darkly_logo_resize.png")
        #label.setPixmap(pixmap)
        label.resize(600, 133)
        label.move(300, 130)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowData()
    sys.exit(app.exec_())