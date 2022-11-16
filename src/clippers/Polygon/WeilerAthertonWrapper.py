# from clippers.Polygon.WeilerAtherton import *
from clippers.Polygon.WeilerAtherton import *
from elements.Geometry import Line
from elements.Geometry import Point
from elements.Geometry import Polygon
from elements import Window

class WeilerAthertonWrapper:
		def __init__(self):
				self.wa = WeilerAtherton()
		def clipPolygon(self, line: Line, window: Window):
				# print(line, window.getCoordinates())
				print(line)
				print(window.getCoordinates())
				x1, y1 = line.getLine()[0].getPoint()
				x2, y2 = line.getLine()[1].getPoint()
				xwMin, ywMin = window.getMinCoordinates()
				xwMax, ywMax = window.getMaxCoordinates()
				result = self.cs.clipLine(x1, y1, x2, y2, xwMin, ywMin, xwMax, ywMax)
				if(result is None):
						print('none')
						return None
				x1, y1, x2, y2 = result
				# self.cs.clipLine(x1, y1, x2, y2, xwMin, ywMin, xwMax, ywMax)
				p1 = Point((x1, y1))
				p2 = Point((x2, y2))
				return Line(p1, p2)