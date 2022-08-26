class Trans:
  def __init__(self):
    self.teste = 2

  def transformar(self, pontos, limitesJanelaX, limitesJanelaY, limitesViewPortX , limitesViewPortY):
    Xw, Yw = pontos
    XwMin, XwMax = limitesJanelaX
    YwMin, YwMax = limitesJanelaY
    XvpMin,XvpMax = limitesViewPortX
    YvpMin, YvpMax = limitesViewPortY
    Xvp = ((Xw - XwMin) / (XwMax - XwMin)) * (XvpMax - XvpMin)
    Yvp = (1 - (Yw - YwMin) / (YwMax - YwMin)) * (YvpMax - YvpMin)
    return (Xvp, Yvp)

teste = Trans()

pontos = (0,2)
limitesJanelaX = (0,10)
limitesJanelaY = (0,10)
limitesViewPortX = (10,630)
limitesViewPortY = (10, 470)

print(teste.transformar(pontos, limitesJanelaX, limitesJanelaY, limitesViewPortX, limitesViewPortY))
