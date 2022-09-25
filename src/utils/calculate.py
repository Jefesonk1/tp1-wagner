import numpy as np
def calculate(x, y, matrix):
	coord = matrix @ np.array([x, y, 1])
	return (coord[0], coord[1])