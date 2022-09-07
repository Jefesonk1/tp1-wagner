from typing import Union
from typing import List
from Elements.Window import *
from Elements.Viewport import *
from Elements.Geometry import *


class WindowToViewportConversor:
    def __transform(self, pontos, window: Window, viewport: Viewport):
        Xw, Yw = pontos
        XwMin = window.getXwMin()
        XwMax = window.getXwMax()
        YwMin = window.getYwMin()
        YwMax = window.getYwMax()
        xvMin = viewport.getXvMin()
        XvMax = viewport.getXvMax()
        YvpMin = viewport.getYvMin()
        YvpMax = viewport.getYvMax()
        Xvp = ((Xw - XwMin) / (XwMax - XwMin)) * (XvMax - xvMin)
        Yvp = (1 - (Yw - YwMin) / (YwMax - YwMin)) * (YvpMax - YvpMin)
        return (Xvp, Yvp)

    def convertToViewport(self, element: Union[Point, Line, Polygon], window: Window, viewport: Viewport) -> List[Union[Point, Line, Polygon]]:
        if (type(element) == Point):
            point = self.__transform(
                element.getPoint(), window, viewport)
            return Point(point)

        if (type(element) == Line):
            line = []
            for ponto in element.getLine():
                line.append(self.__transform(
                    ponto.getPoint(), window, viewport))
            return Line(*(line))

        if (type(element) == Polygon):
            polygon = []
            for point in element.getPolygon():
                polygon.append(self.__transform(
                    point.getPoint(), window, viewport))
            return Polygon(*polygon)
