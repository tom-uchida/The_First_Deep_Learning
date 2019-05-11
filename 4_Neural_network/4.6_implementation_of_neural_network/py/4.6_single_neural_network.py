import numpy as np
import matplotlib.pyplot as plt

# x,y coords
X = np.arange(-1.0, 1.0, 0.2)
Y = np.arange(-1.0, 1.0, 0.2)

# Grid
grid = np.zeros( (10,10) )

# weight
w_x = 2.5
w_y = 3.0

# bias
b = 0.1

# Calc the neurons in each grid square
for j in range(10):
    for i in range(10):

        # Sum of input and weight products + bias
        u = X[i]*w_x + Y[j]*w_y + b

        # Store output in grid
        y = 1/(1+np.exp(-u))
        grid[j][i] = y
    # end for
# end for

# Show grid
plt.imshow(grid, "gray", vmin=0.0, vmax=1.0)
plt.colorbar()
plt.show()