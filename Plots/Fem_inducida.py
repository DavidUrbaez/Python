import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

plt.style.use('dark_background')


x=np.array([5,4,3,2,1])
y=0.08*1000/x

x1=np.linspace(1,5,20)
y1=0.08*1000/x1

plt.plot(x1,y1,'--')
plt.scatter(x,y)

plt.gca().spines['right'].set_visible(False) #se quita la linea de abajo
plt.gca().spines['top'].set_visible(False) #Se quita la linea de arriba

for xs, ys in zip(x, y):
    pl.text(xs, ys + 5, str(round(ys, 2)) + ' [V]')

plt.ylabel('Fem inducida  \u03B5 [V]')
plt.xlabel('Tiempo [seg]')


plt.show()
