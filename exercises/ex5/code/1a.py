from math import pi
from numpy import linspace

# Setting initial values
f0   = 1.0
df0  = 0.0
ddf0 = -6.5

# Setting other values
Re    = 30.0
alpha = pi/10
dx    = 0.05
xmax  = 0.15

# Initializing arrays
f    = []
df   = []
ddf  = []
dddf = []

# Function for the third derivative
def dddf_fun(f, df):
    return -2*Re*alpha*f*df - 4*alpha*alpha*df

# Appending initial values to arrays
f.append(f0)
df.append(df0)
ddf.append(ddf0)
dddf.append(dddf_fun(f[-1],df[-1]))
x = 0.0

while x <= xmax:
    f.append(f[-1] + dx*df[-1])
    df.append(df[-1] + dx*ddf[-1])
    ddf.append(ddf[-1] + dx*dddf[-1])
    dddf.append(dddf_fun(f[-1],df[-1]))
    x += dx

print f
print df
print ddf
print dddf
