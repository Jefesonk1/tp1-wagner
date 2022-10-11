class PointClipper:
    # def __init__(self, point, window: Window):
    #     self.window = window
    #     self.point = point
    #     self.__clipping()

    def clipPoint(self, x, y, xwMin, ywMin, xwMax, ywMax):
        # xwMin, ywMin, xwMax, ywMax = self.window.getCoordinates()
        # x, y = self.point.getCoordinates()
        if((xwMin <= x and x <= xwMax) and (ywMin <= y and y <= ywMax)):
            # self.point.setClipping(True)
            return x,y
        else:
            # self.point.setClipping(False)
            return None
