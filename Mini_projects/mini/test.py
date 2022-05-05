from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.b1 = None
        self.label = None
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("test")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my Label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(50, 70)
        self.b1.setText("button")
        self.b1.clicked.connect(self.clicks)

    def clicks(self):
        self.label.setText("Button Clcickedawdawd fawf")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
