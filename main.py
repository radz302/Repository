import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.st = False

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.st:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            self.circle(qp)
            qp.end()

    def paint(self):
        self.st = True
        self.repaint()

    def circle(self, qp):
        a = random.randrange(50, 200)
        qp.drawEllipse(300, 100, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(250, 300, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(100, 40, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(50, 350, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(500, 300, a, a)
        self.st = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
