# station code for Seattle,WA: GHCND:US1WAKG0038
import csv
import json
import datetime

empty_list_months = [0] * 12
#assignment 1.1 and 1.2 (finally correct!)
with open('precipitation.json') as file: #open JSON file ('r' argument used by default)
    weather_dict = json.load(file) #stores contents in dictionary
    for entry in weather_dict: #looping over all singular entries
        if entry['station'] == "GHCND:US1WAKG0038": #checking if the station is equal to the station code for seattle
            date = entry['date'].split('-') #create a list of year, month, day
            month = int(date[1]) #only select the month
            empty_list_months[month-1] += entry['value'] 

print(empty_list_months)

#save seatlle precipitation as a new json file
with open('precipitation2.json','w') as file:
    json.dump(empty_list_months, file, indent=4)

total_sum = 0
relative_prec = [] #creates an empty list
with open('precipitation2.json') as file: #open JSON file ('r' argument used by default)
    values_seattle = json.load(file) #stores contents in dictionary
    for entry in values_seattle: #looping over all singular entries
        total_sum += entry
    for entry in values_seattle:
        relative_prec.append(entry/total_sum) #adds the relative values to the empty list

print('The total sum of precipitation in Seattle per month is ' + str(total_sum) + '.')
print('The relative precipitation in Seattle per month is ' + str(relative_prec) + '.')