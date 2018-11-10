#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
QPixmap 是处理图片的组件。本例中，我们使用 QPixmap 在窗口里显示一张图片。

"""

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()


    def initUI(self):
        hbox = QHBoxLayout(self)
        # 创建一个 QPixmap 对象，接收一个文件作为参数
        pixmap = QPixmap('../images/pixmap.jpg')

        # 把 QPixmap 实例放到 QLabel 组件里
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())


