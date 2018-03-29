import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
k = 5

for i in range(0,k-1):
    path = 'D:/SemesterProject/Radiation_Record/panel'+str(i)+'Radiation.csv'
    path_new = 'D:/SemesterProject/Radiation_Record/panel'+str(i+1)+'Radiation.csv'
    column_name = ['look_up_Group', 'hour', 'radiation_panel' + str((i+1))]  # the column meaning of the files

    if i == 0:
        old = pd.read_csv(path, header=None)
        old_data = pd.DataFrame(data=old)
        column_name_old = ['look_up_Group', 'hour', 'radiation_panel' + str(i)]  # the column meaning of the files
        old_data.columns = column_name_old
        merge = old_data

    new = pd.read_csv(path_new, header=None) #panel i+1
    new_data = pd.DataFrame(data=new)

    print(old_data)
    #print(new_data)

    #assign column names to dataframes
    new_data.columns = column_name

    merge = pd.concat([merge,new_data.iloc[:,2]],axis=1)
print(merge)
merge.to_csv('../Radiation_Record/merge_panel_radiation.csv')
