from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QBrush, QPen,QPainter, QPolygon
from PyQt5.QtCore import QPoint, Qt, QPointF, QLineF


class Window(QMainWindow):
		def __init__(self):
				super().__init__()

				self.title = "PyQt5 Drawing Polygon"
				self.top = 300
				self.left = 500
				self.width = 1280
				self.height = 720


				self.InitWindow()

	


		def InitWindow(self):
				self.setWindowIcon(QtGui.QIcon("icon.png"))
				self.setWindowTitle(self.title)
				self.setGeometry(self.left, self.top, self.width, self.height)
				self.show()

		def converter(self, x,y, xwmin, xwmax, ywmin, ywmax, xvmin, xvmax, yvmin, yvmax):
				Xw, Yw = x,y
				XwMin = xwmin
				XwMax = xwmax
				YwMin = ywmin
				YwMax = ywmax
				xvMin = xvmin
				XvMax = xvmax
				YvpMin = yvmin
				YvpMax = yvmax
				Xvp = ((Xw - XwMin) / (XwMax - XwMin)) * (XvMax - xvMin)
				Yvp = (1 - (Yw - YwMin) / (YwMax - YwMin)) * (YvpMax - YvpMin)
				return (Xvp, Yvp)

		def paintEvent(self, event):
				painter = QPainter(self)
				painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
				#painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
				painter.setBrush(QBrush(Qt.red, Qt.VerPattern))

				xwmin, xwmax, ywmin, ywmax= -5.0, 5.0, -5.0, 5.0
				xvmin, xvmax, yvmin, yvmax = 0, 800, 0, 600

				#pontos = [[(1.0, 2.0), (11.0, 2.0)], [(11.0, 2.0), (11.0, -4.0)], [(11.0, -4.0), (1.0, -4.0)], [(1.0, -4.0), (7.0, -2.0)], [(7.0, -2.0), (1.0, 2.0)]]
				pontos = [[(1.0, 5.0), (11.0, 5.0)], [(11.0, 5.0), (11.0, -1.0)], [(11.0, -1.0), (1.0, -1.0)], [(1.0, -1.0), (7.0, 1.0)], [(7.0, 1.0), (1.0, 5.0)]]
				pontos = [[(5.0, 5.0), (15.0, 5.0)], [(15.0, 5.0), (15.0, -1.0)], [(15.0, -1.0), (5.0, -1.0)], [(5.0, -1.0), (11.0, 1.0)], [(11.0, 1.0), (5.0, 5.0)]]
				points = QPolygon([
						QPoint(10,10),
						QPoint(10,100),
						QPoint(100,10),
						QPoint(100,100)



				])
				arrPontos = []
				for idx,point in enumerate(pontos):
					if idx%2 == 0:
						p1 = self.converter(*point[0], xwmin, xwmax, ywmin, ywmax, xvmin, xvmax, yvmin, yvmax)
						p2 = self.converter(*point[1], xwmin, xwmax, ywmin, ywmax, xvmin, xvmax, yvmin, yvmax)
						print(p1,p2)
						arrPontos.append(QPointF(*p1))
						arrPontos.append(QPointF(*p2))
					print(idx)
					# arrPontos.append()
				# points = QPolygon([
				# ])
				desloca = 0
				painter.drawLine(QLineF(0+desloca,0+desloca,800+desloca,0+desloca))
				painter.drawLine(QLineF(800+desloca,0+desloca,800+desloca,600+desloca))
				painter.drawLine(QLineF(800+desloca,600+desloca,0+desloca,600+desloca))
				painter.drawLine(QLineF(0+desloca,600+desloca,0+desloca,0+desloca))
				painter.drawPolygon(arrPontos)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())