from matplotlib import pyplot as pl
from numpy import linspace, sum

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'size':14.0})
rc('text', usetex=True)


def fib(n):
    F = [0, 1]
    for i in range(2,n):
        F.append(F[-1]+F[-2])
    return F

fibsums = []
for i in range(1,50):
    fibsums.append(sum(fib(i)))

pl.semilogy(fibsums)
pl.xlabel('$n$')
pl.ylabel('$fib(n)$')
pl.title('Plott av fibonaccitall')

pl.savefig('1e-fibplot.pdf')
pl.show()


