import numpy as np
import matplotlib.pyplot as plt

# Funciones trigonometricas en grados (360)
sin = lambda x: np.sin(x * np.pi / 180)
cos = lambda x: np.cos(x * np.pi / 180)


# Se define la clase de Vector
class Vector:
    def __init__(self, xorigen, yorigen, x=None, y=None, color='k'):
        '''
        Se agregan los parametros del vector
        :param xorigen: coordenada x de la cola del vector
        :param yorigen: coordenada y de la cola del vector
        :param x: coordenada x de la cabeza del vector
        :param y: coordenada y de la cabeza del vector
        :param color: color del vector
        '''
        self.xorigen = xorigen
        self.yorigen = yorigen
        self.x, self.y = x, y
        self.color = color

    def __rshift__(self, other):
        '''
        Funcion que modifica la ubciación espacial del vector si A>>B A la cola de A se mueve a la cabeza de B
        :param other: Vector nuevo de ubicación origen
        :return: Vector con origen desfasado
        '''
        self.xorigen = other.xorigen + other.x
        self.yorigen = other.yorigen + other.y
        return self

    def __add__(self, other, color='g'):
        suma = Vector(self.xorigen, self.yorigen, self.x, self.y, color)
        suma.x = self.x + other.x
        suma.y = self.y + other.y
        return suma

    def __sub__(self, other, color='c'):
        resta = Vector(self.xorigen, self.yorigen, self.x, self.y, color)
        resta.x = self.x - other.x
        resta.y = self.y - other.y
        return resta

    def plot(self):
        '''
        Se grafica el vector en cuestion
        '''
        plt.quiver(self.xorigen, self.yorigen, self.x, self.y, angles='xy', scale_units='xy', scale=1, color=self.color)


def vector_r_theta(r, theta, color='k'):
    return Vector(0, 0, x=r * cos(theta), y=r * sin(theta), color=color)


angle = -30

Va = vector_r_theta(6, 0, 'r')
Ia = vector_r_theta(2, angle, 'c')
VRA = vector_r_theta(3, angle, 'b')
VXA = vector_r_theta(4, angle + 90, 'k')

Ea = Va + VRA + VXA

VRA >> Va
VXA >> VRA

for vector_name in ['Va', 'VRA', 'VXA', 'Ea', 'Ia']:
    vector = eval(vector_name)
    plt.text(vector.xorigen + vector.x * 0.5 + 0.1, vector.yorigen + vector.y * 0.5 + 0.1, vector_name)
    vector.plot()

plt.gca().set_aspect(1)
plt.xlim(-1, 15)
plt.ylim(-10, 10)

# (Ea - VXA).plot()
plt.show()
