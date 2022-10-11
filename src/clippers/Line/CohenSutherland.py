# #from Window import Window
# from timeit import default_timer as timer
# start = timer()

LEFT_EDGE = 0x1
RIGHT_EDGE = 0x2
BOTTOM_EDGE = 0x4
TOP_EDGE = 0x8


class CohenSutherland:
    # def __init__(self):
    def ACCEPT(self, a, b):
        return (not (a | b))  # accepts when region code of both points are 0

    def REJECT(self, a, b):
        return (a & b)  # rejects when they have a common bit position set to 1

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
            elif (self.REJECT(code1, code2)):  # Totalmente fora
                break
            else:  # some segment lies within the rectangle
                x, y = None, None
                codeOut = code1
                if (self.INSIDE(code1)):
                    codeOut = code2
                if codeOut & TOP_EDGE:
                    x = x1 + (x2 - x1) * (ywMax - y1) / (y2 - y1)
                    y = ywMax
                elif codeOut & BOTTOM_EDGE:
                    # point is below the clip rectangle
                    x = x1 + (x2 - x1) * (ywMin - y1) / (y2 - y1)
                    y = ywMin
                elif codeOut & RIGHT_EDGE:
                    # point is to the right of the clip rectangle
                    y = y1 + (y2 - y1) * (xwMax - x1) / (x2 - x1)
                    x = xwMax
                elif codeOut & LEFT_EDGE:
                    # point is to the left of the clip rectangle
                    y = y1 + (y2 - y1) * (xwMin - x1) / (x2 - x1)
                    x = xwMin
                    # Now intersection point x, y is found
                    # We replace point outside clipping rectangle
                    # by intersection point
                if codeOut == code1:
                    x1 = x
                    y1 = y
                    code1 = self.encode(x1, y1, xwMin, ywMin, xwMax, ywMax)
                else:
                    x2 = x
                    y2 = y
                    code2 = self.encode(x2, y2, xwMin, ywMin, xwMax, ywMax)
        if accept:
            print(f"Line accepted from {x1:.2f}, {y1:.2f} to {x2:.2f}, {y2:.2f}")
            return x1, y1, x2, y2
            #print(f"{x1:.2f}")
        else:
            print("Line rejected")
            return None


a = CohenSutherland()

p1 = (12,30)
p2 = (16,4)
wmin = (10,10)
wmax = (20,20)


a.clipLine(*p1, *p2, *wmin, *wmax)
# end = timer()
# print(end - start) # Time in seconds, e.g. 5.38091952400282