from clippers.Line.LiangBarsky import LiangBarsky
from elements.Geometry import Line
from elements.Geometry import Point
from elements import Window

class LiangBarskyWrapper:
		def __init__(self):
				self.lb = LiangBarsky()
		def clipLine(self, line: Line, window: Window):
				x1, y1 = line.getLine()[0].getPoint()
				x2, y2 = line.getLine()[1].getPoint()
				xwMin, ywMin = window.getMinCoordinates()
				xwMax, ywMax = window.getMaxCoordinates()
				result = self.lb.clipLine(x1, y1, x2, y2, xwMin, ywMin, xwMax, ywMax)
				if(result is None):
						return None
				x1, y1, x2, y2 = result
				p1 = Point((x1, y1))
				p2 = Point((x2, y2))
				return Line(p1, p2)