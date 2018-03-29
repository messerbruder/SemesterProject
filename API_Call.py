import forecastio
from darksky import forecast
import datetime

zuri_location = 47.37,8.54 #west is negative
api_key = "a40f38a7e918fb1d240f8489558fc6cf" #API KEY (personal key only, from Darksky)

lat = 47.37 #latitude of Zurich
long = 8.54 #Longtitude of Zurich
Weather_Zurich = forecast(api_key,lat,long) #call Weather forecast in Zurich
Weather_Zurich.refresh(units='si') # change from F to C
cloud_cover = [] # This list store the cloud cover for the next  XXX hours
list_of_hour = [] # This list shows the time (date and hour) of the forecast
forecast_temperature = [] # This list shows the forecast temperature

#print(datetime.datetime.fromtimestamp(int("1519300800")).strftime('%Y,%m,%d,%H'))

for i in range(0,24): #for the next X hours
    cc = Weather_Zurich.hourly[i].cloudCover # Call hourly cloud cover data
    T = Weather_Zurich.hourly[i].temperature   # Call hourly temperature Data
    forecast_hour = Weather_Zurich.hourly[i].time        # Call hourly hour data (what time is the forecast)
    hour_display = datetime.datetime.fromtimestamp(forecast_hour).strftime('%Y,%m,%d,%H')  # Call hourly hour data (what time is the forecast)

    cloud_cover.append(round(cc*10,3)) # Creating a list of output data
    list_of_hour.append(hour_display)
    forecast_temperature.append(T)

print(list_of_hour)
print(forecast_temperature)
print(cloud_cover)

filepath ='D:/SemesterProject/API_Realtime/weather_data.csv'
file = open(filepath,'w')
file.close()

file = open(filepath,'a')
file.write('Year,Month,Day,Hour,Temperature,SkyCover' + '\n')
for i in range(0,24):
    file.write(str(list_of_hour[i])+','+str(forecast_temperature[i])+','+str(cloud_cover[i])+'\n')
file.close