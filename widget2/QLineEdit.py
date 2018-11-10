#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
QLineEdit 组件提供了编辑文本的功能，自带了撤销、重做、剪切、粘贴、拖拽等功能

这里展示了一个编辑组件和一个标签，我们在输入框里键入的文本，
会立即在标签里显示出来
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)   #创建一个 QLineEdit对象

        qle.move(60, 100)
        self.lbl.move(60, 40)

        # 如果输入框的值有变化，就调用 onChanged()方法
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # 在 onChanged()方法内部，我们把文本框里的值赋给了标签组件，
    # 然后调用 adjustSize()方法让标签自适应文本内容
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())



