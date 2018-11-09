#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
# 导入PyQt5基本模块，这个模块包含了基本的组件
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    # 创建一个PyQt5应用对象
    # sys.argv是一组命令行参数的列表
    app = QApplication(sys.argv)

    # QWidget控件是一个用户界面的基本控件，它提供基本的应用构造器
    # 构造器是没有父级的，也被称为窗口（window）
    # resize()方法改变控件的大小，这里宽250px,高150px
    # move()是控件位置的方法，它把控件放置到屏幕坐标的(300, 300)的位置，从左上角开始
    # setWindowTitle()设置标题
    # show()能让控件在桌面显示。控件在内存里创建，之后才能在显示器上显示出来
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    # 最后，进入应用的主循环中，事件处理器这个时候开始工作
    # 主循环从窗口接收事件，并把事件传入到派发到应用控件里

    # 当调用exit()方法或直接销毁主控件时，主循环就会结束
    # sys.exit()方法能确保主循环安全退出
    # 外部环境能通知主控件怎么结束
    sys.exit(app.exec_())
