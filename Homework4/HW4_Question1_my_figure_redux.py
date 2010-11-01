# Recreating an Old Figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec

# This figure compares the Jeffreys to the Bayes-Laplace prior for multinomial distribution
# Made this figure to explain our particular choice of prior for an analysis I ran.

# load all the relevant information
jeffreys = csv2rec("jeffreys.txt")
laplace  = csv2rec("laplace.txt")
N        = np.arange(1,1002)
As       = np.array([10,100,10,100])
prob     = np.array([0.1,0.01,0.01,0.0001])

# Figure Specs
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# Plot the data
# first axis
ax1.plot(N,jeffreys['jest1'],color='gray'),
ax1.plot(N,jeffreys['jest1']+jeffreys['j_std1'],linestyle='--',color='gray'),
ax1.plot(N,jeffreys['jest1']-jeffreys['j_std1'],linestyle='--',color='gray')

ax1.plot(N,laplace['lest1'],color='k'),
ax1.plot(N,laplace['lest1']+laplace['l_std1'],linestyle='--',color='k'),
ax1.plot(N,laplace['lest1']-laplace['l_std1'],linestyle='--',color='k')

ax1.set_xlim((1,1000))
ax1.set_yticks((0,.05,.1,.15,.2))
ax1.set_xticks((0,500,1000))
ax1.set_ylabel('Probability',fontname='Cambria',fontsize=12)
ax1.set_title("Comparing Priors Categories = 10, p = 0.1",fontname='Cambria',fontsize=16)

# second axis
ax2.plot(N,jeffreys['jest2'],color='gray'),
ax2.plot(N,jeffreys['jest2']+jeffreys['j_std2'],linestyle='--',color='gray'),
ax2.plot(N,jeffreys['jest2']-jeffreys['j_std2'],linestyle='--',color='gray')

ax2.plot(N,laplace['lest2'],color='k'),
ax2.plot(N,laplace['lest2']+laplace['l_std2'],linestyle='--',color='k'),
ax2.plot(N,laplace['lest2']-laplace['l_std2'],linestyle='--',color='k')

ax2.set_xlim((1,1000))
ax2.set_yticks(np.linspace(0.0,0.02,5))
ax2.set_xticks((0,500,1000))
ax2.set_title("Comparing Priors Categories = 100, p = 0.01",fontname='Cambria',fontsize=16)

# third axis
ax3.plot(N,jeffreys['jest3'],color='gray'),
ax3.plot(N,jeffreys['jest3']+jeffreys['j_std3'],linestyle='--',color='gray'),
ax3.plot(N,jeffreys['jest3']-jeffreys['j_std3'],linestyle='--',color='gray')

ax3.plot(N,laplace['lest3'],color='k'),
ax3.plot(N,laplace['lest3']+laplace['l_std3'],linestyle='--',color='k'),
ax3.plot(N,laplace['lest3']-laplace['l_std3'],linestyle='--',color='k')
ax3.axhline(prob[1],color='k',linestyle='--',linewidth=2)

ax3.set_xlim((1,1000))
ax3.set_yticks(np.linspace(0.0,0.1,6))
ax3.set_xticks((0,500,1000))
ax3.set_xlabel('Samples',fontname='Cambria',fontsize=12)
ax3.set_ylabel('Probability',fontname='Cambria',fontsize=12)
ax3.set_title("Comparing Priors Categories = 10, p = 0.01",fontname='Cambria',fontsize=16)

# fourth axis
ax4.plot(N,jeffreys['jest4'],color='gray',label='Jeffreys'),
ax4.plot(N,jeffreys['jest4']+jeffreys['j_std4'],linestyle='--',color='gray'),
ax4.plot(N,jeffreys['jest4']-jeffreys['j_std4'],linestyle='--',color='gray')

ax4.plot(N,laplace['lest4'],color='k',label='Bayes-Laplace'),
ax4.plot(N,laplace['lest4']+laplace['l_std4'],linestyle='--',color='k'),
ax4.plot(N,laplace['lest4']-laplace['l_std4'],linestyle='--',color='k')
ax4.axhline(prob[-1],color='k',linestyle='--',linewidth=2)
plt.legend(loc='upper right')

ax4.set_xlim((1,1000))
ax4.set_yticks(np.linspace(0.0,0.01,6))
ax4.set_xticks((0,500,1000))
ax4.set_xlabel('Samples',fontname='Cambria',fontsize=12)
ax4.set_title("Comparing Priors Categories = 100, p = 0.0001",fontname='Cambria',fontsize=16)

plt.show()