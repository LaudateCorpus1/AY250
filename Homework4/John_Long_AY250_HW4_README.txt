John Long
SID 13843882
AY 250

HOMEWORK4:
Question 1: Recreating an old figure
The original figure is marked "HW1_Q1_original.png" and the recreation is "HW4_Q1_figure_recreation.png"
Run "HW4_Question1_my_figure_redux.py" to generate the figure. A few things came up:
1) how do you do multiline title, xlabels, etc?
2) How do I get rid of the border around the legend?

Question 2: Recreating the provided figure
To Generate the figure you need to be in the directory where you have the yahoo, google, and ny_temps
files. Then just run "HW4_Question2_stock_figure.py". The figure that appears needs to be expanded
in the window. How do you set figure sizes? Relative to monitor size? Also, I couldn't figure
out how to link the legend between the axes, nor could I figure out how to turn off the border
on the legend.


Question 3: Brushing
To test the brushing code I rode, simply run 'HW4_Question3_brushing.py'. The selection rectangle
draws after clicking two points within the same axes (I didn't use the motion feature). Right
clicking removes the current selection box and associated data highlights. I wrote some figure
layout elements that creates an appropriate number of axes, given the data dimensions. I ran 
into a few problems that I was not able to solve within the time constraints: 1) the figures
initialize to a small size. How do I a) get the dimensions of the computer monitor? b) tell 
python to make the figure that big? 2) I ran into a problem with comparing datetime to floats 
e.g. the Hormel date with date as x-data and open price as y-data. I got lost in a labrynth 
trying to find a solution to this problem. I didn't succeed. Is there a simple solution? Lastly,
I found it frustrating that all numpy.core.records.recarray are numpy.ndarray...this ambiguity
made instance checking awkward.