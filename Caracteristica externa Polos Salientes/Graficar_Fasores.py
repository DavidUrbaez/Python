import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Funciones trigonometricas en grados (360)
sin = lambda x: np.sin(x * np.pi / 180)
cos = lambda x: np.cos(x * np.pi / 180)


# Se define la clase de Vector
class Vector:
    def __init__(self, z=0,zorigen=0, color='b'):
        '''
        Se agregan los parametros del vector
        :param xorigen: coordenada x de la cola del vector
        :param yorigen: coordenada y de la cola del vector
        :param x: coordenada x de la cabeza del vector
        :param y: coordenada y de la cabeza del vector
        :param color: color del vector
        '''
        self.zorigen = zorigen
        self.z = z
        self.color = color
        self.m=abs(self.z)

    def __rshift__(self, other):
        '''
        Funcion que modifica la ubciación espacial del vector si A>>B A la cola de A se mueve a la cabeza de B
        :param other: Vector nuevo de ubicación origen
        :return: Vector con origen desfasado
        '''
        self.zorigen = other.zorigen + other.z

        return self

    def __add__(self, other):
        suma = Vector( self.z,self.zorigen)
        suma.z += other.z
        suma.m = abs(suma.z)
        return suma

    def __sub__(self, other):
        resta = Vector(self.z,self.zorigen)
        resta.z -= other.z
        resta.m=abs(resta.z)
        return resta


    def __mul__(self, other):
        mul = Vector(self.z,self.zorigen)
        try:
            mul.z *= other.z
        except:
            mul.z *= other
        mul.m=abs(mul.z)
        return mul

    def __truediv__(self, other):
        div = Vector(self.z, self.zorigen)
        div.z *= other.z
        div.m=abs(div.z)
        return div

    def __repr__(self):
        return str(self.z) +'   -   '+str(abs(self.z))+' ∠ '+str(np.angle(self.z)*180/np.pi)


    def plot(self):
        '''
        Se grafica el vector en cuestion
        '''
        plt.quiver(self.zorigen.real, self.zorigen.imag,
                   self.z.real, self.z.imag,
                   angles='xy', scale_units='xy', scale=1, color=self.color)


def vector_r_theta(r, theta, color='g'):
    return Vector(z=r * np.exp(theta * 1j), color=color)


