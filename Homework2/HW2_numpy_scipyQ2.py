##################################
### Homework2: Numpy and Scipy ###
##################################
### QUESTION2: Image Cleaning ###

# import the tools
import numpy as np
import matplotlib.image as mimage
import matplotlib.cm as cm
from matplotlib.pylab import figure, plot, show

# Admittedly, I have the Scientific Computing in Python book which contains this example
# But it's not so bad to just type out an example now and again is it?
X = mimage.imread('C:\Documents and Settings\John Long\My Documents\John\Programming\Python\seminar2010\Week2_scipy_numpy_stats\moonlanding.png')
Nr, Nc = X.shape

# the original image
fig = figure()
fig.subplots_adjust(hspace=0.1, wspace=0.1)
ax1 = fig.add_subplot(221)
im1 = ax1.imshow(X, cmap=cm.gray)
ax1.set_title('image')
ax1.set_ylabel('original')

# the original spectrum
ax2 = fig.add_subplot(222)
ax2.set_title('spectrum')
F = np.fft.fft2(X)
im2 = ax2.imshow(abs(F),cmap=cm.Blues)
im2.set_clim(0,300)

# set the high frequencies to zero and invert the transformation to recover the filtered image
Fc = F.copy()
Fc[50:-50,:]=0
Fc[:,50:-50]=0
Xf = np.fft.ifft2(Fc).real

# plot the filtered image
ax3 = fig.add_subplot(223)
im3 = ax3.imshow(Xf, cmap=cm.gray)
ax3.set_ylabel('filtered')

# plot the filtered spectrum
ax4 = fig.add_subplot(224)
im4 = ax4.imshow(abs(Fc), cmap=cm.Blues)
im4.set_clim(0,300)

# turn off the x and y tick labels
for ax in ax1, ax2, ax3, ax4:
	ax.set_xticks([])
	ax.set_yticks([])
	
show()