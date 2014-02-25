from __future__ import print_function

def fib(n):
    F = []
    for i in range(0,n):
        if i==0 or i==1:
            F.append(i)
        else:
            F.append(F[-1]+F[-2])
        print(F[-1], end=' + ')
    print('...')

fib(9)
