#!/usr/bin/python


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Elements.Geometry import Point, Line, Polygon

class Draw(QWidget):
    newPoint = pyqtSignal(QPoint)
    def __init__(self, parent=None):
        super(Draw,self).__init__(parent)
        self.path = QPainterPath()
        self.initUI()

    def initUI(self):
        self.points: Point = []
        self.lines: Line = []
        self.polygons: Polygon = []
        #self.setGeometry(0, 0, 800, 600)
        #self.setWindowTitle('Colours')
        #self.widget = QLabel('Hello', self)
        #self.setMinimumSize(200, 100)
        #self.pintar = QWidget(self)
        #self.label = QLabel('testes',self)
        pass
        #self.show()
    def mouseMoveEvent(self, event):
       # self.path.moveTo(event.pos())
        #print(event.pos())
        self.newPoint.emit(event.pos())
        self.update()

    # def mouseMoveEvent(self, event):
    #     self.path.lineTo(event.pos())
    #     self.newPoint.emit(event.pos())
    #     self.update()

    def paintEvent(self, e):
        self.setMouseTracking(True)
        qp = QPainter()
        qp.begin(self)
        self.pal = self.palette()
        self.pal.setColor(QPalette.Background, Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)
        self.drawRectangles(qp)
        for point in self.points:
            qp.drawPoint(*(point.getPoint()))
        for line in self.lines:
            p1, p2 = line.getLine()
            qp.drawLine(*p1, *p2)
            print(*p1, *p2)
        for polygon in self.polygons:
            xxx = []
            lines = polygon.getPolygon()
            for line in lines:
                for point in line:
                    xxx.append(QPointF(*point))
            polyg = QPolygonF(xxx)
            qp.drawPolygon(polyg)
            #exit(0)
       # qp.drawPolygon(QPolygonF([QPointF(0, 0), QPointF(100, 0), QPointF(100, 100), QPointF(0, 100)]))
        self.qp = qp
        qp.end()

    def drawPoint(self, point: Point):
        # qp = self.qp
        # qp.setPen(Qt.red)
        # size = self.size()
        # print('foi')
        # qp.drawPoint(x, y)
        if point not in self.points:
            self.points.append(point)
            self.update()
    def drawLine(self, line: Line):
        # qp = self.qp
        # qp.setPen(Qt.red)
        # size = self.size()
        # print('foi')
        # qp.drawPoint(x, y)
        if line not in self.lines:
            self.lines.append(line)
            self.update()
    def drawPolygon(self, polygon: Polygon):
        # qp = self.qp
        # qp.setPen(Qt.red)
        # size = self.size()
        # print('foi')
        # qp.drawPoint(x, y)
        if polygon not in self.polygons:
            self.polygons.append(polygon)
            self.update()
    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#ff00ff')
        #qp.setPen(col)
        pen = QPen(col)
        pen.setWidth(8)
        qp.setPen(pen)

        # qp.setBrush(QColor(200, 0, 0))
        # qp.drawRect(0, 100, 300, 200)

        #qp.setBrush(QColor(200, 0, 0))
        #qp.drawRect(0, 100, 300, 200)

        # qp.setPen(QColor(255.80,0,255))
        # qp.drawLine(62,414,62,368)
        # qp.drawLine(62,368,124,368)
        # qp.drawLine(124,368,124,414)
        # qp.drawLine(124,414,62,414)

        # pen = QPen(QColor(255,80,0,255))
        # pen.setWidth(4)
        # qp.setPen(pen)
        # #qp.setBrush(234)
        # qp.drawPoint(0,368)
        # qp.drawPoint(124, 276)
        # qp.drawPoint(248, 184)


        # qp.setBrush(QColor(255, 80, 0, 160))
        # qp.drawRect(130, 15, 90, 60)

        # qp.setBrush(QColor(25, 0, 90, 200))
        # qp.drawRect(250, 15, 90, 60)


def main():
    app = QApplication(sys.argv)
    ex = Draw()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()