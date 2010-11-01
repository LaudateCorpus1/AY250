from matplotlib.pylab import plot,figure,show
from numpy import array
import time

month = []
for i in range(11):
	month.append(str(i+1) + '/01/2010')

yday = []
for i in month:
	temp = time.strptime(i,"%m/%d/%Y")
	yday.append([temp.tm_yday,temp.tm_yday**2])
	
yday = array(yday)

fig = figure()
ax  = fig.add_subplot(111)
ax.plot(yday[:,0],yday[:,1])
ax.set_xticks(yday[:,0])
ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
show()
