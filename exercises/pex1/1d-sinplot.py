from matplotlib import pyplot as pl
from numpy import pi, sin, linspace

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'size':14.0})
rc('text', usetex=True)

x10  = linspace(0,2*pi,10)
x100 = linspace(0,2*pi,100)
sin10 = sin(x10)
sin100 = sin(x100)

pl.figure()
p10,  = pl.plot(x10, sin10, 'r')
p100, = pl.plot(x100,sin100, '--')

p100.set_dashes([10, 5, 20, 5])

pl.legend( [p10,       p100],
           ['$n = 10$', '$n = 100$'])
pl.xticks([0,     pi/2,                pi,       3*pi/2,               2*pi],
          ['$0$', '$\\frac{\\pi}{2}$', '$\\pi$', '$\\frac{3\\pi}{2}$', '$2\\pi$'])

pl.xlim([0, 2*pi])

pl.xlabel('$\\alpha$')
pl.ylabel('$\\sin(\\alpha)$')
pl.title('Plott av $\\sin(\\alpha)$')

pl.savefig('1d-sineplot.pdf')
pl.show()
