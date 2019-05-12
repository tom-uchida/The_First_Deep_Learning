import numpy as np
import matplotlib.pyplot as plt

# x,y coords
X = np.arange(-1.0, 1.0, 0.2)
Y = np.arange(-1.0, 1.0, 0.2)

# Grid
grid = np.zeros( (10,10) )

# Weight
w_inp_mid = np.array([[4.0, 4.0], 
                      [4.0, 4.0]])   # Middle-layer：2×2
w_mid_out = np.array([[1.0], 
                      [-1.0]])       # Output-layer：2×1

# Bias
b_inp_mid = np.array([3.0, -3.0])   # Middle
b_mid_out = np.array([0.1])         # Output

# Middle layer
def middle_layer(x, w, b):
    u = np.dot(x, w) + b
    return 1/(1+np.exp(-u))

# Output layer
def output_layer(x, w, b):
    u = np.dot(x, w) + b
    return u


# Calc the neurons in each grid square
for j in range(10):
    for i in range(10):

        # Forward propagation
        inp = np.array( [X[i], Y[j]] )
        mid = middle_layer(inp, w_inp_mid, b_inp_mid)
        out = output_layer(mid, w_mid_out, b_mid_out)

        # Store output of NN in grid
        grid[j][i] = out[0]

    # end for
# end for

# Show grid
plt.imshow(grid, "gray", vmin=0.0, vmax=1.0)
plt.colorbar()
plt.show()