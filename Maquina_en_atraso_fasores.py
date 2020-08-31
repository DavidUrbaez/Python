from Fasor_Graph import vector_r_theta,Vector
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

angle_V_I = -20
Ra = 2
Xa = 4

Va = vector_r_theta(6, 0, 'r')
Ia = vector_r_theta(2, angle_V_I, 'c')
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



plt.gca().set_aspect(1)
plt.gca().spines['right'].set_visible(False)  # se quita la linea de abajo
plt.gca().spines['top'].set_visible(False)  # Se quita la linea de arriba
plt.show()
