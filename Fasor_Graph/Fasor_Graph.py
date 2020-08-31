import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

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

    def __mul__(self, k):
        mul = Vector(self.xorigen, self.yorigen, self.x, self.y, self.color)
        mul.x = ((self.x + self.y * 1j) * k).real
        mul.y = ((self.x + self.y * 1j) * k).imag
        return mul

    def plot(self):
        '''
        Se grafica el vector en cuestion
        '''
        plt.quiver(self.xorigen, self.yorigen, self.x, self.y, angles='xy', scale_units='xy', scale=1, color=self.color)


def vector_r_theta(r, theta, color='k'):
    return Vector(0, 0, x=r * cos(theta), y=r * sin(theta), color=color)



