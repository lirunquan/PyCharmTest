# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :

import sys
import urllib.request
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.crawl_start)
        self.label = QLabel('Ready', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.thread = CrawlThread()
        self.thread.status.connect(self.crawl_status)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def crawl_start(self):
        self.thread.start()

    def crawl_status(self, status):
        self.label.setText(status)


class CrawlThread(QThread):
    _status = pyqtSignal(str)

    def __init__(self):
        super(CrawlThread, self).__init__()

    def run(self) -> None:
        self._status.emit('Crawling')
        response = urllib.request.urlopen('https://www.python.org')
        self._status.emit('Saving')
        with open('python.txt', 'w') as f:
            f.write(response.read().decode('utf-8'))
        self._status.emit('Done')

    @property
    def status(self):
        return self._status


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
