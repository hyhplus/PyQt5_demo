#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
本例中，我们使用了QSlider和一个自定义组件，由进度条控制。
显示的有物体（也就是CD/DVD）的总容量和剩余容量。
进度条的范围是1~750。如果值达到了700（OVER_CAPACITY）,
就显示为红色，代表了烧毁了的意思。
烧录组件在窗口的底部，这个组件是用QHBoxLayout和QVBoxLayout组成的。

"""
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import sys

class Communticate(QObject):

    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):
        # 修改组件进度条的高度，默认的有点小
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]


    def setValue(self, value):

        self.value = value


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):

        MAX_CAPACITY = 700
        OVER_CAPACITY = 750

        # 使用比默认更小一点的字体，这样更匹配
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        # 动态的渲染组件，随着窗口的大小而变化，这就是我们计算窗口大小的原因。
        # 最后一个参数决定了组件的最大范围，进度条的值是由窗口大小按比例计算而来的。
        # 最大值的地方填充的是红色。注意这里使用的是浮点数，能提高计算和渲染的精度。
        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10))

        till = int(((w / OVER_CAPACITY) * self.value))
        full = int(((w / OVER_CAPACITY) * MAX_CAPACITY))

        if self.value >= MAX_CAPACITY:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20 ,20), 1, Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0

        for i in range(step, 10*step, step):
            qp.drawLine(i, 0, i, 5)
            # 这里使用字体去渲染文本。必须要知道文本的宽度，这样才能
            # 让文本的中间点正好落在竖线上。
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1



class Example(QWidget):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.initUI()


    def initUI(self):

        OVER_CAPACITY = 750

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, OVER_CAPACITY)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communticate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 210)
        self.setWindowTitle('Burning widget')
        self.show()


    # 拖动滑块的时候，调用了 changeValue()方法。这个方法内部，我们自定义了一个可以传参的
    # updateBW信号。参数就是滑块的当前位置。这个数值之后还用于Burning组件，
    # 然后重新渲染Burning组件。
    def changeValue(self, value):

        self.c.updateBW.emit(value)
        self.wid.repaint()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

