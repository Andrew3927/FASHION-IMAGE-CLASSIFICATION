# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiImgClassificationWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(941, 894)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 851, 651))
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 801, 611))
        self.textEdit.setObjectName("textEdit")
        self.fileBtn = QtWidgets.QPushButton(Dialog)
        self.fileBtn.setGeometry(QtCore.QRect(60, 690, 271, 151))
        self.fileBtn.setObjectName("fileBtn")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(580, 690, 271, 151))
        self.save.setObjectName("save")
        self.Excel = QtWidgets.QPushButton(Dialog)
        self.Excel.setGeometry(QtCore.QRect(350, 690, 211, 151))
        self.Excel.setObjectName("Excel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Display Window"))
        self.fileBtn.setText(_translate("Dialog", "Select Folder"))
        self.save.setText(_translate("Dialog", "Save as .txt"))
        self.Excel.setText(_translate("Dialog", "Save as Excel"))
