#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
信号发送

我们创建一个叫closeApp的信号，这个信号会在鼠标按下时触发，
事件与QMainWindow绑定
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    # Communicate类创建一个pyqtSignal()属性的信号
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        # closeApp信号与QMainWindow的close()方法绑定
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    # 点击窗口的时候，发送closeApp信号，程序终止
    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())