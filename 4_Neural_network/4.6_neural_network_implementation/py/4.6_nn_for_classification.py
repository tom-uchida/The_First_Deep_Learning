import numpy as np
import matplotlib.pyplot as plt

# x,y coords
X = np.arange(-1.0, 1.0, 0.1)
Y = np.arange(-1.0, 1.0, 0.1)

# Weight
w_inp_mid = np.array([[1.0, 2.0], 
                      [2.0, 3.0]])  # Middle-layer：2×2
w_mid_out = np.array([[-1.0, 1.0], 
                      [1.0, -1.0]]) # Output-layer：2×2

# Bias
b_inp_mid = np.array([0.3, -0.3])   # Middle
b_mid_out = np.array([0.4, 0.1])    # Output

# Middle layer
def middle_layer(x, w, b):
    u = np.dot(x, w) + b
    return 1/(1+np.exp(-u)) # sigmoid function

# Output layer
def output_layer(x, w, b):
    u = np.dot(x, w) + b
    return np.exp(u)/np.sum(np.exp(u)) # softmax function

# List for storing analysis results
x_1 = []
y_1 = []
x_2 = []
y_2 = []


# Calc the neurons in each grid square
for j in range(20):
    for i in range(20):

        # Forward propagation
        inp = np.array( [X[i], Y[j]] )
        mid = middle_layer(inp, w_inp_mid, b_inp_mid)
        out = output_layer(mid, w_mid_out, b_mid_out)

        # Compare the value of a probability and then classify
        if out[0] > out[1]:
            x_1.append( X[i] )
            y_1.append( Y[j] )
        else:
            x_2.append( X[i] )
            y_2.append( Y[j] )

    # end for
# end for

# Show scatter plot
plt.scatter(x_1, y_1, marker="+")
plt.scatter(x_2, y_2, marker="o")
plt.show()