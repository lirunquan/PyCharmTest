# _*_coding:utf-8_*_
# Created by #Lirunquan, on 2019-09.
# Copyright (c) 2019 3KWan.
# Description :

import re
import sys

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QPushButton, QLabel

dictChannel = {
    "应用宝": "qq",
    "oppo": "oppo",
    "vivo": "vivo",
    "九游": "uc",
    "华为": "huawei",
    "小米": "mi",
    "360": "360",
    "4399": "4399",
    "三星": "samsung",
    "魅族": "meizu",
    "联想": "lenovo",
    "百度多酷": "baidu",
    "tt": "",
    "草花": ""
}


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox = QComboBox(self)
        self.button = QPushButton('Test', self)
        self.button.clicked.connect(self.do_get_channel)
        self.button.setStyleSheet("border-image:url();border: none")
        self.button.setCursor(Qt.PointingHandCursor)
        self.label = QLabel('', self)
        self.load_combo(dictChannel)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.comboBox)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def load_combo(self, data: dict):
        self.comboBox.clear()
        for k,v in data.items():
            self.comboBox.addItem("{0}[{1}]".format(k, v))
        self.comboBox.setCurrentIndex(-1)

    def do_get_channel(self):
        text = self.comboBox.currentText()
        if len(text):
            m = re.search(r'(?<=\[)\w+(?=\])', text)
            if len(m.group(0)):
                self.label.setText(m.group(0))
            else:
                raise ValueError("Empty str of channel.")
        else:
            self.label.setText('no selected channel')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
