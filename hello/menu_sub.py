#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QMenu,
                             QAction, qApp)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    """
    状态栏是由QMainWindow创建的
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        # menuBar()创建菜单栏
        # addMenu()添加一个file菜单和一个view菜单
        menu_bar = self.menuBar()
        fileMenu = menu_bar.addMenu('&File')
        viewMenu = menu_bar.addMenu('&View')

        # 这里是嵌套的子菜单
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        # 一般菜单
        newAct = QAction('New', self)

        # 退出菜单,这里也绑定了工具栏
        exitAct = QAction(QIcon('../images/exit.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        # 这里将菜单栏添加到应用中
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

        # 下面设置view菜单栏(勾选菜单栏),行为菜单
        # 这个动作能切换状态栏显示或者隐藏
        viewStatAct = QAction('View statusBar', self, checkable=True)
        viewStatAct.setStatusTip('View statusBar')
        viewStatAct.setChecked(True)   # 设置默认为选中状态
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        # 工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Sub/Check-Menu & toolBar')
        self.setWindowIcon(QIcon('web.jpg'))
        self.show()

    # 状态为显示或者隐藏
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    # 鼠标右键可以弹出菜单
    def contextMenuEvent(self, event):
        cm = QMenu(self)

        # 使用exec_()方法显示菜单，从鼠标右键事件对象中获得当前坐标
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口的绝对坐标
        newAct = cm.addAction('添加')
        openAct = cm.addAction('打开')
        quitAct = cm.addAction('退出')
        action = cm.exec_(self.mapToGlobal(event.pos()))

        if action == newAct:
            pass
        if action == openAct:
            pass
        if action == quitAct:
            qApp.quit()     # 触发退出事件


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
