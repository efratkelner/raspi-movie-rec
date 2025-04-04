# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_default.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

try:
    from PyQt5 import QtCore, QtGui, QtWidgets

except ImportError as e:
    print(f"Installation error: {e}")
    raise


class Ui_DefaultWindow(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 411)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 255);\n"
                             "background: url(C:/Users/User/PycharmProjects/raspberrypi/netflix_movies_cover.jpg)\n"
                             "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -20, 521, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslate_ui(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate_ui(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; "
                                      "color:#ffffff;\">Scaning your face to get recommendations to</span></p><p "
                                      "align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">movies for "
                                      "you.</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "START"))
        self.pushButton.clicked.connect(Dialog.on_push_button_click)
