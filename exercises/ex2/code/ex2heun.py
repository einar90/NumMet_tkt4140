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
yp  = [];
dyp = [];

# Setting initial values
y.append(1)
dy.append(0)

for n in range(0,nmax+1):

