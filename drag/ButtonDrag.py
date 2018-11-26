#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
拖放按钮组件

本例中，展示怎么拖放一个button组件
窗口上有一个 QPushButton组件。左键点击按钮，控制台就会输出press.
右键可以点击然后拖放按钮。
"""
import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


# Button类继承 QPushButton类，然后重构 QPushButton的两个方法：mouseMoveEvent()
# 和mousePressEvent()。 mouseMoveEvent()是拖拽开始的事件。
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        # 我们只劫持按钮的右键事件，左键的操作还是默认行为
        if e.buttons() != Qt.RightButton:
            return

        mimeDate = QMimeData()

        # 创建一个 QDrag对象，用来传输MIME-based数据
        drag = QDrag(self)
        drag.setMimeData(mimeDate)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        # 注意在父级上也调用了 mousePressEvent()方法，
        # 不然的话，我们是看不到按钮按下的效果的。
        super().mousePressEvent(e)

        # 左键点击按钮，会在控制台输出“press”
        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        # 获得鼠标移动的位置，然后把按钮放在这个地方
        position = e.pos()
        self.button.move(position)

        # 指定放下的动作类型为moveAction
        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
