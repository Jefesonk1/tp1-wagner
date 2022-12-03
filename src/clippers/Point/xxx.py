# Python3 program to implement
# Window to ViewPort Transformation

# Function for window to viewport transformation
def WindowtoViewport(x_w, y_w, x_wmax, y_wmax,
					x_wmin, y_wmin, x_vmax,
					y_vmax, x_vmin, y_vmin):
							
	# point on viewport
	# calculating Sx and Sy
	sx = (x_vmax - x_vmin) / (x_wmax - x_wmin)
	sy = (y_vmax - y_vmin) / (y_wmax - y_wmin)

	# calculating the point on viewport
	x_v = x_vmin + ((x_w - x_wmin) * sx)
	y_v = y_vmin + ((y_w - y_wmin) * sy)

	print("The point on viewport:(", int(x_v),
								",", int(y_v), ")")

# Driver Code
if __name__ == '__main__':
	
	# boundary values for window
	x_wmax = 10
	y_wmax = 10
	x_wmin = 0
	y_wmin = 0

	# boundary values for viewport
	x_vmax = 630
	y_vmax = 470
	x_vmin = 10
	y_vmin = 10

	# point on window
	x = 1
	y = 1

	WindowtoViewport(x,y, x_wmax, y_wmax,
					x_wmin, y_wmin, x_vmax,
					y_vmax, x_vmin, y_vmin)
	
# This code is contributed by Surendra_Gangwar
