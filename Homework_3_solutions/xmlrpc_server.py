#!/usr/bin/env python
"""
AY 250 - Scientific Research Computing with Python
Homework Assignment 3 Solutions
Author: Christopher Klein
"""
import SimpleXMLRPCServer, sys
from numpy import array, append, shape
from matplotlib import pyplot 

class Some_Class_We_Want_Remotely_Accessible:
    def image_distort_1(self, im_list):
        """
        Multiply each pixel value by 0.5
        """
        # Convert the list back to an array for easier manipulation.
        im_array = array(im_list)
        # Perform the distortion operation.
        distorted_im_array = im_array*0.5
        # Write out the distorted image.
        pyplot.imshow(distorted_im_array[::-1])
        pyplot.savefig("server_distorted1.png")
        # Convert the distorted image array back to a list to transport to 
        # client.
        distorted_im_list = distorted_im_array.tolist()
        return distorted_im_list
    
    def image_distort_2(self, im_list):
        """
        Move bottom third of rows to the top
        """
        im_array = array(im_list)
        distorted_im_array = append(im_array[shape(im_array)[0]/3:], 
            im_array[:shape(im_array)[0]/3], 0)
        pyplot.imshow(distorted_im_array[::-1])
        pyplot.savefig("server_distorted2.png")
        distorted_im_list = distorted_im_array.tolist()
        return distorted_im_list
    
    def image_distort_3(self, im_list):
        """
        Subsample the image by 2 and then repeat it out in a 2x2 new image 
        called the "add_image". Then add this to the original image.
        """
        im_array = array(im_list)
        sub_im = im_array[::2, ::2]
        sub_im2 = append(sub_im, sub_im, 0)
        add_array = append(sub_im2, sub_im2, 1)
        distorted_im_array = im_array + add_array
        pyplot.imshow(distorted_im_array[::-1])
        pyplot.savefig("server_distorted3.png")
        distorted_im_list = distorted_im_array.tolist()
        return distorted_im_list

host = ""
# Allow the user to change the port number when running the script. If no port
# number is provided, use a default.
if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 5020
# Here we set up the server.
server = SimpleXMLRPCServer.SimpleXMLRPCServer((host, port), allow_none=True)
# Register the class (and underlying functions) that we want to serve.
server.register_instance(Some_Class_We_Want_Remotely_Accessible())
# Also, register introspection functions to allow the client to list the 
# available methods and their docstrings.
server.register_introspection_functions()
# Start serving, and continue to do so until killed with control-c.
print "XMLRPC Server is starting at:", host, port
server.serve_forever()