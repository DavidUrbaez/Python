import numpy as np
import matplotlib.pyplot as plt




class vector():
    def __init__(self, xorigen, yorigen, x=None, y=None):
        self.xorigen = xorigen
        self.yorigen = yorigen
        self.x, self.y = x, y
        if x is not None and y is not None:
            plt.quiver(xorigen, yorigen, x, y, angles='xy', scale_units='xy', scale=1)

    def __add__(self, other):
        self.xorigen = other.xorigen + other.x
        self.yorigen = other.yorigen + other.y
        plt.quiver(self.xorigen, self.yorigen, self.x, self.y, angles='xy', scale_units='xy', scale=1)


a = vector(1, 1, x=5, y=0)
b = vector(1, 1, x=0, y=5)
a + b
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
