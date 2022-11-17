from itertools import cycle


class WeilerAtherton:

    def winMinMaxToPolygon(self, xwmin, ywmin, xwmax, ywmax):
        x0 = xwmin, ywmin
        x1 = xwmin, ywmax

        x2 = x1
        x3 = xwmax, ywmax

        x4 = x3
        x5 = ywmax, ywmin

        x6 = x5
        x7 = x0

        pol = [[x0, x1], [x2, x3], [x4, x5], [x6, x7]]
        return pol

    def ordernarTupla(self, tupla, primeiro=True, decrescente=False):
        if primeiro:
            return sorted(
                tupla, key=lambda t: (t[0], t[1]), reverse=decrescente)
        return sorted(tupla, key=lambda t: (t[1], t[0]), reverse=decrescente)

    def liangBarsky(self, x0, y0, x1, y1, xwmin, ywmin, xwmax, ywmax):
        intercept = True
        interceptCount = 0

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
            return False, False, 0, 0, 0, 0, 'false'

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
            return False, False, 0, 0, 0, 0, 'false'

        xn1 = x0 + p2 * rn1
        yn1 = y0 + p4 * rn1

        xn2 = x0 + p2 * rn2
        yn2 = y0 + p4 * rn2

        if (rn1 == 0 and rn2 == 1):
            intercept = False
        elif (rn1 != 0 and rn2 != 1):
            intercept = True
            interceptCount = 2
        else:
            intercept = True
            interceptCount = 1

        return intercept, interceptCount, xn1, yn1, xn2, yn2

    def clipPolygon(self, pol, xwmin, ywmin, xwmax, ywmax):
        print(pol)
        #exit(0)
        l1 = []
        l2 = []
        interceptPoints = []
        quantidadeEntradas = 0

        for line in pol:
            p1, p2 = line
            result = self.liangBarsky(*p1, *p2, xwmin, ywmin, xwmax, ywmax)
            interceptCount = result[1]

            if interceptCount == 0:
                l1.append(p1)

            if interceptCount == 2:
                quantidadeEntradas += 2
                l1.append(p1)
                l1.append(
                    (result[2], result[3], 'fora pra dentro', 'not visited'))
                l1.append((result[4], result[5], 'dentro pra fora'))
                interceptPoints.append(
                    (result[2], result[3], 'fora pra dentro'))
                interceptPoints.append(
                    (result[4], result[5], 'dentro pra fora'))

            if interceptCount == 1:
                x0 = p1[0]
                y0 = p1[1]
                if (x0 >= xwmin and x0 <= xwmax) and (y0 >= ywmin and
                                                      y0 <= ywmax):
                    quantidadeEntradas += 1
                    l1.append(p1)
                    l1.append((result[4], result[5], 'dentro pra fora'))
                    interceptPoints.append(
                        (result[4], result[5], 'dentro pra fora'))
                else:
                    quantidadeEntradas += 1
                    l1.append(p1)
                    l1.append((result[2], result[3], 'fora pra dentro',
                               'not visited'))
                    interceptPoints.append(
                        (result[2], result[3], 'fora pra dentro'))

        polygonWin = self.winMinMaxToPolygon(xwmin, ywmin, xwmax, ywmax)
        coluna = 1

        for reta in polygonWin:
            indiceInserido = None
            achouIgual = False
            for x in l2:
                if x[:2] == reta[0]:
                    achouIgual = True

            if not achouIgual:
                l2.append(reta[0])
                indiceInserido = len(l2) - 1
            if (coluna == 1):
                interceptPoints = self.ordernarTupla(
                    interceptPoints, primeiro=False)  # y menor primeiro
                for ponto in interceptPoints[:]:
                    if (reta[0][0] == ponto[0]):
                        print(ponto)
                        if ponto[:2] == l2[indiceInserido]:
                            l2.pop(indiceInserido)
                        interceptPoints.remove(ponto)
                        l2.append(ponto)

            if (coluna == 2):
                interceptPoints = self.ordernarTupla(interceptPoints, primeiro=True)
                for ponto in interceptPoints[:]:
                    if (reta[0][1] == ponto[1]):
                        if ponto[:2] == l2[indiceInserido]:
                            l2.pop(indiceInserido)
                        interceptPoints.remove(ponto)
                        l2.append(ponto)

            if (coluna == 3):
                interceptPoints = self.ordernarTupla(
                    interceptPoints, primeiro=False, decrescente=True)
                for ponto in interceptPoints[:]:
                    if (reta[1][0] == ponto[0]):
                        if ponto[:2] == l2[indiceInserido]:
                            l2.pop(indiceInserido)
                        interceptPoints.remove(ponto)
                        l2.append(ponto)

            if (coluna == 4):
                interceptPoints = self.ordernarTupla(
                    interceptPoints, primeiro=True, decrescente=True)
                for ponto in interceptPoints[:]:
                    if (reta[1][1] == ponto[1]):
                        if ponto[:2] == l2[indiceInserido]:
                            l2.pop(indiceInserido)
                        interceptPoints.remove(ponto)
                        l2.append(ponto)

            coluna += 1

        # print("\n######l1######\n")
        # for x in l1:
        # 	print(x)
        # print("\n######l2######\n")
        # for x in l2:
        # 	print(x)
        # print("\n######end######\n")

        l1_circular = cycle(l1)
        l2_circular = cycle(l2)

        newPol = [[]]
        quantidadeVisitados = 0
        quantidadeEntradas = int(quantidadeEntradas / 2)
        currentPolygonIndex = 0
        intercecao = None
        breaked = False
        primeiraRodada = True
        condicao = None
        visited = []
        entrada = None
        breakedByEnd = False

        for ponto in l1_circular:
            breaked = False
            breakedByEnd = False

            if quantidadeVisitados == quantidadeEntradas:
                if newPol[-1] == []:
                    newPol.pop()
                if newPol == []:
                    return None
                return newPol
                break

            entradaNaoVisitada = len(
                ponto
            ) == 4 and ponto not in visited and ponto[2] == 'fora pra dentro'
            saida = len(ponto) == 3 and ponto[2] == 'dentro pra fora'

            if primeiraRodada:
                condicao = entradaNaoVisitada
                entrada = ponto[:-1]
            else:
                condicao = (entradaNaoVisitada or saida)

            if intercecao == None and len(ponto) != 4:
                continue

            if intercecao != None:
                if ponto[:-1] != intercecao:
                    continue

            if condicao:
                primeiraRodada = False
                newPol[currentPolygonIndex].append(ponto[:2])

                if (len(ponto) == 4):
                    visited.append(ponto)
                    quantidadeVisitados += 1

                while (True):
                    if breakedByEnd:
                        break
                    if breaked:
                        break

                    proximo = next(l1_circular)
                    newPol[currentPolygonIndex].append(proximo[:2])

                    if len(proximo) == 3:
                        for x in l2_circular:

                            continua = True

                            if x == proximo:
                                while (True):
                                    proximo2 = next(l2_circular)
                                    if proximo2 == entrada:
                                        primeiraRodada = True
                                        currentPolygonIndex += 1
                                        newPol.append([])
                                        breakedByEnd = True
                                        intercecao = None
                                        breaked = False
                                        primeiraRodada = True
                                        condicao = None
                                        entrada = None
                                        break
                                    elif len(proximo2) != 3:
                                        newPol[currentPolygonIndex].append(
                                            proximo2[:2])
                                    if (len(proximo2) == 3):
                                        intercecao = proximo2
                                        continua = False
                                        break
                                if breakedByEnd:
                                    break
                            if not continua:
                                breaked = True
                                break
