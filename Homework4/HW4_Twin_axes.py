# Twin Axes
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
a = np.random.normal(0,1,size=[100,2])
ax.plot(a[:,0],a[:,1],'ok')

ax2 = ax.twinx()
ax2.plot(a[:,1],a[:,0],'or')
plt.show()
