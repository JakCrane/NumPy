import numpy as np
import matplotlib.pyplot as plt
import math as m

impulse = np.array([ 108, 107, 84, 116, 108, 93, 110, ])
max_force_lb = np.array([ 19, 22, 19, 38, 21, 25, 65 ])
burn_t = np.array([ 1.89, 1.29, 0.96, 0.93, 1.61, 1.15, 0.45 ])
max_force_n = max_force_lb * 4.45
M = 1

Cd = 0.75
D = 0.043
rho = 1.29
g = 9.81

A = m.pi*(D*D)
k = 0.5*rho*Cd*A


Vmax = []
Amax = []
for I, t in zip(impulse, burn_t):
    T = I/t
    q = m.sqrt((T - M*g)/k)
    x = 2*k*q/M
    V_max = q*( (1 - m.exp( -x*t )) / (1 + m.exp( -x*t )) )
    Vmax.append(V_max)
    A_0fuel = (-M/(2*k))*m.log((T-M*g-k*(V_max*V_max))/(T-M*g))
    Amax.append(A_0fuel + (+M/(2*k))*m.log((M*g+k*(V_max*V_max))/(M*g)))

plt.scatter(impulse, max_force_n)
plt.scatter(impulse[5], max_force_n[5], color='red')
plt.xlabel('Impulse',size=16)
plt.ylabel('Max Force (N)',size=16)
plt.title('Impulse v Max Force',size=16)
plt.show()
plt.close

plt.scatter(impulse, max_force_n)
plt.scatter(impulse[5], max_force_n[5], color='red')
plt.xlabel('Impulse',size=16)
plt.ylabel('Max Force (N)',size=16)
plt.title('Impulse v Max Force',size=16)
plt.xlim([0, 120])
plt.ylim([0, 300])
plt.show()
plt.close

plt.scatter(max_force_n, Vmax)
plt.scatter(max_force_n[5], Vmax[5], color='red')
plt.xlabel('Max Force (N)',size=16)
plt.ylabel('Maximum Velocity (m/s)',size=16)
plt.title('Max Force v Maximum Velocity',size=16)
plt.show()
plt.close

plt.scatter(max_force_n, Amax)
plt.scatter(max_force_n[5], Amax[5], color='red')
plt.xlabel('Max Force (N)',size=16)
plt.ylabel('Maximum Altitude (m)',size=16)
plt.title('Max Force v Maximum Altitude',size=16)
plt.show()
plt.close