# Homework 5: Senate Polling Data: Main File
# import tools
from numpy import loadtxt,array,zeros,arange, concatenate
from matplotlib.pylab import figure,plot,legend,text,show,savefig,close
import sqlite3,urllib2,webbrowser,time

######################################
### Request Query and Check inputs ###
######################################

def senate_polls(stateID, output = 1):
	"""If output is left equal to 1, then this code will generate .png files for the
		polling information as well as the candidates pictures obtained from the web.
		These will then be displayed in your web browser. Either way, the code will 
		output these values:
		dem   = democrat polling values in that state
		gop   = dop polling values in that state
		demID = name of democratic candidate
		gopID = name of gop candidate
		ind   = independent polling values
		indID = name of independent candidate"""
	
	# Load state names and codes for checking inputs
	states = loadtxt('state_abbrev.txt',delimiter=",",skiprows=1,dtype='|S14,|S2')

	# Set stateID to appropriate type and check for statehood
	stateID = str(stateID).upper()
	
	#Check this input against states list
	query = []
	for state in states:
		if (stateID == state[0]):
			query.append(state[1])
		elif (stateID == state[1]):
			query.append(state[1])

	if (len(query) == 0):
		print "Not a validate stateID: Check State name or Mail Code"
		return
	
	# check to see if the state ID input is having a race
	sr_data = loadtxt("senate_races.txt", skiprows=1, delimiter=",", \
		  dtype='|S2,|S25,|S25,|S25,|S12')
		  
	races   = []
	for race in sr_data:
		races.append(race[0])

	flag = 0
	for race in races:
		if race == query[0]:
			flag +=1
	
	if (flag == 0):
		print "That state is not holding a Senate race this year"
		return
		
	##########################
	### Run Database Query ###
	##########################
	connection = sqlite3.connect("senate_race_polls.db")
	cursor = connection.cursor()
	sql_cmd = """SELECT senate_polls.state, senate_polls.dem,senate_polls.gop,senate_polls.ind,
				 senate_polls.date, senate_races.dem,senate_races.gop,senate_races.ind 
				 FROM senate_polls LEFT JOIN senate_races ON
				 senate_polls.mc = senate_races.mc
				 WHERE senate_polls.mc =""" + """'""" + query[0] + """'"""

	cursor.execute(sql_cmd)

	# Grab the data
	db_info = cursor.fetchall()
	connection.close()


	#####################################
	### Generate Media for Webbrowser ###
	#####################################
	# Pull the state for display in plot
	state = str(db_info[0][0])

	# Pull relevant Candidate
	demID   = str(db_info[0][5])
	gopID   = str(db_info[0][6])
	indID   = str(db_info[0][7])
	
	# Pull information for all candidates
	# Candidate data to be filled
	dem  = zeros((len(db_info),),dtype=float)
	gop  = zeros((len(db_info),),dtype=float)
	ind  = zeros((len(db_info),),dtype=float)
	date = zeros((len(db_info),),dtype=int)

	for i,entry in enumerate(db_info):
		# fill in candidate data
		dem[i]  = entry[1]
		gop[i]  = entry[2]
		ind[i]  = entry[3]
		
		# fill in the day the poll was posted
		temp = time.strptime(str(entry[4]),"%m/%d/%Y")
		date[i] = temp.tm_yday

	# Determine whether or not to generate figure output
	if (output == 1):
		# Generate date structure for plotting
		month = []
		for i in range(11):
			month.append(str(i+1) + '/01/2010')

		yday = []
		for i in month:
			temp = time.strptime(i,"%m/%d/%Y")
			yday.append(temp.tm_yday)
			
		yday = array(yday)

		# Draw up canvas
		fig = figure()
		ax  = fig.add_subplot(111)

		# Plot data and text (taking care of case for independents)
		if (len(indID) == 1):
			ax.plot(date,dem,'b',linewidth=2,label=demID)
			ax.plot(date,dem,'ob',linewidth=2)
			ax.plot(date,gop,'r',linewidth=2,label=gopID)
			ax.plot(date,gop,'or',linewidth=2)
			
			lb = min(concatenate((dem,gop)))
			ub = max(concatenate((dem,gop)))
			text(min(date)+2,ub+2,state,fontname='Cambria',fontsize=18)
			indstr = """ """
			
		else:
			ax.plot(date,dem,'b',linewidth=2,label=demID)
			ax.plot(date,dem,'ob',linewidth=2)
			ax.plot(date,gop,'r',linewidth=2,label=gopID)
			ax.plot(date,gop,'or',linewidth=2)
			ax.plot(date,ind,'g',linewidth=2,label=indID)
			ax.plot(date,ind,'og',linewidth=2)
			
			lb = min(concatenate((dem,gop,ind)))
			ub = max(concatenate((dem,gop,ind)))
			text(min(date)+2,ub+2,state,fontname='Cambria',fontsize=18)
			indstr = """<div style="position:absolute; left:750; top:25; width:250; height:125">
					<p>
					<img id = "image3" width = 100 height = 125 src = "ind.png" align="left">
					""" + indID + """
					</p>
					</div>"""
		
		# Set Specs of figure
		ax.set_xticks(yday)
		ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
		ax.set_yticks(arange(lb-(lb%5),ub+10,5))
		ax.set_xlim([min(date), ax.get_xlim()[1]])
		ax.set_ylim([(lb-10)+(lb%5),(ub+10)-(ub%5)])
		ax.set_ylabel('Percent Favored')
		ax.grid()
		leg = legend(loc='lower left')
		leg.get_frame().set_alpha(0.5)
		# show()
		
		# Save the current queries figure to a dictated buffer
		savefig('poll_fig')
		close(fig)
		
		# Download the pictures associated with the candidates
		if (len(indID) == 1):
			urlD = 'http://astro.berkeley.edu/~amorgan/candidates/' + demID.split()[0] \
				+ '%20' + demID.split()[1] +'.gif'
			urlR = 'http://astro.berkeley.edu/~amorgan/candidates/' + gopID.split()[0] \
				+ '%20' + gopID.split()[1] +'.gif'
			
			imgD = urllib2.urlopen(urlD).read()
			imgR = urllib2.urlopen(urlR).read()
			
			with open('dem.png','wb') as f:
				f.write(imgD)

			with open('gop.png','wb') as f:
				f.write(imgR)
		else:
			urlD = 'http://astro.berkeley.edu/~amorgan/candidates/' + demID.split()[0] \
					+ '%20' + demID.split()[1] +'.gif'
			urlR = 'http://astro.berkeley.edu/~amorgan/candidates/' + gopID.split()[0] \
					+ '%20' + gopID.split()[1] +'.gif'
			urlI = 'http://astro.berkeley.edu/~amorgan/candidates/' + indID.split()[0] \
					+ '%20' + indID.split()[1] +'.gif'
			
			imgD = urllib2.urlopen(urlD).read()
			imgR = urllib2.urlopen(urlR).read()
			imgI = urllib2.urlopen(urlI).read()
			
			with open('dem.png','wb') as f:
				f.write(imgD)

			with open('gop.png','wb') as f:
				f.write(imgR)
				
			with open('ind.png','wb') as f:
				f.write(imgI)
				
		####################################
		### Post the Data via Webbrowser ###
		####################################
		str1 = """
		<html>
		<head>
		<title>Senate Race: """ + query[0] + """</title>
		</head>
		<body bgcolor="white">
		<!-- you may need to supply your own image files -->
		<!-- and adjust their widths and heights accordingly -->

		<div style="position:absolute; left:250; top:25; width:250; height:125">
		<p>
		<img id = "image1" width = 100 height = 125 src = "dem.png" align="left">
		""" + demID + """
		</p>
		</div>
		 
		<div style="position:absolute; left:500; top:25; width:250; height:125">
		<p>
		<img id = "image2" width = 100 height = 125 src = "gop.png" align="left">
		""" + gopID + """
		</p>
		</div>
		 
		""" + indstr + """
		<div style="position:absolute; left:150; top:185; width:800; height:400">
		<img id = "image4" width = 800 height = 400 src = "poll_fig.png">
		</div>

		</body>
		</html>"""
		 
		# write the html file to the working folder
		fout = open("senate_race.htm", "w")
		fout.write(str1)
		fout.close()
		 
		# now open your web browser to run the file
		webbrowser.open("senate_race.htm")
		return dem,gop,demID,gopID,ind,indID
	else:
		return dem,gop,demID,gopID,ind,indID