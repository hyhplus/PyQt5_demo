#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
俄罗斯方块游戏开发

没有图片，所以就自己用绘画画出来几个图形。
每个游戏里都有数学模型的，这个也是。

开工之前：
    用 QtCore.QBasicTimer()创建一个游戏循环
    模型是一直下落的
    模型的运动是以小块为基础单位的，不是按像素
    从数学意义上来说，模型就是一串数字而已

代码由四个类组成: Tetris, Board, Tetrominoe和Shape.
    Tetris类创建游戏
    Board类是游戏的主要逻辑
    Tetrominoe类包含了所有的砖块
    Shape类是所有砖块的代码

"""

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys, random


class Tetris(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusBar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusBar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()


    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)



class Board(QFrame):

    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()


    def initBoard(self):

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()


    def shapeAt(self, x, y):

        return self.board[(y * Board.BoardWidth) + x]


    def setShapeAt(self, x, y, shape):

        self.board[(y * Board.BoardWidth) + x] = shape


    def squareWidth(self):

        return self.contentsRect().width() // Board.BoardWidth


    def squareHeight(self):

        return self.contentsRect().height() // Board.BoardHeight


    def start(self):

        if self.isPaused:
            return

        self.isPaused = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)


    def pause(self):

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit('paused')

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()


    def paintEvent(self, event):

        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter, rect.left()+j*self.squareWidth(),
                                    boardTop+i*self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):

                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x*self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())


        def keyPressEvent(self, event):

            if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
                super(Board, self).keyPressEvent(event)
                return

            key = event.key()

            pass




class Tetrominoe():
    pass