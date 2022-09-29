from statistics import mean
from typing import Tuple
from elements.Transformations import *

import numpy as np
def calculate(x, y, matrix):
	coord = matrix @ np.array([x, y, 1])
	return (coord[0], coord[1])
class Element2d:
    def __init__(self):
        self.tx = 0
        self.ty = 0
        self.sx = 1
        self.sy = 1
        self.rotationAngle = 0
    def translate(self, dx, dy):
        pass
    def scale(self, sx, sy):
        pass
    def rotate(self, angle):
        pass


class Point(Element2d):
    def __init__(self, point: Tuple):
        super().__init__()
        self.point = point

    def __str__(self):
       return 'Point = '+''.join(str(self.point))

    def getPoint(self):
        return self.point

    def translate(self, dx, dy):
        self.point = (self.point[0] + dx, self.point[1] + dy)
        return self.getPoint()

    def scale(self, sx, sy):
        self.point = (self.point[0] * sx, self.point[1] * sy)
        return self.getPoint()

    # def rotate(self,angle):
    #     return self.getPoint()

class Line(Element2d):
    def __init__(self, point1: Point, point2: Point):
        super().__init__()
        self.line = [point1, point2]

    def __str__(self):
       return 'Line = '+''.join(str(e) for e in [self.line[0].getPoint(), self.line[1].getPoint()])

    def getMeanPoint(self):
        x1,y1 = self.line[0].getPoint()
        x2,y2 = self.line[1].getPoint()
        xMean = (x1+x2)/2
        yMean = (y1+y2)/2
        return Point((xMean, yMean))

    def getLine(self):
        return self.line

    def translate(self, dx, dy):
        for point in self.getLine():
            point = (point.getPoint()[0] + dx, point.getPoint()[1] + dy)
        return self.getLine()

    def scale(self, sx, sy):
        meanPoint = self.getMeanPoint()
        x, y = meanPoint.getPoint()
        transformations = Transformations()
        moveToOrigin = transformations.translade(-x,-y)
        scale = transformations.scale(sx,sy)
        moveToOriginalPosition = transformations.translade(x,y)
        transformationMatrix = moveToOriginalPosition @ (scale @ moveToOrigin)
        npt = []
        for point in self.getLine():
            p = point.getPoint()
            point = calculate(*p, transformationMatrix)
            npt.append(point)
        return npt

    # def rotate(self,angle):
    #     return self.getLine()
class Polygon(Element2d):
    def __init__(self, *points: Point):
        super().__init__()
        self.polygon = []
        for point in points:
            self.polygon.append(point)

    def __str__(self):
       return 'Polygon = ' + ''.join(str(e) for e in [x.getPoint()  for x in self.polygon])

    def getPolygon(self):
        return self.polygon

    def translate(self, dx, dy):
        for point in self.getPolygon():
            point = point.translate(dx,dy)
        return self.getPolygon()

    def scale(self, sx, sy):
        for point in self.getPolygon():
            self.point = point.scale(sx,sy)
        return self.getPolygon()

    def rotate(self,angle):
        return self.getPolygon()

# p1 = Point((1,2))
# print(p1)
# print(p1.translate(1,1))
# print(p1.scale(2,2))
# print(p1.rotate(1))
l1 = Line(Point((2,2)), Point((5,5)))
print(l1)
# for x in l1.translate(3,4):
#     print(x)
print(l1.scale(3,3))

#print(l1.translate(1,2))
# pl1 = Polygon(p1,p1,p1,Point((2,4)))
# print(pl1)
# print(pl1.tx)
# pl1 = Polygon(Point((2,3)),Point((4,5)), Point((4,3)))

# print(pl1)
# #for x in pl1.translate(2,2): print(x)
# for x in pl1.scale(2,2): print(x)