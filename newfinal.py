from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import resources.resource as resource
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
        self.widgetTrasformations = QtWidgets.QWidget(self.frameTransformations)
        self.widgetTrasformations.setGeometry(QtCore.QRect(10, 10, 210, 480))
        self.widgetTrasformations.setStyleSheet("")
        self.widgetTrasformations.setObjectName("widgetTrasformations")
        self.buttomRotateLeft = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttomRotateLeft.setGeometry(QtCore.QRect(20, 80, 50, 30))
        self.buttomRotateLeft.setStyleSheet("")
        self.buttomRotateLeft.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/rotate-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomRotateLeft.setIcon(icon)
        self.buttomRotateLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttomRotateLeft.setCheckable(False)
        self.buttomRotateLeft.setAutoExclusive(False)
        self.buttomRotateLeft.setObjectName("buttomRotateLeft")
        self.buttomRight_2 = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttomRight_2.setGeometry(QtCore.QRect(140, 80, 50, 30))
        self.buttomRight_2.setStyleSheet("")
        self.buttomRight_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/icons/rotate-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomRight_2.setIcon(icon1)
        self.buttomRight_2.setIconSize(QtCore.QSize(24, 24))
        self.buttomRight_2.setCheckable(False)
        self.buttomRight_2.setAutoExclusive(False)
        self.buttomRight_2.setObjectName("buttomRight_2")
        self.buttomUp = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttomUp.setGeometry(QtCore.QRect(80, 80, 50, 30))
        self.buttomUp.setStyleSheet("")
        self.buttomUp.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/up-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomUp.setIcon(icon2)
        self.buttomUp.setIconSize(QtCore.QSize(24, 24))
        self.buttomUp.setCheckable(False)
        self.buttomUp.setAutoExclusive(False)
        self.buttomUp.setObjectName("buttomUp")
        self.buttomDown = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttomDown.setGeometry(QtCore.QRect(80, 160, 50, 30))
        self.buttomDown.setStyleSheet("")
        self.buttomDown.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/icons/down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomDown.setIcon(icon3)
        self.buttomDown.setIconSize(QtCore.QSize(24, 24))
        self.buttomDown.setCheckable(False)
        self.buttomDown.setAutoExclusive(False)
        self.buttomDown.setObjectName("buttomDown")
        self.buttomLeft = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttomLeft.setGeometry(QtCore.QRect(20, 120, 50, 30))
        self.buttomLeft.setStyleSheet("")
        self.buttomLeft.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/icons/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomLeft.setIcon(icon4)
        self.buttomLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttomLeft.setCheckable(False)
        self.buttomLeft.setAutoExclusive(False)
        self.buttomLeft.setObjectName("buttomLeft")
        self.buttomRight = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttomRight.setGeometry(QtCore.QRect(140, 120, 50, 30))
        self.buttomRight.setStyleSheet("")
        self.buttomRight.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomRight.setIcon(icon5)
        self.buttomRight.setIconSize(QtCore.QSize(24, 24))
        self.buttomRight.setCheckable(False)
        self.buttomRight.setAutoExclusive(False)
        self.buttomRight.setObjectName("buttomRight")
        self.spinBoxRotateStepSize = QtWidgets.QSpinBox(self.widgetTrasformations)
        self.spinBoxRotateStepSize.setGeometry(QtCore.QRect(130, 300, 42, 25))
        self.spinBoxRotateStepSize.setObjectName("spinBoxRotateStepSize")
        self.labelMoveRotate = QtWidgets.QLabel(self.widgetTrasformations)
        self.labelMoveRotate.setGeometry(QtCore.QRect(40, 30, 121, 20))
        self.labelMoveRotate.setObjectName("labelMoveRotate")
        self.spinBoxTranslateStepSize = QtWidgets.QSpinBox(self.widgetTrasformations)
        self.spinBoxTranslateStepSize.setGeometry(QtCore.QRect(130, 270, 42, 25))
        self.spinBoxTranslateStepSize.setObjectName("spinBoxTranslateStepSize")
        self.labelTranslateStepSize = QtWidgets.QLabel(self.widgetTrasformations)
        self.labelTranslateStepSize.setGeometry(QtCore.QRect(10, 270, 101, 20))
        self.labelTranslateStepSize.setObjectName("labelTranslateStepSize")
        self.labelRotateStepSize = QtWidgets.QLabel(self.widgetTrasformations)
        self.labelRotateStepSize.setGeometry(QtCore.QRect(10, 300, 101, 20))
        self.labelRotateStepSize.setObjectName("labelRotateStepSize")
        self.buttomHome = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttomHome.setGeometry(QtCore.QRect(80, 120, 50, 30))
        self.buttomHome.setStyleSheet("")
        self.buttomHome.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomHome.setIcon(icon6)
        self.buttomHome.setIconSize(QtCore.QSize(24, 24))
        self.buttomHome.setCheckable(False)
        self.buttomHome.setAutoExclusive(False)
        self.buttomHome.setObjectName("buttomHome")
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
        self.widgetDrawer = Draw(self.frameDrawer) #self.frameDrawer)
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
        self.labelMoveRotate.setText(_translate("MainWindow", "Move/Rotate Window"))
        self.labelTranslateStepSize.setText(_translate("MainWindow", "Traslation step size"))
        self.labelRotateStepSize.setText(_translate("MainWindow", "Rotation step size"))
        self.buttonSaveXml.setText(_translate("MainWindow", "save as xml"))
        self.buttonUseless.setText(_translate("MainWindow", "teste2"))
        self.labelCoordinates.setText(_translate("MainWindow", "coordinates:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

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
        self.labelNameAbout.setText(u"<html><head/><body><p><a href=\"https://github.com/Jefesonk1\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>")
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
        fileName, _  = fileDialog.getSaveFileName(
            self.centralwidget, "Save", "", "XML Files (*.xml)", options=options)
        if fileName:
            return fileName


    def saveFileAsXml(self):
        pathFilename = self.saveFileDialog()
        if(pathFilename):
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
        viewportWidth = int(self.viewport.getXvMax() - self.viewport.getXvMin())
        viewportHeight = int(self.viewport.getYvMax() - self.viewport.getYvMin())
        self.widgetDrawer.setGeometry(QtCore.QRect(10, 10, viewportWidth, viewportHeight))

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
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
