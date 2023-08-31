import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})

nmax = 24

# Naive complexity 
C_naive = np.zeros(nmax)
for j in range(1,nmax):
    n = 2**j
    C_naive[j] = 1+3*j

n = 2.**np.arange(nmax)
    
C_strassen = np.log2(7*n**(np.log2(7.))-6*n**2)
    
plt.clf()
ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xticks((1,1.E3,1.E6,1.E9,1.E12,1.E15))
ax.set_yticks((1,1.E9,1.E18,1.E27,1.E36))
ax.set_xlabel('matrix size $n$')
ax.set_ylabel('number of operations')
plt.plot(n,2.**C_naive,
         linewidth=2,
         color='red',
         marker='o',
         markersize=0,
         markerfacecolor='white',
         markeredgewidth=2,
         markeredgecolor='red',
         label='naive')
plt.plot(n,2.**C_strassen,
         linewidth=2,
         color='blue',
         marker='s',
         markersize=0,
         markerfacecolor='blue',
         markeredgewidth=2,
         markeredgecolor='blue',
         label='Strassen')
a = 1.E2
b = 1.E8
rho = 10000
plt.plot([a,a*rho],[b,b*rho**3],
         linewidth=2,
         linestyle='-',
         label=r'$\propto n^3$',
         color='black')
a = 1.E2
b = 1.E5
rho = 10000
plt.plot([a,a*rho],[b,b*rho**(np.log2(7.))],
         linewidth=2,
         linestyle='--',
         label=r'$\propto n^{\log_2 7}$',
         color='black')
plt.legend(loc='lower right')
plt.savefig('CostMatMatMult.png',bbox_inches='tight')
