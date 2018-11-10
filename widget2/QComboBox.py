#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
QComboBox 组件能让用户在多个选项中选择一个 (即下拉框)

本例包含了一个QComboBox和一个QLabel。
下拉选择框有多个选项，都是Linux/windows的发行版名称，
标签内容为选定的发行版名称。

"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)


class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        self.lbl = QLabel('Win10', self)

        # 创建一个 QComboBox组件和五个选项
        combo = QComboBox(self)
        combo.addItem('Win10')
        combo.addItem('Mac OS X')
        combo.addItem('Ubuntu 18')
        combo.addItem('Arch')
        combo.addItem('Fedora')

        combo.move(50, 50)
        self.lbl.move(50, 150)

        # 在选中的条目上调用 onActivated()方法
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    # 在方法内部，设置标签内容为选定的字符串，然后设置自适应文本大小
    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())

