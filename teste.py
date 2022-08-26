from XmlReader import *
from Trans import *



teste = XmlReader('entrada.xml')
windowSize = teste.getWindowSize()
viewPortSize = teste.getViewportSize()
pontos = teste.getPontos()
retas = teste.getRetas()
poligonos = teste.getPoligonos()
print(viewPortSize,' \n', windowSize, '\n', pontos)
print("##")

trans = Trans()

limitesJanelaX = (windowSize[0][0], windowSize[1][0])
limitesJanelaY = (windowSize[0][1], windowSize[1][1])
limitesViewPortX = (viewPortSize[0][0], viewPortSize[1][0])
limitesViewPortY = (viewPortSize[0][1], viewPortSize[1][1])

for ponto in pontos:
  result = trans.transformar(ponto, limitesJanelaX, limitesJanelaY, limitesViewPortX, limitesViewPortY )
  print(result)

for reta in retas:
  for ponto in reta:
    result = trans.transformar(ponto, limitesJanelaX, limitesJanelaY, limitesViewPortX, limitesViewPortY )
    #print(result)

for poligono in poligonos:
  for ponto in poligono:
    result = trans.transformar(ponto, limitesJanelaX, limitesJanelaY, limitesViewPortX, limitesViewPortY )
    #print(result)

