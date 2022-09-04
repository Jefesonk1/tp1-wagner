import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Drawer(QWidget):

    newPoint = pyqtSignal(QPoint)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.path = QPainterPath()    

        # set black background
        pal = self.palette()
        pal.setColor(QPalette.Background, Qt.magenta)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        self.newPoint.emit(event.pos())
        self.update()

    def sizeHint(self):
        return QSize(400, 400)


class MyWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        #MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        label = QLabel(self)
        drawer = Drawer(self)
        drawer.newPoint.connect(lambda p: label.setText(
                        'Coordinates: ( %d : %d )' % (p.x(), p.y())))
        self.layout().addWidget(label)
        self.layout().addWidget(drawer)
        self.layout().addWidget(drawer)
        


app = QApplication(sys.argv)
widget = MyWidget()
widget.show()

sys.exit(app.exec_())