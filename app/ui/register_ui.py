# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerQfxEhH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class register_ui(QMainWindow):
    signal = QtCore.pyqtSignal(str, str, str, str)

    def __init__(self, *args, **kwargs):
        # print(5)
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.setWindowIcon(QIcon('./ui/img/bg.ico'))
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 480)

        font2 = QFont()
        font2.setFamily(u"\u6977\u4f53")
        font2.setPointSize(16)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 360, 100, 40))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton")
        self.pushButton_2.setGeometry(QRect(380, 360, 100, 40))
        self.name_in = QLineEdit(self.centralwidget)
        self.name_in.setObjectName(u"lineEdit_2")
        self.name_in.setGeometry(QRect(120, 110, 360, 60))
        self.phone_in = QLineEdit(self.centralwidget)
        self.phone_in.setObjectName(u"lineEdit")
        self.phone_in.setGeometry(QRect(120, 40, 360, 60))
        self.password_in = QLineEdit(self.centralwidget)
        self.password_in.setObjectName(u"lineEdit_3")
        self.password_in.setGeometry(QRect(120, 180, 360, 60))
        self.repassword_in = QLineEdit(self.centralwidget)
        self.repassword_in.setObjectName(u"lineEdit_4")
        self.repassword_in.setGeometry(QRect(120, 250, 360, 60))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 541, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.phone_in.setFont(font2)
        self.name_in.setFont(font2)
        self.password_in.setFont(font2)
        self.repassword_in.setFont(font2)
        self.pushButton.setFont(font2)
        self.pushButton_2.setFont(font2)
        self.password_in.setEchoMode(QLineEdit.Password)
        self.repassword_in.setEchoMode(QLineEdit.Password)
        # self.bar = QtWidgets.QMenuBar(MainWindow)
        # self.bar.setGeometry(QRect(0, 0, 200, 30))
        # file = self.bar.addMenu('菜单')
        # file.addAction('关闭软件')
        # self.setMenuBar(self.bar)
        self.retranslateUi(MainWindow)
        self.setWindowOpacity(0.93)

        self.pushButton.clicked.connect(self.reg_click)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"注册", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"返回", None))
        self.name_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.phone_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u624b\u673a", None))
        self.password_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.repassword_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5bc6\u7801", None))

    # retranslateUi
    def reg_click(self):
        self.signal.emit(
            self.phone_in.text(), self.name_in.text(),
            self.password_in.text(), self.repassword_in.text()
        )
