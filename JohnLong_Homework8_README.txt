John Long: AY 250: Homework8

My adjustments to the SenatePolls.py are in Senate_Polls_Update.py. I can't imagine how this is 
going to work on another system that doesn't have the requisite files in a folder the same name
as the one I used (see note below). Please do enlighten me as to how this problem is solved. 
On my computer I check my sys.path for the colder in which the files live, and append the 
directory when necessary. I was able to get argparse to work with AddNewPoll in the solutions,
but displaying the polling information didn't work correctly. I have some basic questions that
came up while doing this homework. I'd like to stop by during office hours to clarify. I don't
think I get how branching works if you don't remain in the git bash window.

NOTES:
-When using the solution for homework 5, I ran into an issue with paths. 
	Specifically, the solutions would you a path syntax that would not work on my
	system. e.g. '.\senate2010.sqlite' I get that the basic logic of this command
	is to tell the system to look within the current folder. But this did not work
	when I was importingthe module from a different location. I had to fill in the
	path. Is there another solution?