# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tw = QtWidgets.QTableWidget(self.centralwidget)
        self.tw.setGeometry(QtCore.QRect(0, 0, 801, 461))
        self.tw.setObjectName("tw")
        self.tw.setColumnCount(0)
        self.tw.setRowCount(0)
        self.ccbtn = QtWidgets.QPushButton(self.centralwidget)
        self.ccbtn.setGeometry(QtCore.QRect(0, 460, 400, 75))
        self.ccbtn.setObjectName("ccbtn")
        self.nlbtn = QtWidgets.QPushButton(self.centralwidget)
        self.nlbtn.setGeometry(QtCore.QRect(400, 460, 400, 75))
        self.nlbtn.setObjectName("nlbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ccbtn.setText(_translate("MainWindow", "изменить выбранную ячейку"))
        self.nlbtn.setText(_translate("MainWindow", "новая строка"))
