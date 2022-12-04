from elements.Window import Window
from elements.Transformations import Transformations
from elements.ObjectsConvert import ObjectsConvert
from utils.calculate import calculate
import math


def WorldToPPC(window: Window):
    tx, ty = window.getTranslation()
    theta = window.getRotation()
    sx, sy = window.getScale()
    wt = Transformations()
    xmin, ymin = window.getMinCoordinates()
    xmax, ymax = window.getMaxCoordinates()
    scale = wt.scale(sx, sy)
    transladeToOrigin = wt.translade(-xmin, -ymin)
    transladeToOriginalPosition = wt.translade(xmin+tx, ymin+ty)
    rotate = wt.rotate(math.radians(theta))
    transformationMatrix = transladeToOriginalPosition @ (
        rotate @ (scale @ transladeToOrigin))
    xMin, yMin = calculate(xmin, ymin, transformationMatrix)
    xMax, yMax = calculate(xmax, ymax, transformationMatrix)
    xCenter, yCenter = ((xMin + xMax) / 2, (yMin + yMax) / 2)
    finalTransformationMatrix = wt.rotate(
        math.radians(-theta)) @ wt.translade(-xCenter, -yCenter)
    xwMin, ywMin = calculate(xMin, yMin, finalTransformationMatrix)
    xwMax, ywMax = calculate(xMax, yMax, finalTransformationMatrix)
    return finalTransformationMatrix, Window(xwMin, xwMax, ywMin, ywMax)