# from clippers.Polygon.WeilerAtherton import *
from clippers.Polygon.WeilerAtherton import *
from elements.Geometry import Line
from elements.Geometry import Point
from elements.Geometry import Polygon
from elements import Window

class WeilerAthertonWrapper:
		def __init__(self):
				self.wa = WeilerAtherton()
		def clipPolygon(self, polygon: Polygon, window: Window):
				#print('type:', type(polygon.getPolygon()[0].getPoint()))
				# if type(polygon.getPolygon()[0].getPoint()) == np.ndarray
				# 	print('numpy')
				#print('polygon received', polygon)
				# print(line, window.getCoordinates())
				# print("#poligono")
				# #print(polygon)
				# print("#poligono")
				#exit(0)
				# print(window.getCoordinates())
				pol = polygon.getPolygon()
				pol2 = []
				for i in range(len(pol)-1):
					pol2.append([pol[i].getPoint(),pol[i+1].getPoint()])
				pol2.append([pol[-1].getPoint(), pol[0].getPoint()])

				xwMin, ywMin = window.getMinCoordinates()
				xwMax, ywMax = window.getMaxCoordinates()
				# print('tipo fora:',type(pol2))
				# for x in pol2:
				# 	print('tipo dentro:',type(x))
				# 	for y in x:
				# 		print('tipo mais dentro:', type(y))
				# print(xwMin, ywMin, xwMax, ywMax)
				# try:
				# 	for i in range(len(pol2)):
				# 			for j in range(len(pol2[i])):
				# 					#print(pol2[i][j])
				# 					pol2[i][j] = pol2[i][j].tolist()
				# except:
				# 	pass
				#print(pol2)

				result = self.wa.clipPolygon(pol2, xwMin, ywMin, xwMax, ywMax)
				# print('result', result)
				# exit(0)
				if(result is None):
						#print('none')
						return None
				arrPontos = []
				for index,polygo in enumerate(result):
					arrPontos.append([])
					for x in polygo:
						arrPontos[index].append(Point(x))
					#break
					#print(ponto)
					#exit(0)
					
				#p1 = Polygon()
				# self.cs.clipLine(x1, y1, x2, y2, xwMin, ywMin, xwMax, ywMax)
				#print(Polygon(*arrPontos))
				#exit(0)
				# for x in arrPontos:
				# 	print(x)
				#exit(0)
				return [Polygon(*x) for x in arrPontos]