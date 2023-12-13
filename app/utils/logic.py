# 引入所需的库
import asyncio
import datetime
import hashlib
import math
import random
import re
from PyQt5.QtWidgets import QMessageBox
from utils.mongo import db

# 显示警告信息的函数，使用Qt的消息框
def show_warn(title='警告', word='用户不存在'):
    warn = QMessageBox(QMessageBox.Warning, title, word, QMessageBox.Ok)
    warn.show()
    warn.exec_()

# 显示提示信息的函数
def show_info(title='提示', word='登陆成功!'):
    info = QMessageBox(QMessageBox.Information, title, word, QMessageBox.Ok)
    info.show()
    info.exec_()

# 显示错误信息的函数
def show_err(title='错误', word='账号或密码错误'):
    err = QMessageBox(QMessageBox.Critical, title, word, QMessageBox.Ok)
    err.show()
    err.exec_()

# 检查密码是否符合条件的函数，条件包括：包含数字，大小写字母，并且长度大于7
def check_password(password: str) -> bool:
    return (re.search('[0-9]', password) and
            re.search('[a-z]', password) and
            re.search('[A-Z]', password)
            ) is not None and \
           len(password) > 7 and \
           not re.search('[^A-Za-z0-9]', password)

# 检查手机号是否符合条件的函数，条件是长度为11并且全都是数字
def check_phone(phone: str) -> bool:
    return len(phone) == 11 and \
           re.search('[^0-9]', phone) is None

# 检查用户名是否符合条件的函数，条件是只包含字母和数字
def check_name(name: str) -> bool:
    return re.search('[^A-Za-z0-9]', name) is None

# 检查车牌号是否符合条件的函数，条件是满足中国大陆车牌号的正则表达式
def check_card(card: str) -> bool:
    return \
        re.search(
            r'^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$'
            , card) is not None

# 这个函数向数据库插入了666个测试用户
async def test():
    temp = []
    for i in range(0, 666):
        temp.append(
            dict({'phone': '%d' % (int(19577034779) + int(i)),
                  'password': hashlib.md5('123456'.encode('UTF-8')).hexdigest(),
                  'username': 'user%d' % (int(19577034779) + int(i)), }
                 ))
        print(i)
    db.users.insert_many(temp)

# 这个类包含了一些逻辑方法，如检查登录，找到用户，添加用户，更新用户等。

class logic:
    # 初始化方法，当一个logic对象被创建时会自动调用
    def __init__(self):
        # 初始化res为None，这个变量稍后可能用来存储查询结果
        self.res = None

    # 检查登录的方法，它需要电话号码和密码作为参数，并返回一个列表
    def check_login(self, phone: str, password: str) -> list:
        # 初始化一个空的结果列表
        res = list()

        # 调用find_user方法来查找该电话号码的用户
        if not self.find_user(phone):
            # 如果用户不存在，则显示警告，并返回[1, False]
            show_warn()
            return [1, False]
        else:
            # 检查密码是否正确
            if hashlib.md5(password.encode('UTF-8')).hexdigest() == self.res['password']:
                # 如果用户被禁止，则将3添加到结果列表中
                if 'banned' in self.res and self.res['banned']:
                    res.append(3)
                else:
                    # 否则将0添加到结果列表中
                    res.append(0)
            else:
                # 密码错误，将2添加到结果列表中
                res.append(2)

            # 检查用户是否是管理员，并将结果添加到结果列表中
            if 'admin' in self.res:
                res.append(self.res['admin'])
            else:
                res.append(False)

        # 返回结果列表
        return res

    # 查找用户的方法，使用电话号码作为查询条件
    def find_user(self, phone: str) -> bool:
        # 在数据库中查找用户，并将结果存储在res变量中
        self.res = db.users.find_one({
            'phone': phone,
        })
        # 如果找到用户，返回True，否则返回False
        return self.res is not None

    # 添加新用户的方法，需要电话号码，用户名和密码作为参数
    def add_user(self, phone: str, username: str, password: str):
        # 密码使用MD5加密
        en_password = hashlib.md5(password.encode('UTF-8')).hexdigest()
        # 在数据库中插入新用户
        db.users.insert_one({
            'phone': phone,
            'username': username,
            'password': en_password
        })

    # 更新用户信息的方法
    def update_user(self, phone: str, username="", password="", re_password="", banned=None, admin=None):
        # 从数据库中查找用户
        self.res = db.users.find_one({
            'phone': phone,
        })
        if banned is not None:
            self.res['banned'] = banned
        if admin is not None:
            self.res['admin'] = admin
        if username != "":
            if not check_name(username):
                show_info(word='非法用户名')
            else:
                self.res['username'] = username
        if password != "" and re_password != "":
            if password != re_password:
                show_warn(word='两次密码不一致')
                return
            if not check_password(password=password):
                show_info(word="密码要求至少8位且有数字和大小写字母")
                return
            self.res['password'] = hashlib.md5(password.encode('UTF-8')).hexdigest()

        db.users.update_one(
            {'phone': phone, },
            {'$set': self.res}
        )
        show_info(word='修改成功')

    # 删除用户的方法，使用电话号码作为条件
    def del_user(self, phone=''):
        db.users.delete_one({
            'phone': phone
        })

    # 添加车辆的方法，需要车牌号，时间，类型和位置作为参数
    def add_car(self, card: str, time: int, type: str, locate: str):
        db.parks.insert_one({
            'card': card,
            'time': time,
            'type': type,
            'locate': locate
        })

    # 车辆出库的方法，需要车牌号作为参数
    def out_car(self, card: str):

        self.res = db.parks.find_one({
            'card': card
        })

        price = int(db.sys.find_one({
            'type': self.res['type']
        })['price'])

        self.res['out_time'] = math.ceil(datetime.datetime.timestamp(datetime.datetime.now()))
        time_tot = (self.res['out_time'] - int(self.res['time'])) / 60

        self.res['cost'] = \
            0 if \
                time_tot <= int(
                    db.sys.find_one({'type': 'free_time'})['time']
                ) \
                else round(math.ceil(time_tot / 60) * price, 2)

        db.parks.delete_one({
            'card': card
        })

        db.bill.insert_one(self.res)

    # 更新车位状态的方法，需要车位编号和状态作为参数
    def update_space(self, no: str, status: str):
        self.res = db.park_space.find_one({
            'no': no
        })
        self.res['status'] = status

        db.park_space.update_one(
            {'no': no, },
            {'$set': self.res}
        )


# 这个函数向数据库插入了1000个停车位的信息
async def test2():
    temp = []
    typex = ['四', '两']
    for i in range(0, 1000):
        temp.append(
            dict({'no': '%d' % (int(i)),
                  'name': '车位%d' % (int(i)),
                  'type': '%s轮车' % (typex[random.randint(0, 1)]),
                  'tips': '%d的位置提示' % (int(i)),
                  'status': '0', }
                 ))
        print(i)
    db.park_space.insert_many(temp)


if __name__ == '__main__':
    # logic().update_user(phone='852',banned=False)
    # print(check_password('09sfAdfsd'))
    # 创建一个异步事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    #asyncio.get_event_loop().run_until_complete(test())
    # for i in range(120):
    #     print(random.randint(0, 1))
    pass
