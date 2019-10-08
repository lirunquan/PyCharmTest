from PyQt5.QtWidgets import QApplication, QWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(600, 300)
    w.setWindowTitle('SimpleTest')
    w.show()

    sys.exit(app.exec_())
