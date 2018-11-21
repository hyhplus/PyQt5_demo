#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction, qApp)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    """
    状态栏是由QMainWindow创建的
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        
        # 创建只有一个命令的菜单栏，这个命令就是终止应用
        # 同时也创建了一个状态栏
        # 而且还能使用快捷键退出
        exit_act = QAction(QIcon('images/exit.jpg'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        # 触发退出应用事件，即这个事件与QApplication的quit()行为相关联
        exit_act.triggered.connect(qApp.quit)

        self.statusBar().showMessage('Ready')

        # menuBar()创建菜单栏
        # addMenu()添加一个file菜单
        # 并关联了点击退出应用的事件
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('StatusBar & simple menu')
        self.setWindowIcon(QIcon('web.jpg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



