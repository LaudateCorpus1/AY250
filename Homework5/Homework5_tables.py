# Homework 5: tables
# import the tools
import urllib2, sqlite3, datetime, time
from numpy import loadtxt, array
from matplotlib.pylab import *

############################################
### Load the senate poll data into tabel ###
############################################
sp_data = loadtxt("senate_polls.txt", skiprows=1, delimiter=",", \
		  dtype='float, float,|S14,|S2,float,float,float,|S10,|S15', \
		  converters = {6: lambda s: float(s or 0)})
		  
#Insert state abbreviations
state_ID = loadtxt("state_abbrev.txt",skiprows=1, delimiter=",",dtype='|S30,|S2')
for line in sp_data:
	state = line[2].upper()
	for ID in state_ID:
		if (state == ID[0]):
			line[3] = ID[1]
			
# Convert State names to uppercase
for i,name in enumerate(sp_data['f2']):
	sp_data['f2'][i] = name.upper()

# Let's convert our dates into a format that sqlite3 can handle
for line in sp_data:
	temp = time.strptime(line[7] + ' 2010',"%b %d %Y")
	temp = time.strftime("%m/%d/%Y",temp)
	line[7] = temp

		
### Create a Table for this data ###
connection = sqlite3.connect("senate_race_polls.db")
cursor = connection.cursor()
sql_cmd = """CREATE TABLE senate_polls (id INTEGER PRIMARY KEY AUTOINCREMENT,
			 day FLOAT, length INT, state TEXT, mc TEXT, dem FLOAT, gop FLOAT,
			 ind FLOAT, date DATE, pollster TEXT)"""
cursor.execute(sql_cmd)
	
### Insert the data into the senate_polls table ###
for poll in sp_data:
	sql_cmd = ("INSERT into senate_polls (day,length,state,mc,dem,gop,ind,date,pollster) " +
			  "VALUES " + str(poll))
	cursor.execute(sql_cmd)
connection.commit()


############################################
### Load the senate race data into table ###
############################################
sr_data = loadtxt("senate_races.txt", skiprows=1, delimiter=",", \
		  dtype='|S2,|S25,|S25,|S25,|S12')
sql_cmd = """CREATE TABLE senate_races (id INTEGER PRIMARY KEY AUTOINCREMENT,
			 mc TEXT, dem TEXT, gop TEXT, ind TEXT, incumb TEXT)"""
cursor.execute(sql_cmd)

### Insert the data into the senate_races table ###
for race in sr_data:
	sql_cmd = ("INSERT into senate_races (mc,dem,gop,ind,incumb) VALUES " + str(race))
	cursor.execute(sql_cmd)
connection.commit()

connection.close()
