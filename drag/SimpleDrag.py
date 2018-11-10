#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
本例使用了QLineEdit 和 QPushButton.
把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）。

"""
import sys
from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)

# 重构一些方法，首先用 QPushButton上构造一个按钮实例
class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        # 激活组件的拖拽事件
        self.setAcceptDrops(True)

    # 首先我们重构了 dragEnterEvent()方法。
    # 设定好接收拖拽的数据类型(plain text)
    def dragEnterEvent(self, e):
        if e.mimeDate().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # 重构 dropEvent()方法，更改按钮接受鼠标的释放事件的默认行为
    def dropEvent(self, e):
        self.setText(e.mimeDate().text())


class Example(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        # QLineEdit默认支持拖拽操作，所以我们只要调用 setDragEnabled()方法
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()