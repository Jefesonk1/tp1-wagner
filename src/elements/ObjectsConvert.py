
from typing import List, Union
from elements.Geometry import *
import numpy as np


class ObjectsConvert:
    def convert(self, objectsList: Union[List[Polygon], List[Line], List[Point]], transformationMatrix: np.ndarray):
        self.transformationMatrix = transformationMatrix
        self.convertedObjectsList = []
        if transformationMatrix.shape != (3, 3):
            raise Exception('transformationMatrix must be shape = (3,3)')
        if isinstance(objectsList, list):
            # #print('list')
            for object in objectsList:
                if isinstance(object, Polygon):
                    # #print('polygon')
                    self.convertedObjectsList.append(
                        self.convertPolygon(object))
                elif isinstance(object, Line):
                    # #print('line')
                    self.convertedObjectsList.append(self.convertLine(object))

                elif isinstance(object, Point):
                    # #print('point')
                    self.convertedObjectsList.append(self.convertPoint(object))
                else:
                    raise TypeError("Invalid type of object")
        else:
            raise TypeError("Not a list")
        return self.convertedObjectsList

    def convertPoint(self, point: Point):
        p = (self.transformationMatrix @ [*(point.getPoint()), 1])[:-1]
       # #print(Point(p).getPoint())
        return Point(p)

    def convertLine(self, line: Line):
        newLine = []
        for point in line.getLine():
            newPoint = self.convertPoint(point)
            newLine.append(newPoint)
        return Line(*newLine)

    def convertPolygon(self, polygon: Polygon):
        newPolygon = []
        for point in polygon.getPolygon():
            newPoint = self.convertPoint(point)
            newPolygon.append(newPoint)
        return Polygon(*newPolygon)


# matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# oc = ObjectsConvert()
# p = Point((1, 2))
# l = Line(p, p)
# pl = Polygon(p, p, p)
# a = []
# a.append(p)
# a.append(l)
# a.append(pl)
# list = oc.convert(a, matrix)
# #print(list)
# #print('point', a[0].getPoint())

# for x in a[1].getLine():
#     #print('line', x.getPoint())

# for x in a[2].getPolygon():
#     #print('polygon', x.getPoint())
