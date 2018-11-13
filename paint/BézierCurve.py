#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
贝塞尔曲线
使用PyQt5的 QPainterPath创建贝塞尔曲线。
绘画路径是由许多构建图形的对象，具体表现就是一些
线的形状，比如矩形，椭圆，线和曲线。
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bézier curve')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):
        # 用QPainterPath 路径创建贝塞尔曲线。使用 cubicTo()方法生成，
        # 分别需要三个点：起始点，控制点和终止点。
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        # drawPath()绘制最后的图像。
        qp.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

