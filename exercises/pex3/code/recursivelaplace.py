import numpy as np

n = 4
T_north = 30
T_south = 20
T_east = 10
T_west = 10

# Initializing grid to zero
grid = np.zeros((n, n))

# Setting edge values
for i in range(3):
    grid[0][i] = T_south
    grid[i][0] = T_west
    grid[n-1][i] = T_north
    grid[i][n-1] = T_east

# Setting corner values to avg. of edges
grid[0][0] = (grid[0][1] + grid[1][0]) / 2
grid[0][n-1] = (grid[0][n-2] + grid[1][n-1]) / 2
grid[n-1][0] = (grid[n-2][0] + grid[n-1][1]) / 2
grid[n-1][n-1] = (grid[n-1][n-2] + grid[n-2][n-1]) / 2

print grid
