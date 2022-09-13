from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Elements.Geometry import Point, Line, Polygon


class Draw(QWidget):
    newPoint = pyqtSignal(QPoint)

    def __init__(self, parent=None):
        super(Draw, self).__init__(parent)
        self.path = QPainterPath()
        self.initUI()

    def initUI(self):
        self.points: Point = []
        self.lines: Line = []
        self.polygons: Polygon = []

    def mouseMoveEvent(self, event):
        self.newPoint.emit(event.pos())
        self.update()

    def erase(self):
        self.points: Point = []
        self.lines: Line = []
        self.polygons: Polygon = []
        self.update()

    def paintEvent(self, e):
        self.setMouseTracking(True)
        qp = QPainter()
        qp.begin(self)
        self.pal = self.palette()
        self.pal.setColor(QPalette.Background, QColor('#3d3d3d'))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)
        penColor = QColor(255, 0, 255)
        pen = QPen(penColor)
        pen.setWidth(8)
        qp.setPen(pen)

        for point in self.points:
            pointF = QPointF(*(point.getPoint()))
            qp.drawPoint(pointF)

        for line in self.lines:
            p1, p2 = line.getLine()
            pointF1 = QPointF(*p1)
            pointF2 = QPointF(*p2)
            qp.drawLine(pointF1, pointF2)

        for polygon in self.polygons:
            currentPolygon = []
            points = polygon.getPolygon()
            for point in points:
                currentPolygon.append(QPointF(*point))
            qp.drawPolygon(QPolygonF(currentPolygon))

        self.qp = qp
        qp.end()

    def drawPoint(self, point: Point):
        self.points.append(point)
        self.update()

    def drawLine(self, line: Line):
        self.lines.append(line)
        self.update()

    def drawPolygon(self, polygon: Polygon):
        self.polygons.append(polygon)
        self.update()
