# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push = QtWidgets.QPushButton(self.centralwidget)
        self.push.setGeometry(QtCore.QRect(90, 360, 211, 151))
        self.push.setObjectName("push")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 360, 211, 151))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Imglabel = QtWidgets.QLabel(self.centralwidget)
        self.Imglabel.setGeometry(QtCore.QRect(10, 0, 781, 601))
        self.Imglabel.setText("")
        self.Imglabel.setObjectName("Imglabel")
        self.Imglabel.raise_()
        self.push.raise_()
        self.pushButton_2.raise_()
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
        self.push.setText(_translate("MainWindow", "Single Image\n"
"Classification"))
        self.pushButton_2.setText(_translate("MainWindow", "Multi Images\n"
"Classification"))
