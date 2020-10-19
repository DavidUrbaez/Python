from Graficar_Fasores import vector_r_theta, Vector
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')


def R2P(x):
    return np.abs(x), np.angle(x) * 180 / np.pi, 'Grados'

Ea_real=13800/np.sqrt(3)


Xbase = (abs(13800) ** 2) / abs(45700 * 10 ** 3)

Ra = 0.02465 * (115 + 234.5) / (20 + 234.5)

Rf = 0.05915 * (115 + 234.5) / (20 + 234.5)

Xq = Xbase * 0.66
Xd = Xbase * 1.02
for theta in [-np.arccos(0.9),-np.arccos(1),np.arccos(0.9)]:

    Va_final=[]
    Ia_final=np.arange(0,1750,10)
    for Ia_mag in Ia_final:
        Ia = Vector(Ia_mag*np.exp(-theta*1j))

        for Va_mag in range(int(1.3*13800/np.sqrt(3)),10,-1):

            Va = Vector(Va_mag)

            delta = np.arctan((Ia.m * Xq * np.cos(theta) - Ia.m * Ra * np.sin(theta)) /
                              (Va.m + Ia.m * (Ra * np.cos(theta) + Xq * np.sin(theta))))

            Id = Vector(Ia.m * np.sin(delta + theta) * np.exp((delta - np.pi / 2) * 1j))
            Iq = Vector(Ia.m * np.cos(delta + theta) * np.exp(delta * 1j))

            VRa = (Ia * Ra)
            VXd = (Id * Xd * 1j)
            VXq = (Iq * Xq * 1j)
            Ea = Va + VRa + VXd + VXq

            if abs(Ea_real-Ea.m)<50:
                break
        Va_final.append(Va.m)

    plt.plot(Ia_final,np.array(Va_final))
plt.text(700, 3000, 'Fp=0.9 Atraso', fontsize=12)
plt.text(1000, 6000, 'Fp=1', fontsize=12)
plt.text(1000, 8000, 'Fp=0.9 Adelanto', fontsize=12)
plt.ylim(0,10000)
plt.xlabel('Ia [A]')
plt.ylabel('Va [V]')
plt.show()