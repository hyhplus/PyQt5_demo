#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
有时候我们会想知道是哪个组件发出了一个信号，
PyQt5里的 sender() 方法能搞定这件事
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建两个按钮
        # buttonClicked()方法决定了是哪个按钮调用sender()方法
        # 两个按钮都和同一个slot绑定
        btn1 = QPushButton('Button 1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        # 调用sender()方法的方式决定了事件源。状态栏显示了被点击的按钮
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

