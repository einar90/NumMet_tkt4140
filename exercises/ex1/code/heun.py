# Setting values
D = 0.5     # m
f = 0.05    # 
L = 392.0   # m
g = 9.8     # m/s^2

# Variables
z  = []     # Will hold displacement values
v  = []     # Will hold velocity values
zp = []     # Will hold displacement predicate values
vp = []     # Will hold velocity predicate values


# Timestep and max time
dt = 1.0
tmax = 3

# Setting initial values
z.append(-6.0)
v.append(0.0)

def dv_dt(z,v):
   return -(2.0*g*z/L + f/(2.0*D)*v*abs(v))

for t in range(1,tmax+1):
  zn = z[-1]; vn = v[-1]

  # Calculating predicates
  zp.append(zn + dt * vn)
  vp.append(vn + dt * dv_dt(zn, vn))
  
  # Calculating velocity and displacement
  z.append(zn + dt/2.0 * (vn + vp[-1]))
  v.append(vn + dt/2.0 * (dv_dt(zn,vn) + dv_dt(zp[-1],vp[-1])))

for t in range(0,tmax+1):
  print("z%d = %f \t\t v%d = %f" % (t, z[t], t, v[t]))