
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
            for object in objectsList:
                if isinstance(object, Polygon):
                    self.convertedObjectsList.append(
                        self.convertPolygon(object))
                elif isinstance(object, Line):
                    self.convertedObjectsList.append(self.convertLine(object))
                elif isinstance(object, Point):
                    self.convertedObjectsList.append(self.convertPoint(object))
                else:
                    raise TypeError("Invalid type of object")
        else:
            raise TypeError("Not a list")
        return self.convertedObjectsList

    def convertPoint(self, point: Point):
        p = (self.transformationMatrix @ [*(point.getPoint()), 1])[:-1]
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