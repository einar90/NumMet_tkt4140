"""
TKT4140 Numerical Caluclations -- Python Exercise 2.
Test-implementation using Euler
"""

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


# Initializing the arrays that will hold the computed results
x = np.zeros(len(ts))
y = np.zeros(len(ts))
u = np.zeros(len(ts))
v = np.zeros(len(ts))

def du(x, y):
    return -MG * x / (np.sqrt(x**2 + y**2)**3)


def dv(x, y):
    return -MG * y / (np.sqrt(x**2 + y**2)**3)

# Setting t0 values in arrays
x[0] = x0
y[0] = y0
u[0] = u0
v[0] = v0


# RK4 main loop
for i in range(0, len(ts)-1):
    x[i+1] = x[i] + DT * u[i]
    y[i+1] = y[i] + DT * v[i]
    u[i+1] = u[i] + DT * du(x[i], y[i])
    v[i+1] = v[i] + DT * dv(x[i], y[i])

pl.plot(x, y)
pl.show()
