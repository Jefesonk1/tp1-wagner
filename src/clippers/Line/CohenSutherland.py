LEFT_EDGE = 0x1
RIGHT_EDGE = 0x2
BOTTOM_EDGE = 0x4
TOP_EDGE = 0x8

class CohenSutherland:
    def ACCEPT(self, a, b):
        return (not (a | b))

    def REJECT(self, a, b):
        return (a & b)

    def INSIDE(self, a):
        return (not a)

    def encode(self, x, y, xwMin, ywMin, xwMax, ywMax):
        code = 0x00
        if (x < xwMin):
            code = code | LEFT_EDGE
        if (x > xwMax):
            code = code | RIGHT_EDGE
        if (y < ywMin):
            code = code | BOTTOM_EDGE
        if (y > ywMax):
            code = code | TOP_EDGE
        return (code)

    def clipLine(self, x1, y1, x2, y2, xwMin, ywMin, xwMax, ywMax):
        code1 = None
        code2 = None
        accept = False

        while (True):
            code1 = self.encode(x1, y1, xwMin, ywMin, xwMax, ywMax)
            code2 = self.encode(x2, y2, xwMin, ywMin, xwMax, ywMax)
            if (self.ACCEPT(code1, code2)):
                accept = True
                break
            elif (self.REJECT(code1, code2)):
                break
            else:
                x, y = None, None
                codeOut = code1
                if (self.INSIDE(code1)):
                    codeOut = code2
                if codeOut & TOP_EDGE:
                    x = x1 + (x2 - x1) * (ywMax - y1) / (y2 - y1)
                    y = ywMax
                elif codeOut & BOTTOM_EDGE:
                    x = x1 + (x2 - x1) * (ywMin - y1) / (y2 - y1)
                    y = ywMin
                elif codeOut & RIGHT_EDGE:
                    y = y1 + (y2 - y1) * (xwMax - x1) / (x2 - x1)
                    x = xwMax
                elif codeOut & LEFT_EDGE:
                    y = y1 + (y2 - y1) * (xwMin - x1) / (x2 - x1)
                    x = xwMin
                if codeOut == code1:
                    x1 = x
                    y1 = y
                    code1 = self.encode(x1, y1, xwMin, ywMin, xwMax, ywMax)
                else:
                    x2 = x
                    y2 = y
                    code2 = self.encode(x2, y2, xwMin, ywMin, xwMax, ywMax)
        if accept:
            return x1, y1, x2, y2
        else:
            return None