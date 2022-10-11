from clippers.Point.PointClipper import PointClipper
from elements.Geometry import Point
from elements.Window import Window

class PointClipperWrapper:
		def __init__(self):
				self.pc = PointClipper()

		def clipPoint(self, point, window):
				x1, y1 = point.getPoint()
				xwMin, ywMin = window.getMinCoordinates()
				xwMax, ywMax = window.getMaxCoordinates()
				result = self.pc.clipPoint(x1, y1, xwMin, ywMin, xwMax, ywMax)
				if(result is None):
						print('none')
						return None
				x1, y1 = result
				return point