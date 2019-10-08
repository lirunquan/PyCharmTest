# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09-12.
# Copyright (c) 2019 3KWan.
# Description :

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
import sys
import win32con
from win32process import SuspendThread, ResumeThread
class Worker(QThread):
    valueChanged = pyqtSignal(int)

    def run(self) -> None:
        print('thread id', int(QThread.currentThreadId()))
        for i in range(1, 101):
            print('value:', i)
            self.valueChanged.emit(i)
            QThread.msleep(10)


class ThreadWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(ThreadWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0, 100)
        layout.addWidget(self.progressBar)
        self.buttonStart = QPushButton('Start Thread', self)
        self.buttonStart.clicked.connect(self.on_start_clicked)
        layout.addWidget(self.buttonStart)
        self._worker = Worker(self)
        self._worker.finished.connect(self._worker.deleteLater)
        self._worker.valueChanged.connect(self.progressBar.setValue)

    def on_start_clicked(self):
        print('main id:', int(QThread.currentThreadId()))
        self._worker.start()

    def closeEvent(self, event) -> None:
        if self._worker.isRunning():
            self._worker.quit()
        del self._worker
        super(ThreadWindow, self).closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ThreadWindow()
    w.show()
    sys.exit(app.exec_())
