from typing import Tuple

class Element2D():
  def __init__(self) -> None:
    pass

class Point(Element2D):
  def __init__(self, point: Tuple):
    super().__init__()
    self.point = point
  def getPoint(self):
    return self.point

class Line(Point):
  def __init__(self, p1: Tuple, p2: Tuple):
    #super().__init__()
    self.line = [Point(p1), Point(p2)]
  def getLine(self):
    return [self.line[0].getPoint(), self.line[1].getPoint()]


class Polygon(Line):
  def __init__(self, *points):
    #super().__init__()
    self.polygon = []
    for cur, nxt in zip(points, points[1:]):
      self.polygon.append(Line(cur, nxt))
  def getPolygon(self):
    def bla(line):
      return (line.getLine())
    xxx = map(bla, self.polygon)
    return list(xxx)

