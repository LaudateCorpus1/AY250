# Downloading images from the internet
import urllib2
url = 'http://astro.berkeley.edu/~amorgan/candidates/Blanche%20Lincoln.gif'

img = urllib2.urlopen(url).read()

with open('dem.png','wb') as f:
	f.write(img)