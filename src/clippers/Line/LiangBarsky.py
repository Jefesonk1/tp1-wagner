class LiangBarsky:

    def clipLine(self, x0, y0, x1, y1, xwmin, ywmin, xwmax, ywmax):
        p1 = -1 * (x1 - x0)
        p2 = x1 - x0
        p3 = -1 * (y1 - y0)
        p4 = y1 - y0

        q1 = x0 - xwmin
        q2 = xwmax - x0
        q3 = y0 - ywmin
        q4 = ywmax - y0

        posarr = [1]
        negarr = [0]

        if (p1 == 0 and q1 < 0) or (p2 == 0 and
                                    q2 < 0) or (p3 == 0 and
                                                q3 < 0) or (p4 == 0 and q4 < 0):
            return None

        if (p1 != 0):
            r1 = q1 / p1
            r2 = q2 / p2
            if (p1 < 0):
                negarr.append(r1)
                posarr.append(r2)
            else:
                negarr.append(r2)
                posarr.append(r1)
        if (p3 != 0):
            r3 = q3 / p3
            r4 = q4 / p4
            if (p3 < 0):
                negarr.append(r3)
                posarr.append(r4)
            else:
                negarr.append(r4)
                posarr.append(r3)

        rn1 = max(negarr)
        rn2 = min(posarr)

        if (rn1 > rn2):
            return None

        xn1 = x0 + p2 * rn1
        yn1 = y0 + p4 * rn1

        xn2 = x0 + p2 * rn2
        yn2 = y0 + p4 * rn2

        return xn1, yn1, xn2, yn2