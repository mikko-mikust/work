from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class edit_space_ui(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"edit_space_ui")
        MainWindow.resize(360, 360)
        self.edit_ui = QWidget(MainWindow)
        self.edit_ui.setGeometry(QRect(30, 30, 280, 280))
        self.edit_ui_layout = QGridLayout(self.edit_ui)
        self.edit_ui_layout.setContentsMargins(0, 0, 0, 0)

        self.space_no = QLineEdit(self.edit_ui)
        self.space_no.setObjectName(u"space_no")
        self.space_no.setReadOnly(True)

        self.edit_ui_layout.addWidget(self.space_no, 0, 1, 1, 1)

        self.space_info = QLineEdit(self.edit_ui)
        self.space_info.setObjectName(u"space_info")
        self.space_info.setReadOnly(True)

        self.edit_ui_layout.addWidget(self.space_info, 1, 1, 1, 1)

        self.edit_out_car = QPushButton(self.edit_ui)
        self.edit_out_car.setObjectName(u"edit_out_car")

        self.edit_ui_layout.addWidget(self.edit_out_car, 4, 0, 1, 1)

        self.card = QLineEdit(self.edit_ui)
        self.card.setObjectName(u"card")

        self.edit_ui_layout.addWidget(self.card, 2, 1, 1, 1)

        self.label = QLabel(self.edit_ui)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.edit_ui_layout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.edit_ui)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.edit_ui_layout.addWidget(self.label_2, 0, 0, 1, 1)

        self.edit_in_car = QPushButton(self.edit_ui)
        self.edit_in_car.setObjectName(u"edit_in_car")

        self.edit_ui_layout.addWidget(self.edit_in_car, 4, 1, 1, 1)

        self.label_3 = QLabel(self.edit_ui)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.edit_ui_layout.addWidget(self.label_3, 1, 0, 1, 1)

        self.edit_in_time = QLabel(self.edit_ui)
        self.edit_in_time.setObjectName(u"edit_in_time")
        self.edit_in_time.setMouseTracking(False)
        self.edit_in_time.setAlignment(Qt.AlignCenter)

        self.edit_ui_layout.addWidget(self.edit_in_time, 3, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.edit_ui)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        self.edit_ui_layout.addWidget(self.dateTimeEdit, 3, 1, 1, 1)



        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"修改车位信息", None))
        self.edit_out_car.setText(QCoreApplication.translate("MainWindow", u"取车", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u4f4d\u53f7", None))
        self.edit_in_car.setText(QCoreApplication.translate("MainWindow", u"停车", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u4f4d\u4fe1\u606f", None))
        self.edit_in_time.setText(QCoreApplication.translate("MainWindow", u"\u505c\u8f66\u65f6\u95f4", None))

    # retranslateUi
