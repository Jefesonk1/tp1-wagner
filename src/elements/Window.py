from elements.Transformations import *


class Window:
    def __init__(self, xwMin, xwMax, ywMin, ywMax):
        self.xwMin = xwMin
        self.xwMax = xwMax
        self.ywMin = ywMin
        self.ywMax = ywMax
        self.tx = 0
        self.ty = 0
        self.sx = 1
        self.sy = 1
        self.degree = 0

    def setXwMin(self, xwMin):
        self.xwMin = xwMin

    def setXwMax(self, xwMax):
        self.xwMax = xwMax

    def setYwMin(self, ywMin):
        self.ywMin = ywMin

    def setYwMax(self, ywMax):
        self.ywMax = ywMax

    def getXwMin(self):
        return self.xwMin

    def getXwMax(self):
        return self.xwMax

    def getYwMin(self):
        return self.ywMin

    def getYwMax(self):
        return self.ywMax

    def getCoordinates(self):
        return [(self.xwMin, self.ywMin), (self.xwMax, self.ywMax)]

    def getMinCoordinates(self):
        return self.xwMin, self.ywMin

    def getMaxCoordinates(self):
        return self.xwMax, self.ywMax

    def getCenter(self):
        return (self.xwMin + self.xwMax) / 2, (self.ywMin + self.ywMax) / 2

    def addRotation(self, degree):
        self.degree += degree
        if (self.degree >= 360):
            self.degree = self.degree % 360
        if (self.degree <= -360):
            self.degree = (self.degree * -1) % 360

    def getRotation(self):
        return self.degree

    def addTranslation(self, tx, ty):
        self.tx += tx
        self.ty += ty

    def addScale(self, sx, sy):
        self.sx *= sx
        self.sy *= sy

    def getTranslation(self):
        return self.tx, self.ty

    def getScale(self):
        return self.sx, self.sy