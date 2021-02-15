import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor, QPolygonF
from math import radians, cos, sin, sqrt
from xxx import Ui_MainWindow

SCREEN_SIZE = [500, 500]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.paint)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.x, self.y = randint(0, 500), randint(0, 500)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(5, 200)
        qp.drawEllipse(self.x - r, self.y - r, self.x + r, self.y + r)
        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
