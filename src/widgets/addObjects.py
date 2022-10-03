from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from elements.Geometry import Line, Point, Polygon

class Ui_Dialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.points = []
        self.lines = []
        self.polygons = []

    def setupUi(self, Dialog):
        # Dialog.setObjectName("Dialog")
        # Dialog.resize(670, 280)
        self.roiGroups = {}
        self.treeWidget = QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QRect(10, 10, 200, 261))
        self.treeWidget.setObjectName("treeWidget")
        font = QFont()
        font.setBold(True)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.headerItem().setFont(1, font)
        self.treeWidget.headerItem().setFont(2, font)
        self.treeWidget.setColumnWidth(0, 55)
        self.treeWidget.setColumnWidth(1, 60)
        self.frame = QFrame(Dialog)
        self.frame.setGeometry(QRect(220, 10, 440, 260))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textInstructions = QTextBrowser(self.frame)
        self.textInstructions.setGeometry(QRect(10, 50, 400, 71))
        self.textInstructions.setObjectName("textInstructions")
        self.input = QLineEdit(self.frame)
        self.input.setGeometry(QRect(10, 170, 310, 27))
        self.input.setPlaceholderText("")
        self.input.setObjectName("input")
        self.buttonDelete = QPushButton(self.frame)
        self.buttonDelete.setGeometry(QRect(10, 10, 75, 27))
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonDelete.hide()
        self.buttonAdd = QPushButton(self.frame)
        self.buttonAdd.setGeometry(QRect(330, 170, 75, 27))
        self.buttonAdd.setObjectName("buttonAdd")
        self.buttonAdd.clicked.connect(self.addObject)
        self.buttonSaveAll = QPushButton(self.frame)
        self.buttonSaveAll.setGeometry(QRect(245, 220, 75, 27))
        self.buttonSaveAll.setObjectName("buttonSaveAll")
        self.buttonSaveAll.clicked.connect(self.handleSave)
        self.buttonCancel = QPushButton(self.frame)
        self.buttonCancel.setGeometry(QRect(330, 220, 75, 27))
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonCancel.clicked.connect(self.handleCancel)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(10, 150, 111, 16))
        self.label.setObjectName("label")
        self.frame.raise_()
        self.treeWidget.raise_()

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Object"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "ID"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Type"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "Coordinates"))
        self.textInstructions.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To create a <span style=\" font-weight:700;\">Point</span> -&gt; (x0, y0)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To create a <span style=\" font-weight:700;\">Line</span> -&gt; (x0,y0), (x1,y1)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To create a <span style=\" font-weight:700;\">Polygon</span> -&gt; (x0, y0), (x1, y1), (x2, y2), (xn, yn)</p></body></html>"))
        self.buttonDelete.setText(_translate("Dialog", "Delete"))
        self.buttonAdd.setText(_translate("Dialog", "add"))
        self.buttonSaveAll.setText(_translate("Dialog", "Save all"))
        self.buttonCancel.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Object Coordinates"))

    def fillObjectsList(self, object):
            if isinstance(object, Polygon):
                ##print('Polygon')
                items = []
                item = None
                objectId = 'pl'
                item = QTreeWidgetItem([objectId, 'Polygon'])
                # ##print(polygon, index)
                for indexPoint, point in enumerate(object.getPolygon()):
                    xCoord = str(point.getPoint()[0])
                    yCoord = str(point.getPoint()[1])
                    coord = '('+xCoord+', '+yCoord+')'
                    pointId = 'p'+str(indexPoint)
                    child = QTreeWidgetItem([pointId, 'Point', coord])
                    item.addChild(child)
                items.append(item)
                self.treeWidget.insertTopLevelItems(0, items)
            elif isinstance(object, Line):
                ##print('Line')
                items = []
                p1, p2 = object.getLine()
                xCoordp1 = str(p1.getPoint()[0])
                yCoordp1 = str(p1.getPoint()[1])
                xCoordp2 = str(p2.getPoint()[0])
                yCoordp2 = str(p2.getPoint()[1])
                coord = '('+xCoordp1+', '+yCoordp1+')'
                coord2 = '('+xCoordp2+', '+yCoordp2+')'
                objectId = 'l'
                item = QTreeWidgetItem([objectId, 'Line'])
                child = QTreeWidgetItem(['p1', 'Point', coord])
                child2 = QTreeWidgetItem(['p2', 'Point', coord2])
                item.addChild(child)
                item.addChild(child2)
                items.append(item)
                self.treeWidget.insertTopLevelItems(0, items)

            elif isinstance(object, Point):
                ##print('Point')
                items = []
                xCoord = str(object.getPoint()[0])
                yCoord = str(object.getPoint()[1])
                coord = '('+xCoord+', '+yCoord+')'
                objectId = 'p'
                item = QTreeWidgetItem([objectId, 'Point', coord])
                items.append(item)
                self.treeWidget.insertTopLevelItems(0, items)

    def addObject(self):
        a = self.input.text()
        s = a.replace('(', '').replace(')', '').replace(' ', '').split(',')
        ##print(s)
        if len(s)%2 == 1:
            ##print('invalid input')
            return None
        if(len(s) == 2):
            ##print("Point")
            self.fillObjectsList(Point((float(s[0]), float(s[1]))))
            self.points.append(Point((float(s[0]), float(s[1]))))
        elif(len(s) == 4):
            ##print("Line")
            self.fillObjectsList(Line(Point((float(s[0]), float(s[1]))), Point((float(s[2]), float(s[3])))))
            self.lines.append(Line(Point((float(s[0]), float(s[1]))), Point((float(s[2]), float(s[3])))))
        elif(len(s) > 4):
            ##print("Polygon")
            ##print(s)
            PointList = []
            it_a = iter(s)
            it_b = iter(s[1:])
            for item, next_item in zip(it_a, it_b):
                ##print(item, next_item)
                PointList.append(Point((float(item), float(next_item))))
                try:
                    item = next(it_a)
                    next_item = next(it_b)
                except StopIteration:
                    pass
            ##print(PointList)
            self.polygons.append(Polygon(*PointList))
            self.fillObjectsList(Polygon(*PointList))

    def handleCancel(self):
        self.reject()

    def handleSave(self):
        ##print("save")
        for point in self.points:
            self.parent.displayFilePointsCoordinates.append(point)
        for line in self.lines:
            #print(line)
            self.parent.displayFileLinesCoordinates.append(line)
        for polygon in self.polygons:
            #print(polygon)
            self.parent.displayFilePolygonsCoordinates.append(polygon)

        self.parent.fillDrawerWidget(self.parent.window, self.parent.viewport, self.parent.displayFilePointsCoordinates,self.parent.displayFileLinesCoordinates, self.parent.displayFilePolygonsCoordinates)
        self.parent.clearObjectsList()
        self.parent.fillObjectsList(self.parent.displayFilePolygonsCoordinates)
        self.parent.fillObjectsList(self.parent.displayFileLinesCoordinates)
        self.parent.fillObjectsList(self.parent.displayFilePointsCoordinates)
        self.accept()
