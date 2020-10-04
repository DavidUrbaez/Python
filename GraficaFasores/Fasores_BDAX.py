from Graficar_Fasores import vector_r_theta, Vector
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


def R2P(x):
    return np.abs(x), np.angle(x) * 180 / np.pi, 'Grados'


Va = Vector(13800/np.sqrt(3))

theta = np.arccos(0.85)

S = Vector(82974 * 10 ** 3 * np.exp(theta * 1j))

Ia = Vector(np.conj(S.z / (3*Va.z)))

Xbase = (abs(13800) ** 2) / abs(82974*10**3)

Ra = 0.0028 * (123 + 234.5) / (20 + 234.5)

Rf = 0.156 * (125 + 234.5) / (20 + 234.5)


Xd = Xbase * 2.40

Ea=Va+Ia*Ra+Ia*Xd*1j

VRa = (Ia * Ra)
VXs=(Ia*Xd*1j)


VRa.color = 'y'
VXs.color='r'
Ea.color = 'c'
Ia.color = 'g'

VXs>>Va

for vector_name in ['Va', 'VXs', 'Ea', 'Ia']:
    vector = eval(vector_name)
    plt.text(vector.zorigen.real + vector.z.real * 0.5 + 0.1, vector.zorigen.imag + vector.z.imag * 0.5 + 0.1, vector_name)
    vector.plot()

plt.xlim(-1000, 20000)

plt.ylim(-4000, 20000)

plt.gca().set_aspect(1)
plt.gca().spines['right'].set_visible(False)  # se quita la linea de abajo
plt.gca().spines['top'].set_visible(False)  # Se quita la linea de arriba
plt.show()

print('Regulación: ' + str(((abs(Ea.z) - Va.m) / Va.m) * 100) + '%')
