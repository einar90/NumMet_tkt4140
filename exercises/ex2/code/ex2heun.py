import numpy as np;

dx = 0.2                     # Step
endx = 0.6                   # Last x-value
nmax = (int)(round(endx/dx)) # Largest n


# Defining ddy function
def ddy(yn):
    return 2.0*yn*(1.0-3.0*yn/2.0)


# Initializing arrays
y   = [];
dy  = [];
yp  = [];
dyp = [];

# Setting initial values
y.append(1.0)
dy.append(0.0)

for n in range(1,nmax+1):
    yn = y[-1]
    dyn = dy[-1]

    dyp.append(dyn + dx*ddy(yn))
    yp.append( yn  + dx*dyn)

    dy.append( dyn + dx/2.0 * (ddy(yn) + ddy(yp[-1])))
    y.append(  yn  + dx/2.0 * (dyn     + dyp[-1]))
    print("%d \t x=%f \t yp=%f \t dyp=%f \t y=%f \t dy=%f" % (n, 0.2*n, yp[-1], dyp[-1], y[-1], dy[-1]))

