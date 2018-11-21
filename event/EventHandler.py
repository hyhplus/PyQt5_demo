#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
重构事件处理器
在PyQt5中，事件处理器经常被重写（也就是用自己写的 覆盖 库里面自带的）
这个例子，我们替换了事件处理器函数keyPressEvent()

"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):

        # 这里设置按下ESC键，程序就会退出
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

