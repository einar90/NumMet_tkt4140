from matplotlib import pyplot as pl
from numpy import pi, sin, arcsin, cos, linspace
from scipy.special import ellipk, ellipj

from matplotlib import rc
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('font', **{'size': 14.0})
rc('text', usetex=True)

theta0 = pi/3
dtheta0 = 0
tmax = 15
dt = 0.01
nmax = round(tmax/dt)
t = linspace(0, tmax, nmax)

theta = []
dtheta = []
ddtheta = []
E = []


# Fuinction for second derivetive
def ddtheta_fun(theta):
    return -sin(theta)


# Energy function
def E_fun(theta, dtheta):
    return 0.5*(dtheta**2-dtheta0**2) + cos(theta0) - cos(theta)


# Initial values
theta.append(theta0)
dtheta.append(dtheta0)
ddtheta.append(ddtheta_fun(theta0))
E.append(E_fun(theta[-1], dtheta[-1]))

# Euler iteration
while len(theta) < nmax:
    theta.append(theta[-1] + dt*dtheta[-1])
    dtheta.append(dtheta[-1] + dt*ddtheta[-1])
    ddtheta.append(ddtheta_fun(theta[-1]))
    E.append(E_fun(theta[-1], dtheta[-1]))


# Analytical solution
def analytical_theta(t):
    k = sin(theta0/2)
    T = ellipk(k**2)
    (sn, cn, dn, ph) = ellipj(T-t, k)
    return 2 * arcsin(k*sn)


def analytical_dtheta(t):
    k = sin(theta0/2)
    T = ellipk(k**2)
    (sn, cn, dn, ph) = ellipj(T-t, k)
    return -2*k*cn

theta_a = [analytical_theta(T) for T in t]
dtheta_a = [analytical_dtheta(T) for T in t]
E_a = [E_fun(theta_a[i], dtheta_a[i]) for i in range(0, len(t))]

pl.figure('Theta')
thetaplot, = pl.plot(t, theta, label='Euler iteration, dt=%3.3f' % dt)
thetaplot_a, = pl.plot(t, theta_a, '--', label='Analytical solution')
pl.xlim([0, tmax])
pl.xlabel('$t$')
pl.ylabel('$\\theta$')
pl.title('$\\theta$ over time.')
pl.legend(loc=3, ncol=2, mode="expand", borderaxespad=0.)
pl.savefig("pendel_theta.pdf")

pl.figure('Energy')
energyplot = pl.plot(t, E, label='Euler iteration, dt=%3.3f' % dt)
energyplot_a = pl.plot(t, E_a, '--', label='Analytical solution')
pl.xlim([0, tmax])
pl.xlabel('$t$')
pl.ylabel('$E$')
pl.title('Energy function')
pl.legend(loc=3, ncol=2, mode="expand", borderaxespad=0.)
pl.savefig("pendel_E.pdf")

pl.show()

