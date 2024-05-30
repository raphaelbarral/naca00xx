import numpy as np
from math import pi
import matplotlib.pyplot as plt

naca = input('Numero du profil NACA?\n')
corde = float(input('Corde du profil (m)?\n'))
N = int(input('Nombre de points\n'))
lineaire = False if input('Non lineaire? (y/n)').lower() == 'n' else False

if lineaire:
    xc = np.linspace(0, 1, N)
else:
    theta = np.linspace(0, pi, N)
    xc = 1/2*(1-np.cos(theta))

xup = xc*corde
xdown = xc*corde

t = int(naca[2:4])/100
yt = 5*t*(0.2969*xc**(1/2)-0.1260*xc-0.3516*xc**2+0.2843*xc**3-0.1036*xc**4)

yup = yt*corde
ydown = -yt*corde

up = np.array([xup, yup])
down = np.array([xdown, ydown])

plt.plot(up[0,:], up[1,:])
plt.plot(down[0,:], down[1,:])
plt.show()

indice_max = np.argmax(yup)
epaisseur_max = 2*yup[indice_max]
x_max = xup[indice_max]

print(f'L\'épaisseur maximale est de {epaisseur_max:.2f}m et est atteint à {x_max:.2f}m le long de la corde')