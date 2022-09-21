from typing import Tuple


class Point():
    def __init__(self, point: Tuple):
        self.point = point

    def __str__(self):
       return 'Point = '+''.join(str(self.point))


    def getPoint(self):
        return self.point
    

class Line(Point):
    def __init__(self, point1: Point, point2: Point):
        self.line = [point1, point2]
    def __str__(self):
       return 'Line = '+''.join(str(e) for e in [self.line[0].getPoint(), self.line[1].getPoint()])
        #return [self.line[0].getPoint(), self.line[1].getPoint()]
    def getLine(self):
        return self.line


class Polygon(Line):
    def __init__(self, *points: Point):
        self.polygon = []
        for point in points:
            self.polygon.append(point)
    def __str__(self):
       return 'Polygon = ' + ''.join(str(e) for e in [x.getPoint()  for x in self.polygon])

       # return [x.getPoint()  for x in self.polygon]
    def getPolygon(self):
        return self.polygon

# p1 = Point((1,2))
# print(p1)
# l1 = Line(Point((1,2)), Point((3,4)))
# print(l1)
# pl1 = Polygon(p1,p1,p1,Point((2,4)))
# print(pl1)