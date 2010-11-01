##################################
### Homework2: Numpy and Scipy ###
##################################
### QUESTION1: Fitting Data ###

# import the tools
import numpy as np
from scipy.interpolate import splrep,splev
from scipy.optimize import leastsq
from matplotlib.pylab import figure,plot,show

### Question 1: Simple Fitting
# Set the constants
a     = 2
alpha = -0.75
k     = 0.1

# Generate domain and function output
x     = np.arange(0,4,.01)
y     = a*np.exp(alpha*x)+k
err   = np.sqrt(y)

# now let's add some Gaussian [0,0.1] noise to y
yn    = y + np.random.normal(0,0.1,len(y))

# now define our residual function for least squares fitting
def resid_fun(params):
	return (yn - params[0]*np.exp(params[1]*x)**2)/err

# Let's reset our parameters to see how well least squares does without a 
# good initial guess
par = np.array([0.0,0.0])	
par_lstsq = leastsq(resid_fun,par,full_output=True)
	
# let's do some interpolating
x_skip = x[::10]
y_skip = yn[::10]

# For the life of me, I couldn't get the basic 'spline' method to work well
# so I went with splrep and splev, which follows a methology like polyfit and polyval
# Let's interpolate
sp       = splrep(x_skip,y_skip)

# How let's fit a 0-2nd degree polynomial to the data as the inital conditions 
# for our sequent least squares fit
par0     = np.polyfit(x,y,0)
par1     = np.polyfit(x,y,1)
par2     = np.polyfit(x,y,2)

# Set up figure
fig = figure()
# Declare initial axis
ax1 = fig.add_subplot(111)
# The data
ax1.plot(x,yn,'ob',linewidth=2,label='Noisy Data')
# the data generator
ax1.plot(x,y,'--c',linewidth=3,label='Data Generator')
# The least squares fit
ax1.plot(x,par_lstsq[0][0]*np.exp(par_lstsq[0][1]*x)**2,linewidth=2,color='k',label='Least Squares')
# interpolated fit
ax1.plot(x,splev(x,sp),linewidth=2,color='g',label='Spline Interp')
# The second degree polynomial fit
ax1.plot(x,np.polyval(par0,x),linewidth=2,color='r',linestyle=':',label='0 degree poly')
ax1.plot(x,np.polyval(par1,x),linewidth=2,color='r',linestyle='--',label='1 degree poly')
ax1.plot(x,np.polyval(par2,x),linewidth=2,color='r',label='2 degree poly')

# Specs for this axis
ax1.set_title('Noisy Data: Various Methods\n for fitting this data')
ax1.set_xlabel('Sample #')
ax1.set_ylabel('Data Value')
leg = ax1.legend(loc='upper right', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.5)
show()