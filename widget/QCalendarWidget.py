#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
QCalendarWidget 提供了基于月份的日历插件，十分简单而且直观

这个例子有日期组件和标签组件组成，标签显示被选中的日期
"""
import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QLabel,
                             QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate


class Example(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        vBox = QVBoxLayout(self)

        # 创建一个QCalendarWidget
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        # 选择一个日期，QDate 的点击信号就触发了，把这个信号和我们自己定义的
        # showDate()方法关联起来
        cal.clicked[QDate].connect(self.showDate)

        vBox.addWidget(cal)

        self.lbl = QLabel(self)
        # 使用 selectDate()方法获取选中的日期
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vBox.addWidget(self.lbl)

        self.setLayout(vBox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calender')
        self.show()


    def showDate(self, date):
        # 把日期对象转为字符串，在标签里面显示出来
        self.lbl.setText(date.toString())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())

