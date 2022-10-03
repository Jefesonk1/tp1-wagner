from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from elements.Geometry import Point, Line, Polygon


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
        width = self.geometry().width()
        height = self.geometry().height()
        qp.setRenderHint(QPainter.Antialiasing)
        padding = 10

        penColor = QColor('#0099d5')
        pen = QPen(penColor)
        pen.setWidth(1)
        qp.setPen(pen)
        qp.drawLine(padding,padding,padding,height-padding)
        qp.drawLine(padding,height-padding,width-padding,height-padding)
        qp.drawLine(width-padding,height-padding,width-padding,padding)
        qp.drawLine(width-padding,padding,padding,padding)

        pointColor = 224, 142, 69
        lineColor = 229, 83, 129
        polygonColor = 117, 139, 253
        paddingShift = QPointF(10,10)
        for point in self.points:
            penColor = QColor(*pointColor)
            pen = QPen(penColor)
            pen.setWidth(3)
            qp.setPen(pen)
            pointF = QPointF(*(point.getPoint())) + paddingShift
            self.drawCoordinatesText(qp, pointF - paddingShift)
            qp.drawPoint(pointF)

        for line in self.lines:
            penColor = QColor(*lineColor)
            pen = QPen(penColor)
            pen.setWidth(3)
            qp.setPen(pen)
            p1, p2 = line.getLine()
           # print(line.getLine())
            pointF1 = QPointF(*p1.getPoint()) + paddingShift
            pointF2 = QPointF(*p2.getPoint()) + paddingShift
            self.drawCoordinatesText(qp, pointF1 - paddingShift)
            self.drawCoordinatesText(qp, pointF2 - paddingShift)
            qp.drawLine(pointF1, pointF2)

        for polygon in self.polygons:
            penColor = QColor(*polygonColor)
            pen = QPen(penColor)
            pen.setWidth(3)
            qp.setPen(pen)
            currentPolygon = []
            points = polygon.getPolygon()
            for idx,point in enumerate(points):
                currentPolygon.append(QPointF(*point.getPoint()) + paddingShift)
                self.drawCoordinatesText(qp, currentPolygon[idx] - paddingShift)
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

    def drawCoordinatesText(self, painter, qtPoint):
        # if not self.isDrawCoordinatesEnabled: return
        x, y = qtPoint.x(), qtPoint.y()
        tooltipPoint = QPointF(x + 15, y + 20)
        self.drawText(painter, tooltipPoint, f'({x:.0f}, {y:.0f})')

    def drawText(self, painter, qtPoint, text):
        painter.setFont(QFont('Tahoma', 7))
        painter.drawText(qtPoint, text)
