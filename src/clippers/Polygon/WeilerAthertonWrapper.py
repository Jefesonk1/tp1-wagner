from clippers.Polygon.WeilerAtherton import *
from elements.Geometry import Line
from elements.Geometry import Point
from elements.Geometry import Polygon
from elements import Window

class WeilerAthertonWrapper:
		def __init__(self):
				self.wa = WeilerAtherton()
		def clipPolygon(self, polygon: Polygon, window: Window):
				pol = polygon.getPolygon()
				pol2 = []
				for i in range(len(pol)-1):
					pol2.append([pol[i].getPoint(),pol[i+1].getPoint()])
				pol2.append([pol[-1].getPoint(), pol[0].getPoint()])
				xwMin, ywMin = window.getMinCoordinates()
				xwMax, ywMax = window.getMaxCoordinates()
				result = self.wa.clipPolygon(pol2, xwMin, ywMin, xwMax, ywMax)
				if(result is None):
						return None
				arrPontos = []
				for index,polygo in enumerate(result):
					arrPontos.append([])
					for x in polygo:
						arrPontos[index].append(Point(x))
				return [Polygon(*x) for x in arrPontos]