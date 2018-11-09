#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QMessageBox, QToolTip, QDesktopWidget,
                             QMainWindow)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 默认窗口提示框
        QToolTip.setFont(QFont('SanaSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 按钮，提示框
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # 退出按钮
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)

        # # 设置窗口位置，标题以及图标
        # self.setGeometry(300, 300, 300, 220)
        # self.setWindowTitle('note')
        # self.setWindowIcon(QIcon('web.jpg'))
        #
        # self.show()

        # 设置窗口居中，调用自定义的center()方法
        self.resize(250, 130)
        self.center()

        self.setWindowTitle('Center')
        self.setWindowIcon(QIcon('web.jpg'))
        self.show()

    # 关闭窗口时弹出提示框
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 窗口居中
    def center(self):
        """
        QtGui.QDesktopWidget 提供了用户的桌面信息，包括屏幕大小
        """
        qr = self.frameGeometry()   #获得主窗口大小
        cp = QDesktopWidget().availableGeometry().center() #获取显示器的分辨率，然后得到中间点位置
        qr.moveCenter(cp)     #把自己窗口的中心点放置到qr的中心点
        self.move(qr.topLeft())  #然后把窗口的左上角的坐标设置为qr 的矩形左上角的坐标，这样窗口就居中了


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
