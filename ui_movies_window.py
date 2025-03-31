# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_movies_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import random

try:
    import urllib
    from PyQt5 import QtCore, QtGui, QtWidgets

except ImportError as e:
    print(f"Installation error: {e}")
    raise


class Ui_Dialog(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 455)
        Dialog.setStyleSheet("background:rgb(255, 255, 255);\n"
                             "background: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, -10, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 420, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 70, 201, 131))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 201, 131))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 250, 201, 131))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 201, 131))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.retranslate_ui(Dialog)
        self.display_images(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate_ui(self, MovieWindow):
        _translate = QtCore.QCoreApplication.translate
        MovieWindow.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "movies for you:"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton.clicked.connect(MovieWindow.on_push_button_click)

    def display_images(self, MovieWindow):
        movies = MovieWindow.get_movies()
        length = len(movies)
        lblarr = [self.label_4, self.label_5, self.label_6, self.label_7]
        choose = []
        for i in range(4):
            if length == i:
                break
            j = random.randint(0, length - 1)
            while (j in choose):
                j = random.randint(0, length - 1)
            choose.append(j)
            url = movies[j]
            data = urllib.request.urlopen(url).read()
            image = QtGui.QImage()

            image.loadFromData(data)
            pixmap1 = QtGui.QPixmap(image)
            lblarr[i].setPixmap(pixmap1.scaled(201, 131))
