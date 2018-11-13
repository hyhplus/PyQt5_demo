#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
点是最简单的绘画了

这里我们在窗口里随机的画出了10000个点
"""
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys, random

class Example(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 190)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        # 设置笔的颜色为绿色，使用的是Qt预定义的颜色
        qp.setPen(Qt.green)
        # 每次更改窗口大小，都会产生绘画事件，从size()方法里获取当前窗口的大小，
        # 然后把产生的点随机的分配到窗口的所有位置上。
        size = self.size()

        for i in range(10000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            # drawPoint()方法绘画。
            qp.drawPoint(x, y)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


