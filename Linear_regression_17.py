import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

panel_number = 4
pathpath = 'D:/SemesterProject/Radiation_Record/Panel'+str(panel_number)+'Radiation.csv'
panel = pd.read_csv(pathpath) #Read the radiation file
cloudiness = pd.read_csv('D:/SemesterProject/Cloudiness/cloudiness.csv') #Read cloudiness file

cloud_dataframe = pd.DataFrame(data=cloudiness) # Cloud dataframe
radiation_dataframe = pd.DataFrame(data=panel)  # Radiation dataframe
#print(cloud_dataframe)
#print(radiation_dataframe)

columnNames = ['hour_index','month', 'day', 'hour', 'radiation'] #Radiation file columns
radiation_dataframe.columns = columnNames # radiation dataFrame

cloud_column = ['hour_index','cloudiness']
cloud_dataframe.columns = cloud_column

cloud_only = cloud_dataframe.iloc[:,1]
cloud_only.columns = 'cloudiness'
#print(cloud_only)


merge_table = pd.merge(radiation_dataframe, cloud_dataframe,how = 'left',on='hour_index') #Merge 2 dataframe together
#print(merge_table)


horizon = 17 # data per regression

#radlut = {'hour_of_year': pd.Series([1,2,3], dtype = 'int32'),
          #'normalised_radiation': pd.Series([0,0,0], dtype= 'float32')}

#dfRad = pd.DataFrame(radlut)

lm = linear_model.LinearRegression()

filepath = 'D:/SemesterProject/Radiation_Record/'

file_name = 'Radiation_regression.csv'




LookupTable = open(filepath + 'panel'+ str(panel_number) + file_name, 'w') #reset or create file
LookupTable.write('Look up group, Hour, Max Radiation, c1, c2, c3, c4, c5, c6, c7, c8, c9, Min Radiation \n')
LookupTable.close()

index = 0 # hour of year
RUN = True

#counter = 1
# 8160


while index < 5780: #20groups*17days*17hours
    lrGroup = (index // 289) + 1 #look-up group 1-20


    pickList = np.arange(start=index, stop=(index)+17*17, step=17) # pick the hour of a day
    #print(pickList)

    trad = merge_table.iloc[pickList,4]  # pick radiation column
    tcod = merge_table.iloc[pickList,5]  # pick cloudiness column

    cloud_hourly = pd.DataFrame(tcod) # frame the cloudiness column
    radiation_hourly = pd.DataFrame(trad) # frame the radiation column

    X = cloud_hourly # assign it as X variable of linear regression
    y = radiation_hourly # assign it as y variable of linear regression model
    #print('counter = ' + str(counter)) # un comment it for checking only

    lm.fit(X,y)
    Max_radiation = lm.predict(0) # generate prediction when sky is clear (cloudiness = 0)
    c1 = lm.predict(1)
    c2 = lm.predict(2)
    c3 = lm.predict(3)
    c4 = lm.predict(4)
    c5 = lm.predict(5)
    c6 = lm.predict(6)
    c7 = lm.predict(7)
    c8 = lm.predict(8)
    c9 = lm.predict(9)
    Min_radiation = lm.predict(10)  # predict when cloudiness = 10
    display_hour = index%17+6
    #print('index = '+str(index))

    LookupTable = open(filepath + 'panel' + str(panel_number) + file_name, 'a')
    LookupTable.write(str(lrGroup) + ',' + str(display_hour) + ',' + str(Max_radiation[0][0]) + ',' +
                      str(c1[0][0]) + ',' + str(c2[0][0]) + ',' + str(c3[0][0]) + ',' + str(c4[0][0]) + ',' + str(c5[0][0]) + ',' +
                      str(c6[0][0]) + ',' + str(c7[0][0]) + ',' + str(c8[0][0]) + ',' + str(c9[0][0]) + ',' + str(Min_radiation[0][0]) +  '\n')
    if index % 17 + 6 == 22:
        index += 290 # 289 (17*17)+1 = 290
    else:
        index += 1



dolast = True
index = 5780 # (6204 - 25day*17hours +1) @ 6 o'clock final loop

while dolast == True:
    lrGroup = 21

    pickList = np.arange(start=index,stop=(index)+17*25, step=17)
    #print(pickList)
    trad = merge_table.iloc[pickList,4]
    tcod = merge_table.iloc[pickList,5]
    cloud_hourly = pd.DataFrame(tcod)
    radiation_hourly = pd.DataFrame(trad)
    X = cloud_hourly
    y = radiation_hourly
    #print('counter = ' + str(counter))


    lm.fit(X,y)
    Max_radiation = lm.predict(0) # predict when cloudiness = 0
    c1 = lm.predict(1)
    c2 = lm.predict(2)
    c3 = lm.predict(3)
    c4 = lm.predict(4)
    c5 = lm.predict(5)
    c6 = lm.predict(6)
    c7 = lm.predict(7)
    c8 = lm.predict(8)
    c9 = lm.predict(9)
    Min_radiation = lm.predict(10) #predict when cloudiness = 10
    print(Max_radiation)
    print('.....')
    print(Min_radiation)

    display_hour = index%17+6
    #print('index = '+str(index))

    LookupTable = open(filepath + 'panel' + str(panel_number) + file_name, 'a')
    LookupTable.write(str(lrGroup) + ',' + str(display_hour) + ',' + str(Max_radiation[0][0]) + ',' +
                      str(c1[0][0]) + ',' + str(c2[0][0]) + ',' + str(c3[0][0]) + ',' + str(c4[0][0]) + ',' + str(c5[0][0]) + ',' +
                      str(c6[0][0]) + ',' + str(c7[0][0]) + ',' + str(c8[0][0]) + ',' + str(c9[0][0]) + ',' + str(Min_radiation[0][0]) +  '\n')

    if index % 17+6 == 22:
        dolast = False
    else:
        index += 1

LookupTable.close()
