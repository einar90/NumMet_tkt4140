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
h = 0.001
tmin = 0.0
tmax = 20.0
ts = np.linspace(tmin, tmax, tmax/h)



# Initializing the arrays that will hold the computed results
x = np.zeros(len(ts))
y = np.zeros(len(ts))
u = np.zeros(len(ts))
v = np.zeros(len(ts))


def du(x, y):
    return -(x / (np.sqrt(x**2.0 + y**2.0)**3.0))


def dv(x, y):
    return -(y / (np.sqrt(x**2.0 + y**2.0)**3.0))

# Setting t0 values in arrays
x[0] = x0
y[0] = y0
u[0] = u0
v[0] = v0


# RK4 main loop
for i in range(0, len(ts)-1):

    # u and v
    k1u = h * du(x[i], y[i])
    k1v = h * dv(x[i], y[i])

    k2u = h * du(x[i]+k1u/2.0, y[i]+k1v/2.0)
    k2v = h * dv(x[i]+k1u/2.0, y[i]+k1v/2.0)

    k3u = h * du(x[i]+k2u/2.0, y[i]+k2v/2.0)
    k3v = h * dv(x[i]+k2u/2.0, y[i]+k2v/2.0)

    k4u = h * du(x[i]+k3u, y[i]+k3v)
    k4v = h * dv(x[i]+k3u, y[i]+k3v)

    u[i+1] = u[i] + (k1u + 2.0*k2u + 2.0*k3u + k4u) / 6.0
    v[i+1] = v[i] + (k1v + 2.0*k2v + 2.0*k3v + k4v) / 6.0

    # x and y with Heuns method
    # x[i+1] = x[i] + h/2.0 * (u[i] + u[i+1])
    # y[i+1] = y[i] + h/2.0 * (v[i] + v[i+1])

    k1x = h * u[i]
    k1y = h * v[i]

    k2x = h * (u[i]+k1x/2.0)
    k2y = h * (v[i]+k1y/2.0)

    k3x = h * (u[i]+k2x/2.0)
    k3y = h * (v[i]+k2y/2.0)

    k4x = h * (u[i]+k3x)
    k4y = h * (v[i]+k3y)

    x[i+1] = x[i] + (k1x + 2*k2x + 2*k3x + k4x) / 6.0
    y[i+1] = y[i] + (k1y + 2*k2y + 2*k3y + k4y) / 6.0


pl.plot(x, y)
pl.show()
