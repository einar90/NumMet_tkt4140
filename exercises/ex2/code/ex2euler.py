import numpy as np;

dx = 0.2                     # Step
endx = 0.6                   # Last x-value
nmax = (int)(round(endx/dx)) # Largest n

# Defining ddy function
def ddy(yn):
  return 2*yn*(1-3*yn/2)


# Initializing arrays
y   = [];
dy  = [];

# Setting initial values
y.append(1)
dy.append(0)

for n in range(0,nmax+1):
  yn = y[-1]; dyn = dy[-1]
  dy.append(dyn+dx*ddy(yn))
  y.append(yn+dx*dyn)
  print("%d \t\t x=%f \t\t y=%f \t\t dy=%f" % (n, 0.2*n, y[-1], dy[-1]))