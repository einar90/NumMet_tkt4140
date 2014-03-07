#planmot.py

import odespy
import numpy as np
import matplotlib.pylab as plt

#Defining functions


def axf(x, y):   #=d^2x/dt^2
    return -(x/((np.sqrt(x**2 + y**2))**3))


def ayf(x, y):   #=d^2y/dt^2
    return -(y/((np.sqrt(x**2 + y**2))**3))


def uuf(u):  #=dx/dt=u
    return u


def vvf(v):  #=dy/dt=v
    return v


#Constants
dt = 0.001
tmax = 20
nmax = round(tmax/dt)
nn = np.linspace(0, tmax, nmax)
ncur = 0

#Instantiating vectors
uu = []
vv = []
xx = []
yy = []
tt = []


#initial values
uu.append(0)
vv.append(0.7)
xx.append(1)
yy.append(0)
tt.append(0)

print uu
print vv
print xx
print yy

while ncur < nmax:
    ncur = ncur+1
    tt.append(tt[-1]+dt)

    #RK on X and Y
    k1ax = axf(xx[-1], yy[-1])
    k1ay = ayf(xx[-1], yy[-1])

    k2ax = axf(xx[-1]+dt/2*k1ax, yy[-1]+dt/2*k1ay)
    k2ay = ayf(xx[-1]+dt/2*k1ax, yy[-1]+dt/2*k1ay)

    k3ax = axf(xx[-1]+dt/2*k2ax, yy[-1]+dt/2*k2ay)
    k3ay = ayf(xx[-1]+dt/2*k2ax, yy[-1]+dt/2*k2ay)

    k4ax = axf(xx[-1]+dt*k3ax, yy[-1]+dt*k3ay)
    k4ay = ayf(xx[-1]+dt*k3ax, yy[-1]+dt*k3ay)

    #RK on U and V
    k1u = uuf(uu[-1])
    k1v = vvf(vv[-1])

    k2u = uuf(uu[-1]+dt/2*k1u)
    k2v = vvf(vv[-1]+dt/2*k1v)

    k3u = uuf(uu[-1]+dt/2*k2u)
    k3v = vvf(vv[-1]+dt/2*k2v)

    k4u = uuf(uu[-1]+dt*k3u)
    k4v = vvf(vv[-1]+dt*k3v)

    xx.append(xx[-1]+dt/6*(k1u+2*k2u+2*k3u+k4u))
    yy.append(yy[-1]+dt/6*(k1v+2*k2v+2*k3v+k4v))

    uu.append(uu[-1]+dt/6*(k1ax+2*k2ax+2*k3ax+k4ax))
    vv.append(vv[-1]+dt/6*(k1ay+2*k2ay+2*k3ay+k4ay))


plt.plot(xx, yy)
plt.grid()
plt.savefig('planpos2.pdf')
plt.title('Position of the satellite')
plt.show()

plt.plot(uu, vv)
plt.grid()
plt.savefig('planvel2.pdf')
plt.title('Velocity of the satellite')
plt.show()
