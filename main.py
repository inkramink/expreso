import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.data()

    def data(self):
        res = self.connection.cursor().execute("SELECT * FROM coff").fetchall()
        self.tw.setColumnCount(7)
        self.tw.setRowCount(0)
        for i, row in enumerate(res):
            self.tw.setRowCount(
                self.tw.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tw.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())

