from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})

plt.clf()
ax = plt.gca()
ax.set_xlim(0,9)
X = np.arange(1,8,0.001)
ax.set_xlabel('$x$')
plt.plot(X,np.log2(X),linewidth=2,color='blue',label='$\log_2(x)$')
plt.fill_between(X,np.log2(X),linewidth=0,color='blue',alpha=0.2)
X_disc = np.arange(0,9,1)
plt.plot(X,np.log2(np.floor(X)),linewidth=2,color='black',label=r'$\log_2(\lfloor x\rfloor)$')
plt.fill_between(X,np.log2(np.floor(X)),linewidth=0,color='gray',alpha=0.2)
X = np.arange(2,8,0.001)
plt.plot(X,np.log2(X-1),linewidth=2,color='red',label='$\log_2(x-1)$')
plt.fill_between(X,np.log2(X-1),linewidth=0,color='red',alpha=0.2,)
for n in range(6):
    plt.annotate('$\log_2('+str(n+1)+')$',(n+2.5,np.log2(n+1)+0.01),color='black',fontsize=10)
plt.legend(loc='upper left',frameon=False)
plt.savefig("log_bound.png",bbox_inches='tight')
