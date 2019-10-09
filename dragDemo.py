# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFrame


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(500, 400)
        self.label = QLabel('', self)
        self.label.setGeometry(0, 100, 400, 38)
        self.frame = QFrame(self)
        self.frame.setGeometry(120, 120, 100, 100)
        self.frame.setStyleSheet('background-color : #B9F9C5')
        self.setAcceptDrops(True)

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        self.setWindowTitle('mouse in')
        print(a0.mimeData().text())
        a0.accept()

    def dragMoveEvent(self, a0: QtGui.QDragMoveEvent) -> None:
        print('mouse move')
        # pass

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        self.setWindowTitle('mouse drop')
        self.label.setText(a0.mimeData().text().replace('file:///', ''))
        print(a0.mimeData().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
