from numpy import array,add,dot,transpose
from numpy.linalg import inv,solve

a = array([ 1, 2, 3 ])
b = array([ 4, 5, 6 ])
A = array([1, 1, 2, 2, 3, 3, 4, 4, 5]).reshape(3,3)
B = array([2, 4, 6, 8, 10, 12, 14, 16, 18]).reshape(3,3)

print '1: a+b = ', add(a,b)
print '\n2: a dot b = ', dot(a,b)
print '\n3: AB = \n', dot(A,B)
print '\n4: A^T = \n', transpose(A)
print '\n5: A^-1 = \n', inv(A)
print '\n6: A*x = b => x = ', solve(A,b)
