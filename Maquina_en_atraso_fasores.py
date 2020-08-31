from Fasor_Graph import vector_r_theta
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

Va = vector_r_theta(4, 0, 'r')
Vb = vector_r_theta(4, 120, 'g')
Vc = vector_r_theta(4, 240, 'b')

Vab = Va - Vb
Vca = Vc - Va
Vbc = Vb - Vc

Vab.color, Vca.color, Vbc.color = 'c', 'y', 'm'

Vab >> Vb
Vca >> Va
Vbc >> Vc
# angle_V_I = -20
# Ra = 2
# Xa = 1
#
# Va = vector_r_theta(6, 0, 'r')
# Ia = vector_r_theta(2, angle_V_I, 'c')
# VRA = Ia * Ra
# VXA = Ia * Xa * 1j
# VRA.color, VXA.color = 'y', 'b'
#
# Ea = Va + VRA + VXA
#
# VRA >> Va  # Se une la cola de VRA con la cabeza de VA
# VXA >> VRA  # Se une la cola de VXA con la cabeza de VRA

for vector_name in ['Va', 'Vb', 'Vc', 'Vab', 'Vca', 'Vbc']:
    vector = eval(vector_name)
    plt.text(vector.xorigen + vector.x * 0.5 + 0.1 * vector.y, vector.yorigen + vector.y * 0.5 - 0.1 * vector.x, vector_name)
    vector.plot()

plt.xlim(-8, 8)
plt.ylim(-8, 8)

# (Ia * 4j).plot()

plt.gca().set_aspect(1)
plt.gca().spines['right'].set_visible(False)  # se quita la linea de abajo
plt.gca().spines['top'].set_visible(False)  # Se quita la linea de arriba
plt.show()
