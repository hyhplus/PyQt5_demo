#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
QSlider是个有一个小滑块的组件，这个小滑块能拖着前后滑动，
这个经常用于修改一些具有范围的数值，
比文本框或者点击增加减少的文本框（spin box）方便多了

本例用一个滑块和一个标签展示。标签为一个图片，滑块控制标签的值
这里是模拟的音量控制器。拖动滑块，能改变标签位置的图片
"""
import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个水平的 QSlider
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        # 把 valueChanged 信号跟 changeValue() 方法关联起来
        sld.valueChanged[int].connect(self.changeValue)

        # 创建一个 QLabel 组件并给它设置一个静音图标
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self, value):

        # 根据音量值的大小更换标签位置的图片
        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

