JOHN LONG
SID 13843882
AY 250
HOMEWORK 7

README

-The Code should run fine out of the box. Just cd into ./bibtex/ and run manage.py syncdb at the command line. This will build everything you need.
-Then just run manage.py runserver to start things up.
-I've included 2 .bib files in the main 'Homework7' folder for uploading to the database. These are the ones I tested my code with for bugs.
-I linked collections to articles via foreign keys, type "run manage.py sql articles" to check, which allows the same article to be in multiple 
	collections, but currently searching by a collection doesn't work. I would have to parse out 'collection' from the query strings, filter 
	on the Collection class, and then input the instance of the collection class, if it exists, to the query string. 
	I ran out of time, but at least gained a little functionality.
-Something that came up: how do you render foreign characters, from say German, correctly?
-Also, the bibtex parser did not like double quotes (") within curly brackets, so I had to edit my .bib files a bit.
-THANKS A LOT FOR YOUR HELP CHRIS! I got seriously stuck at 2 points, and your nudges really helped.
Cheers,
John