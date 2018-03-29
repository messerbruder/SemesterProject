import pandas as pd
import matplotlib.pyplot as plt
#the library for treemap
import squarify
from numpy.random import rand
##################################################
# Information from The Python Graph Glddery #200 #
##################################################

def random_colors(n):
    return list(zip(rand(n), rand(n), rand(n)))

#Read data from the merge panel csv file, disable header and index
data = pd.read_csv('../Radiation_Record/merge_panel_radiation.csv',header=0,index_col=0)
#
Data = pd.DataFrame(data=data)

#Remove the unused columns
essentialData = Data.drop(['hour_index','hour','day','month'],axis=1)

# Plot labels
labels = essentialData.columns.values.tolist()

#print(labels)

#print(essentialData)
#Sum up the column
sum_radiation = essentialData.sum()
#transverse the dataset
Sum = sum_radiation.T
#print(Sum)

# Create plot data list
plotList = []
for i in range(0,len(labels)):
    plotList.append(Sum[i])
    #round up 4 decimal points
    labels[i] = 'panel ' + str(i) + '\n'+ str(round(Sum[i],4)) + 'kWh'
#print(plotList)

squarify.plot(sizes = plotList, label = labels, color = random_colors(len(labels)))
plt.axis('off')
plt.title('Total Radiation on Panels')
plt.show()