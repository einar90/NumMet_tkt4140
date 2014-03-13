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

    h2 = h / 2.0
    h6 = h / 6.0

    # u and v
    k1u = du(x[i], y[i])
    k1v = dv(x[i], y[i])

    k2u = du(x[i]+h2*k1u, y[i]+h2*k1v)
    k2v = dv(x[i]+h2*k1u, y[i]+h2*k1v)

    k3u = du(x[i]+h2*k2u, y[i]+h2*k2v)
    k3v = dv(x[i]+h2*k2u, y[i]+h2*k2v)

    k4u = du(x[i]+h*k3u, y[i]+h*k3v)
    k4v = dv(x[i]+h*k3u, y[i]+h*k3v)

    u[i+1] = u[i] + h6 * (k1u + 2.0*k2u + 2.0*k3u + k4u)
    v[i+1] = v[i] + h6 * (k1v + 2.0*k2v + 2.0*k3v + k4v)

    # x and y
    k1x = u[i]
    k1y = v[i]

    k2x = (u[i]+u[i+1])/2.0 + h2*k1x
    k2y = (v[i]+v[i+1])/2.0 + h2*k1y

    k3x = (u[i]+u[i+1])/2.0 + h2*k2x
    k3y = (v[i]+v[i+1])/2.0 + h2*k2y

    k4x = u[i+1] + h*k3x
    k4y = v[i+1] + h*k3y

    x[i+1] = x[i] + h6 * (k1x + 2.0*k2x + 2.0*k3x + k4x)
    y[i+1] = y[i] + h6 * (k1y + 2.0*k2y + 2.0*k3y + k4y)


pl.figure('RK4 position')
pl.plot(x, y)

pl.figure('RK4 Velocity')
pl.plot(u, v)

pl.show()
