from Graficar_Fasores import vector_r_theta, Vector
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


def R2P(x):
    return np.abs(x), np.angle(x) * 180 / np.pi, 'Grados'


Va = Vector(13800 / np.sqrt(3))

theta = np.arccos(0.9)

S = Vector(45700 * 10 ** 3 * np.exp(theta * 1j))

Ia = Vector(np.conj(S.z / (3 * Va.z)))

Xbase = (abs(13800) ** 2) / abs(45700 * 10 ** 3)

Ra = 0.02465 * (115 + 234.5) / (20 + 234.5)

Rf = 0.05915 * (115 + 234.5) / (20 + 234.5)

Xq = Xbase * 0.66
Xd = Xbase * 1.02

delta = np.arctan((Ia.m * Xq * np.cos(theta) - Ia.m * Ra * np.sin(theta)) /
                  (Va.m + Ia.m * (Ra * np.cos(theta) + Xq * np.sin(theta))))

Id = Vector(Ia.m * np.sin(delta + theta) * np.exp((delta - np.pi / 2) * 1j))
Iq = Vector(Ia.m * np.cos(delta + theta) * np.exp(delta * 1j))

VRa = (Ia * Ra)
VXd = (Id * Xd * 1j)
VXq = (Iq * Xq * 1j)
Ea = Va + VRa + VXd + VXq

VRa.color = 'y'
VXd.color = 'c'
VXq.color = 'g'
Ea.color = 'r'

VXq >> (VXd >> (VRa >> Va))
# Ia2 = Ia * 2
Ia.color = 'g'
for vector_name in ['Va', 'VRa', 'VXd', 'VXq', 'Ea', 'Ia']:
    vector = eval(vector_name)
    plt.text(vector.zorigen.real + vector.z.real * 0.5 + 0.1, vector.zorigen.imag + vector.z.imag * 0.5 + 0.1, vector_name)
    vector.plot()

plt.xlim(-1000, 20000)

plt.ylim(-4000, 8000)

plt.gca().set_aspect(1)
plt.gca().spines['right'].set_visible(False)  # se quita la linea de abajo
plt.gca().spines['top'].set_visible(False)  # Se quita la linea de arriba

#First limit
xc = np.arange(Va.m, Ea.m)
yc=np.sqrt(Ea.m**2-xc**2)
plt.plot(xc,yc)

#second limit
xc2 = np.arange(Va.m-(Ea-Va).m,Ea.z.real)
yc2=np.sqrt((Ea-Va).m**2-(Va.m-xc2)**2)

plt.plot(xc2,yc2)

plt.show()

print('Regulación: ' + str(((abs(Ea.z) - Va.m) / Va.m) * 100) + '%')
