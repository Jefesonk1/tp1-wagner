#!/usr/bin/python


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        # qp.setBrush(QColor(200, 0, 0))
        # qp.drawRect(0, 100, 300, 200)

        #qp.setBrush(QColor(200, 0, 0))
        #qp.drawRect(0, 100, 300, 200)

        qp.setPen(QColor(255.80,0,255))
        qp.drawLine(62,414,62,368)
        qp.drawLine(62,368,124,368)
        qp.drawLine(124,368,124,414)
        qp.drawLine(124,414,62,414)

        pen = QPen(QColor(255.80,0,255))
        pen.setWidth(10)
        qp.setPen(pen)
        #qp.setBrush(234)
        qp.drawPoint(0,368)
        qp.drawPoint(124, 276)
        qp.drawPoint(248, 184)


        # qp.setBrush(QColor(255, 80, 0, 160))
        # qp.drawRect(130, 15, 90, 60)

        # qp.setBrush(QColor(25, 0, 90, 200))
        # qp.drawRect(250, 15, 90, 60)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()