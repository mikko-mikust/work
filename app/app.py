import sys
from PyQt5.QtWidgets import *
import conn
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
if __name__ == '__main__':

    app = QApplication(sys.argv)
    con = conn.Con()
    con.show_login()
    sys.exit(app.exec_())
