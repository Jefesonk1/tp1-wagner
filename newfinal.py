from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import resources.resource as resource
from Draw import *
from XmlReader import *
from XmlWriter import *
import math
print(resource)


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
        self.windowRotation = 0
        self.windowTranslation = 0
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 650)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameTransformations = QtWidgets.QFrame(self.centralwidget)
        self.frameTransformations.setGeometry(QtCore.QRect(800, 90, 230, 500))
        self.frameTransformations.setAutoFillBackground(False)
        self.frameTransformations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTransformations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTransformations.setObjectName("frameTransformations")
        self.widgetTrasformations = QtWidgets.QWidget(
            self.frameTransformations)
        self.widgetTrasformations.setGeometry(QtCore.QRect(10, 10, 210, 480))
        self.widgetTrasformations.setStyleSheet("")
        self.widgetTrasformations.setObjectName("widgetTrasformations")
        self.buttonRotateLeft = QtWidgets.QPushButton(
            self.widgetTrasformations)
        self.buttonRotateLeft.setGeometry(QtCore.QRect(20, 80, 50, 30))
        self.buttonRotateLeft.setStyleSheet("")
        self.buttonRotateLeft.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/rotate-left.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRotateLeft.setIcon(icon)
        self.buttonRotateLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttonRotateLeft.setCheckable(False)
        self.buttonRotateLeft.setAutoExclusive(False)
        self.buttonRotateLeft.setObjectName("buttonRotateLeft")
        self.buttonRotateLeft.clicked.connect(self.buttonRotateLeftAction)
        self.buttonRotateRight = QtWidgets.QPushButton(
            self.widgetTrasformations)
        self.buttonRotateRight.setGeometry(QtCore.QRect(140, 80, 50, 30))
        self.buttonRotateRight.setStyleSheet("")
        self.buttonRotateRight.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "resources/icons/rotate-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRotateRight.setIcon(icon1)
        self.buttonRotateRight.setIconSize(QtCore.QSize(24, 24))
        self.buttonRotateRight.setCheckable(False)
        self.buttonRotateRight.setAutoExclusive(False)
        self.buttonRotateRight.setObjectName("buttonRotateRight")
        self.buttonRotateRight.clicked.connect(self.buttonRotateRightAction)
        self.buttonUp = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonUp.setGeometry(QtCore.QRect(80, 80, 50, 30))
        self.buttonUp.setStyleSheet("")
        self.buttonUp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/up-arrow.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUp.setIcon(icon2)
        self.buttonUp.setIconSize(QtCore.QSize(24, 24))
        self.buttonUp.setCheckable(False)
        self.buttonUp.setAutoExclusive(False)
        self.buttonUp.setObjectName("buttonUp")
        self.buttonUp.clicked.connect(self.buttonUpAction)
        self.buttonDown = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonDown.setGeometry(QtCore.QRect(80, 160, 50, 30))
        self.buttonDown.setStyleSheet("")
        self.buttonDown.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            "resources/icons/down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDown.setIcon(icon3)
        self.buttonDown.setIconSize(QtCore.QSize(24, 24))
        self.buttonDown.setCheckable(False)
        self.buttonDown.setAutoExclusive(False)
        self.buttonDown.setObjectName("buttonDown")
        self.buttonDown.clicked.connect(self.buttonDownAction)
        self.buttonLeft = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonLeft.setGeometry(QtCore.QRect(20, 120, 50, 30))
        self.buttonLeft.setStyleSheet("")
        self.buttonLeft.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            "resources/icons/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLeft.setIcon(icon4)
        self.buttonLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttonLeft.setCheckable(False)
        self.buttonLeft.setAutoExclusive(False)
        self.buttonLeft.setObjectName("buttonLeft")
        self.buttonLeft.clicked.connect(self.buttonLeftAction)
        self.buttonRight = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonRight.setGeometry(QtCore.QRect(140, 120, 50, 30))
        self.buttonRight.setStyleSheet("")
        self.buttonRight.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            "resources/icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRight.setIcon(icon5)
        self.buttonRight.setIconSize(QtCore.QSize(24, 24))
        self.buttonRight.setCheckable(False)
        self.buttonRight.setAutoExclusive(False)
        self.buttonRight.setObjectName("buttonRight")
        self.buttonRight.clicked.connect(self.buttonRightAction)
        self.spinBoxRotateStepSize = QtWidgets.QSpinBox(
            self.widgetTrasformations)
        self.spinBoxRotateStepSize.setGeometry(QtCore.QRect(130, 300, 42, 25))
        self.spinBoxRotateStepSize.setObjectName("spinBoxRotateStepSize")
        self.spinBoxRotateStepSize.setValue(10)
        self.labelMoveRotate = QtWidgets.QLabel(self.widgetTrasformations)
        self.labelMoveRotate.setGeometry(QtCore.QRect(40, 30, 121, 20))
        self.labelMoveRotate.setObjectName("labelMoveRotate")
        self.spinBoxTranslateStepSize = QtWidgets.QSpinBox(
            self.widgetTrasformations)
        self.spinBoxTranslateStepSize.setGeometry(
            QtCore.QRect(130, 270, 42, 25))
        self.spinBoxTranslateStepSize.setObjectName("spinBoxTranslateStepSize")
        self.spinBoxTranslateStepSize.setValue(10)
        self.labelTranslateStepSize = QtWidgets.QLabel(
            self.widgetTrasformations)
        self.labelTranslateStepSize.setGeometry(QtCore.QRect(10, 270, 101, 20))
        self.labelTranslateStepSize.setObjectName("labelTranslateStepSize")
        self.labelRotateStepSize = QtWidgets.QLabel(self.widgetTrasformations)
        self.labelRotateStepSize.setGeometry(QtCore.QRect(10, 300, 101, 20))
        self.labelRotateStepSize.setObjectName("labelRotateStepSize")
        self.buttonHome = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonHome.setGeometry(QtCore.QRect(80, 120, 50, 30))
        self.buttonHome.setStyleSheet("")
        self.buttonHome.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/icons/home.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonHome.setIcon(icon6)
        self.buttonHome.setIconSize(QtCore.QSize(24, 24))
        self.buttonHome.setCheckable(False)
        self.buttonHome.setAutoExclusive(False)
        self.buttonHome.setObjectName("buttonHome")
        self.buttonHome.clicked.connect(self.buttonHomeAction)
        self.frameMain = QtWidgets.QFrame(self.centralwidget)
        self.frameMain.setGeometry(QtCore.QRect(9, 10, 1031, 591))
        self.frameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMain.setObjectName("frameMain")
        self.widget_blue = QtWidgets.QWidget(self.frameMain)
        self.widget_blue.setGeometry(QtCore.QRect(340, 10, 101, 61))
        self.widget_blue.setStyleSheet("background-color: blue")
        self.widget_blue.setObjectName("widget_blue")
        self.widget_yellow = QtWidgets.QWidget(self.frameMain)
        self.widget_yellow.setGeometry(QtCore.QRect(460, 10, 111, 61))
        self.widget_yellow.setStyleSheet("background-color: yellow")
        self.widget_yellow.setObjectName("widget_yellow")
        self.widget_magenta = QtWidgets.QWidget(self.frameMain)
        self.widget_magenta.setGeometry(QtCore.QRect(590, 10, 111, 61))
        self.widget_magenta.setStyleSheet("background-color: magenta")
        self.widget_magenta.setObjectName("widget_magenta")
        self.frameDrawer = QtWidgets.QFrame(self.frameMain)
        self.frameDrawer.setGeometry(QtCore.QRect(10, 80, 771, 500))
        self.frameDrawer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDrawer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDrawer.setObjectName("frameDrawer")
        self.widgetDrawer = Draw(self.frameDrawer)  # self.frameDrawer)
        self.widgetDrawer.setGeometry(QtCore.QRect(10, 10, 751, 481))
        self.widgetDrawer.setStyleSheet("background-color: \'#3d3d3d\'")
        self.widgetDrawer.setObjectName("widgetDrawer")
        self.buttonSaveXml = QtWidgets.QPushButton(self.frameMain)
        self.buttonSaveXml.setGeometry(QtCore.QRect(10, 30, 70, 27))
        self.buttonSaveXml.setStyleSheet("")
        self.buttonSaveXml.setObjectName("buttonSaveXml")
        self.buttonSaveXml.clicked.connect(self.saveFileAsXml)
        self.buttonUseless = QtWidgets.QPushButton(self.frameMain)
        self.buttonUseless.setGeometry(QtCore.QRect(100, 30, 70, 27))
        self.buttonUseless.setObjectName("buttonUseless")
        self.buttonUseless.hide()
        self.labelCoordinates = QtWidgets.QLabel(self.frameMain)
        self.labelCoordinates.setGeometry(QtCore.QRect(190, 20, 140, 41))
        self.labelCoordinates.setObjectName("labelCoordinates")
        self.widgetDrawer.newPoint.connect(lambda p: self.labelCoordinates.setText(
            'Coordinates: ( %d : %d )' % (p.x(), p.y())))
        self.frameMain.raise_()
        self.frameTransformations.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 25))
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
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionAbout.triggered.connect(self.triggerAbout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelMoveRotate.setText(_translate(
            "MainWindow", "Move/Rotate Window"))
        self.labelTranslateStepSize.setText(
            _translate("MainWindow", "Traslation step size"))
        self.labelRotateStepSize.setText(
            _translate("MainWindow", "Rotation step size"))
        self.buttonSaveXml.setText(_translate("MainWindow", "save as xml"))
        self.buttonUseless.setText(_translate("MainWindow", "teste2"))
        self.labelCoordinates.setText(_translate("MainWindow", "coordinates:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def calcular(self, x, y, matrix):
        # print(x,y)
        print(matrix @ np.array([x, y, 1]))
        coord = matrix @ np.array([x, y, 1])
        return (coord[0], coord[1])

    def newWinCoordinates(self):
        coord = self.window.getCoordinates()
        print('coord :', coord)
        # a = self.calcular(coord[0][0], 0, self.window.getTransformationMatrix())
        # b = self.calcular(coord[0][0], coord[1][0], self.window.getTransformationMatrix())
        # c = self.calcular(coord[1][0], 0, self.window.getTransformationMatrix())
        # d = self.calcular(coord[1][0], coord[1][1], self.window.getTransformationMatrix())
       # print(a,b,c,d)
        xwMin, ywMin = self.calcular(
            *coord[0], self.window.getTransformationMatrix())
        xwmax, ywmax = self.calcular(
            *coord[1], self.window.getTransformationMatrix())
        #print(xwMin,ywMin, xwmax,ywmax)

        newWindow = Window(xwMin, xwmax, ywMin, ywmax)

        print('wincoord', newWindow.getCoordinates())
        # conversor = WindowToViewportConversor()
        # # self.window = xmlReader.getWindow()
        # # self.viewport = xmlReader.getViewport()
        # # self.displayFilePointsCoordinates = xmlReader.getPontos()
        # # self.displayFileLinesCoordinates = xmlReader.getRetas()
        # # self.displayFilePolygonsCoordinates = xmlReader.getPoligonos()
        # print(self.viewport)
        # viewportWidth = int(self.viewport.getXvMax() - self.viewport.getXvMin())
        # viewportHeight = int(self.viewport.getYvMax() - self.viewport.getYvMin())
        # self.widgetDrawer.setGeometry(QtCore.QRect(10, 10, viewportWidth, viewportHeight))

        # for point in self.displayFilePointsCoordinates:
        #     convertedPoint = conversor.convertToViewport(
        #         point, newWindow, self.viewport)
        #     self.viewPortPointsCoordinates.append(convertedPoint)

        # for line in self.displayFileLinesCoordinates:
        #     convertedLine = conversor.convertToViewport(
        #         line, newWindow, self.viewport)
        #     self.viewPortLinesCoordinates.append(convertedLine)

        # for polygon in self.displayFilePolygonsCoordinates:
        #     convertedPolygon = conversor.convertToViewport(
        #         polygon, newWindow, self.viewport)
        #     self.viewPortPolygonsCoordinates.append(convertedPolygon)

        # for ponto in self.viewPortPointsCoordinates:
        #     self.widgetDrawer.drawPoint(ponto)

        # for line in self.viewPortLinesCoordinates:
        #     self.widgetDrawer.drawLine(line)

        # for polygon in self.viewPortPolygonsCoordinates:
        #     self.widgetDrawer.drawPolygon(polygon)

        #print('new win coordinates', coord)

    def buttonUpAction(self):
        print('moveu up')
        self.window.addTranslation(0, self.spinBoxTranslateStepSize.value())
        print(self.window.getTranslation())
        print(self.window.getTransformationMatrix())
        self.newWinCoordinates()

    def buttonDownAction(self):
        print('moveu down')
        self.window.addTranslation(0, -self.spinBoxTranslateStepSize.value())
        print(self.window.getTranslation())
        self.newWinCoordinates()

    def buttonLeftAction(self):
        print('moveu left')
        self.window.addTranslation(-self.spinBoxTranslateStepSize.value(), 0)
        print(self.window.getTranslation())
        self.newWinCoordinates()

    def buttonRightAction(self):
        print('moveu right')
        self.window.addTranslation(self.spinBoxTranslateStepSize.value(), 0)
        print(self.window.getTranslation())
        self.newWinCoordinates()

    def buttonHomeAction(self):
        print('moveu home')
        self.window.resetTransformation()
        self.newWinCoordinates()
        self.widgetDrawer.erase()

    def buttonRotateLeftAction(self):
        print('rotate left')
        self.window.addRotation(-self.spinBoxRotateStepSize.value())
        print(self.window.getRotation())
        print(math.radians(self.window.getRotation()))
        self.newWinCoordinates()

    def buttonRotateRightAction(self):
        print('rotate right')
        self.window.addRotation(self.spinBoxRotateStepSize.value())
        print(self.window.getRotation())
        print(math.radians(self.window.getRotation()))
        self.newWinCoordinates()

    def triggerAbout(self):
        my_dialog = QDialog(MainWindow)
        my_dialog.setWindowTitle("About")
        # my_dialog.setWindowModality(Qt.ApplicationModal)
        my_dialog.setGeometry(0, 0, 400, 300)
        my_dialog.move(MainWindow.rect().center())
        # my_dialog.move(QDesktopWidget().availableGeometry().center().x() - self.frameGeometry().center().x() * 0.5, QDesktopWidget().availableGeometry().center().y() - self.frameGeometry().center().y() * 0.5)
        self.labelNameAbout = QtWidgets.QLabel(my_dialog)

        #self.labelNameAbout.setGeometry(QtCore.QRect(10, 270, 101, 20))
        self.labelNameAbout.setObjectName("labelNameAbout")
        self.labelNameAbout.move(my_dialog.rect().center())
        self.labelNameAbout.setText(
            u"<html><head/><body><p><a href=\"https://github.com/Jefesonk1\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>")
        self.labelNameAbout.setOpenExternalLinks(True)
        #self.labelNameAbout.setText("Feito por: Jefeson Martins Delazeri\n email: jefesonk1@outlook.com \n github: https://github.com/Jefesonk1")
        my_dialog.exec_()  #
        # self.about = QtWidgets.QDialog()

        # self.aboutUi = Ui_Dialog()
        # self.aboutUi.setupUi(self.about)
        # self.about.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self.centralwidget, "Open", "", "XLM Files (*.xml)", options=options)
        if fileName:
            return fileName

    def saveFileDialog(self):
        options = QFileDialog.Options()
        fileDialog = QFileDialog(self, 'Projects')
        fileDialog.setAttribute(Qt.WA_QuitOnClose, False)
        fileName, _ = fileDialog.getSaveFileName(
            self.centralwidget, "Save", "", "XML Files (*.xml)", options=options)
        if fileName:
            return fileName

    def saveFileAsXml(self):
        pathFilename = self.saveFileDialog()
        if (pathFilename):
            xml = XmlWriter(pathFilename)
            xml.write(self.viewPortPointsCoordinates,
                      self.viewPortLinesCoordinates, self.viewPortPolygonsCoordinates)
            self.buttonSaveXml.hide()
            self.buttonSaveXml.setText("Saved")

    def openFile(self):
        filePath = self.openFileNameDialog()
        xmlReader = XmlReader(filePath)
        conversor = WindowToViewportConversor()
        self.window = xmlReader.getWindow()
        self.viewport = xmlReader.getViewport()
        self.displayFilePointsCoordinates = xmlReader.getPontos()
        self.displayFileLinesCoordinates = xmlReader.getRetas()
        self.displayFilePolygonsCoordinates = xmlReader.getPoligonos()
        print(self.viewport)
        viewportWidth = int(self.viewport.getXvMax() -
                            self.viewport.getXvMin())
        viewportHeight = int(self.viewport.getYvMax() -
                             self.viewport.getYvMin())
        self.widgetDrawer.setGeometry(QtCore.QRect(
            10, 10, viewportWidth, viewportHeight))

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
            self.widgetDrawer.drawPoint(ponto)

        for line in self.viewPortLinesCoordinates:
            self.widgetDrawer.drawLine(line)

        for polygon in self.viewPortPolygonsCoordinates:
            self.widgetDrawer.drawPolygon(polygon)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    styleFile = QFile("style.qss")
    styleFile.open(QFile.ReadOnly)
    stylesheet = QTextStream(styleFile).readAll()
    app.setStyleSheet(stylesheet)

    ui = Ui_MainWindow(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
