import numpy as np
import math as m
def calculateAandVmax(params,enginf):
    [M,Cd,D,rho,g] = params
    A = m.pi*(D*D)
    k = 0.5*rho*Cd*A

    enginf['Thrust'] = enginf['Impulse']/enginf['Burn Time']
    enginf['q'] = np.sqrt((enginf['Thrust'] - M*g)/k)
    enginf['x'] = 2*k*enginf['q']/M 
    enginf['V max'] = enginf['q']*(  1 + -1*np.exp( -1*enginf['x']*enginf['Burn Time'] )  ) / (1 + np.exp( -1*enginf['x']*enginf['Burn Time'] ))
    enginf['A 0 fuel'] = (-M/(2*k))*np.log((enginf['Thrust']-M*g-k*(enginf['V max']*enginf['V max'])) / (enginf['Thrust']-M*g))
    enginf['A max'] = enginf['A 0 fuel'] + (+M/(2*k))*np.log((M*g+k*(enginf['V max']*enginf['V max']))/(M*g))
    
    return enginf