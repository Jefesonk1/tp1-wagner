from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 300)) 

        pybutton = QPushButton('button', self)
        pybutton.clicked.connect(self.draw_line)
        pybutton.resize(100,100)
        pybutton.move(0, 0) 

        pybutton2 = QPushButton('button2', self)
        pybutton2.clicked.connect(self.draw_line)
        pybutton2.resize(100,100)
        pybutton2.move(200, 0) 
        self.lines = []

    def draw_line(self):
        button = self.sender()
        r = button.geometry()
        p1 = QPoint(r.left() + r.width()/2, r.height())
        p2 = p1+QPoint(0, 100)
        line = QLine(p1, p2)
        if line not in self.lines:
            self.lines.append(line)
            self.update()

    def paintEvent(self,event):
        QMainWindow.paintEvent(self, event)
        painter = QPainter(self)
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        for line in self.lines:
            painter.drawLine(line)


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()