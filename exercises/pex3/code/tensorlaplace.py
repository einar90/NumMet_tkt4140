import numpy as np
import matplotlib.pyplot as plt

n = 10
T_north = 30
T_south = 20
T_east = 10
T_west = 10


# Initializing boundary value matrix to zero
boundaries = np.zeros((n, n))

# Setting edge values
for i in range(n):
    boundaries[0][i] = T_south
    boundaries[i][0] = T_west
    boundaries[n-1][i] = T_north
    boundaries[i][n-1] = T_east

# Setting corner values to avg. of edges
boundaries[0][0] = (boundaries[0][1] + boundaries[1][0]) / 2
boundaries[0][n-1] = (boundaries[0][n-2] + boundaries[1][n-1]) / 2
boundaries[n-1][0] = (boundaries[n-2][0] + boundaries[n-1][1]) / 2
boundaries[n-1][n-1] = (boundaries[n-1][n-2] + boundaries[n-2][n-1]) / 2


# Constructing 2D difference matrix T applying the 5-point scheme
# and using left-to-right equation numbering
A = np.zeros((n, n))  # 1D Difference matrix
for i in range(n):
    for j in range(n):
        if i == j and i < n-1 and j < n-1:
            A[i][j] = 2
            A[i][j+1] = -1
            A[i+1][j] = -1
        if i == j:
            A[i][j] = 2

I = np.identity(n)  # identity matrix
T = np.kron(A, I) + np.kron(I, A)  # 2D Difference matrix


# Right side b matrix, initiall zeros
b = np.zeros(n**2)


# Applying boundary conditions by manipulating the transformation
# matrix and right-side b-vector.
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == (n-1) or j == (n-1):
            b[i*n+j] = boundaries[i][j]
            T[i*n+j] = np.zeros(n*n)
            T[i*n+j][i*n+j] = 1


# Solving the system
u = np.linalg.solve(T, b)


# Map the n*n vector onto a n x n 2D grid by reversing the
# left-to-right equation numbering.
temps = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        temps[i][j] = u[i*n+j]


#Visualitzation of results
x = np.arange(0, 1, n**(-1))
y = np.arange(0, 1, n**(-1))
fig = plt.figure(1)
CS2 = plt.contourf(x, y, temps, levels=np.arange(10, 30, 0.1))
cb = plt.colorbar(orientation='vertical')

fig.savefig('temps.pdf')

plt.show()
