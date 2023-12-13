from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class edit_user_ui(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"edit_user_ui")
            MainWindow.resize(360, 360)
            self.centralwidget = QWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")
            self.gridLayoutWidget = QWidget(self.centralwidget)
            self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
            self.gridLayoutWidget.setGeometry(QRect(10, 0, 281, 321))
            self.gridLayout = QGridLayout(self.gridLayoutWidget)
            self.gridLayout.setObjectName(u"gridLayout")
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.label_3 = QLabel(self.gridLayoutWidget)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setAlignment(Qt.AlignCenter)

            self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

            self.is_banned = QComboBox(self.gridLayoutWidget)
            self.is_banned.addItem("")
            self.is_banned.addItem("")
            self.is_banned.setObjectName(u"is_banned")

            self.gridLayout.addWidget(self.is_banned, 4, 1, 1, 1)

            self.is_admin = QComboBox(self.gridLayoutWidget)
            self.is_admin.addItem("")
            self.is_admin.addItem("")
            self.is_admin.setObjectName(u"is_admin")

            self.gridLayout.addWidget(self.is_admin, 3, 1, 1, 1)

            self.label = QLabel(self.gridLayoutWidget)
            self.label.setObjectName(u"label")
            self.label.setAlignment(Qt.AlignCenter)

            self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

            self.label_2 = QLabel(self.gridLayoutWidget)
            self.label_2.setObjectName(u"label_2")
            self.label_2.setAlignment(Qt.AlignCenter)

            self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

            self.buttonBox = QDialogButtonBox(self.gridLayoutWidget)
            self.buttonBox.setObjectName(u"buttonBox")
            self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
            self.buttonBox.setCenterButtons(True)

            self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)

            self.label_4 = QLabel(self.gridLayoutWidget)
            self.label_4.setObjectName(u"label_4")
            self.label_4.setAlignment(Qt.AlignCenter)

            self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

            self.label_5 = QLabel(self.gridLayoutWidget)
            self.label_5.setObjectName(u"label_5")
            self.label_5.setAlignment(Qt.AlignCenter)

            self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
            self.setWindowOpacity(0.93)

            self.phone = QLineEdit(self.gridLayoutWidget)
            self.phone.setObjectName(u"phone")
            self.phone.setReadOnly(True)
            self.gridLayout.addWidget(self.phone, 0, 1, 1, 1)

            self.name_in = QLineEdit(self.gridLayoutWidget)
            self.name_in.setObjectName(u"name_in")

            self.gridLayout.addWidget(self.name_in, 1, 1, 1, 1)

            self.password_in = QLineEdit(self.gridLayoutWidget)
            self.password_in.setObjectName(u"password_in")

            self.gridLayout.addWidget(self.password_in, 2, 1, 1, 1)
            self.buttonBox.rejected.connect(self.click_no)

            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)

            QMetaObject.connectSlotsByName(MainWindow)

        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"修改用户信息", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5458", None))
        self.is_banned.setItemText(0, QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.is_banned.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.password_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"未修改", None)
        )
        self.is_admin.setItemText(0, QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.is_admin.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5426", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7981\u6b62\u767b\u5f55", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a", None))
    # retranslateUi

    def click_no(self):
        self.close()
        pass
