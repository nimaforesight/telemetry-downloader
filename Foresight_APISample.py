import requests
import csv
import json
import time

# This is where you set the start time and end time of the data you want 
year = '2024'
month ='06'
#dayStart is the day you would like data for
dayStart ='21'
#Time start is the time of day you would like to start retrieving data for. This uses 24h UTC clock so 2pm would be 14
timeStart = 9
#hours is how many hours you would like the data for. If you set start time for 9am and hours is set to 5 you will get the data from 9am-2pm 
hours = 12
#do not change anything below 
timeCount = 0
timeEnd = timeStart+1
data  = []
# this is the loop that automatically recives the data for every 1 hour period 
while timeCount != hours :

    #Prints the start time, and end time you are about to get data for 
    print (timeCount,timeStart,timeEnd)
    
    #This is a pause to give you time to see if the numbers are correct 
    time.sleep(1)


    #Below is what sets the actual start and end time that the API sees. When combined the start and end time will look like this : 2024-06-21T18:00:12.199Z
    startTime = year+'-'+month+'-'+dayStart+'T'+str(timeStart).zfill(2)+'%3A00%3A00.000Z'
    endTime = year+'-'+month+'-'+dayStart+'T'+str(timeEnd).zfill(2)+'%3A00%3A00.000Z'

    #This sets the API key for your user. Make sure to set the correct API token or you will not be able to access the data. You can generate a new token through the portal
    head = {'X-API-KEY':'ENTER YOUR TOKEN HERE', }

    #Below is where you will set the device ID and the data you want to recive such as CAN or GPS. Refer to the API documentation to see what url is needed for each set of data
    myURL = 'https://foresightdata.ca/device/nf-1248/can?startTime='+startTime+'&endTime='+endTime
    response = requests.get(myURL,headers=head)

    if (len(response.json()) == 0):
        timeStart = timeStart+1
        timeEnd = timeEnd+1
        timeCount = timeCount+1
        continue
    #This prints the data into the terminal
    data.append(response.json())


    timeStart = timeStart+1
    timeEnd = timeEnd+1
    timeCount = timeCount+1
    print(myURL)
    #This opens or creates a new CSV files for the data, each block of data will be added to the bottom of the previous set. You can also change the file type if you don't want CSV
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)   