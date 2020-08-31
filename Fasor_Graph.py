import numpy as np
import matplotlib.pyplot as plt

sin = lambda x: np.sin(x * np.pi / 180)
cos = lambda x: np.cos(x * np.pi / 180)


class Vector():
    def __init__(self, xorigen, yorigen, x=None, y=None, color='k'):
        self.xorigen = xorigen
        self.yorigen = yorigen
        self.x, self.y = x, y
        self.color = color
        # plt.quiver(xorigen, yorigen, x, y, angles='xy', scale_units='xy', scale=1, color=self.color)

    def __add__(self, other):
        self.xorigen = other.xorigen + other.x
        self.yorigen = other.yorigen + other.y
        return self

    def plot(self):
        plt.quiver(self.xorigen, self.yorigen, self.x, self.y, angles='xy', scale_units='xy', scale=1, color=self.color)


def vector_r_theta(r, theta, color='k'):
    return Vector(0, 0, x=r * cos(theta), y=r * sin(theta), color=color)


Va = vector_r_theta(8, 0, 'r')
Vb = vector_r_theta(8, 120, 'b')
Vc = vector_r_theta(8, 240, 'g')

Vc = Vc + Vb
Va = Va + Vc

for vector_name in ['Va', 'Vb', 'Vc']:
    vector = eval(vector_name)
    plt.text(vector.xorigen + vector.x, vector.yorigen + vector.y, vector_name)
    vector.plot()

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
