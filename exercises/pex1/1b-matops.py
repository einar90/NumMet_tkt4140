import numpy as np
from numpy import array,add,dot,transpose
from numpy.linalg import inv

a = array([ 1, 2, 3 ])
b = array([ 4, 5, 6 ])
A = array([1, 1, 2, 2, 3, 3, 4, 4, 5]).reshape(3,3)
B = array([2, 4, 6, 8, 10, 12, 14, 16, 18]).reshape(3,3)

print 'a+b = ', add(a,b)
print '\na dot b = ', dot(a,b)
print '\nAB = \n', dot(A,B)
print '\nA^T = \n', transpose(A)
print '\nA^-1 = \n', inv(A)
