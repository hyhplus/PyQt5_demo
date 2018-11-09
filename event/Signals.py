#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
这个例子中，显示了QtGui.QLCDNumber和QtGui.QSlider模块，
我们能拖动滑块让数字跟着发生改变

sender 是信号的发送者
receiver 是信号的接收者
slot 是对这个信号应该做出的反应

"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        # 把滑块的变化和数字的变化绑定在一起
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
