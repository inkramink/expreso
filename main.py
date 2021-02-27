import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

COLUMS = ['id', 'name',
          'bake_state', 'is_milled',
          'discription', 'price',
          'package']


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window()

    def main_window(self):
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.select_data()
        self.ccbtn.clicked.connect(self.change_data_window)
        self.nlbtn.clicked.connect(self.new_line)

    def select_data(self):
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

    def new_line(self):
        self.connection.cursor().execute(
            "INSERT INTO coff VALUES (0, '', 0, 0, '', 0, 0)"
        )
        self.connection.commit()
        self.select_data()

    def change_data_window(self):
        self.connection = sqlite3.connect("coffee.db")
        data = self.tw.selectedItems()[0].text()
        self.ind = self.tw.selectedIndexes()[0]
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.save.clicked.connect(self.save_to_db)
        self.new_data.setPlainText(str(data))

    def save_to_db(self):
        changed_data = self.new_data.toPlainText()
        column, row = COLUMS[self.ind.column()], self.ind.row()

        if self.ind.column() in [1, 4]:
            self.connection.cursor().execute(
                f"UPDATE coff set {column} = '{changed_data}' WHERE id = {row}"
            )
        else:
            self.connection.cursor().execute(
                f"UPDATE coff set {column} = {changed_data} WHERE id = {row}"
            )

        self.connection.commit()
        self.connection.close()
        self.main_window()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
