import matplotlib.pyplot as plt
import numpy as np
import time
# b = (a[:,0]>-1) & (a[:,0]<1) & (a[:,1]>-1) & (a[:,1]<1)

# Let's allow for the option of looking at all possible pairs of parameters
def nchoosek(n,k):
	ntok = 1
	for t in xrange(min(k,n-k)):
		ntok = ntok*(n-t)//(t+1)
	return ntok


class draw_rectangle:
	# register instance of a rectangle
	def __init__(self,data,fig):
		self.data = data
		self.mark = []
		self.fig  = fig
		self.ca   = []	# current axes
		# General axes assignment later
		self.ax1  = fig.axes[0]
		self.ax2  = fig.axes[1]
		self.prev_point = []
		self.rectangles = []
		self.cid  = fig.canvas.mpl_connect('button_press_event', self)
		
	def __call__(self, event):
		""" called after a button_press_event """
		
		current = event.inaxes
		
		if event.button == 1: # left mouse button
			if len(self.prev_point) == 0:
				self.prev_point.append((event.xdata, event.ydata))
				# if previous selection, clear previous rectangle and reset data
				if len(self.rectangles) > 0:
					# remove the rectangle
					self.ax1.lines.remove(self.rectangles.pop(-1))
					# reset these axes
					self.ax1.clear()
					self.ax1.plot(self.data[:,0],self.data[:,1],'ok')
					self.ax2.clear()
					self.ax2.plot(self.data[:,2],self.data[:,3],'ok')
					
					plt.draw()
					
			elif len(self.prev_point) == 1:
				line, = self.ax1.plot([self.prev_point[0][0], event.xdata, event.xdata,
								  self.prev_point[0][0], self.prev_point[0][0]],
								 [self.prev_point[0][1], self.prev_point[0][1], event.ydata,
								  event.ydata, self.prev_point[0][1]],
								 color='k')
				self.rectangles.append(line)
				plt.draw()
				time.sleep(0.25) # pauses for a bit
				
				# Now mark selected data
				data = self.data
				rect = self.rectangles[0]
				
				# Get indices of data within the box
				ind = (data[:,0]>min(rect.get_xdata())) & \
					  (data[:,0]<max(rect.get_xdata())) & \
					  (data[:,1]>min(rect.get_ydata())) & \
					  (data[:,1]<max(rect.get_ydata()))
				
				# Grab the associated subset of the data
				temp = data[ind]
				self.ax1.plot(temp[:,0],temp[:,1],'or')
				self.ax2.plot(temp[:,2],temp[:,3],'oy')
				plt.draw()
				
				self.prev_point = [] # delete previously selected point
		
		# Erase current rectangle if you don't like the selection
		elif event.button == 3: # right mouse button
			if len(self.rectangles) > 0: # if there exist a selected rectangle
				self.ax1.lines.remove(self.rectangles.pop())
				self.ax1.clear()
				self.ax1.plot(self.data[:,0],self.data[:,1],'ok')
				self.ax2.clear()
				self.ax2.plot(self.data[:,2],self.data[:,3],'ok')
				plt.draw()
	
	def close(self):
		""" Disconnect the Drawing of Rectangles """
		self.fig.canvas.mpl_disconnect(self.cid)

# After testing everything we'll make this a general function wrapper around the above
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
a = np.random.normal(0,1,size=[100,4])
ax1.plot(a[:,0],a[:,1],'ok')
ax2.plot(a[:,2],a[:,3],'ok')
d = draw_rectangle(a,fig)

plt.show()
