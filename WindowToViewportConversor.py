class WindowToViewportConversor:
  def transform(self, pontos, limitesJanelaX, limitesJanelaY, limitesViewPortX , limitesViewPortY):
    Xw, Yw = pontos
    XwMin, XwMax = limitesJanelaX
    YwMin, YwMax = limitesJanelaY
    XvpMin,XvpMax = limitesViewPortX
    YvpMin, YvpMax = limitesViewPortY
    Xvp = ((Xw - XwMin) / (XwMax - XwMin)) * (XvpMax - XvpMin)
    Yvp = (1 - (Yw - YwMin) / (YwMax - YwMin)) * (YvpMax - YvpMin)
    return (Xvp, Yvp)