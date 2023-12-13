# -*- coding: utf-8 -*-
import datetime

from PyQt5 import QtWidgets

################################################################################
## Form generated from reading UI file 'designercApEZI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class main_ui(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.setWindowIcon(QIcon('./ui/img/bg2.gif'))
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Main_ui")
        MainWindow.resize(681, 527)
        font2 = QFont()
        font2.setFamily(u"\u6977\u4f53")
        font2.setPointSize(17)
        self.setAutoFillBackground(True)
        self.pic = QPixmap('./ui/img/bg3.jpg')
        self.pic2 = QPixmap('./ui/img/bg4.jpg')
        self.palette = QPalette()
        self.palette2 = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(self.pic.scaled(self.width(), self.height())))
        self.palette2.setBrush(QPalette.Background, QBrush(self.pic2.scaled(self.width(), self.height())))
        self.setPalette(self.palette)

        self.warn = QMessageBox(
            QMessageBox.Warning, '警告', '真的要删除该用户喵?', QMessageBox.Ok | QMessageBox.Cancel
        )

        self.ui1 = QWidget(MainWindow)
        self.ui1.setObjectName(u"ui1")
        self.ui1.setGeometry(QRect(44, 90, 601, 271))
        self.ui1_layout = QGridLayout(self.ui1)
        self.ui1_layout.setObjectName(u"ui1_layout")
        self.ui1_layout.setContentsMargins(0, 0, 0, 0)
        self.topic_text = QTextBrowser(self.ui1)
        self.ui1_layout.addWidget(self.topic_text, 0, 0, 1, 5)


        self.horizontalLayoutWidget = QWidget(MainWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 30, 581, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.ui_1_but = QPushButton(self.horizontalLayoutWidget)
        self.ui_1_but.setObjectName(u"ui_1_but")
        self.horizontalLayout.addWidget(self.ui_1_but)

        self.ui_2_but = QPushButton(self.horizontalLayoutWidget)
        self.ui_2_but.setObjectName(u"ui_2_but")
        # self.ui_1_but.hide()
        # self.ui_2_but.hide()
        self.horizontalLayout.addWidget(self.ui_2_but)

        self.ui_3_but = QPushButton(self.horizontalLayoutWidget)
        self.ui_3_but.setObjectName(u"ui_3_but")
        self.horizontalLayout.addWidget(self.ui_3_but)

        self.ui_4_but = QPushButton(self.horizontalLayoutWidget)
        self.ui_4_but.setObjectName(u"ui_4_but")
        self.horizontalLayout.addWidget(self.ui_4_but)

        self.ui_5_but = QPushButton(self.horizontalLayoutWidget)
        self.ui_5_but.setObjectName(u"ui_5_but")
        self.horizontalLayout.addWidget(self.ui_5_but)

        self.ui_6_but = QPushButton(self.horizontalLayoutWidget)
        self.ui_6_but.setObjectName(u"ui_6_but")
        self.horizontalLayout.addWidget(self.ui_6_but)

        self.ui_7_but = QPushButton(self.horizontalLayoutWidget)
        self.ui_7_but.setObjectName(u"ui_7_but")
        self.horizontalLayout.addWidget(self.ui_7_but)
        #
        self.park_space_gui_widget = QWidget(MainWindow)
        self.park_space_gui_widget.setObjectName(u"park_space_gui_widget")
        self.park_space_gui_widget.setGeometry(QRect(40, 90, 601, 420))
        self.park_space_gui = QGridLayout(self.park_space_gui_widget)
        self.park_space_gui.setObjectName(u"park_space_gui")
        self.park_space_gui.setContentsMargins(0, 0, 0, 0)
        self.table_park_space_model=QStandardItemModel(4, 5)
        self.table_park_space = QTableView(self.park_space_gui_widget)
        self.table_park_space.setObjectName(u"table_park_space")
        self.table_park_space.setModel(self.table_park_space_model)
        self.table_park_space.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # self.table_park_space.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_park_space.setSelectionMode(QAbstractItemView.SingleSelection)
        #self.table_park_space.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_park_space.setEditTriggers(QTableView.NoEditTriggers)
        #self.table_park_space.doubleClicked.connect(self.show)
        self.park_space_gui.addWidget(self.table_park_space, 2, 0, 1, 5)
        #
        self.admin_users_gui_widget = QWidget(MainWindow)
        self.admin_users_gui_widget.setObjectName(u"admin_users_gui_widget")
        self.admin_users_gui_widget.setGeometry(QRect(40, 90, 601, 420))
        self.admin_users_gui = QGridLayout(self.admin_users_gui_widget)
        self.admin_users_gui.setObjectName(u"admin_users_gui")
        self.admin_users_gui.setContentsMargins(0, 0, 0, 0)
        self.table_user_model = QStandardItemModel(0, 3)
        self.table_user_model.setHorizontalHeaderLabels(['手机', '用户名', '禁止登录', '管理员'])
        self.table_user = QTableView(self.admin_users_gui_widget)
        self.table_user.setObjectName(u"table_user")
        self.table_user.setModel(self.table_user_model)
        self.table_user.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # self.table_user.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_user.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_user.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_user.setEditTriggers(QTableView.NoEditTriggers)
        self.admin_users_gui.addWidget(self.table_user, 1, 0, 1, 5)
        self.admin_users_ser_but = QPushButton(self.admin_users_gui_widget)
        self.admin_users_ser_but.setObjectName(u"ser_but")
        self.ser_input = QLineEdit(self.admin_users_gui_widget)
        self.ser_input.setObjectName("ser_input")
        self.ser_input.setClearButtonEnabled(True)
        self.admin_users_gui.addWidget(self.ser_input, 0, 2, 1, 2)
        self.admin_users_gui.addWidget(self.admin_users_ser_but, 0, 4, 1, 1)
        self.edit_user_but = QPushButton(self.admin_users_gui_widget)
        self.edit_user_but.setObjectName('edit_user_but')
        self.admin_users_gui.addWidget(self.edit_user_but, 0, 1, 1, 1)
        self.del_user_but = QPushButton(self.admin_users_gui_widget)
        self.del_user_but.setObjectName('del_user_but')
        self.admin_users_gui.addWidget(self.del_user_but, 0, 0, 1, 1)

        self.admin_park_gui_widget = QWidget(MainWindow)
        self.admin_park_gui_widget.setObjectName('admin_park_gui_widget')
        self.admin_park_gui_widget.setGeometry(QRect(40, 90, 601, 420))
        self.admin_park_gui = QGridLayout(self.admin_park_gui_widget)
        self.admin_park_gui.setObjectName('admin_park_gui')
        self.admin_park_gui.setContentsMargins(0, 0, 0, 0)
        #self.park_in_but = QPushButton(self.admin_park_gui_widget)
        # self.park_out_but = QPushButton(self.admin_park_gui_widget)
        # #self.park_in_but.setObjectName('park_in_but')
        # self.park_out_but.setObjectName('park_out_but')
        # self.admin_park_gui.addWidget(self.park_out_but, 0, 0, 1, 1)
        #self.admin_park_gui.addWidget(self.park_in_but, 1, 4, 1, 1)

        self.admin_park_ser_but = QPushButton(self.admin_park_gui_widget)
        self.admin_park_ser_but.setObjectName(u"admin_park_ser_but")
        self.admin_park_ser_input = QLineEdit(self.admin_park_gui_widget)
        self.admin_park_ser_input.setObjectName("admin_park_ser_input")
        self.admin_park_ser_input.setClearButtonEnabled(True)
        self.admin_park_gui.addWidget(self.admin_park_ser_input, 0, 2, 1, 2)
        self.admin_park_gui.addWidget(self.admin_park_ser_but, 0, 4, 1, 1)

        self.table_park_model = QStandardItemModel(0, 3)
        self.table_park_model.setHorizontalHeaderLabels(['车辆类型', '车牌号', '停车时间'])
        self.table_park = QTableView(self.admin_park_gui_widget)
        self.table_park.setObjectName(u"table_park")
        self.table_park.setModel(self.table_park_model)
        self.table_park.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # self.table_park.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.table_park.horizontalHeader().setResizeContentsPrecision(20)
        # self.table_park.horizontalHeader().se
        self.table_park.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_park.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_park.setEditTriggers(QTableView.NoEditTriggers)
        self.admin_park_gui.addWidget(self.table_park, 2, 0, 1, 5)
        # self.park_in_time = QDateTimeEdit(self.admin_park_gui_widget)
        # self.park_in_time.setObjectName('park_in_time')
        # self.park_in_time.setCalendarPopup(True)
        # self.admin_park_gui.addWidget(self.park_in_time, 1, 3, 1, 1)
        # self.park_in_time.setDateTime(QDateTime.currentDateTime())
        # # print(self.park_in_time.dateTime().toTime_t())
        # # print(datetime.datetime.fromtimestamp(1687161678))
        # self.admin_card_in = QLineEdit(self.admin_park_gui_widget)
        # self.admin_card_in.setObjectName('admin_card_in')
        # # self.admin_card_in.resize(30, 50)
        # self.admin_park_gui.addWidget(self.admin_card_in, 1, 1, 1, 1)
        # self.admin_locate_in = QLineEdit(self.admin_park_gui_widget)
        # self.admin_park_gui.addWidget(self.admin_locate_in, 1, 2, 1, 1)
        # self.admin_car_type = QComboBox(self.admin_park_gui_widget)
        # self.admin_car_type.setObjectName('admin_car_type')
        # self.admin_car_type.addItem('四轮车')
        # self.admin_car_type.addItem('两轮车')
        # self.admin_park_gui.addWidget(self.admin_car_type, 1, 0, 1, 1)

        self.admin_bill_gui_widget = QWidget(MainWindow)
        self.admin_bill_gui_widget.setObjectName('admin_bill_gui_widget')
        self.admin_bill_gui_widget.setGeometry(QRect(40, 90, 601, 420))
        self.admin_bill_gui = QGridLayout(self.admin_bill_gui_widget)
        self.admin_bill_gui.setObjectName('admin_bill_gui')
        self.admin_bill_gui.setContentsMargins(0, 0, 0, 0)
        self.admin_bill_ser_but = QPushButton(self.admin_bill_gui_widget)
        self.admin_bill_ser_but.setObjectName(u"admin_bill_ser_but")
        self.admin_bill_ser_input = QLineEdit(self.admin_bill_gui_widget)
        self.admin_bill_ser_input.setObjectName("admin_bill_ser_input")
        self.admin_bill_ser_input.setClearButtonEnabled(True)
        self.admin_bill_gui.addWidget(self.admin_bill_ser_input, 0, 2, 1, 2)
        self.admin_bill_gui.addWidget(self.admin_bill_ser_but, 0, 4, 1, 1)
        self.table_bill_model = QStandardItemModel(3, 5)
        self.table_bill_model.setHorizontalHeaderLabels(
            ['车牌号', '车辆类型', '停车时间', '取车时间', '时长/小时', '费用'])
        self.table_bill = QTableView(self.admin_bill_gui_widget)
        self.table_bill.setObjectName(u"table_bill")
        self.table_bill.setModel(self.table_bill_model)
        self.table_bill.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # self.table_bill.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_bill.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_bill.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_bill.setEditTriggers(QTableView.NoEditTriggers)
        self.admin_bill_gui.addWidget(self.table_bill, 2, 0, 1, 6)

        self.admin_set_gui_widget = QWidget(MainWindow)
        self.admin_set_gui_widget.setObjectName('admin_set_gui_widget')
        self.admin_set_gui_widget.setGeometry(QRect(40, 90, 601, 420))
        self.admin_set_gui = QGridLayout(self.admin_set_gui_widget)
        self.admin_set_gui.setObjectName('admin_set_gui')
        self.admin_set_gui.setContentsMargins(0, 0, 0, 0)
        self.admin_set_car_type = QComboBox(self.admin_set_gui_widget)
        self.admin_set_car_type.setObjectName('f')
        self.admin_set_car_type.addItem("")
        self.admin_set_car_type.addItem("")
        # self.admin_set_car_type.currentIndexChanged.connect()
        self.admin_label = QLabel(self.admin_set_gui_widget)
        self.admin_label.setText('停车价格设置')
        self.admin_set_gui.addWidget(self.admin_label, 0, 0, 1, 1)
        self.admin_set_gui.addWidget(self.admin_set_car_type, 0, 1, 1, 1)
        self.admin_set_price_in = QLineEdit(self.admin_set_gui_widget)
        self.admin_set_gui.addWidget(self.admin_set_price_in, 0, 2, 1, 1)
        self.text = QLabel(self.admin_set_gui_widget)
        self.text.setText('元/小时')
        self.admin_set_gui.addWidget(self.text, 0, 3, 1, 1)
        self.admin_set_price_update_but = QPushButton(self.admin_set_gui_widget)
        self.admin_set_gui.addWidget(self.admin_set_price_update_but, 0, 4, 1, 1)
        self.admin_set_free_text = QLabel(self.admin_set_gui_widget)
        self.admin_set_free_text.setText('免费停车时间设置')
        self.admin_set_gui.addWidget(self.admin_set_free_text, 1, 0, 1, 1)
        self.admin_set_free_time_in = QLineEdit(self.admin_set_gui_widget)
        self.admin_set_gui.addWidget(self.admin_set_free_time_in, 1, 1, 1, 1)
        self.admin_set_time_update_but = QPushButton(self.admin_set_gui_widget)
        self.admin_set_gui.addWidget(self.admin_set_time_update_but, 1, 3, 1, 1)

        self.text3 = QLabel(self.admin_set_gui_widget)
        self.text3.setText('分钟')
        self.admin_set_gui.addWidget(self.text3, 1, 2, 1, 1)

        # self.admin_set_size_text = QLabel(self.admin_set_gui_widget)
        # self.admin_set_size_text.setText('车位容量设置')
        # self.admin_set_gui.addWidget(self.admin_set_size_text, 2, 0, 1, 1)
        # self.admin_set_size_type = QComboBox(self.admin_set_gui_widget)
        # self.admin_set_size_type.setObjectName('f')
        # self.admin_set_size_type.addItem("两轮车")
        # self.admin_set_size_type.addItem("四轮车")
        # self.admin_set_gui.addWidget(self.admin_set_size_type, 2, 1, 1, 1)

        # self.text2 = QLabel(self.admin_set_gui_widget)
        # self.text2.setText('位')
        # self.admin_set_gui.addWidget(self.text2, 2, 3, 1, 1)
        self.user_text = QLabel(self.ui1)
        self.park_space_gui.addWidget(self.user_text, 0, 1, 1, 1)
        self.user_ser_but = QPushButton(self.ui1)
        self.user_ser_in = QLineEdit(self.ui1)
        self.park_space_gui.addWidget(self.user_ser_but, 0, 3, 1, 1)
        self.park_space_gui.addWidget(self.user_ser_in, 0, 1, 1, 1)
        self.user_ser_select = QComboBox(self.ui1)
        self.user_ser_select.addItem('车牌号')
        self.user_ser_select.addItem('车位号')
        self.park_space_gui.addWidget(self.user_ser_select, 0, 2, 1, 1)
        self.user_ser_but.setText(QCoreApplication.translate("Main_ui", u"车牌号搜索", None))

        #
        #
        #
        self.user_myself = QWidget(MainWindow)
        self.user_myself.setObjectName(u"user_myself")
        self.user_myself.setGeometry(QRect(100, 100, 500, 400))
        self.user_myself_layout = QGridLayout(self.user_myself)
        self.user_myself_layout.setObjectName(u"user_myself_layout")
        self.user_myself_layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.user_myself)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.user_myself_layout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.user_myself)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.user_myself_layout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self.user_myself)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.user_myself_layout.addWidget(self.label_3, 4, 0, 1, 1)

        self.user_name_in = QLineEdit(self.user_myself)
        self.user_name_in.setObjectName(u"user_name_in")

        self.user_myself_layout.addWidget(self.user_name_in, 2, 1, 1, 1)

        self.user_password_in = QLineEdit(self.user_myself)
        self.user_password_in.setObjectName(u"user_password_in")
        self.user_myself_layout.addWidget(self.user_password_in, 3, 1, 1, 1)

        self.user_repassword_in = QLineEdit(self.user_myself)
        self.user_repassword_in.setObjectName(u"user_repassword_in")
        self.user_myself_layout.addWidget(self.user_repassword_in, 4, 1, 1, 1)

        self.user_update_but = QPushButton(self.user_myself)
        self.user_update_but.setObjectName('user_but')
        self.user_myself_layout.addWidget(self.user_update_but, 5, 0, 1, 2)

        self.user_photo = QGraphicsView(self.user_myself)
        self.sense = QGraphicsScene()
        self.sense.addPixmap(self.pic)
        self.user_photo.setScene(self.sense)
        self.user_photo.fitInView(0, 0, 250, 150)
        self.user_photo.hide()
        # self.user_myself_layout.addWidget(self.user_photo, 0, 0, 1, 2)

        #
        # end user self
        #

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.ui1.hide()
        self.park_space_gui_widget.hide()
        self.user_myself.hide()
        self.admin_users_gui_widget.hide()
        self.admin_park_gui_widget.hide()
        self.admin_bill_gui_widget.hide()
        self.admin_set_gui_widget.hide()

        self.bar = QtWidgets.QMenuBar(MainWindow)
        self.bar.setGeometry(QRect(0, 0, 60, 30))
        self.file = self.bar.addMenu('菜单')
        #self.file.addAction('个人信息管理')
        self.file.addAction('退出登录')

        self.setWindowOpacity(0.93)

        self.ui_1_but.clicked.connect(self.click_ui1)
        self.ui_2_but.clicked.connect(self.click_ui2)
        self.ui_4_but.clicked.connect(self.click_ui4)
        self.ui_3_but.clicked.connect(self.click_ui3)
        self.ui_5_but.clicked.connect(self.click_ui5)
        self.ui_6_but.clicked.connect(self.click_ui6)
        self.ui_7_but.clicked.connect(self.click_ui7)

    # setupUi

    def retranslateUi(self, Main_ui):
        Main_ui.setWindowTitle(QCoreApplication.translate("Main_ui", u"主页面", None))

        self.ui_1_but.setText(QCoreApplication.translate("Main_ui", u"公告栏", None))
        self.ui_2_but.setText(QCoreApplication.translate("Main_ui", u"车位信息", None))
        self.ui_3_but.setText(QCoreApplication.translate("Main_ui", u"个人信息", None))
        self.ui_4_but.setText(QCoreApplication.translate("Main_ui", u"用户管理", None))
        self.ui_5_but.setText(QCoreApplication.translate("Main_ui", u"停车信息", None))
        self.ui_6_but.setText(QCoreApplication.translate("Main_ui", u"账单", None))
        self.ui_7_but.setText(QCoreApplication.translate("Main_ui", u"系统设置", None))
        self.admin_users_ser_but.setText(QCoreApplication.translate("Main_ui", u"查找", None))
        self.admin_park_ser_but.setText(QCoreApplication.translate("Main_ui", u"查找", None))
        self.admin_bill_ser_but.setText(QCoreApplication.translate("Main_ui", u"查找", None))
        self.edit_user_but.setText(QCoreApplication.translate("Main_ui", u"修改信息", None))
        self.del_user_but.setText(QCoreApplication.translate("Main_ui", u"删除用户", None))

        self.admin_set_price_update_but.setText(QCoreApplication.translate("Main_ui", u"更新价格", None))
        self.admin_set_time_update_but.setText(QCoreApplication.translate("Main_ui", u"更新时间", None))
        #self.admin_set_car_type.setItemText(0, QCoreApplication.translate("MainWindow", u"两轮车", None))
        #self.admin_set_car_type.setItemText(1, QCoreApplication.translate("MainWindow", u"四轮车", None))

        # self.admin_card_in.setPlaceholderText(
        #     QCoreApplication.translate("MainWindow", u"车牌", None)
        # )
        # self.admin_locate_in.setPlaceholderText(
        #     QCoreApplication.translate("MainWindow", u"车位号", None)
        # )

        #
        self.user_password_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"未修改", None)
        )
        self.user_repassword_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"未修改", None)
        )
        self.user_ser_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"车牌号", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"确认\u5bc6\u7801", None))
        self.user_update_but.setText(QCoreApplication.translate("MainWindow", u"更新信息", None))
        self.admin_set_car_type.setItemText(0, QCoreApplication.translate("MainWindow", u"两轮车", None))
        self.admin_set_car_type.setItemText(1, QCoreApplication.translate("MainWindow", u"四轮车", None))


        # retranslateUi

    def click_ui1(self):
        self.setPalette(self.palette)

        self.ui1.show()
        self.user_myself.hide()
        self.park_space_gui_widget.hide()
        self.admin_users_gui_widget.hide()
        self.admin_park_gui_widget.hide()
        self.admin_bill_gui_widget.hide()
        self.admin_set_gui_widget.hide()

    def click_ui2(self):
        self.setPalette(self.palette)
        self.park_space_gui_widget.show()
        self.ui1.hide()
        self.user_myself.hide()
        self.admin_users_gui_widget.hide()
        self.admin_park_gui_widget.hide()
        self.admin_bill_gui_widget.hide()
        self.admin_set_gui_widget.hide()


    def click_ui3(self):
        self.setPalette(self.palette)
        self.user_myself.show()
        self.admin_users_gui_widget.hide()
        self.ui1.hide()
        self.admin_park_gui_widget.hide()
        self.admin_bill_gui_widget.hide()
        self.admin_set_gui_widget.hide()
        self.park_space_gui_widget.hide()

    def click_ui4(self):
        self.setPalette(self.palette)
        self.admin_users_gui_widget.show()
        self.ui1.hide()
        self.user_myself.hide()
        self.admin_park_gui_widget.hide()
        self.admin_bill_gui_widget.hide()
        self.admin_set_gui_widget.hide()
        self.park_space_gui_widget.hide()

    def click_ui5(self):
        self.ui1.hide()
        self.user_myself.hide()
        self.admin_park_gui_widget.show()
        self.admin_users_gui_widget.hide()
        self.admin_bill_gui_widget.hide()
        self.admin_set_gui_widget.hide()
        self.park_space_gui_widget.hide()
        self.setPalette(self.palette2)

        pass

    def click_ui6(self):
        self.setPalette(self.palette)
        self.ui1.hide()
        self.user_myself.hide()
        self.admin_park_gui_widget.hide()
        self.admin_users_gui_widget.hide()
        self.admin_bill_gui_widget.show()
        self.admin_set_gui_widget.hide()
        self.park_space_gui_widget.hide()
        pass

    def click_ui7(self):
        self.setPalette(self.palette)
        self.ui1.hide()
        self.user_myself.hide()
        self.admin_park_gui_widget.hide()
        self.admin_users_gui_widget.hide()
        self.admin_bill_gui_widget.hide()
        self.admin_set_gui_widget.show()
        self.park_space_gui_widget.hide()
        pass
