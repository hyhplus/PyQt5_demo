#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
QPen 是基本的绘画对象，能用来画直线、曲线、矩形框、椭圆、多边形和其他形状。

这里我们用不同的笔画了6条直线。
PyQt5有五个预定义的笔，还可以我们自定义笔的样式。
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 270, 270)
        self.setWindowTitle('Pen Styles')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        # 新建一个QPen对象，设置颜色黑色，宽2像素，这样就能看出各个笔样式的区别。
        # Qt.SolidLine是预定义样式的一种。
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        """
        这里我们自定义了一个笔的样式。定义为Qt.CustomDashLine，
        然后调用 setDashPattern()方法。
        数字列表是线的样式，要求必须是个数为奇数，
        奇数位定义的是空格，偶数位为线长，
        数字越大，空格或线长越大，
        比如本例的就是1像素线，4像素空格，5像素线，4像素空格。
        """
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())