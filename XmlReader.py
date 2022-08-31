from typing import List
import xml.etree.ElementTree as ET
from Elements.Geometry import *
import numpy as np


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
        print(self.poitList)
        for x in self.poitList:
            print(x.getPoint())

        for reta in self.root.findall("./reta"):
            retaAtual = []
            for ponto in reta:
                x0 = int(float(ponto.attrib.get('x')))
                y0 = int(float(ponto.attrib.get('y')))
                retaAtual.append((x0, y0))
            self.lineList.append(Line(retaAtual[0], retaAtual[1]))
        for x in self.lineList:
            pass
            print(x.getLine())

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
        for x in self.polygonList:
            print(x.getPolygon())


    def getViewportSize(self):
        return self.vpMin, self.vpMax

    def getWindowSize(self):
        return self.wMin, self.wMax

    def getPontos(self) -> List[Point]:
        return self.poitList

    def getRetas(self) -> List[Line]:
        return self.lineList

    def getPoligonos(self) -> List[Polygon]:
        return self.polygonList


a = XmlReader('entrada.xml')
xx = a.getViewportSize()
print(xx)