#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore


app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.resize(400, 400)
widget.setWindowTitle('Hello world')
widget.show()

sys.exit(app.exec_())
