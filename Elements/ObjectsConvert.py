
from typing import List, Union

from Elements.Geometry import Line, Point, Polygon


class ObjectsConvert:
  def convert(self, object: Union[List[Polygon], List[Line], List[Point]]):
    if isinstance(object, Polygon):
      self.convertPolygon(object)
    elif isinstance(object, Line):
      self.convertLine(object)
    elif isinstance(object, Point):
      self.convertPoint(object)
    else:
      raise TypeError("Invalid type of object")

  def convertPoint(self, point: Point):
    pass  # TODO

  def convertLine(self, line: Line):
    pass  # TODO
  
  def convertPolygon(self, polygon: Polygon):
    pass  # TODO
  
  