#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout,
                             QVBoxLayout, QApplication)

"""
盒子布局
"""
class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        # 这里创建了两个按钮
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 创建一个水平布局，增加两个按钮和弹性空间
        # stretch函数在两个按钮前面增加了一些弹性空间
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面
        # 弹性元素会把所有的元素一起都放置在应用的右下角
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
