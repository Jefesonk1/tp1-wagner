from typing  import Union
from typing import List
import xml.etree.ElementTree as ET
from Elements.Geometry import *
from WindowToViewportConversor import *
class XmlReader:
    def __init__(self, filepath):
        self.filepath = filepath
        tree = ET.parse(self.filepath)
        self.root = tree.getroot()
        self.wMin = None
        self.wMax = None
        self.vMin = None
        self.vMax = None
        self.poitList = []
        self.lineList = []
        self.polygonList = []

        for wmin in self.root.findall("./window/wmin"):
            self.wMin = (int(float(wmin.attrib.get('x'))),
                         int(float(wmin.attrib.get('y'))))

        for wmax in self.root.findall("./window/wmax"):
            self.wMax = (int(float(wmax.attrib.get('x'))),
                         int(float(wmax.attrib.get('y'))))

        for vpmin in self.root.findall("./viewport/vpmin"):
            self.vpMin = (int(float(vpmin.attrib.get('x'))),
                          int(float(vpmin.attrib.get('y'))))

        for vpmin in self.root.findall("./viewport/vpmax"):
            self.vpMax = (int(float(vpmin.attrib.get('x'))),
                          int(float(vpmin.attrib.get('y'))))

        for ponto in self.root.findall("./ponto"):
            x0 = int(float(ponto.attrib.get('x')))
            y0 = int(float(ponto.attrib.get('y')))
            self.poitList.append(Point((x0, y0)))

        for reta in self.root.findall("./reta"):
            retaAtual = []
            for ponto in reta:
                x0 = int(float(ponto.attrib.get('x')))
                y0 = int(float(ponto.attrib.get('y')))
                retaAtual.append((x0, y0))
            self.lineList.append(Line(retaAtual[0], retaAtual[1]))

        for poligono in self.root.findall("./poligono"):
            poligonoAtual = []
            for ponto in poligono:
                x0 = int(float(ponto.attrib.get('x')))
                y0 = int(float(ponto.attrib.get('y')))
                poligonoAtual.append(Point((x0, y0)))
            firstPoint = poligonoAtual[0].getPoint()
            poligonoAtual.append(Point(firstPoint))
            lista = list(map(lambda x: (x.getPoint()), poligonoAtual))
            polig = Polygon(*lista)
            self.polygonList.append(polig)

    def getViewportSize(self):
        return ((self.vpMin[0], self.vpMax[0]), (self.vpMin[1], self.vpMax[1]))

    def getWindowSize(self):
        return ((self.wMin[0], self.wMax[0]), (self.wMin[1], self.wMax[1]))

    def getPontos(self) -> List[Point]:
        return self.poitList

    def getRetas(self) -> List[Line]:
        return self.lineList

    def getPoligonos(self) -> List[Polygon]:
        return self.polygonList

    def convertToViewport(self, element: Union[Point, Line, Polygon]) -> List[Union[Point, Line, Polygon]]:
        windowToViewportConversor = WindowToViewportConversor()
        limitesJanelaX, limitesJanelaY, = self.getWindowSize()
        limitesViewPortX , limitesViewPortY = self.getViewportSize()

        if (type(element) == Point):
            print('instance of point')
            ponto = windowToViewportConversor.transform(element.getPoint(), limitesJanelaX, limitesJanelaY, limitesViewPortX, limitesViewPortY)
            return Point(ponto)

        if (type(element) == Line):
            print('instance of line')
            curr = []
            for ponto in element.getLine():
                ponto_tupla = (ponto[0], ponto[1])
                curr.append(windowToViewportConversor.transform(ponto_tupla, limitesJanelaX, limitesJanelaY, limitesViewPortX, limitesViewPortY))
            return Line(*(curr))

        if (type(element) == Polygon):
            print('instance of polygon')
            curr = []
            for line in element.getPolygon():
                for ponto in line:
                    ponto_tupla = (ponto[0], ponto[1])
                    curr.append(windowToViewportConversor.transform(ponto_tupla, limitesJanelaX, limitesJanelaY, limitesViewPortX, limitesViewPortY))
            return Polygon(*curr)