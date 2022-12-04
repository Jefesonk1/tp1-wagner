class PointClipper:
    def clipPoint(self, x, y, xwMin, ywMin, xwMax, ywMax):
        if((xwMin <= x and x <= xwMax) and (ywMin <= y and y <= ywMax)):
            return x,y
        else:
            return None
