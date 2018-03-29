import pandas as pd
import os
import os.path
from pathlib import Path

pth = "status/status_"
small = "0"
end = ".csv"


for i in range(2,38): #the last number of status file
    number = i
    num = str(number)
    if i < 10:
        ipath = pth + small + num + end
    else:
        ipath = pth + num + end

    o = os.path.exists(ipath)

    if o == False:
        number += 1
        continue


    d = pd.read_csv(ipath, header=None)
    df = pd.DataFrame(data=d)
    columnNames=['Date-Time', 'path-point', 'like-dislike', 'familiar-unfailiar', 'ordered-chaotic', 'quiet-noisy', 'public-private','interesting-boring',
                 'empty-crowded', 'secure-insecure', 'beautiful-ugly', 'spacious-narrow', 'open-enclosed', 'light-dark']
    df.columns = columnNames

    #transpose = df.T[1:14] #打横

    q = df.iloc[:,13:] # ############ change here


    #print(transpose)

    #print(q2)
    #print(q3)
    #merge

    if i == 2:
        add = df.iloc[:,13:]
        continue

    mer = [add,q]
    merge = pd.concat(mer, axis=1)

    add = merge

print(merge)
merge.to_csv('light-dark') #change here


