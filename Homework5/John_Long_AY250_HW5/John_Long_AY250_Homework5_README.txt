John Long
SID 13843882
AY 250
Homework 5

General Notes: To run these scripts you will be access to the internet. Also, keep
in mind that some of these scripts will write files to your current directory. This code
uses the webbrowser module and was tested on a system with firefox. It should work with 
your default browser, but I'm not sure how it will look (first attempt at html).

Instructions:
	1) Homework5_data.py grabs all the data, excluding candidate pictures, from
		web and stores them as .txt files.
	2) Homework5_tables.py take the data files generated in 1) and makes a sqlite
		database from these with appropriate tables.
	3) Homework5_main_file.py generates the main function for querying the basebase.
		The doc string for the function 'senate_polls' details the output. The input
		should be a string. One question that came up in writing the code: How do you
		write a figure witout it ever showing up? For example, my code generates a 
		figure that I just want to write to a .png file. I'm not interested in seeing the 
		figure pop up. Even without calling 'show()' or 'draw()' the graphics still gets
		flushed. Any way around this?
	4) Homework5_Qe.py evaluates how many losses the democrats are expected to have in the 
		senate. I use a weighted sum of the last 5 polls using y = exp(-0.5*x) where x = 0:4
		for the weights. Personally, I think the democrats are going to gain some as the election
		gets closer.