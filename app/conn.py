import datetime
import math
import re

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui import edit_space_ui, main_ui, login_ui, register_ui, main_edit_user_ui
from utils import logic


class Con(QMainWindow):

    def __init__(self):
        super(Con, self).__init__()

        self.res = None
        self.admin = None
        self.phone = None
        # 初始化一些界面对象
        self.edit_space = edit_space_ui.edit_space_ui()
        self.edit_user = main_edit_user_ui.edit_user_ui()
        self.logic = logic.logic()
        self.login_ui = login_ui.login_ui()
        self.register_ui = register_ui.register_ui()
        self.main_ui = main_ui.main_ui()
        # 隐藏edit_user和edit_space界面
        self.edit_user.hide()
        self.edit_space.hide()

        # 将各种按钮和事件关联起来
        self.main_ui.edit_user_but.clicked.connect(self.show_edit_user)
        self.login_ui.login_but.clicked.connect(self.login_ui.login_click)
        self.login_ui.signal.connect(self.login_init)
        self.login_ui.register_but.clicked.connect(self.show_reg)
        # self.signal1.connect(self.show_main)
        self.register_ui.pushButton_2.clicked.connect(self.close_reg)
        self.register_ui.signal.connect(self.register_init)
        self.main_ui.file.triggered.connect(lambda: self.return_main())
        # self.main_ui.ui_2_but.clicked.connect(lambda: logic.show_err(title='别点了', word='还没想好呢'))
        self.main_ui.admin_users_ser_but.clicked.connect(lambda: self.search_user(
            self.main_ui.ser_input.text()
        ))
        self.edit_user.buttonBox.accepted.connect(self.update_commit)
        self.main_ui.ui_4_but.clicked.connect(lambda: self.search_user())

        self.main_ui.warn.accepted.connect(lambda: self.main_ui_del_user(
            phone=self.main_ui.table_user_model.item(
                self.main_ui.table_user.selectedIndexes()[0].row(),
                self.main_ui.table_user.selectedIndexes()[0].column()).text()
        ))
        self.main_ui.warn.accepted.connect(lambda: self.search_user())
        self.main_ui.del_user_but.clicked.connect(lambda: self.main_del_warn())
        self.edit_space.edit_in_car.clicked.connect(self.edit_add_car)
        self.main_ui.admin_park_ser_but.clicked.connect(lambda: self.main_ser_car())
        # self.main_ui.park_out_but.clicked.connect(self.main_out_car)
        # self.main_ui.park_in_but.clicked.connect(lambda: self.main_ser_car())
        self.main_ui.ui_5_but.clicked.connect(lambda: self.main_ser_car())
        self.main_ui.admin_bill_ser_but.clicked.connect(lambda: self.main_ser_bill())
        self.main_ui.ui_6_but.clicked.connect(lambda: self.main_ser_bill())
        self.main_ui.ui_7_but.clicked.connect(lambda: self.main_free_time_take())
        self.main_ui.admin_set_car_type.currentIndexChanged.connect(lambda: self.main_car_price_take())
        self.main_ui.admin_set_time_update_but.clicked.connect(lambda: self.main_free_time_update())
        self.main_ui.admin_set_price_update_but.clicked.connect(lambda: self.main_car_price_update())
        self.main_ui.table_user.doubleClicked.connect(lambda: self.show_edit_user())
        self.main_ui.ui_3_but.clicked.connect(lambda: self.main_myself_click())
        self.main_ui.user_update_but.clicked.connect(lambda: self.logic.update_user(
            phone=self.phone,
            username=self.main_ui.user_name_in.text(),
            password=self.main_ui.user_password_in.text(),
            re_password=self.main_ui.user_repassword_in.text(),
        ))
        self.main_ui.ui_7_but.clicked.connect(self.main_car_price_take)
        self.main_ui.ui_1_but.clicked.connect(self.main_show_ui1_topic)
        self.main_ui.user_ser_but.clicked.connect(self.main_car_locate_ser)
        self.main_ui.user_ser_select.currentIndexChanged.connect(self.refush_user_sel)
        self.main_ui.ui_2_but.clicked.connect(self.park_space_take)
        self.edit_space.edit_out_car.clicked.connect(self.edit_out_car)
        self.edit_space.edit_in_car.clicked.connect(self.park_space_take)
        self.edit_space.edit_out_car.clicked.connect(self.park_space_take)

    # 返回到主界面的函数
    def return_main(self):
        # 清除登录界面的密码输入框
        self.login_ui.password_in.clear()
        # 关闭主界面并显示登录界面
        if self.admin:
            self.main_ui.table_park_space.doubleClicked.disconnect(self.space_init)
        self.main_ui.close()
        self.login_ui.show()

        # 显示登录界面的函数

    def show_login(self):
        self.login_ui.show()

        # 显示注册界面的函数

    def show_reg(self):
        # 清除注册界面的所有输入框
        self.register_ui.password_in.setText('')
        self.register_ui.repassword_in.setText('')
        self.register_ui.phone_in.setText('')
        self.register_ui.name_in.setText('')
        # 显示注册界面
        self.register_ui.show()

        # 显示主界面的函数

    def show_main(self):
        # 关闭登录界面并显示主界面
        self.login_ui.close()
        if self.admin:
            self.search_user()
        self.main_ui.show()

    # 关闭注册界面的函数
    def close_reg(self):
        self.register_ui.close()

    def show_edit_user(self):
        # 显示编辑用户界面的函数
        sel = self.main_ui.table_user.selectedIndexes()
        temp = {'是': 0, '否': 1}
        if not sel:
            logic.show_warn(word='必须选择一行')
            return
        self.edit_user.phone.setText(
            self.main_ui.table_user_model.item(sel[0].row(), sel[0].column()).text()
        )
        self.edit_user.name_in.setText(
            self.main_ui.table_user_model.item(sel[1].row(), sel[1].column()).text()
        )
        self.edit_user.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                u"修改%s信息" % self.main_ui.table_user_model.item(
                    sel[0].row(),
                    sel[0].column()).text(),
                None
            )
        )
        self.edit_user.is_banned.setCurrentIndex(
            temp[self.main_ui.table_user_model.item(sel[2].row(), sel[2].column()).text()])
        self.edit_user.is_admin.setCurrentIndex(
            temp[self.main_ui.table_user_model.item(sel[3].row(), sel[3].column()).text()])
        self.edit_user.show()

    # 登录初始化的函数
    def login_init(self, phone: str, password: str):
        # 验证用户名和密码，以及账户状态等
        if phone == "" or password == "":
            logic.show_info(word="信息不足")
        else:
            temp = self.logic.check_login(phone, password)
            if temp[0] == 3:
                logic.show_err(word='您已被禁止登陆')
            elif temp[0] == 0:
                logic.show_info()
                self.phone = phone
                self.admin = temp[1]
                if not self.admin:
                    self.main_ui.ui_2_but.setText(QCoreApplication.translate("Main_ui", u"车位信息", None))
                    self.main_ui.ui_4_but.hide()
                    self.main_ui.ui_5_but.hide()
                    self.main_ui.ui_6_but.hide()
                    self.main_ui.ui_7_but.hide()
                    self.main_ui.admin_users_gui_widget.hide()
                    self.main_ui.admin_bill_gui_widget.hide()
                    self.main_ui.admin_park_gui_widget.hide()
                    self.main_ui.admin_set_gui_widget.hide()
                    # self.main_ui.table_park_space.doubleClicked.disconnect(self.space_init)
                else:
                    self.main_ui.table_park_space.doubleClicked.connect(self.space_init)
                    self.main_ui.ui_2_but.setText(QCoreApplication.translate("Main_ui", u"车位管理", None))
                    self.main_ui.ui_4_but.show()
                    self.main_ui.ui_5_but.show()
                    self.main_ui.ui_6_but.show()
                    self.main_ui.ui_7_but.show()
                    # self.main_ui.admin_users_gui_widget.show()
                self.main_ui.setWindowTitle('手机号:%s' % self.phone)
                self.show_main()
            elif temp[0] == 2:
                logic.show_err()

    def register_init(self, phone: str, username: str, password: str, re_password: str):
        # print(phone+"dsd")
        # 验证输入的有效性，如密码是否匹配，手机号是否有效
        if phone == "" or username == "" or password == "" or re_password == "":
            logic.show_info(word="信息不足")
            return
        if logic.logic().find_user(phone):
            logic.show_info(word="用户已注册")
            return
        if password != re_password:
            logic.show_info(word="密码不一致")
            return
        if not logic.check_phone(phone=phone):
            logic.show_info(word='手机非法,应为11位')
            return
        if not logic.check_name(name=username):
            logic.show_info(word='非法用户名,只能为数字字母')
            return
        if not logic.check_password(password=password):
            logic.show_info(word="密码要求至少8位且有数字和大小写字母")
            return
        self.logic.add_user(phone, username, password)
        logic.show_info(word="注册成功")
        self.register_ui.close()

    def search_user(self, text=''):
        # 清除主界面上用户表格的所有数据
        self.main_ui.table_user_model.clear()
        # 设置表格的列标题
        self.main_ui.table_user_model.setHorizontalHeaderLabels(['手机', '用户名', '禁止登录', '管理员'])

        # 从数据库中检索所有用户
        res = logic.db.users.find({})
        # 遍历检索到的所有用户
        for item in res:
            # 如果text不为空，并且text不在用户信息中，则跳过该用户
            if text != '' and text not in str(item):
                pass
            else:
                # 将符合条件的用户信息添加到表格中
                self.main_ui.table_user_model.appendRow(
                    [QStandardItem(item['phone']),
                     QStandardItem(item['username']),
                     QStandardItem('是' if 'banned' in item and item['banned'] else '否'),
                     QStandardItem('是' if 'admin' in item and item['admin'] else '否'),
                     ])

    def update_commit(self):
        # 创建一个字典，将'是'映射为True，'否'映射为False
        temp = {
            '是': True,
            '否': False
        }
        # 调用逻辑层的update_user方法，使用编辑界面中的信息更新用户
        self.logic.update_user(
            phone=self.main_ui.table_user_model.item(
                self.main_ui.table_user.selectedIndexes()[0].row(),
                self.main_ui.table_user.selectedIndexes()[0].column()).text(),
            username=self.edit_user.name_in.text(),
            password=self.edit_user.password_in.text(),
            re_password=self.edit_user.password_in.text(),
            admin=temp[self.edit_user.is_admin.currentText()],
            banned=temp[self.edit_user.is_banned.currentText()]
        )

        # 隐藏编辑用户界面
        self.edit_user.hide()
        # 刷新用户列表
        self.search_user()

    def main_ui_del_user(self, phone=''):
        # 调用逻辑层的del_user方法删除指定手机号的用户
        self.logic.del_user(phone=phone)
        # 显示删除成功的信息
        logic.show_info(word='删除成功')

    def edit_add_car(self):
        # 从编辑空间界面获取车牌号
        card = self.edit_space.card.text()
        # 从编辑空间界面获取时间
        time = self.edit_space.dateTimeEdit.dateTime().toUTC().toTime_t()
        # 检查车牌是否合法，如果不合法则显示警告信息并返回
        if not logic.check_card(card=card):
            logic.show_warn(word='车牌不合法')
            return
        # 检查车辆是否已在停车库，如果是则显示警告信息并返回
        if logic.db.parks.find_one({'card': card}):
            logic.show_warn(word='车辆已入库')
            return

        # 添加车辆到数据库，并更新车位状态
        self.logic.add_car(type=self.res['type'], card=card, time=time, locate=self.res['no'])
        self.logic.update_space(no=self.edit_space.space_no.text(), status='1')
        # 显示停车成功的信息
        logic.show_info(word='停车成功')
        # 隐藏编辑空间界面
        self.edit_space.hide()

    def edit_out_car(self):
        # 从数据库中删除车辆信息
        self.logic.out_car(card=self.res['card'])
        # 获取车位信息
        res = dict(logic.db.park_space.find_one({
            'no': self.edit_space.space_no.text()
        }))
        # 更新车位状态为可用
        res['status'] = '0'
        res.pop('_id')
        # 更新数据库中的车位信息
        logic.db.park_space.update_one(
            {
                'no': self.edit_space.space_no.text()
            }, {'$set': res}
        )
        # 显示取车完成的信息
        logic.show_info(word='取车完成')
        # 隐藏编辑空间界面
        self.edit_space.hide()

    def main_del_warn(self):
        # 检查用户是否已在表格中选择一行
        if self.main_ui.table_user.selectedIndexes():
            # 显示警告对话框
            self.main_ui.warn.show()
            # 执行警告对话框
            self.main_ui.warn.exec_()
        else:
            # 如果没有选择行，则显示警告信息
            logic.show_warn(word='必须选择一行')

    def main_ser_car(self, text=''):
        # 如果text为空，则从输入框获取查询文本
        if text == '':
            text = self.main_ui.admin_park_ser_input.text()
        # 清除停车表格的所有数据
        self.main_ui.table_park_model.clear()
        # 设置停车表格的列标题
        self.main_ui.table_park_model.setHorizontalHeaderLabels(['车辆类型', '车牌号', '车位', '停车时间'])
        # 设置表格的行高和列宽
        self.main_ui.table_park.verticalHeader().setDefaultSectionSize(50)
        self.main_ui.table_park.horizontalHeader().setDefaultSectionSize(120)
        # 从数据库中检索所有的停车记录
        res = logic.db.parks.find({})
        # 遍历停车记录
        for item in res:
            item = dict(item)
            item.pop('_id')
            # 如果查询文本不为空并且不在停车记录中，则跳过该记录
            if text != '' and text not in str(item.values()):
                pass
            else:
                # 将符合条件的停车记录添加到表格中
                self.main_ui.table_park_model.appendRow(
                    [
                        QStandardItem(item['type']),
                        QStandardItem(item['card']),
                        QStandardItem(item['locate']),
                        QStandardItem(str(datetime.datetime.fromtimestamp(item['time']))),
                    ]
                )

    def main_ser_bill(self, text=''):
        # 如果text为空，则从输入框获取查询文本
        if text == '':
            text = self.main_ui.admin_bill_ser_input.text()
        # 清除账单表格的所有数据
        self.main_ui.table_bill_model.clear()
        # 设置账单表格的列标题
        self.main_ui.table_bill_model.setHorizontalHeaderLabels(
            ['车牌号', '车辆类型', '停车时间', '取车时间', '车位', '停车时长', '费用'])
        # 设置表格的行高和列宽
        self.main_ui.table_bill.verticalHeader().setDefaultSectionSize(50)
        self.main_ui.table_bill.horizontalHeader().setDefaultSectionSize(120)
        # 从数据库中检索所有的账单记录
        res = logic.db.bill.find({})
        # 遍历账单记录
        for item in res:
            item = dict(item)
            item.pop('_id')
            # 如果查询文本不为空并且不在账单记录中，则跳过该记录
            if text != '' and text not in str(item.values()):
                pass
            else:
                # 计算停车时长
                time_tol = math.ceil((int(item['out_time']) - int(item['time'])) / 60)
                s = '%s分钟' % (time_tol % 60)
                time_tol //= 60
                s = ('%s小时' % (time_tol % 24)) + s
                time_tol //= 24
                s = ('%s天' % time_tol) + s
                # 将符合条件的账单记录添加到表格中
                self.main_ui.table_bill_model.appendRow(
                    [
                        QStandardItem(item['card']), QStandardItem(item['type']),
                        QStandardItem(str(datetime.datetime.fromtimestamp(item['time']))),
                        QStandardItem(str(datetime.datetime.fromtimestamp(item['out_time']))),
                        QStandardItem(item['locate']),
                        QStandardItem(s),
                        QStandardItem(str(item['cost'])),
                    ]
                )

    def main_free_time_take(self):
        # 从数据库中检索免费时间并将其设置在输入框中
        self.main_ui.admin_set_free_time_in.setText(
            str(logic.db.sys.find_one({
                'type': 'free_time'
            })['time'])
        )

    def main_free_time_update(self):
        # 检索当前免费时间值
        res = logic.db.sys.find_one({
            'type': 'free_time'
        })
        # 获取输入框中的值
        res['time'] = self.main_ui.admin_set_free_time_in.text()
        # 检查输入是否有效（仅包含数字）
        if re.search('[^0-9]', res['time']):
            # 如果输入无效，则显示警告信息
            logic.show_warn(word='时间无效')
            return
        else:
            # 更新数据库中的免费时间
            logic.db.sys.update_one(
                {
                    'type': 'free_time'
                },
                {
                    '$set': res
                }
            )
            # 显示更新成功的信息
            logic.show_info(word='更新时间成功')
            # 重新获取免费时间值
            self.main_free_time_take()

    def main_myself_click(self):
        # 当用户点击时，检索用户名并将其显示在输入框中
        self.main_ui.user_name_in.setText(
            logic.db.users.find_one({
                'phone': self.phone
            })['username']
        )

    def main_car_price_take(self):
        # 检索选择的车型
        res = self.main_ui.admin_set_car_type.currentText()
        # 根据选择的车型检索价格
        res2 = str(logic.db.sys.find_one({
            'type': res
        })['price'])
        # 将价格显示在输入框中
        self.main_ui.admin_set_price_in.setText(
            res2
        )

    def main_car_price_update(self):
        # 根据当前选择的车型检索数据库中的记录
        res = logic.db.sys.find_one({
            'type': self.main_ui.admin_set_car_type.currentText()
        })
        # 更新价格字段的值
        res['price'] = self.main_ui.admin_set_price_in.text()
        # 检查价格是否有效（仅包含数字）
        if re.search('[^0-9]', res['price']):
            # 如果价格无效，则显示警告信息
            logic.show_warn(word='价格无效')
            return
        else:
            # 更新数据库中的价格记录
            logic.db.sys.update_one(
                {
                    'type': self.main_ui.admin_set_car_type.currentText()
                },
                {
                    '$set': res
                }
            )
            # 显示更新成功的信息
            logic.show_info(word='更新成功')
            # 重新获取车辆价格信息
            self.main_car_price_take()

    def main_show_ui1_topic(self):
        # 初始化主题列表
        topic_list = []
        # 获取两轮车和四轮车的当前停车数量和总车位数
        car2_now = len(list(logic.db.parks.find({'type': '两轮车'})))
        car4_now = len(list(logic.db.parks.find({'type': '四轮车'})))
        car2_size = len(list(logic.db.park_space.find({'type': '两轮车'})))
        car4_size = len(list(logic.db.park_space.find({'type': '四轮车'})))

        # 添加主题内容到列表中
        topic_list.append('两轮车还有%d个车位，四轮车还有%d个车位' % (car2_size - car2_now, car4_size - car4_now))
        topic_list.append('停车价格:四轮车%s元/小时,两轮车%s元/小时' % (
            logic.db.sys.find_one({'type': '四轮车'})['price'], logic.db.sys.find_one({'type': '两轮车'})['price']))
        topic_list.append('停车时间不足%s分钟不收费,超过按一小时计费' % (
            logic.db.sys.find_one({'type': 'free_time'})['time']))
        topic_list.append('不足一小时按一小时收费')

        # 构建HTML格式的文本
        text = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" " + \
               "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n " + \
               "<html><head><meta name=\"qrichtext\" content=\"1\" " + \
               "/><style type=\"text/css\">\n " + \
               "p, li { white-space: pre-wrap; }\n" + \
               "</style></head><body style=\" font-family:'SimSun'; " + \
               "font-size:9pt; font-weight:400; font-style:normal;\">\n " + \
               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;font-weight:600;\">\u516c\u544a\u680f</span></p>\n "

        num = 1
        # 将主题内容添加到HTML文本中
        for item in topic_list:
            text += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">%d.</span><span style=\" font-size:16pt; color:#aa55ff;\">%s</span></p>\n " % (
                num, item
            )
            num += 1

        text += "</body></html>"

        # 在主界面上显示HTML文本
        self.main_ui.topic_text.setHtml(QCoreApplication.translate("MainWindow", text, None))

    def main_car_locate_ser(self):
        # 获取选择的搜索类型和搜索文本
        type = self.main_ui.user_ser_select.currentText()
        mp = {
            '车牌号': 'card',
            '车位号': 'locate'
        }
        text = self.main_ui.user_ser_in.text()
        # 如果搜索类型为"车牌号"且搜索文本不合法，则显示警告信息
        if type == '车牌号' and not logic.check_card(text):
            logic.show_warn(word='车牌不合法')
            return
        # 根据搜索类型和文本在数据库中进行搜索
        res = logic.db.parks.find_one({
            mp[type]: text
        })

        if res is not None:
            # 如果找到匹配的记录，则显示相关信息
            logic.show_info(
                word=('车牌号%s,停车位%s\n停车时间%s' % (
                    res['card'], res['locate'], datetime.datetime.fromtimestamp(res['time'])))
            )
        else:
            if type == '车牌号':
                # 如果未找到匹配的车辆记录，则显示警告信息
                logic.show_warn(word='车辆未入库')
            else:
                # 如果搜索类型为"车位号"且未找到匹配的车位记录，则显示警告信息
                logic.show_warn(word='车位不存在或未停车')

    def refush_user_sel(self):
        # 更新搜索按钮的文本和输入框的占位符
        self.main_ui.user_ser_but.setText(
            QCoreApplication.translate("MainWindow", u"%s搜索" % (self.main_ui.user_ser_select.currentText()), None))
        self.main_ui.user_ser_in.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"输入%s" % (self.main_ui.user_ser_select.currentText()), None))

    def park_space_take(self):
        # 清空停车位表格模型
        self.main_ui.table_park_space_model.clear()
        # 从数据库中获取停车位信息
        res = list(logic.db.park_space.find({}))
        col = math.ceil(math.sqrt(len(res)))
        car4 = QIcon('./ui/img/car4.jpeg')
        car2 = QIcon('./ui/img/car2.jpeg')
        status = {
            '0': '空闲',
            '1': '停车',
            '2': '维护',
        }

        res_row = []
        for i in range(0, len(res)):
            temp = QStandardItem()
            temp.setToolTip('车位号:' + res[i]['no'] + '\n' + res[i]['tips'] + '\n' + status[res[i]['status']])
            temp.setText(res[i]['name'])
            temp.setIcon(
                car2 if res[i]['type'] == '两轮车' else car4
            )
            if res[i]['status'] == '1':
                temp.setBackground(QBrush(QColor("#FF1493")))
            if res[i]['status'] == '0':
                temp.setBackground(QBrush(QColor("#66CCFF")))
            if res[i]['status'] == '2':
                temp.setBackground(QBrush(QColor("#C0C0C0")))

            res_row.append(temp)
            if len(res_row) % col == 0:
                self.main_ui.table_park_space_model.appendRow(res_row)
                res_row.clear()
        if len(res_row) != 0:
            self.main_ui.table_park_space_model.appendRow(res_row)

    def space_init(self):
        status = {
            '0': '空闲',
            '1': '停车',
            '2': '维护',
        }
        # 获取选定的停车位名称
        text = self.main_ui.table_park_space_model.item(
            self.main_ui.table_park_space.selectedIndexes()[0].row(),
            self.main_ui.table_park_space.selectedIndexes()[0].column()).text()
        # 在数据库中查找选定停车位的详细信息
        self.res = logic.db.park_space.find_one({'name': text})

        self.edit_space.space_no.setText(
            self.res['no']
        )
        self.edit_space.space_info.setText(self.res['type'] + ',' + status[self.res['status']])
        if self.res['status'] == '1':
            # 如果停车位状态为"停车"
            self.res = logic.db.parks.find_one({
                'locate': self.res['no']
            })
            self.edit_space.dateTimeEdit.setDateTime(datetime.datetime.fromtimestamp(self.res['time']))
            self.edit_space.card.setText(self.res['card'])
            self.edit_space.card.setReadOnly(True)
            self.edit_space.dateTimeEdit.setReadOnly(True)

            self.edit_space.edit_in_car.hide()
            self.edit_space.edit_out_car.show()
            pass
        elif self.res['status'] == '0':
            # 如果停车位状态为"空闲"
            self.edit_space.dateTimeEdit.setDateTime(datetime.datetime.now())
            self.edit_space.card.setText('')
            self.edit_space.card.setReadOnly(False)
            self.edit_space.dateTimeEdit.setReadOnly(False)

            self.edit_space.edit_out_car.hide()
            self.edit_space.edit_in_car.show()
            pass
        elif self.res['status'] == '2':
            # 如果停车位状态为"维护"
            self.edit_space.edit_in_car.hide()
            self.edit_space.edit_out_car.hide()
            pass

        self.edit_space.show()
        pass

