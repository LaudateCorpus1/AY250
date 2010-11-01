#!/usr/bin/env python
import sys
import argparse

### Homework 8: Question 3
# First: let's parse are arguments
parser = argparse.ArgumentParser(description='Senate_polls_input')
parser.add_argument('-st',action='store',dest='state', help = 'Store State ID')
parser.add_argument('-pd',action='store',dest='poll_date', help = 'Store Poll Date')    
parser.add_argument('-r',action='store',dest='rep_pct', help = 'GOP percentage',type=int)
parser.add_argument('-d',action='store',dest='dem_pct', help = 'DEM percentage',type=int)
parser.add_argument('-i',action='store',dest='ind_pct', help = 'Ind percentage',type=int)
parser.add_argument('-pl',action='store',dest='pollster', help = 'Pollster ID')
parser.add_argument('-t',action='store_true',default=False,dest='boolean_switch', help = 'Switch on Plotting')    

results = parser.parse_args()

# Second: check current path of user and append if necessary for importing database code
flag = False

temp = 'C:\\Python26\\Scripts\\seminar2010\\Week5_databases_source\\Homework5\\Solutions'

for i in sys.path:
	if i == temp:
		flag = True

if flag == False:
	sys.path.append(temp)
	
# Now import Homework 5 module
import SenatePolls

basepath = 'C:\Python26\Scripts\seminar2010\Week5_databases_source\Homework5\Solutions'
dbpath   = basepath + '\senate2010.sqlite'

state     = results.state
poll_date = results.poll_date
rep_pct   = results.rep_pct
dem_pct   = results.dem_pct
ind_pct   = results.ind_pct
pollster  = results.pollster

if state is None:
	pass
else:
	if not ind_pct:
		ind_pct = -1
		
	SenatePolls.AddNewPoll(dbpath,state,poll_date,rep_pct,dem_pct,ind_pct,pollster)
	if results.boolean_switch == True:
		SenatePolls.PlotPollingData(dbpath,state)