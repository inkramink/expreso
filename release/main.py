import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from main_ui import Ui_Main
from addEditCoffeeForm_ui import Coffee_ui

COLUMS = ['id', 'name',
    'bake_state', 'is_milled',
    'discription', 'price',
    'package']


class DBSample(QMainWindow, Ui_Main, Coffee_ui):
    def __init__(self):
        super().__init__()
        self.main_window()
    
    def main_window(self):
        self.setupUi_main(self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.select_data()
        self.change_chosen_btn.clicked.connect(self.change_data_window)
        self.new_line_btn.clicked.connect(self.new_line)

    def select_data(self):
        res = self.connection.cursor().execute("SELECT * FROM coffee_list").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()

    def new_line(self):
        self.connection.cursor().execute(
            "INSERT INTO coffee_list VALUES (0, '', 0, 0, '', 0, 0)"
            )
        self.connection.commit()
        self.select_data()
    
    def change_data_window(self):
        self.connection = sqlite3.connect("coffee.sqlite")
        data = self.tableWidget.selectedItems()[0].text()
        self.ind = self.tableWidget.selectedIndexes()[0]
        self.setupUi_coffee(self)
        self.save.clicked.connect(self.save_to_db)
        self.new_data.setPlainText(str(data))
    
    def save_to_db(self):
        changed_data = self.new_data.toPlainText()
        column, row = COLUMS[self.ind.column()], self.ind.row()

        if self.ind.column() in [1, 4]:
            self.connection.cursor().execute(
                f"UPDATE coffee_list set {column} = '{changed_data}' WHERE id = {row}"
                )
        else:
            self.connection.cursor().execute(
                f"UPDATE coffee_list set {column} = {changed_data} WHERE id = {row}"
                )

        self.connection.commit()
        self.connection.close()
        self.main_window()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
