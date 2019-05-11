import numpy as np
import matplotlib.pyplot as plt

def ReLU_function(x):
    return np.where(x<=0, 0, x)

x = np.linspace(-5, 5)
y = ReLU_function(x)

plt.plot(x, y)
plt.show()