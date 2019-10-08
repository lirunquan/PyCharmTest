# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
import sys


class HideWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(HideWindow, self).__init__(*args, **kwargs)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.resize(800, 600)
        self._width = QApplication.desktop().availableGeometry(self).width()
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton('Close Window', self))

    def mousePressEvent(self, event):
        super(HideWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self._pos = event.globalPos() - self.pos()
            self._canMove = not self.isMaximized() or not self.isFullScreen()

    def mouseMoveEvent(self, event):
        super(HideWindow, self).mouseMoveEvent(event)
        if event.buttons() == Qt.LeftButton and self._canMove:
            self.move(event.globalPos() - self._pos)

    def mouseReleaseEvent(self, event):
        super(HideWindow, self).mouseReleaseEvent(event)
        self._canMove = False
        pos = self.pos()
        x = pos.x()
        y = pos.y()
        print(self._pos)
        print(self.width())
        print(self._width)
        if x < 0:
            return self.move(1 - self.width(), y)
        if y < 0:
            return self.move(x, 1 - self.height())
        if x > self._width - self.width() / 2:
            return self.move(self._width - 1, y)

    def enterEvent(self, event):
        super(HideWindow, self).enterEvent(event)
        pos = self.pos()
        x = pos.x()
        y = pos.y()
        if x < 0:
            return self.move(0, y)
        if y < 0:
            return self.move(x, 0)
        if x > self._width - self.width() / 2:
            return self.move(self._width - self.width(), y)

    def leaveEvent(self, event):
        super(HideWindow, self).leaveEvent(event)
        pos = self.pos()
        x = pos.x()
        y = pos.y()
        if x == 0:
            return self.move(1 - self.width(), y)
        if y == 0:
            return self.move(x, 1 - self.height())
        if x == self._width - self.width():
            return self.move(self._width - 1, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HideWindow()
    w.show()
    sys.exit(app.exec_())
