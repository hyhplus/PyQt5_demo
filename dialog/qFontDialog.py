#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
QFontDialog 能做字体的选择

这里我们创建了一个有一个按钮和一个标签的 QFontDialog 的对话框，
我们可以使用这个功能修改字体样式
"""

import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QSizePolicy,
                             QLabel, QFontDialog, QApplication)

class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        vBox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        btn.move(20, 20)

        vBox.addWidget(btn)
        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vBox.addWidget(self.lbl)
        self.setLayout(vBox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font Dialog')
        self.show()

    def showDialog(self):
        # 弹出一个字体选择对话框。getFont()方法返回一个字体名称和状态信息
        font, ok = QFontDialog.getFont()

        # 如果点击OK, 标签的字体就会随之更改
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
