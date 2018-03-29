import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import pi

##################################################
# Information from The Python Graph Glddery #391 #
##################################################

#read the csv file
data = pd.read_csv('../Radiation_Record/merge_panel_radiation.csv',header=0)

Data = pd.DataFrame(data=data)

#print(Data)

# remove unwanted columns
plotData = Data.drop(['hour_index','day','month'],axis=1)
#print(plotData)

summerData = plotData.iloc[range(3077,3604),:]
#print(summerData)
# sums up all radiation according to day hour
sum_up = summerData.groupby('hour').sum()

#print(sum_up)
# create CSV File for optional excel output
#sum_up.to_csv('../Radiation_Record/Radar_Graph.csv')


################################
#  Start drawing radar graph ###
################################



rad_data = sum_up.T


#print(rad_data)
# Define labels of lines (Panel 1, Panel 2 etc.)
labels=rad_data.columns.values.tolist()
#print(labels)

# N different panels
# Same thing
categories = rad_data.columns.values.tolist()
#print(categories)
N = 17
#print(N)


# What will be the angle of each axis in the plot
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
#print(len(angles))


# Initialise the spider plot
ax = plt.subplot(111, polar=True)


# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], categories)


ax.set_rlabel_position(0)

# Major scale lines
axis_list = np.arange(start=0,stop=15,step=1)
plt.yticks(axis_list, color="grey", size=7)
# Range
plt.ylim(0,15)


# ------- PART 2: Add plots

# Plot each individual = each line of the data





# how many panels are in the same graph
lllist = rad_data.index
#print(lllist)
length_of_list=len(lllist)

#print(length_of_list)

for i in range(0,length_of_list):

    values = rad_data.iloc[i,:].values.flatten().tolist()
    #print(values)

    values += values[:1]
    values

    ax.plot(angles,values,linewidth=2,linestyle='solid',label='Panel '+str(i))

#ax.fill(angles, values, 'b', alpha=0.1)

#plt.interactive(False)

# Insert Legend
plt.legend(bbox_to_anchor=(0.1,0.1),loc='upper right',borderaxespad=0)

# Give a title
plt.title('Monthly Radiation Analysis by Hour (July) (kWh)')

# Show Graph
plt.show()
