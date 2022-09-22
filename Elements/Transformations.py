import numpy as np


class Transformations:
    def translade(self, tx, ty):
        return np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

    def rotate(self, degree):
        cos = np.cos(degree)
        sin = np.sin(degree)
        return np.array([[cos,-sin,0],[sin, cos,0],[0,0,1]])

    def scale(self, sx, sy):
        return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
