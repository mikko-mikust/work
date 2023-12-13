# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


################################################################################
## Form generated from reading UI file 'designerbhMoUO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class login_ui(QMainWindow):
    # logic = logic.logic()
    signal = QtCore.pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        # print()
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.setWindowIcon(QIcon('./ui/img/bg3.jpg'))
        MainWindow.resize(800, 660)

        self.setAutoFillBackground(True)
        self.pic = QPixmap('./ui/img/bg5.jpeg')
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(self.pic.scaled(self.width(), self.height())))
        self.setPalette(self.palette)

        MainWindow.setObjectName(u"主菜单")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.login_but = QPushButton(self.centralwidget)
        self.login_but.setObjectName(u"login_but")
        self.login_but.setGeometry(QRect(260, 300, 131, 51))
        font = QFont()
        font.setFamily(u"\u6977\u4f53")
        font.setPointSize(18)
        self.login_but.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 130, 51, 41))
        font1 = QFont()
        font1.setFamily(u"\u6977\u4f53")
        font1.setPointSize(12)
        font1.setStrikeOut(False)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setIndent(0)
        self.phone_in = QLineEdit(self.centralwidget)
        self.phone_in.setObjectName(u"phone_in")
        self.phone_in.setGeometry(QRect(250, 120, 360, 60))
        font2 = QFont()
        font2.setFamily(u"\u6977\u4f53")
        font2.setPointSize(16)
        self.phone_in.setFont(font2)
        self.phone_in.setMaxLength(11)
        self.phone_in.setEchoMode(QLineEdit.Normal)
        self.phone_in.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.phone_in.setClearButtonEnabled(True)
        self.password_in = QLineEdit(self.centralwidget)
        self.password_in.setObjectName(u"password_in")
        self.password_in.setGeometry(QRect(250, 200, 360, 60))
        self.password_in.setFont(font2)
        self.password_in.setMaxLength(16)
        self.password_in.setEchoMode(QLineEdit.Password)
        self.password_in.setDragEnabled(False)
        self.password_in.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.password_in.setClearButtonEnabled(True)
        self.register_but = QPushButton(self.centralwidget)
        self.register_but.setObjectName(u"register_but")
        self.register_but.setGeometry(QRect(450, 300, 121, 51))
        self.register_but.setFont(font)
        self.eye_but = QPushButton(self.centralwidget)
        self.eye_but.setObjectName(u"eye_but")
        self.eye_but.setGeometry(QRect(630, 200, 61, 51))
        self.not_eye_but = QPushButton(self.centralwidget)
        self.not_eye_but.setObjectName(u"not_eye_but")
        self.not_eye_but.setGeometry(QRect(630, 200, 61, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        # self.register_but.clicked.connect(self.logic.register_click)
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        # self.login_but.clicked.connect(self.login_click)
        self.not_eye_but.hide()
        self.eye_but.clicked.connect(self.eye_click)
        self.not_eye_but.clicked.connect(self.not_eye_click)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"登陆", None))
        self.login_but.setText(QCoreApplication.translate("MainWindow", u"\u767b\u9646", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.phone_in.setText("")
        self.phone_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u624b\u673a\u53f7", None))
        self.password_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.register_but.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.eye_but.setText(QCoreApplication.translate("MainWindow", u"显示", None))
        self.not_eye_but.setText(QCoreApplication.translate("MainWindow", u"隐藏", None))
        # self.signal.connect(self.logic.check_login)
        self.setWindowOpacity(0.93)

    def login_click(self):
        self.signal.emit(
            self.phone_in.text(), self.password_in.text()
        )

    def eye_click(self):
        self.password_in.setEchoMode(QLineEdit.Normal)
        self.eye_but.hide()
        self.not_eye_but.show()


    def not_eye_click(self):
        self.password_in.setEchoMode(QLineEdit.Password)
        self.not_eye_but.hide()
        self.eye_but.show()

    # retranslateUi
