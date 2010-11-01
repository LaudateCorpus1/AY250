import sqlite3
connection = sqlite3.connect("senate_race_polls.db")
cursor = connection.cursor()

# # Test1: Query Senate Poll Table
# input = str(raw_input("Please enter a USA mail code:"))
# sql_cmd = "SELECT dem, gop FROM senate_polls WHERE mc=" + "'" + input + "'"
# cursor.execute(sql_cmd)
# db_info = cursor.fetchall()
# for entry in db_info: 
	# print str(entry)	


# Test2: Query Senate Race Table
# input = str(raw_input("Please enter a USA mail code:"))
# sql_cmd = "SELECT * FROM senate_races WHERE mc=" + "'" + input + "'"
# cursor.execute(sql_cmd)
# db_info = cursor.fetchall()
# for entry in db_info: 
	# print str(entry)	

# Test3: Basic Join
input = str(raw_input("Please enter a USA mail code:"))
sql_cmd = """SELECT senate_polls.state, senate_polls.dem,senate_polls.gop,senate_polls.ind,
			 senate_polls.date, senate_races.dem,senate_races.gop,senate_races.ind 
			 FROM senate_polls LEFT JOIN senate_races ON
			 senate_polls.mc = senate_races.mc
			 WHERE senate_polls.mc =""" + """'""" + input + """'"""

cursor.execute(sql_cmd)
db_info = cursor.fetchall()
for entry in db_info: 
	print str(entry)	

connection.close()

