import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#Wave Amplitude
A=5
#Wave Period
T = 0.02;
#Time Samples
r = 10
c = 0.001
f = 50

t = np.linspace(-2.5*T,2.5*T,1e4)
#Plot wave
plt.plot(t, np.cos(2*np.pi*f*t))
plt.plot(t,(1/np.sqrt(1+(2*np.pi*f*r*c)**2))*np.cos(2*np.pi*f*t - np.arctan(r*c*2*np.pi*f)))
plt.ylim(-1, 6)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('$g(t)$')
#Save figure
#plt.savefig('../figs/1.1.eps')
plt.show()


