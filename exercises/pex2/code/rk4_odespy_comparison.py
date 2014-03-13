import odespy as ode
import numpy as np
from matplotlib import pyplot as pl


# Setting initial values
x0 = 1.0
y0 = 0.0
u0 = 0.0
v0 = 0.7

# Setting other parameters/variables
DT = 0.001
tmin = 0.0
tmax = 20.0
ts = np.linspace(tmin, tmax, tmax/DT)
MG = 1.0

g0 = np.zeros(len(ts))


def du(x, y):
    return -MG * x / (np.sqrt(x**2 + y**2)**3)


def dv(x, y):
    return -MG * y / (np.sqrt(x**2 + y**2)**3)

solver = ode.RungeKutta4
