##################################
### Homework2: Numpy and Scipy ###
##################################
### QUESTION#: Matrix inverse  ###

# import tools
import numpy as np

# Bust out the older linear algebra textbook to get a few examples of 
# square invertible matrices
# simple case
A0 = np.array([[2,1,0],[-4,-1,-3],[3,1,2]],dtype=float)

# a little more interesting
A1 = np.array([[3,4,-1,0],[4,-1,0,3],[-6,4,8,-2],[-1,1,2,7]],dtype=float)

# let's throw in a singular matrix for testing too
A2 = np.array([[2,1,0],[-4,-1,-3],[3,1,3./2.]],dtype=float)

# In order to find the determinant and inverse of these, and other matrices
# I'm going to program up a Gaussian elimination routine
def gaus_jord_elim(mat):
	# check to make sure 'mat' is a numpy array
	if not(isinstance(mat,np.ndarray)):
		print 'Input must be a numpy array.'
		return
	
	# check to make sure the matrix is square
	Nr,Nc = np.shape(mat)
	if not(Nr==Nc):
		print 'Input must be a square matrix.'
		return
	
	###################################
	### Gaussian-Jordan Elimination ###
	###################################
	# I abapted the initial Gaussian-Elimination code from the wikipedia entry. 
	# Dealing with the issue of interchanging rows has been a pain in the ass.
	# I'm just going to ignore the problem of swapping rows (even though I know
	# numerically it is more sound
	
	# Augment original matrix on right with corresponding identity matrix
	A = np.concatenate([mat,np.identity(Nr)],axis=1)
		
	# Gaussian Elimination
	for i in range(Nr):
		for j in range(i+1,Nr):
			if A[j,i] != 0:
				A[j] += -A[j,i]/A[i,i]*A[i]
		
	determ = np.diagonal(A).prod()
	if determ == 0:
		print 'Matrix is Singular!'
		return
	
	
	# Backward Gaussian Elimination
	for i in range(Nr-1,-1,-1):
		for j in range(i-1,-1,-1):
			if A[j,i] != 0:
				A[j] += -A[j,i]/A[i,i]*A[i]
	
	# Normalize
	for i in range(Nr):
		A[i] *= 1/A[i,i]
	
	return determ, A[:,Nc:]

	
# now let's test it out
print 'Attempting to invert A0'
temp0,temp1 = gaus_jord_elim(A0)
print "Inverse Matrix is: " 
print temp1
print "Checking Inverse: "
print np.dot(A0,temp1)

print 'Attempting to invert A1'
temp0,temp1 = gaus_jord_elim(A1)
print "Inverse Matrix is: " 
print temp1
print "Checking Inverse: "
print np.dot(A1,temp1)

print 'Attempting to invert A2'
gaus_jord_elim(A2)
