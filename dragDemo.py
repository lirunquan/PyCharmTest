# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFrame, QLineEdit


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(500, 400)
        self.label = QLineEdit(self)
        self.label.setGeometry(0, 10, 450, 38)
        self.frame = QFrame(self)
        self.frame.setGeometry(120, 120, 100, 100)
        self.frame.setStyleSheet('background-color : #B9F9C5')
        print(self.frame.width())
        print(self.frame.height())
        print(self.frame.pos())
        self.setAcceptDrops(True)

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        self.setWindowTitle('mouse in')
        print(a0.mimeData().text())
        a0.accept()

    def dragMoveEvent(self, a0: QtGui.QDragMoveEvent) -> None:
        print(a0.pos())
        # pass

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        self.setWindowTitle('mouse drop')
        if self.frame.pos().x() <= a0.pos().x() <= self.frame.pos().x() + self.frame.width() \
                and self.frame.pos().y() <= a0.pos().y() <= self.frame.pos().y() + self.frame.height():
            self.label.setText(a0.mimeData().text().replace('file:///', ''))
        print(a0.mimeData().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
