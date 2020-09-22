from Fasor_Graph import vector_r_theta,Vector
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')


def R2P(x):
    return np.abs(x), np.angle(x)*180/np.pi ,'Grados'


Va= 13800

S=16200*10**3*np.exp(np.arccos(0.85)*1j)

Ia=np.conj(S/(np.sqrt(3)*Va))

Xbase=(Va**2)/abs(S)

Ra=0.0517*(120+234.5)/(75+234.5)

Rf=0.0901*(120+234.5)/(75+234.5)

theta=np.arccos(0.85)

Xq=Xbase*0.678
Xd=Xbase*1.02

delta=np.arctan((abs(Ia)*Xq*np.cos(theta)-abs(Ia)*Ra*np.sin(theta))/(Va+abs(Ia)*(Ra*np.cos(theta)+Xq*np.sin(theta))))

Id=abs(Ia)*np.sin(delta+theta)*np.exp((delta-np.pi/2)*1j)
Iq=abs(Ia)*np.cos(delta+theta)*np.exp((delta)*1j)

Va=Vector(x=13800,y=0)
Va.plot()

plt.xlim(0,20000)
plt.show()




Va = vector_r_theta(r=6, theta=0,color= 'r')
Ia = vector_r_theta(r=2, theta=angle_V_I,color= 'c')
VRA = Ia * Ra
VXA = Ia * Xa * 1j
VRA.color, VXA.color = 'y', 'b'

Ea = Va + VRA + VXA

VRA >> Va
VXA >> VRA

for vector_name in ['Va', 'VRA', 'VXA', 'Ea', 'Ia']:
    vector = eval(vector_name)
    plt.text(vector.xorigen + vector.x * 0.5 + 0.1, vector.yorigen + vector.y * 0.5 + 0.1, vector_name)
    vector.plot()

plt.xlim(-1, 15)
plt.ylim(-5, 8)

# (Ia * 4j).plot()

plt.gca().set_aspect(1)
plt.gca().spines['right'].set_visible(False)  # se quita la linea de abajo
plt.gca().spines['top'].set_visible(False)  # Se quita la linea de arriba
plt.show()
