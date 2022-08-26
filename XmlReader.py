import xml.etree.ElementTree as ET

class XmlReader:
  pontos = []
  retas = []
  poligonos = []

  def __init__(self, filepath):
    self.filepath = filepath
    tree = ET.parse(self.filepath)
    self.root = tree.getroot()

    self.wMin = None
    self.wMax = None
    self.vMin = None
    self.vMax = None

    for wmin in self.root.findall("./window/wmin"):
      self.wMin = (int(float(wmin.attrib.get('x'))), int(float(wmin.attrib.get('y'))))

    for wmax in self.root.findall("./window/wmax"):
      self.wMax = (int(float(wmax.attrib.get('x'))), int(float(wmax.attrib.get('y'))))

    for vpmin in self.root.findall("./viewport/vpmin"):
      self.vpMin = (int(float(vpmin.attrib.get('x'))), int(float(vpmin.attrib.get('y'))))

    for vpmin in self.root.findall("./viewport/vpmax"):
      self.vpMax = (int(float(vpmin.attrib.get('x'))), int(float(vpmin.attrib.get('y'))))

    for ponto in self.root.findall("./ponto"):
      XmlReader.pontos.append((int(float(ponto.attrib.get('x'))), int(float(ponto.attrib.get('y')))))

    for reta in self.root.findall("./reta"):
     retaAtual = []
     for ponto in reta:
      retaAtual.append((int(float(ponto.attrib.get('x'))), int(float(ponto.attrib.get('y')))))
     XmlReader.retas.append(retaAtual)

    for poligono in self.root.findall("./poligono"):
     poligonoAtual = []
     for ponto in poligono:
      poligonoAtual.append((int(float(ponto.attrib.get('x'))), int(float(ponto.attrib.get('y')))))
     XmlReader.poligonos.append(poligonoAtual)

  def getViewportSize(self):
    return (self.vpMin,self.vpMax)

  def getWindowSize(self):
    return (self.wMin,self.wMax)

  def getPontos(self):
    return XmlReader.pontos
  def getRetas(self):
    return XmlReader.retas
  def getPoligonos(self):
    return XmlReader.poligonos