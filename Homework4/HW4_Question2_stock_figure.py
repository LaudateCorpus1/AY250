import numpy as np
import matplotlib.pyplot as plt

# Grab data
yahoo    = np.loadtxt("yahoo_data.txt",dtype={'names':('date','value'),'formats':('S5','f8')})
google   = np.loadtxt("google_data.txt",dtype={'names':('date','value'),'formats':('S5','f8')})
ny_temps = np.loadtxt("ny_temps.txt",dtype={'names':('date','maxtemp'),'formats':('S5','f8')})

# Plot it up
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

ax1.plot(google['date'],google['value'],linewidth=2,label="Google Stock Value")
ax1.plot(yahoo['date'],yahoo['value'],color="purple",linewidth=2,label="Yahoo! Stock Value")
ax2.plot(ny_temps['date'],ny_temps['maxtemp'],"--r",linewidth=2,label="NY Mon. High Temp")
ax1.set_ylim(-20,780)
ax1.set_xlim(48800,55640)
ax1.minorticks_on()
ax2.set_ylim(-150,100)
ax2.minorticks_on()

# Annotations
ax1.set_title("New York Temperature, Google, Yahoo!",fontname="Times New Roman",fontsize=20)
ax1.set_xlabel("Date (MJD)",fontname="Times New Roman",fontsize=16)
ax1.set_ylabel("Value (Dollars)",fontname="Times New Roman",fontsize=16)
ax2.set_ylabel("Temperature ($^o$F)",fontname="Times New Roman",fontsize=16)
ax1.legend(loc="lower left", bbox_to_anchor=(0.06,0.35))
ax2.legend(loc="lower left", bbox_to_anchor=(0.06,0.3))

plt.show()