import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
k = 6

for i in range(0,k-1):
    path = 'D:/SemesterProject/Radiation_Record/panel'+str(i)+'Radiation_regression.csv'
    path_new = 'D:/SemesterProject/Radiation_Record/panel'+str(i+1)+'Radiation_regression.csv'
    column_name = ['Look up Group', 'Hour', 'MaxRadiation_panel '+str(i+1),'c1','c2','c3','c4','c5','c6','c7','c8','c9', 'Min Radiation']  # the column meaning of the files

    if i == 0:
        old = pd.read_csv(path, header=0,nrows=6206) #Only the first 6206 rows are read (to mitigate the bug of double recording in ladybug)
        old_data = pd.DataFrame(data=old) #create data frame
        column_name_old = ['Look up Group', 'Hour', 'MaxRadiation_panel '+str(i),'c1','c2','c3','c4','c5','c6','c7','c8','c9', 'Min Radiation']  # the column meaning of the files
        old_data.columns = column_name_old #assign column names
        merge = old_data.iloc[:,[0,1,2]] # 'merge' is the resultant dataFrame

    new = pd.read_csv(path_new, header=0,nrows=6206) #panel i+1
    new_data = pd.DataFrame(data=new)

    #print(old_data)
    #print(new_data)

    #assign column names to dataframes
    new_data.columns = column_name

    merge = pd.concat([merge,new_data.iloc[:,2]],axis=1)
print(merge)
merge.to_csv('../Radiation_Record/merge_panel_radiation_ClearSky.csv',index=False)

