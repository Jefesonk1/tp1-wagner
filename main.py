from PyQt5 import QtCore, QtWidgets
from Draw import *
from XmlReader import *
from XmlWriter import *


class Ui_MainWindow(QMainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__(MainWindow)
        self.viewPortPointsCoordinates = []
        self.viewPortLinesCoordinates = []
        self.viewPortPolygonsCoordinates = []
        self.displayFilePointsCoordinates = []
        self.displayFileLinesCoordinates = []
        self.displayFilePolygonsCoordinates = []
        self.window = Window(0, 0, 0, 0)
        self.viewport = Viewport(0, 0, 0, 0)
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget = Draw(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 90, 751, 451))
        self.widget.setStyleSheet(
            "background-color: green; border: 1px solid magenta")
        self.widget.setObjectName("widget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.changelabeltext)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 30, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 200, 16))
        self.label.setObjectName("label")
        self.widget.newPoint.connect(lambda p: self.label.setText(
            'Coordinates: ( %d : %d )' % (p.x(), p.y())))
        self.widget_blue = QtWidgets.QWidget(self.centralwidget)
        self.widget_blue.setGeometry(QtCore.QRect(350, 10, 101, 61))
        self.widget_blue.setStyleSheet("background-color: blue")
        self.widget_blue.setObjectName("widget_blue")
        self.widget_yellow = QtWidgets.QWidget(self.centralwidget)
        self.widget_yellow.setGeometry(QtCore.QRect(480, 10, 111, 61))
        self.widget_yellow.setStyleSheet("background-color: yellow")
        self.widget_yellow.setObjectName("widget_yellow")
        self.widget_magenta = QtWidgets.QWidget(self.centralwidget)
        self.widget_magenta.setGeometry(QtCore.QRect(620, 10, 111, 61))
        self.widget_magenta.setStyleSheet("background-color: magenta")
        self.widget_magenta.setObjectName("widget_magenta")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionOpen.triggered.connect(self.openFile)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "save as xml"))
        self.pushButton_2.setText(_translate("MainWindow", "teste2"))
        self.label.setText(_translate("MainWindow", "teste3"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "XLM Files (*.xml)", options=options)
        if fileName:
            return fileName

    def openFile(self):
        filePath = self.openFileNameDialog()
        xmlReader = XmlReader(filePath)
        conversor = WindowToViewportConversor()
        self.window = xmlReader.getWindow()
        self.viewport = xmlReader.getViewport()
        self.displayFilePointsCoordinates = xmlReader.getPontos()
        self.displayFileLinesCoordinates = xmlReader.getRetas()
        self.displayFilePolygonsCoordinates = xmlReader.getPoligonos()

        for point in self.displayFilePointsCoordinates:
            convertedPoint = conversor.convertToViewport(
                point, self.window, self.viewport)
            self.viewPortPointsCoordinates.append(convertedPoint)

        for line in self.displayFileLinesCoordinates:
            convertedLine = conversor.convertToViewport(
                line, self.window, self.viewport)
            self.viewPortLinesCoordinates.append(convertedLine)

        for polygon in self.displayFilePolygonsCoordinates:
            convertedPolygon = conversor.convertToViewport(
                polygon, self.window, self.viewport)
            self.viewPortPolygonsCoordinates.append(convertedPolygon)

        for ponto in self.viewPortPointsCoordinates:
            self.widget.drawPoint(ponto)

        for line in self.viewPortLinesCoordinates:
            self.widget.drawLine(line)

        for polygon in self.viewPortPolygonsCoordinates:
            self.widget.drawPolygon(polygon)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "XML Files (*.xml)", options=options)
        if fileName:
            return fileName

    def changelabeltext(self):
        self.label.setText("Saved")
        pathFilename = self.saveFileDialog()
        xml = XmlWriter(pathFilename)
        xml.write(self.viewPortPointsCoordinates,
                  self.viewPortLinesCoordinates, self.viewPortPolygonsCoordinates)
        self.pushButton.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
