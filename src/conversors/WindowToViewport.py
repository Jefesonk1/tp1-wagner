from typing import Union
from typing import List
from elements.Window import *
from elements.Viewport import *
from elements.Geometry import *


class WindowToViewport:
    def __transform(self, pontos, window: Window, viewport: Viewport):
        Xw, Yw = pontos
        xwmin = window.getXwMin()
        xwmax = window.getXwMax()
        ywmin = window.getYwMin()
        ywmax = window.getYwMax()
        xvmin = viewport.getXvMin()
        xvmax = viewport.getXvMax()
        yvmin = viewport.getYvMin()
        yvmax = viewport.getYvMax()
        sx = (xvmax - xvmin) / (xwmax - xwmin)
        sy = (yvmax - yvmin) / (ywmax - ywmin)
        x_v = xvmin + ((Xw - xwmin) * sx)
        y_v = yvmin + ((Yw - ywmin) * sy)
        y_v = yvmax - y_v + yvmin
        return (x_v, y_v)

    def convertToViewport(self, element: Union[Point, Line, Polygon], window: Window, viewport: Viewport) -> List[Union[Point, Line, Polygon]]:
        if (type(element) == Point):
            point = self.__transform(
                element.getPoint(), window, viewport)
            return Point(point)

        if (type(element) == Line):
            line = []
            for ponto in element.getLine():
                currPoint = self.__transform(ponto.getPoint(), window, viewport)
                line.append(Point(currPoint))
            return Line(*(line))

        if (type(element) == Polygon):
            polygon = []
            for point in element.getPolygon():
                currPoint = self.__transform(point.getPoint(), window, viewport) 
                polygon.append(Point(currPoint))
            return Polygon(*polygon)
