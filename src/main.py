import string
import resources.resource
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.addObjects import *
from elements.ObjectsConvert import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets.Draw import *
import math
import copy
from utils.calculate import calculate
from utils.XmlReader import *
from utils.XmlWriter import *
from conversors.ppc import WorldToPPC
from clippers.Line.CohenSutherlandWrapper import CohenSutherlandWrapper
from clippers.Point.PointClipperWrapper import PointClipperWrapper
from clippers.Polygon.WeilerAthertonWrapper import WeilerAthertonWrapper


#print('resources loaded', resources.resource)


class Ui_MainWindow(QMainWindow):
    def __init__(self, MainWindow, debug=False) -> None:

        super().__init__(MainWindow)
        self.debug = debug
        self.viewPortPointsCoordinates = []
        self.viewPortLinesCoordinates = []
        self.viewPortPolygonsCoordinates = []
        self.displayFilePointsCoordinates = []
        self.displayFileLinesCoordinates = []
        self.displayFilePolygonsCoordinates = []
        self.history = []
        self.window = Window(0, 0, 0, 0)
        self.viewport = Viewport(0, 0, 0, 0)
        self.windowRotation = 0
        self.windowTranslation = 0

        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 640)
        MainWindow.setFixedSize(QtCore.QSize(1280, 640))
        self.icons_prefix = 'resources/icons/'
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.frameMain = QtWidgets.QFrame(self.centralwidget)
        self.frameMain.setGeometry(QtCore.QRect(10, 10, 1260, 581))
        self.frameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMain.setObjectName("frameMain")
        self.frameDrawer = QtWidgets.QFrame(self.frameMain)
        self.frameDrawer.setGeometry(QtCore.QRect(220, 80, 770, 491))
        self.frameDrawer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDrawer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDrawer.setObjectName("frameDrawer")
        self.widgetDrawer = Draw(self.frameDrawer)
        self.widgetDrawer.setGeometry(QtCore.QRect(10, 10, 750, 471))
        self.widgetDrawer.setStyleSheet("background-color: \'#3d3d3d\'")
        self.widgetDrawer.setObjectName("widgetDrawer")
        self.buttonAddObject = QtWidgets.QPushButton(self.frameMain)
        self.buttonAddObject.setGeometry(QtCore.QRect(220, 28, 50, 30))
        self.buttonAddObject.setStyleSheet("")
        self.buttonAddObject.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.icons_prefix + "plus.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAddObject.setIcon(icon)
        self.buttonAddObject.setObjectName("buttonAddObject")
        self.buttonAddObject.clicked.connect(self.triggerAddObject)

        self.buttonDeleteObject = QtWidgets.QPushButton(self.frameMain)
        self.buttonDeleteObject.setGeometry(QtCore.QRect(280, 28, 50, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.icons_prefix + "trash-can.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDeleteObject.setIcon(icon)
        self.buttonDeleteObject.setObjectName("buttonDeleteObject")
        self.buttonDeleteObject.clicked.connect(self.triggerDeleteObject)
        self.labelCoordinates = QtWidgets.QLabel(self.frameMain)
        self.labelCoordinates.setGeometry(QtCore.QRect(460, 20, 171, 40))
        self.labelCoordinates.setObjectName("labelCoordinates")
        self.widgetDrawer.newPoint.connect(lambda p: self.labelCoordinates.setText(
            'Coordinates: ( %d : %d )' % (p.x(), p.y())))
        self.frameInformations = QtWidgets.QFrame(self.frameMain)
        self.frameInformations.setGeometry(QtCore.QRect(1000, 10, 250, 280))
        self.frameInformations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInformations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInformations.setObjectName("frameInformations")
        self.widget = QtWidgets.QWidget(self.frameInformations)
        self.widget.setGeometry(QtCore.QRect(10, 10, 231, 261))
        self.widget.setObjectName("widget")



        self.ClippingWidget = QWidget(self.widget)
        self.ClippingWidget.setObjectName(u"ClippingWidget")
        self.ClippingWidget.setGeometry(QRect(0, 0, 221, 131))
        self.ClippingWidget.setStyleSheet(u"background: #ddffee")
        linhass = QButtonGroup(self.ClippingWidget)
        self.labelLineAlgorithm = QLabel(self.ClippingWidget)
        self.labelLineAlgorithm.setObjectName(u"labelLineAlgorithm")
        self.labelLineAlgorithm.setGeometry(QRect(25, 22, 120, 16))
        self.labelPolygonAlgorithm = QLabel(self.ClippingWidget)
        self.labelPolygonAlgorithm.setObjectName(u"labelPolygonAlgorithm")
        self.labelPolygonAlgorithm.setGeometry(QRect(25, 84, 120, 16))
        self.radioButtonCohen = QRadioButton(self.ClippingWidget)
        self.radioButtonCohen.setObjectName(u"radioButtonCohen")
        self.radioButtonCohen.setGeometry(QRect(55, 42, 120, 20))
        self.radioButtonCohen.setChecked(True)
        self.radioButtonCohen.clicked.connect(self.toggleLineAlgorithm)
        self.radioButtonLiang = QRadioButton(self.ClippingWidget)
        self.radioButtonLiang.setObjectName(u"radioButtonLiang")
        self.radioButtonLiang.setGeometry(QRect(55, 62, 120, 20))
        self.radioButtonLiang.setChecked(True)
        self.radioButtonLiang.clicked.connect(self.toggleLineAlgorithm)
        self.checkBoxEnableClipping = QCheckBox(self.ClippingWidget)
        self.checkBoxEnableClipping.setObjectName(u"checkBoxEnableClipping")
        self.checkBoxEnableClipping.setGeometry(QRect(55, 0, 120, 20))
        self.radioButtonWeiler = QRadioButton(self.ClippingWidget)
        self.radioButtonWeiler.setObjectName(u"radioButtonWeiler")
        self.radioButtonWeiler.setGeometry(QRect(55, 104, 120, 20))
        self.radioButtonWeiler.setChecked(True)
        self.radioButtonWeiler.clicked.connect(lambda: self.radioButtonWeiler.setChecked(True))
        linhass.addButton(self.radioButtonCohen)
        linhass.addButton(self.radioButtonLiang)









        self.labelTranslation = QtWidgets.QLabel(self.widget)
        self.labelTranslation.setGeometry(QtCore.QRect(20, 10, 200, 16))
        self.labelTranslation.setObjectName("labelTranslation")
        self.labelRotation = QtWidgets.QLabel(self.widget)
        self.labelRotation.setGeometry(QtCore.QRect(20, 40, 200, 16))
        self.labelRotation.setObjectName("labelRotation")
        self.labelScale = QtWidgets.QLabel(self.widget)
        self.labelScale.setGeometry(QtCore.QRect(20, 70, 200, 16))
        self.labelScale.setObjectName("labelScale")
        self.labelWindowCoordinates = QtWidgets.QLabel(self.widget)
        self.labelWindowCoordinates.setGeometry(QtCore.QRect(20, 100, 200, 16))
        self.labelWindowCoordinates.setObjectName("labelWindowCoordinates")
        ###############################
        self.labelTranslation.hide()
        self.labelRotation.hide()
        self.labelScale.hide()
        self.labelWindowCoordinates.hide()
        ###############################
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(0, 180, 220, 80))
        self.listWidget.setObjectName("listWidget")
        self.buttonApply = QtWidgets.QPushButton(self.widget)
        self.buttonApply.setGeometry(QtCore.QRect(150, 140, 70, 27))
        self.buttonApply.setObjectName("buttonApply")
        self.buttonApply.clicked.connect(self.applyTransformOperations)
        self.buttonUndo = QtWidgets.QPushButton(self.widget)
        self.buttonUndo.setGeometry(QtCore.QRect(0, 140, 70, 27))
        self.buttonUndo.setObjectName("buttonUndo")
        self.buttonUndo.clicked.connect(self.undoAddOnHistory)
        self.treeWidget = QtWidgets.QTreeWidget(self.frameMain)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 200, 561))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "ID")
        font = QtGui.QFont()
        font.setBold(True)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.headerItem().setText(1, "Type")
        font = QtGui.QFont()
        font.setBold(True)
        self.treeWidget.headerItem().setFont(1, font)
        self.treeWidget.headerItem().setText(2, "Coordinates")
        font = QtGui.QFont()
        font.setBold(True)
        self.treeWidget.headerItem().setFont(2, font)
        self.treeWidget.setColumnWidth(0, 55)
        self.treeWidget.setColumnWidth(1, 60)
        self.treeWidget.itemClicked.connect(self.onItemClick)
        self.treeWidget.setIndentation(18)
        # self.treeWidget.setAlternatingRowColors(True)
        self.frameTransformations = QtWidgets.QFrame(self.frameMain)
        self.frameTransformations.setGeometry(
            QtCore.QRect(1000, 300, 250, 271))
        self.frameTransformations.setAutoFillBackground(False)
        self.frameTransformations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTransformations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTransformations.setObjectName("frameTransformations")
        self.widgetTrasformations = QtWidgets.QWidget(
            self.frameTransformations)
        self.widgetTrasformations.setGeometry(QtCore.QRect(10, 10, 230, 250))
        self.widgetTrasformations.setStyleSheet("")
        self.widgetTrasformations.setObjectName("widgetTrasformations")
        self.buttonRotateLeft = QtWidgets.QPushButton(
            self.widgetTrasformations)
        self.buttonRotateLeft.setGeometry(QtCore.QRect(30, 40, 50, 30))
        self.buttonRotateLeft.setStyleSheet("")
        self.buttonRotateLeft.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.icons_prefix +
                        "rotate-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRotateLeft.setIcon(icon1)
        self.buttonRotateLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttonRotateLeft.setCheckable(False)
        self.buttonRotateLeft.setAutoExclusive(False)
        self.buttonRotateLeft.setObjectName("buttonRotateLeft")
        self.buttonRotateLeft.clicked.connect(self.buttonRotateLeftAction)

        self.buttonRotateRight = QtWidgets.QPushButton(
            self.widgetTrasformations)
        self.buttonRotateRight.setGeometry(QtCore.QRect(150, 40, 50, 30))
        self.buttonRotateRight.setStyleSheet("")
        self.buttonRotateRight.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            self.icons_prefix + "rotate-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRotateRight.setIcon(icon2)
        self.buttonRotateRight.setIconSize(QtCore.QSize(24, 24))
        self.buttonRotateRight.setCheckable(False)
        self.buttonRotateRight.setAutoExclusive(False)
        self.buttonRotateRight.setObjectName("buttonRotateRight")
        self.buttonRotateRight.clicked.connect(self.buttonRotateRightAction)

        self.buttonUp = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonUp.setGeometry(QtCore.QRect(90, 40, 50, 30))
        self.buttonUp.setStyleSheet("")
        self.buttonUp.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.icons_prefix + "up-arrow.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUp.setIcon(icon3)
        self.buttonUp.setIconSize(QtCore.QSize(24, 24))
        self.buttonUp.setCheckable(False)
        self.buttonUp.setAutoExclusive(False)
        self.buttonUp.setObjectName("buttonUp")
        self.buttonUp.clicked.connect(self.buttonUpAction)
        
        self.buttonDown = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonDown.setGeometry(QtCore.QRect(90, 120, 50, 30))
        self.buttonDown.setStyleSheet("")
        self.buttonDown.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.icons_prefix +
                        "down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDown.setIcon(icon4)
        self.buttonDown.setIconSize(QtCore.QSize(24, 24))
        self.buttonDown.setCheckable(False)
        self.buttonDown.setAutoExclusive(False)
        self.buttonDown.setObjectName("buttonDown")
        self.buttonDown.clicked.connect(self.buttonDownAction)

        self.buttonLeft = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonLeft.setGeometry(QtCore.QRect(30, 80, 50, 30))
        self.buttonLeft.setStyleSheet("")
        self.buttonLeft.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(self.icons_prefix +
                        "left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLeft.setIcon(icon5)
        self.buttonLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttonLeft.setCheckable(False)
        self.buttonLeft.setAutoExclusive(False)
        self.buttonLeft.setObjectName("buttonLeft")
        self.buttonLeft.clicked.connect(self.buttonLeftAction)

        self.buttonRight = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonRight.setGeometry(QtCore.QRect(150, 80, 50, 30))
        self.buttonRight.setStyleSheet("")
        self.buttonRight.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(self.icons_prefix +
                        "right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRight.setIcon(icon6)
        self.buttonRight.setIconSize(QtCore.QSize(24, 24))
        self.buttonRight.setCheckable(False)
        self.buttonRight.setAutoExclusive(False)
        self.buttonRight.setObjectName("buttonRight")
        self.buttonRight.clicked.connect(self.buttonRightAction)

        self.spinBoxRotateStepSize = QtWidgets.QSpinBox(
            self.widgetTrasformations)
        self.spinBoxRotateStepSize.setValue(10)
        self.spinBoxRotateStepSize.setGeometry(QtCore.QRect(150, 190, 42, 25))
        self.spinBoxRotateStepSize.setObjectName("spinBoxRotateStepSize")
        self.labelMoveRotate = QtWidgets.QLabel(self.widgetTrasformations)
        self.labelMoveRotate.setGeometry(QtCore.QRect(60, 10, 111, 20))
        self.labelMoveRotate.setObjectName("labelMoveRotate")
        self.spinBoxTranslateStepSize = QtWidgets.QSpinBox(
            self.widgetTrasformations)
        self.spinBoxTranslateStepSize.setGeometry(
            QtCore.QRect(150, 160, 42, 25))
        self.spinBoxTranslateStepSize.setObjectName("spinBoxTranslateStepSize")
        self.spinBoxTranslateStepSize.setValue(1)
        self.labelTranslateStepSize = QtWidgets.QLabel(
            self.widgetTrasformations)
        self.labelTranslateStepSize.setGeometry(QtCore.QRect(30, 160, 100, 20))
        self.labelTranslateStepSize.setObjectName("labelTranslateStepSize")
        self.labelRotateStepSize = QtWidgets.QLabel(self.widgetTrasformations)
        self.labelRotateStepSize.setGeometry(QtCore.QRect(30, 190, 100, 20))
        self.labelRotateStepSize.setObjectName("labelRotateStepSize")
        self.buttonHome = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonHome.setGeometry(QtCore.QRect(90, 80, 50, 30))
        self.buttonHome.setStyleSheet("")
        self.buttonHome.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(self.icons_prefix + "home.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonHome.setIcon(icon7)
        self.buttonHome.setIconSize(QtCore.QSize(24, 24))
        self.buttonHome.setCheckable(False)
        self.buttonHome.setAutoExclusive(False)
        self.buttonHome.setObjectName("buttonHome")
        self.buttonHome.clicked.connect(self.buttonHomeAction)

        self.buttonZoomIn = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonZoomIn.setGeometry(QtCore.QRect(150, 120, 50, 30))
        self.buttonZoomIn.setStyleSheet("")
        self.buttonZoomIn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(self.icons_prefix + "zoom-in.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonZoomIn.setIcon(icon8)
        self.buttonZoomIn.setIconSize(QtCore.QSize(24, 24))
        self.buttonZoomIn.setCheckable(False)
        self.buttonZoomIn.setAutoExclusive(False)
        self.buttonZoomIn.setObjectName("buttonZoomIn")
        self.buttonZoomIn.clicked.connect(self.buttonZoomInAction)
        self.buttonZoomOut = QtWidgets.QPushButton(self.widgetTrasformations)
        self.buttonZoomOut.setGeometry(QtCore.QRect(30, 120, 50, 30))
        self.buttonZoomOut.setStyleSheet("")
        self.buttonZoomOut.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(self.icons_prefix + "zoom-out.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonZoomOut.setIcon(icon9)
        self.buttonZoomOut.setIconSize(QtCore.QSize(24, 24))
        self.buttonZoomOut.setCheckable(False)
        self.buttonZoomOut.setAutoExclusive(False)
        self.buttonZoomOut.setObjectName("buttonZoomOut")
        self.buttonZoomOut.clicked.connect(self.buttonZoomOutAction)

        self.radioButtonWindow = QtWidgets.QRadioButton(
            self.widgetTrasformations)
        self.radioButtonWindow.setGeometry(QtCore.QRect(130, 220, 89, 20))
        self.radioButtonWindow.setObjectName("radioButtonWindow")
        self.radioButtonWindow.setChecked(True)
        self.radioButtonWindow.clicked.connect(self.toggle)
        self.radioButtonObjects = QtWidgets.QRadioButton(
            self.widgetTrasformations)
        self.radioButtonObjects.setGeometry(QtCore.QRect(30, 220, 90, 20))
        self.radioButtonObjects.setObjectName("radioButtonObjects")
        self.radioButtonObjects.clicked.connect(self.toggle)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
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
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionExport.triggered.connect(self.exportViewportCoordinates)
        self.actionAbout.triggered.connect(self.triggerAbout)
        # retirar dps
        #self.openFile(self.debug)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Viewport Visualizer"))
       # self.buttonSaveXml.setText(_translate("MainWindow", "Save XML"))
        self.labelLineAlgorithm.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Line Algorithm</span></p></body></html>", None))
        self.labelPolygonAlgorithm.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Polygon Algorithm</span></p></body></html>", None))
        self.radioButtonCohen.setText(QCoreApplication.translate("MainWindow", u"Cohen\u2013Sutherland", None))
        self.radioButtonLiang.setText(QCoreApplication.translate("MainWindow", u"Liang\u2013Barsky", None))
        self.checkBoxEnableClipping.setText(QCoreApplication.translate("MainWindow", u"Enable Clipping", None))
        self.radioButtonWeiler.setText(QCoreApplication.translate("MainWindow", u"Weiler\u2013Atherton", None))
        self.labelCoordinates.setText(_translate("MainWindow", "coordinates:"))
        self.labelTranslation.setText(_translate("MainWindow", "Translation"))
        self.labelRotation.setText(_translate("MainWindow", "Rotation"))
        self.labelScale.setText(_translate("MainWindow", "Scale"))
        self.labelWindowCoordinates.setText(
            _translate("MainWindow", "Window Coordinates"))
        self.buttonApply.setText(_translate("MainWindow", "Apply"))
        self.buttonUndo.setText(_translate("MainWindow", "Undo"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "ID"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Type"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Coordinates"))
        self.labelMoveRotate.setText(
            _translate("MainWindow", "Move/Rotate/Scale"))
        self.labelTranslateStepSize.setText(
            _translate("MainWindow", "Traslation step size"))
        self.labelRotateStepSize.setText(
            _translate("MainWindow", "Rotation step size"))
        self.radioButtonWindow.setText(_translate("MainWindow", "Window"))
        self.radioButtonObjects.setText(_translate("MainWindow", "Objects"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save Display File as"))
        self.actionExport.setText(_translate("MainWindow", "Export Viewport Coordinates"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setShortcut(_translate("MainWindow", "ctrl+o"))
        self.actionSave.setShortcut(_translate("MainWindow", "ctrl+s"))
        self.actionExport.setShortcut(_translate("MainWindow", "ctrl+d"))


    def toggleLineAlgorithm(self):
        if self.radioButtonCohen.isChecked():
            self.lineAlgorithm = 0
        elif self.radioButtonLiang.isChecked():
            self.lineAlgorithm = 1

    def exportViewportCoordinates(self):
        print('exported')
        # for x in self.viewPortPointsCoordinates:
        #     print(x)
        # for x in self.viewPortLinesCoordinates:
        #     print(x.teste())
        # for x in self.viewPortPolygonsCoordinates:
        #     print(x)
        # return 
        pathFilename = self.saveFileDialog('Output Viewport Coordinates')
        if pathFilename is None:
            return
        xml = XmlWriter(pathFilename)
        # print(self.viewPortPointsCoordinates)
        # print(self.viewPortLinesCoordinates)
        # print(self.viewPortPolygonsCoordinates)
        xml.write(self.viewPortPointsCoordinates, self.viewPortLinesCoordinates, self.viewPortPolygonsCoordinates)


    def triggerDeleteObject(self):
        if self.treeWidget.currentItem() is None:
            return
        #print('trigged')
        index, objType = self.getCurrentObject()
        #print('index: ', index, 'type: ', objType)
        if objType == 'Point':
            self.displayFilePointsCoordinates.pop(index)
        elif objType == 'Line':
            self.displayFileLinesCoordinates.pop(index)
        elif objType == 'Polygon':
            self.displayFilePolygonsCoordinates.pop(index)
        #print(self.displayFilePolygonsCoordinates)
        self.treeWidget.clear()
        self.fillObjectsList(self.displayFilePolygonsCoordinates)
        self.fillObjectsList(self.displayFileLinesCoordinates)
        self.fillObjectsList(self.displayFilePointsCoordinates)
        self.widgetDrawer.erase()
        self.fillDrawerWidget(self.window, self.viewport, self.displayFilePointsCoordinates,
                              self.displayFileLinesCoordinates, self.displayFilePolygonsCoordinates)
    def toggle(self):
        #self.buttonHome.setEnabled(not self.radioButtonWindow.isChecked())
        if self.radioButtonWindow.isChecked():
            self.buttonHome.show()
        else:
            self.buttonHome.hide()

    def calculatePPC(self):
        conversor, window = WorldToPPC(self.window)

        oc = ObjectsConvert()
        self.viewPortPointsCoordinates = oc.convert(
            self.displayFilePointsCoordinates, conversor)
        self.viewPortLinesCoordinates = oc.convert(
            self.displayFileLinesCoordinates, conversor)
        self.viewPortPolygonsCoordinates = oc.convert(
            self.displayFilePolygonsCoordinates, conversor)
        self.widgetDrawer.erase()

        newWindow = window
        self.fillDrawerWidget(newWindow, self.viewport, self.viewPortPointsCoordinates,
                              self.viewPortLinesCoordinates, self.viewPortPolygonsCoordinates)

    def updateLabelTranslation(self, x: string, y: string):
        self.labelTranslation.setText(
            f'Translation: ({x}, {y})')

    def updateLabelRotation(self, degree: string):
        self.labelRotation.setText(
            f'Rotation: {degree}')

    def zoomWindowAction(self, sx, sy):
        #print(self.window.getScale())
        self.window.addScale(sx, sy)
        #print(self.window.getScale())
        a = self.window.getScale()
        x = str(a[0])
        y = str(a[1])
        self.updateLabelTranslation(x, y)
        self.calculatePPC()

    def zoomObjectAction(self, sx, sy):
        item = self.treeWidget.currentItem()
        src, index = self.getParentPath(item).split('-')
        index = int(index)
        if src == 'p':
            newPoint = self.displayFilePointsCoordinates[index].scale(
                sx, sy)
            self.displayFilePointsCoordinates[index] = newPoint
        elif src == 'l':
            newPoint = self.displayFileLinesCoordinates[index].scale(
                sx, sy)
            self.displayFileLinesCoordinates[index] = newPoint
        elif src == 'pl':
            newPoint = self.displayFilePolygonsCoordinates[index].scale(
                sx, sy)
            self.displayFilePolygonsCoordinates[index] = newPoint
        self.calculatePPC()

    def buttonZoomOutAction(self):
        if self.radioButtonWindow.isChecked():
            sx, sy = 1.1, 1.1
            self.zoomWindowAction(sx, sy)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
            sx, sy = 0.9, 0.9
            #self.zoomObjectAction(sx, sy)
            self.addOnHistory(['Scale', (sx, sy)])

    def buttonZoomInAction(self):
        if self.radioButtonWindow.isChecked():
            sx, sy = 0.9, 0.9
            self.zoomWindowAction(sx, sy)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
            sx, sy = 1.1, 1.1
            #self.zoomObjectAction(sx, sy)
            self.addOnHistory(['Scale', (sx, sy)])

    def getParentPath(self, item):
        def getParent(item, outstring):
            if item.parent() is None:
                return outstring
            outstring = item.parent().text(0) + '/' + outstring
            return getParent(item.parent(), outstring)
        output = getParent(item, item.text(0))
        return output

    def translateWindowAction(self, tx, ty):
        self.window.addTranslation(tx, ty)
        winTranslation = self.window.getTranslation()
        x = str(winTranslation[0])
        y = str(winTranslation[1])
        self.updateLabelTranslation(x, y)
        self.calculatePPC()

    def getCurrentObject(self):
        item = self.treeWidget.currentItem()
        src, index = self.getParentPath(item).split('-')
        index = int(index)
        if src == 'p':
            src = 'Point'
        elif src == 'l':
            src = 'Line'
        elif src == 'pl':
            src = 'Polygon'
        return index, src

    def translateObjectAction(self, tx, ty):
        item = self.treeWidget.currentItem()
        src, index = self.getParentPath(item).split('-')
        index = int(index)
        if src == 'p':
            newPoint = self.displayFilePointsCoordinates[index].translate(
                tx, ty)
            self.displayFilePointsCoordinates[index] = newPoint
        elif src == 'l':
            newPoint = self.displayFileLinesCoordinates[index].translate(
                tx, ty)
            self.displayFileLinesCoordinates[index] = newPoint
        elif src == 'pl':
            newPoint = self.displayFilePolygonsCoordinates[index].translate(
                tx, ty)
            self.displayFilePolygonsCoordinates[index] = newPoint
        self.calculatePPC()

    def buttonUpAction(self):
        x = 0
        y = self.spinBoxTranslateStepSize.value()

        if self.radioButtonWindow.isChecked():
            self.translateWindowAction(x, y)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
            #self.translateObjectAction(x, y)
            self.addOnHistory(['Translation', (x, y)])

    def buttonDownAction(self):
        x = 0
        y = -self.spinBoxTranslateStepSize.value()

        if self.radioButtonWindow.isChecked():
            self.translateWindowAction(x, y)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
           # self.translateObjectAction(x, y)
            self.addOnHistory(['Translation', (x, y)])

    def buttonLeftAction(self):
        x = -self.spinBoxTranslateStepSize.value()
        y = 0

        if self.radioButtonWindow.isChecked():
            self.translateWindowAction(x, y)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
            #self.translateObjectAction(x, y)
            self.addOnHistory(['Translation', (x, y)])

    def buttonRightAction(self):
        x = self.spinBoxTranslateStepSize.value()
        y = 0

        if self.radioButtonWindow.isChecked():
            self.translateWindowAction(x, y)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
            #self.translateObjectAction(x, y)
            self.addOnHistory(['Translation', (x, y)])

    def buttonHomeAction(self):
        # self.window.resetTransformation()
        a = self.window.getTranslation()
        x = str(a[0])
        y = str(a[1])
        self.updateLabelTranslation(x, y)
        self.window = copy.deepcopy(self.backupWindow)
        self.calculatePPC()

    def rotateWindowAction(self, theta):
        self.window.addRotation(theta)
        b = self.window.getRotation()
        theta = str(b)
        self.updateLabelRotation(theta)
        self.calculatePPC()


    def rotateObjectAction(self, theta):
        item = self.treeWidget.currentItem()
        src, index = self.getParentPath(item).split('-')
        index = int(index)
        if src == 'p':
            newPoint = self.displayFilePointsCoordinates[index].rotate(
                theta)
            self.displayFilePointsCoordinates[index] = newPoint
        elif src == 'l':
            newPoint = self.displayFileLinesCoordinates[index].rotate(
                theta)
            self.displayFileLinesCoordinates[index] = newPoint
        elif src == 'pl':
            newPoint = self.displayFilePolygonsCoordinates[index].rotate(
                theta)
            self.displayFilePolygonsCoordinates[index] = newPoint
        self.calculatePPC()

    def buttonRotateLeftAction(self):
        theta = self.spinBoxRotateStepSize.value()
        if self.radioButtonWindow.isChecked():
            self.rotateWindowAction(theta)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
           # self.rotateObjectAction(theta)
            self.addOnHistory(['Rotation', (theta)])

    def buttonRotateRightAction(self):
        theta = -self.spinBoxRotateStepSize.value()
        if self.radioButtonWindow.isChecked():
            self.rotateWindowAction(theta)
        elif self.radioButtonObjects.isChecked() and self.treeWidget.selectedItems():
           # self.rotateObjectAction(theta)
            self.addOnHistory(['Rotation', (theta)])

    def triggerAbout(self):
        my_dialog = QDialog(MainWindow)
        my_dialog.setWindowTitle("About")
        # my_dialog.setWindowModality(Qt.ApplicationModal)
        my_dialog.setGeometry(0, 0, 400, 300)
        my_dialog.move(MainWindow.rect().center())
        # my_dialog.move(QDesktopWidget().availableGeometry().center().x() - self.frameGeometry().center().x() * 0.5, QDesktopWidget().availableGeometry().center().y() - self.frameGeometry().center().y() * 0.5)
        self.labelNameAbout = QtWidgets.QLabel(my_dialog)

        # self.labelNameAbout.setGeometry(QtCore.QRect(10, 270, 101, 20))
        self.labelNameAbout.setObjectName("labelNameAbout")
        self.labelNameAbout.move(my_dialog.rect().center())
        self.labelNameAbout.setText(
            u"<html><head/><body><p><a href=\"https://github.com/Jefesonk1\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>")
        self.labelNameAbout.setOpenExternalLinks(True)
        # self.labelNameAbout.setText("Feito por: Jefeson Martins Delazeri\n email: jefesonk1@outlook.com \n github: https://github.com/Jefesonk1")
        my_dialog.exec_()  #

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self.centralwidget, "Open", "", "XLM Files (*.xml)", options=options)
        if fileName:
            return fileName

    def saveFileDialog(self, defaultFileName='output.xml'):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileDialog = QFileDialog(self, 'Projects')
        fileDialog.setAttribute(Qt.WA_QuitOnClose, False)
        fileName, _ = fileDialog.getSaveFileName(
            self.centralwidget, "Save", defaultFileName, "XML Files (*.xml)", options=options )
        if fileName:
            return fileName

    def saveFile(self):
        pathFilename = self.saveFileDialog()
        if pathFilename is None:
            return
        if (pathFilename):
            xml = XmlWriter(pathFilename)
           # print(self.viewPortPointsCoordinates)
            # xml.write(self.viewPortPointsCoordinates,
                    #   self.viewPortLinesCoordinates, self.viewPortPolygonsCoordinates)
            #self.buttonSaveXml.hide()
            #self.buttonSaveXml.setText("Saved")
            xml.write(self.displayFilePointsCoordinates,self.displayFileLinesCoordinates, self.displayFilePolygonsCoordinates)

    def fillObjectsList(self, objectList: Union[Point, Line, Polygon]):

        if isinstance(objectList, list):
            if objectList and isinstance(objectList[0], Polygon):
                ##print('Polygon')
                items = []
                for index, polygon in enumerate(objectList):
                    item = None
                    objectId = 'pl-'+str(index)
                    item = QTreeWidgetItem([objectId, 'Polygon'])
                    # #print(polygon, index)
                    for indexPoint, point in enumerate(polygon.getPolygon()):
                        xCoord = str(point.getPoint()[0])
                        yCoord = str(point.getPoint()[1])
                        coord = '('+xCoord+', '+yCoord+')'
                        pointId = 'p'+str(indexPoint)
                        child = QTreeWidgetItem([pointId, 'Point', coord])
                        item.addChild(child)
                    items.append(item)
                self.treeWidget.insertTopLevelItems(0, items)
            elif objectList and isinstance(objectList[0], Line):
                ##print('Line')
                items = []
                for index, key in enumerate(objectList):
                    p1, p2 = key.getLine()
                    xCoordp1 = str(p1.getPoint()[0])
                    yCoordp1 = str(p1.getPoint()[1])
                    xCoordp2 = str(p2.getPoint()[0])
                    yCoordp2 = str(p2.getPoint()[1])
                    coord = '('+xCoordp1+', '+yCoordp1+')'
                    coord2 = '('+xCoordp2+', '+yCoordp2+')'
                    objectId = 'l-'+str(index)
                    item = QTreeWidgetItem([objectId, 'Line'])
                    child = QTreeWidgetItem(['p1', 'Point', coord])
                    child2 = QTreeWidgetItem(['p2', 'Point', coord2])
                    item.addChild(child)
                    item.addChild(child2)
                    items.append(item)
                self.treeWidget.insertTopLevelItems(0, items)

            elif objectList and isinstance(objectList[0], Point):
               # #print('Point')
                items = []
                for index, key in enumerate(objectList):
                    xCoord = str(key.getPoint()[0])
                    yCoord = str(key.getPoint()[1])
                    coord = '('+xCoord+', '+yCoord+')'
                    objectId = 'p-'+str(index)
                    item = QTreeWidgetItem([objectId, 'Point', coord])
                    items.append(item)
                self.treeWidget.insertTopLevelItems(0, items)

    def clearObjectsList(self):
        self.treeWidget.clear()

    def clearHistory(self):
        self.listWidget.clear()


    def initLabels(self):
        a = self.window.getTranslation()
        x = str(a[0])
        y = str(a[1])
        self.labelTranslation.setText(
            'Translation     (' + '<b>X axis:  </b> ' + x + ', ' + '<b>Y axis:  </b> ' + y+')')

        b = self.window.getRotation()
        theta = str(b)
        self.labelRotation.setText(
            'Rotation     (' + '<b>Theta:  </b> ' + theta + 'º)')

        c = self.window.getScale()
        x = str(c[0])
        y = str(c[1])
        self.labelScale.setText(
            'Scale     (' + '<b>X axis:  </b> ' + x + ', ' + '<b>Y axis:  </b> ' + y + ')')

        d = self.window.getCoordinates()
        xMin = str(d[0][0])
        yMin = str(d[0][1])
        xMax = str(d[1][0])
        yMax = str(d[1][1])
        self.labelWindowCoordinates.setText(
            '<b>wMin:</b> (' + xMin + ', ' + yMin + ') <b>wMax:</b> (' + xMax + ', ' + yMax + ')')

    def fillDrawerWidget(self, window: Window, viewport: Viewport, points: Point, lines: Line, polygons: Polygon):
        conversor = WindowToViewport()
        lineClipper = CohenSutherlandWrapper()
        pointClipper = PointClipperWrapper()
        polygonClipper = WeilerAthertonWrapper()

        _viewPortPointsCoordinates = []
        _viewPortLinesCoordinates = []
        _viewPortPolygonsCoordinates = []

        self.initLabels()
        viewportWidth = int(viewport.getXvMax() -
                            viewport.getXvMin())
        viewportHeight = int(viewport.getYvMax() -
                             viewport.getYvMin())

        print(viewportWidth, viewportHeight)
        self.widgetDrawer.setGeometry(QtCore.QRect(
            0,0, viewportWidth+20, viewportHeight+20))
        # print('vpw',viewportWidth)
        for point in points:
            convertedPoint = pointClipper.clipPoint(point, window)
            if convertedPoint is not None:
                convertedPoint = conversor.convertToViewport(
                    convertedPoint, window, viewport)
                _viewPortPointsCoordinates.append(convertedPoint)
            print(convertedPoint)

        for line in lines:
            convertedLine = lineClipper.clipLine(line, window)
            if convertedLine is not None:
                convertedLine = conversor.convertToViewport(
                    convertedLine, window, viewport)
                _viewPortLinesCoordinates.append(convertedLine)

        for polygon in polygons:
           # print(polygon)
            #print("#####################")
           # print(polygon)
            convertedPolygon = polygonClipper.clipPolygon(polygon, window)
            #convertedPolygon = None
            # for pol in convertedPolygon:
            #     print(pol)
            # print(convertedPolygon)
           # print('before',convertedPolygon)
            print(convertedPolygon)
            #exit(0)
            if convertedPolygon != None:
                print('nunca')
                for pol in convertedPolygon:
                    cp = conversor.convertToViewport(
                        pol, window, viewport)
                    _viewPortPolygonsCoordinates.append(cp)
            # else:
            #     cp = conversor.convertToViewport(
            #             polygon, window, viewport)
            #     _viewPortPolygonsCoordinates.append(cp)
            # print('after', _viewPortPolygonsCoordinates[0])

        for ponto in _viewPortPointsCoordinates:
            self.widgetDrawer.drawPoint(ponto)

        for line in _viewPortLinesCoordinates:
            self.widgetDrawer.drawLine(line)

        for polygon in _viewPortPolygonsCoordinates:
            self.widgetDrawer.drawPolygon(polygon)

        self.viewPortPointsCoordinates = _viewPortPointsCoordinates
        self.viewPortLinesCoordinates = _viewPortLinesCoordinates
        self.viewPortPolygonsCoordinates = _viewPortPolygonsCoordinates

    def openFile(self, debug=False):
        if debug:
            filePath = 'entrada.xml'
        else:
            filePath = self.openFileNameDialog()
            if filePath is None:
                return
        xmlReader = XmlReader(filePath)
        self.window = xmlReader.getWindow()
        self.backupWindow = copy.deepcopy(self.window)
        self.viewport = xmlReader.getViewport()
        #print("###", self.viewport.getXvMin(), self.viewport.getXvMax(), self.viewport.getYvMin(), self.viewport.getYvMax())
        self.displayFilePointsCoordinates = xmlReader.getPontos()
        self.displayFileLinesCoordinates = xmlReader.getRetas()
        self.displayFilePolygonsCoordinates = xmlReader.getPoligonos()
        self.fillDrawerWidget(self.window, self.viewport, self.displayFilePointsCoordinates,
                              self.displayFileLinesCoordinates, self.displayFilePolygonsCoordinates)
        self.fillObjectsList(self.displayFilePolygonsCoordinates)
        self.fillObjectsList(self.displayFileLinesCoordinates)
        self.fillObjectsList(self.displayFilePointsCoordinates)

    def triggerAddObject(self):
        #Dialog = QtWidgets.QDialog(MainWindow)
        ui = Ui_Dialog(self)
        ui.exec_()
        #print(self.buttonLeft)

    def addOnHistory(self, object):
        #operation, direction, value = object
        listWidgetItem = QListWidgetItem(''.join(str(object)))
        self.listWidget.addItem(listWidgetItem)

        self.history.append(object)

    def undoAddOnHistory(self):
        if self.history != []:
            self.history.pop()
            self.listWidget.takeItem(self.listWidget.count()-1)

    def onItemClick(self):
        item = self.treeWidget.currentItem()
        # #print(item.text(0))

    def applyTransformOperations(self):
        if self.history != []:
            newList = []
            for item in self.history:
                operation, value = item
                if(newList == []):
                    newList.append(item)
                else:
                    if(newList[-1][0] == operation):
                        if(operation == 'Rotation'):
                            newList[-1] = (operation, newList[-1][1] + value)
                        elif operation == 'Translation':
                            tupla = newList[-1][1]
                            a = tupla[0]+value[0]
                            b = tupla[1]+value[1]
                            newList[-1] = (operation, (a, b))
                        elif operation == 'Scale':
                            tupla = newList[-1][1]
                            a = tupla[0]*value[0]
                            b = tupla[1]*value[1]
                            newList[-1] = (operation, (a, b))
                    else:
                        newList.append(item)

            idxToPop = []
            for idx, element in enumerate(newList):
                operation, value = element
                ##print(operation, value, idx)
                if(operation == 'Translation' and value == (0,0)):
                    #print('entrou translation')
                    #newList.pop(idx)
                    idxToPop.append(idx)
                elif(operation == 'Rotation' and value == 0):
                    #print('entrou rotation')
                    #newList.pop(idx)
                    idxToPop.append(idx)
                elif(operation == 'Scale' and value == (1,1)):
                    #print('entrou scale')
                    #newList.pop(idx)
                    idxToPop.append(idx)
            self.clearHistory()
            self.history.clear()
            newList = [ newList[i] for i in range(len(newList)) if i not in idxToPop ]
            #print(newList)
            index, objType = self.getCurrentObject()
            if objType == 'Polygon':
                objectt = self.displayFilePolygonsCoordinates[index]
                xCenter, yCenter = objectt.getGeometricCenter().getPoint()
                t = Transformations()
                toOrigin = t.translade(-xCenter, -yCenter)
                backToCenter = t.translade(xCenter, yCenter)
                xx = toOrigin
                tx, ty = 0, 0
                for operation, value in newList:
                    #tirar translation pq vai dar ruim
                    if(operation == 'Translation'):
                    #xx = t.translade(value[0], value[1]) @ xx 
                        tx, ty = tx + value[0], ty + value[1]
                    elif(operation == 'Rotation'):
                        xx = t.rotate(np.radians(value)) @ xx
                    elif(operation == 'Scale'):
                        xx = t.scale(value[0], value[1]) @ xx
                xx = backToCenter @ xx
                xx = t.translade(tx, ty) @ xx
                #print(xx)
                points = []
                for point in objectt.getPolygon():
                    x,y = point.getPoint()
                    newPoint = calculate(x,y, xx)
                    points.append(Point(newPoint))
                aaa = Polygon(*points)
                self.displayFilePolygonsCoordinates[index] = aaa
                self.calculatePPC()
                return
            elif objType == 'Line':
                objectt = self.displayFileLinesCoordinates[index]
                xCenter, yCenter = objectt.getGeometricCenter().getPoint()
                t = Transformations()
                toOrigin = t.translade(-xCenter, -yCenter)
                backToCenter = t.translade(xCenter, yCenter)
                xx = toOrigin
                tx, ty = 0, 0
                for operation, value in newList:
                    #tirar translation pq vai dar ruim
                    if(operation == 'Translation'):
                    #xx = t.translade(value[0], value[1]) @ xx 
                        tx, ty = tx + value[0], ty + value[1]
                    elif(operation == 'Rotation'):
                        xx = t.rotate(np.radians(value)) @ xx
                    elif(operation == 'Scale'):
                        xx = t.scale(value[0], value[1]) @ xx
                xx = backToCenter @ xx
                xx = t.translade(tx, ty) @ xx
                #print(xx)
                points = []
                for point in objectt.getLine():
                    x,y = point.getPoint()
                    newPoint = calculate(x,y, xx)
                    points.append(Point(newPoint))
                aaa = Line(*points)
                self.displayFileLinesCoordinates[index] = aaa
                self.calculatePPC()
                return
            elif objType == 'Point':
                objectt = self.displayFilePointsCoordinates[index]
                xCenter, yCenter = objectt.getPoint()
                t = Transformations()
                toOrigin = t.translade(-xCenter, -yCenter)
                backToCenter = t.translade(xCenter, yCenter)
                xx = toOrigin
                tx, ty = 0, 0
                for operation, value in newList:
                    #tirar translation pq vai dar ruim
                    if(operation == 'Translation'):
                    #xx = t.translade(value[0], value[1]) @ xx 
                        tx, ty = tx + value[0], ty + value[1]
                    elif(operation == 'Rotation'):
                        xx = t.rotate(np.radians(value)) @ xx
                    elif(operation == 'Scale'):
                        xx = t.scale(value[0], value[1]) @ xx
                xx = backToCenter @ xx
                xx = t.translade(tx, ty) @ xx
                #print(xx)
                points = []
                
                x,y = xCenter, yCenter
                newPoint = calculate(x,y, xx)
                aaa = Point((newPoint))
                self.displayFilePointsCoordinates[index] = aaa
                self.calculatePPC()
                return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    _Font = QFont("Tahoma", 8)
    QApplication.setFont(_Font)
    MainWindow = QtWidgets.QMainWindow()
    styleFile = QFile("style.qss")
    styleFile.open(QFile.ReadOnly)
    stylesheet = QTextStream(styleFile).readAll()
    app.setStyleSheet(stylesheet)

    ui = Ui_MainWindow(MainWindow, debug=False)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
