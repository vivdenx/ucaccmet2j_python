import csv
import json
import datetime

#import the csv file first
with open('stations.csv') as file: #open CSV file
    loc_dict = {} #initialise dictionary
    headers = file.readline() #read first line and move pointer to second line
    for line in file: #from 2nd line onward
        (location, state, station) = line.strip().split(',') #remove whitespace and then split by comma
        loc_dict[location] = {
            'state' : state,
            'station' : station
        }

print(loc_dict)

#old code that worked
for city in loc_dict.values():
    print(city)
    list_months = [0] * 12
    with open('precipitation.json') as file: #open JSON file ('r' argument used by default)
        weather_dict = json.load(file) #stores contents in dictionary
        for entry in weather_dict:
            if entry['station'] == city['station']: 
                date = entry['date'].split('-') #create a list of year, month, day
                month = int(date[1]) #only select the month
                list_months[month-1] += entry['value'] 
    print(list_months)
    #save precipitation as a new json file
    with open('precipitation3.json','w') as file:
        json.dump(list_months, file, indent=4)
    total_sum = 0
    relative_prec = [] #creates an empty list
    with open('precipitation3.json') as file: #open JSON file ('r' argument used by default)
        values_seattle = json.load(file) #stores contents in dictionary
        for entry in values_seattle: #looping over all singular entries
            total_sum += entry
        for entry in values_seattle:
            relative_prec.append(entry/total_sum) #adds the relative values to the empty list
    print(total_sum)
    print(relative_prec) #relative precipation for all cities