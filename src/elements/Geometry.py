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
        self.point = tuple(point)

    def __str__(self):
       return 'Point = '+''.join(str(self.point))

    def getPoint(self):
        return self.point

    def translate(self, dx, dy):
        x,y = self.point
        return Point((x + dx, y + dy))

    def scale(self, sx, sy):
        x,y = self.point
        transformations = Transformations()
        moveToOrigin = transformations.translade(-x,-y)
        scale = transformations.scale(sx,sy)
        moveToOriginalPosition = transformations.translade(x,y)
        transformationMatrix = moveToOriginalPosition @ (scale @ moveToOrigin)
        point = calculate(x,y, transformationMatrix)
        return Point((point))

    def rotate(self,angle):
        x,y = self.point
        transformations = Transformations()
        moveToOrigin = transformations.translade(-x,-y)
        rotate = transformations.rotate(angle)
        moveToOriginalPosition = transformations.translade(x,y)
        transformationMatrix = moveToOriginalPosition @ (rotate @ moveToOrigin)
        point = calculate(x,y, transformationMatrix)
        return Point((point))

class Line(Element2d):
    def __init__(self, point1: Point, point2: Point):
        super().__init__()
        self.line = [point1, point2]

    def __str__(self):
       return 'Line = '+''.join(str(e) for e in [self.line[0].getPoint(), self.line[1].getPoint()])

    def getGeometricCenter(self):
        x1,y1 = self.line[0].getPoint()
        x2,y2 = self.line[1].getPoint()
        return Point(((x1+x2)/2, (y1+y2)/2))

    def getLine(self):
        return self.line

    def translate(self, dx, dy):
        points = []
        for point in self.getLine():
            x,y = point.getPoint()
            points.append(Point((x + dx, y + dy)))
        return Line(*points)

    def scale(self, sx, sy):
        geometricCenter = self.getGeometricCenter()
        x, y = geometricCenter.getPoint()
        transformations = Transformations()
        moveToOrigin = transformations.translade(-x,-y)
        scale = transformations.scale(sx,sy)
        moveToOriginalPosition = transformations.translade(x,y)
        transformationMatrix = moveToOriginalPosition @ (scale @ moveToOrigin)
        points = []
        for point in self.getLine():
            x,y = point.getPoint()
            newPoint = calculate(x,y, transformationMatrix)
            points.append(Point(newPoint))
        return Line(*points)

    def rotate(self,angle):
        angle = np.radians(angle)
        geometricCenter = self.getGeometricCenter()
        x, y = geometricCenter.getPoint()
        transformations = Transformations()
        moveToOrigin = transformations.translade(-x,-y)
        rotate = transformations.rotate(angle)
        moveToOriginalPosition = transformations.translade(x,y)
        transformationMatrix = moveToOriginalPosition @ (rotate @ moveToOrigin)
        points = []
        for point in self.getLine():
            x,y = point.getPoint()
            newPoint = calculate(x,y, transformationMatrix)
            points.append(Point(newPoint))
        return Line(*points)

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

    def getGeometricCenter(self):
        x = []; y = []
        for point in self.getPolygon():
            x1,y1 = point.getPoint()
            x.append(x1)
            y.append(y1)
        return Point((mean(x), mean(y)))

    def translate(self, dx, dy):
        points = []
        for point in self.getPolygon():
            x,y = point.getPoint()
            points.append(Point((x + dx, y + dy)))
        return Polygon(*points)

    def scale(self, sx, sy):
        geometricCenter = self.getGeometricCenter()
        x, y = geometricCenter.getPoint()
        transformations = Transformations()
        moveToOrigin = transformations.translade(-x,-y)
        scale = transformations.scale(sx,sy)
        moveToOriginalPosition = transformations.translade(x,y)
        transformationMatrix = moveToOriginalPosition @ (scale @ moveToOrigin)
        points = []
        for point in self.getPolygon():
            x,y = point.getPoint()
            newPoint = calculate(x,y, transformationMatrix)
            points.append(Point(newPoint))
        ##print(Polygon(*points))
        return Polygon(*points)


    def rotate(self,angle):
        angle = np.radians(angle)
        geometricCenter = self.getGeometricCenter()
        x, y = geometricCenter.getPoint()
        transformations = Transformations()
        moveToOrigin = transformations.translade(-x,-y)
        rotate = transformations.rotate(angle)
        moveToOriginalPosition = transformations.translade(x,y)
        transformationMatrix = moveToOriginalPosition @ (rotate @ moveToOrigin)
        points = []
        for point in self.getPolygon():
            x,y = point.getPoint()
            newPoint = calculate(x,y, transformationMatrix)
            points.append(Point(newPoint))
        return Polygon(*points)



# p1 = Point((1,2))
# #print('p1 -> ', p1)
# #print('p1 translate-> ',p1.translate(2,3))
# #print('p1 scale-> ',p1.scale(2,2))
# #print('p1 rotate-> ',p1.rotate(30))
# #print('p1 -> ', p1)

# l1 = Line(Point((2,2)), Point((5,5)))
# #print('l1 -> ', l1)
# #print('l1 translate-> ',l1.translate(2,3))
# #print('l1 scale-> ',l1.scale(3,3))
# #print('l1 rotate-> ',l1.rotate(30))
# #print('l1 -> ', l1)


# pl1 = Polygon(Point((2,3)),Point((4,5)), Point((4,3)))
# #print('pl1 -> ', pl1)
# #print('pl1 translate-> ',pl1.translate(2,2))
# #print('pl1 scale-> ',pl1.scale(3,3))
# #print('pl1 rotate-> ',pl1.rotate(30))
# #print('pl1 -> ', pl1)
