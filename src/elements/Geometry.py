from typing import Tuple


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

    def rotate(self,angle):
        return self.getPoint()

class Line(Element2d):
    def __init__(self, point1: Point, point2: Point):
        super().__init__()
        self.line = [point1, point2]

    def __str__(self):
       return 'Line = '+''.join(str(e) for e in [self.line[0].getPoint(), self.line[1].getPoint()])

    def getLine(self):
        return self.line

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

p1 = Point((1,2))
print(p1)
print(p1.translate(1,1))
print(p1.scale(2,2))
print(p1.rotate(1))
# l1 = Line(Point((1,2)), Point((3,4)))
# print(l1)
# pl1 = Polygon(p1,p1,p1,Point((2,4)))
# print(pl1)
# print(pl1.tx)