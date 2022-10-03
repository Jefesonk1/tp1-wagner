import xml.etree.ElementTree as ET
from utils.XmlReader import *


class XmlWriter:
    def __init__(self, pathFilename) -> None:
        self.pathFilename = pathFilename

    def write(self, points, lines, polygons) -> None:
        root = ET.Element("dados")
        for point in points:
            #print(point)
            x = str(point.getPoint()[0])
            y = str(point.getPoint()[1])
            ET.SubElement(root, "ponto", x=x, y=y)

        for line in lines:
            currentLine = line.getLine()
            reta = ET.SubElement(root, "reta")
            for point in currentLine:
                x = str(point.getPoint()[0])
                y = str(point.getPoint()[1])
                ET.SubElement(reta, "ponto", x=x, y=y)

        for polygon in polygons:
            currentPolygon = polygon.getPolygon()
            poligono = ET.SubElement(root, "poligono")
            for point in currentPolygon:
                x = str(point.getPoint()[0])
                y = str(point.getPoint()[1])
                ET.SubElement(poligono, "ponto", x=x, y=y)
        tree = ET.ElementTree(root)
        ET.indent(tree, space="\t", level=0)  # py >= 3.9
        tree.write(self.pathFilename)
