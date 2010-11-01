import matplotlib.pyplot as plt
from matplotlib.mlab import find
import numpy as np
import time
from itertools import combinations

def brushing_EDA(data,fixed=[]):
	# check data type: this code accepts numpy arrays and numpy.core.records.recarray
	# with the first row indicating the names of the columns
	
	# The variable fixed is available if the user wishes to compare a particular axis against
	# all others
	
	if (not isinstance(data,np.core.records.recarray)) & (isinstance(data,np.ndarray)):
		temp, col = np.shape(data)
	elif isinstance(data,np.core.records.recarray):
		names = data.dtype.names
		col = len(names)
		
	else:
		print "This code only accepts numpy arrays and numpy.core.records.recarray. Good bye."
		return
	
	# Determine subplot layout
	# Set a range that is pushing the edge of reasonable for a single figure
	# Let's allow for the option of looking at all possible pairs of parameters
	def nchoosek(n,k):
		ntok = 1
		for t in xrange(min(k,n-k)):
			ntok = ntok*(n-t)//(t+1)
		return ntok
	
	if np.size(fixed) == 0:
		N        = nchoosek(col,2)
		size_ops = np.array([9, 12, 15, 16, 20, 25, 30, 36, 42,49])
		sp_sz    = np.array([[3,4,5,4,5,5,6,6,6,7],[3,3,3,4,4,5,5,6,7,7]]);
		temp     = find(size_ops > N)
		frame    = sp_sz[:,temp[0]]
		
		# Generate all possible variable combinations if fixed = []
		# Now Lay out the figure
		fig = plt.figure()
		for i in range(N):
			fig.add_subplot(frame[0],frame[1],i+1)
		
		# Attach indices of relevant data for each axis
		combos = []
		if not isinstance(data,np.core.records.recarray):
			for i in combinations(np.arange(col),2):
				combos.append(i)
		else:
			for i in combinations(np.arange(col),2):
				combos.append((names[i[0]],names[i[1]]))
	else:
		N = col -1 
		
		size_ops = np.array([9, 12, 15, 16, 20, 25, 30, 36, 42,49])
		sp_sz    = np.array([[3,4,5,4,5,5,6,6,6,7],[3,3,3,4,4,5,5,6,7,7]]);
		temp     = find(size_ops > N)
		frame    = sp_sz[:,temp[0]]
		
		# Generate all possible variable combinations if fixed = []
		# Now Lay out the figure
		fig = plt.figure()
		for i in range(N):
			fig.add_subplot(frame[0],frame[1],i+1)
		
		# Attach indices of relevant data for each axis
		combos = []
		# Attach indices of relevant data for each axis
		combos = []
		if not isinstance(data,np.core.records.recarray):
			for i in range(col):
				if i == fixed:
					pass
				else:
					combos.append ((fixed, i))
		else:
			for i in range(col):
				if i == fixed:
					pass
				else:
					combos.append ((names[fixed], names[i]))
					
	# Attach index information
	for i in range(len(fig.axes)):
		fig.axes[i].ind = combos[i]
	
	
	class draw_rectangle:
		# register instance of a rectangle
		def __init__(self,data,fig):
			# associate data and fig with class
			self.data    = data
			self.fig     = fig
			
			# Draw the figure
			if not isinstance(self.data,np.core.records.recarray):
				for ax in self.fig.axes:
					ax.plot(self.data[:,ax.ind[0]],self.data[:,ax.ind[1]],'ok')
					ax.set_xlabel('Variable = ' + str(ax.ind[0]))
					ax.set_ylabel('Variable = ' + str(ax.ind[1]))
			else:
				
				for ax in self.fig.axes:
					ax.plot(self.data[ax.ind[0]],self.data[ax.ind[1]],'ok')
					ax.set_xlabel('Variable = ' + str(ax.ind[0]))
					ax.set_ylabel('Variable = ' + str(ax.ind[1]))
					
			plt.show()
						
			# Set selection variables
			self.prev_point    = []
			self.prev_point_ax = []
			self.rectangle     = []
			self.rect_ax       = []
			
			# connect callback to figure canvas
			self.cid  = fig.canvas.mpl_connect('button_press_event', self)
			
		def __call__(self, event):
			""" called after a button_press_event """
			
			# set current axes
			current = event.inaxes
			
			if event.button == 1: # left mouse button
				if len(self.prev_point) == 0:
					self.prev_point.append((event.xdata, event.ydata))
					self.prev_point_ax = current
					
					# if previous selection, clear previous rectangle and reset data
					if len(self.rectangle) > 0:
						# remove the rectangle
						self.rect_ax.lines.remove(self.rectangle.pop(-1))
						# reset these axes
						if not isinstance(self.data,np.core.records.recarray):						
							for ax in self.fig.axes:
								ax.clear()
								ax.plot(self.data[:,ax.ind[0]],self.data[:,ax.ind[1]],'ok')
								ax.set_xlabel('Variable = ' + str(ax.ind[0]))
								ax.set_ylabel('Variable = ' + str(ax.ind[1]))
						else:
							for ax in self.fig.axes:
								ax.clear()
								ax.plot(self.data[ax.ind[0]],self.data[ax.ind[1]],'ok')
								ax.set_xlabel('Variable = ' + str(ax.ind[0]))
								ax.set_ylabel('Variable = ' + str(ax.ind[1]))
						
						plt.draw()
						
				elif (len(self.prev_point) == 1) and (current != self.prev_point_ax):
					# clear previous point data that was started for other axis and start anew for this axis
					self.prev_point.pop()
					self.prev_point_ax = []
					
					self.prev_point.append((event.xdata, event.ydata))
					self.prev_point_ax = current
					
				elif (len(self.prev_point) == 1) and (current == self.prev_point_ax):
					# Complete drawing rectangle if it was begun in this axis
					line, = current.plot([self.prev_point[0][0], event.xdata, event.xdata,
									  self.prev_point[0][0], self.prev_point[0][0]],
									 [self.prev_point[0][1], self.prev_point[0][1], event.ydata,
									  event.ydata, self.prev_point[0][1]],
									 color='k')
					# Hold on to rectangle specs
					self.rectangle.append(line)
					# Keep track of it axes as well
					self.rect_ax = current
					plt.draw()
					time.sleep(0.1) # pauses for a bit before draw
					
					# Now mark selected data
					data = self.data
					rect = self.rectangle[0]
					
					# Get indices of data within the box
					if not isinstance(self.data,np.core.records.recarray):
						ind = (data[:,current.ind[0]]>min(rect.get_xdata())) & \
							  (data[:,current.ind[0]]<max(rect.get_xdata())) & \
							  (data[:,current.ind[1]]>min(rect.get_ydata())) & \
							  (data[:,current.ind[1]]<max(rect.get_ydata()))
						
						# Grab the associated subset of the data
						temp = data[ind]
						for ax in self.fig.axes:
							if (ax == current):
								current.plot(temp[:,current.ind[0]],temp[:,current.ind[1]],'or')
							else:
								ax.plot(temp[:,ax.ind[0]],temp[:,ax.ind[1]],'or')
					else:
						ind = (data[current.ind[0]]>min(rect.get_xdata())) & \
							  (data[current.ind[0]]<max(rect.get_xdata())) & \
							  (data[current.ind[1]]>min(rect.get_ydata())) & \
							  (data[current.ind[1]]<max(rect.get_ydata()))
						
						# Grab the associated subset of the data
						temp = data[ind]
						for ax in self.fig.axes:
							if (ax == current):
								current.plot(temp[current.ind[0]],temp[current.ind[1]],'or')
							else:
								ax.plot(temp[ax.ind[0]],temp[ax.ind[1]],'or')
					plt.draw()
					
					self.prev_point    = [] # delete previously selected point
					self.prev_point_ax = []
					
					
			# Erase current rectangle if you don't like the selection
			elif event.button == 3: # right mouse button
				if len(self.rectangle) > 0: # if there exist a selected rectangle
					self.rect_ax.lines.remove(self.rectangle.pop())
					# reset these axes
					if not isinstance(self.data,np.core.records.recarray):						
						for ax in self.fig.axes:
							ax.clear()
							ax.plot(self.data[:,ax.ind[0]],self.data[:,ax.ind[1]],'ok')
							ax.set_xlabel('Variable = ' + str(ax.ind[0]))
							ax.set_ylabel('Variable = ' + str(ax.ind[1]))
					else:
						for ax in self.fig.axes:
							ax.clear()
							ax.plot(self.data[ax.ind[0]],self.data[ax.ind[1]],'ok')
							ax.set_xlabel('Variable = ' + str(ax.ind[0]))
							ax.set_ylabel('Variable = ' + str(ax.ind[1]))
					
					plt.draw()
		
		def close(self):
			""" Disconnect the Drawing of rectangle """
			self.fig.canvas.mpl_disconnect(self.cid)
	
	return draw_rectangle(data,fig)

# Example using some Gaussian Data
data = np.random.normal(0,1,size=[100,4])

b1    = brushing_EDA(data)

# Example using some Gaussian Data with a fixed dimension
b2    = brushing_EDA(data,fixed=0)
