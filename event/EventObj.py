#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
事件对象

事件对象是用Python来描述一系列的事件自身属性的对象

这个示例中，我们在一个组件里显示鼠标的 X 和 Y 坐标
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        # X Y坐标显示在QLabel组件中
        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # 设置默认开启鼠标追踪，即鼠标经过显示坐标
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()


    def mouseMoveEvent(self, e):
        # e 代表事件对象，里面有触发事件（鼠标移动）的事件对象
        # x() 和y() 方法得到鼠标的x 和 y 坐标点，
        # 然后拼成字符串输出到 QLabel 组件里
        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

