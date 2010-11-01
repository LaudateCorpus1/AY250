#!/usr/bin/env python
"""
AY 250 - Scientific Research Computing with Python
Homework Assignment 3 Solutions
Author: Christopher Klein
"""
import xmlrpclib
from numpy import array, append, shape
from matplotlib import pyplot

# Connect to the server.
host, port = "", 5020
server = xmlrpclib.ServerProxy("http://%s:%d" % (host, port))

# Get a list of methods available on the server and print them out, along with 
# their docstrings. This snippet is necessary to first figure out how to reverse
# engineer the distortion methods.
available_methods = server.system.listMethods()
print "Available methods from server:"
for method in server.system.listMethods():
    print method
    print server.system.methodHelp(method)
    print ""

# Read in an image and save it as the original for later comparison.
im_array = pyplot.imread("cake.jpg")
pyplot.imshow(im_array[::-1])
pyplot.savefig("client_original.png")
# Convert the original image array to a list, because we cannot send an array
# over the XMLRPC connection.
im_list = im_array.tolist()

# Call the image distortion method on the original image list.
distorted_im_list = server.image_distort_1(im_list)
# Create an array from the returned distorted image list.
distorted_im_array = array(distorted_im_list)
# Write out the distorted image.
pyplot.imshow(distorted_im_array[::-1])
pyplot.savefig("client_distorted1.png")
# Recover the original image by reversing the operations of the distortion 
# method.
recovered_im_array = distorted_im_array*2
# At this point, the recovered array contains the same data is the original 
# image array, but it is of generic (float) data type. This is because the 
# distortion method, by it's nature, converted the data type. To be safe, we
# "downcast" the recovered image to unsigned 8-bit integer. This is how images
# are generally stored and displayed on a computer screen, because a human can 
# only perceive that much difference in pixel value. Technically, each pixel is
# 24 bits, 8 bit per color channel.
recovered_im_array = recovered_im_array.astype("uint8")
# Write out the recovered image for comparison.
pyplot.imshow(recovered_im_array[::-1])
pyplot.savefig("client_recovered1.png")

# Same as above, but for the second distortion method.
distorted_im_list = server.image_distort_2(im_list)
distorted_im_array = array(distorted_im_list)
pyplot.imshow(distorted_im_array[::-1])
pyplot.savefig("client_distorted2.png")
recovered_im_array = append(append(distorted_im_array[2 *
    shape(distorted_im_array)[0]/3:], 
    distorted_im_array[:shape(distorted_im_array)[0]/3], 0), 
    distorted_im_array[shape(distorted_im_array)[0]/3:2 * 
    shape(distorted_im_array)[0]/3], 0)
recovered_im_array = recovered_im_array.astype("uint8")
pyplot.imshow(recovered_im_array[::-1])
pyplot.savefig("client_recovered2.png")

# Same as above, but for the third distortion method.
distorted_im_list = server.image_distort_3(im_list)
distorted_im_array = array(distorted_im_list)
pyplot.imshow(distorted_im_array[::-1])
pyplot.savefig("client_distorted3.png")
sub_im = im_array[::2, ::2]
sub_im2 = append(sub_im, sub_im, 0)
add_array = append(sub_im2, sub_im2, 1)
recovered_im_array = distorted_im_array - add_array
recovered_im_array = recovered_im_array.astype("uint8")
pyplot.imshow(recovered_im_array[::-1])
pyplot.savefig("client_recovered3.png")