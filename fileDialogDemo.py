# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :
import sys

from PyQt5.QtWidgets import QFileDialog, QWidget, QPushButton, QApplication, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Open', self)
        self.button.clicked.connect(self.open_file)
        self.label = QLabel('', self)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '.', '*.apk')
        self.label.setText(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
