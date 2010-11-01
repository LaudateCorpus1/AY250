# Homework5: Databases: Senate Polling data
import urllib2, sqlite3, datetime, time
from numpy import loadtxt, array
from matplotlib.pylab import *

# Grab the senate polling data from the web
response = urllib2.urlopen("http://electoral-vote.com/evp2010/Senate/senate_polls.csv")
info     = response.read()
response.close()

# Write the information to a file
# Let's get rid of all those useless columns
info     = info.replace(',,,,,,,,',',')
output   = file("senate_polls.txt", "w")
output.write(info)
output.close()

# Let's get those postal codes from the web
# I downloaded a USPS webpage that had them
response = urllib2.urlopen("http://www.usps.com/ncsc/lookups/abbreviations.html#states")
states   = response.readlines()

# Now for each line of my senate_polls data I'm going to look up the postal code
# I'm also going to generate a list of state mail codes
state_codes = [('State','Mail Code')]
for i,line in enumerate(states):
	if ('<TT>' in line) and ('colspan' in line) and not('<U>' in line) \
		and not('<BR>' in line):
		# Grab the mail code associated with this state
		temp,line  = line.split('<TT>')
		line,temp  = line.split('</TT>')
		line       = line.strip()
		
		code       = states[i+1]
		temp,code  = code.split('<TT>')
		code,temp  = code.split('</TT>')
		code       = code.strip()
		
		# Fill in column of senate poll data
		state_codes.append((line,code))
		
# write out the relevant state mail codes
with open("state_abbrev.txt","w") as f:
	for i in state_codes:
		f.write(str(i[0]) + "," + str(i[1]) + "\n")
	
	
# Grab the senate race match up
response = urllib2.urlopen("http://astro.berkeley.edu/~amorgan/candidate_names.txt")
info     = response.read()
with open("senate_races.txt","w") as f:
	f.write(info)
