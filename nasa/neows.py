#!/usr/bin/env python3
import requests
import json
import webbrowser

neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=UcdF2KWKvjyZ7GAnrPfjDfxQQdV9PAyT5Y13oata'

closest = 999999999999999999999999999999
dangerous = 0

neourl = neourl + startdate + mykey
print(neourl)

neourlobj = requests.get(neourl)

decodeneo = neourlobj.json()

print("\n\nConverted Python Data")
print("Total number: {0}".format(decodeneo['element_count']))
dates =  decodeneo['near_earth_objects']

for day in dates:
    for i in dates[day]:
        miles_away = i['close_approach_data'][0]['miss_distance']['miles']
        if closest > float(miles_away):
            closest = float(miles_away)
        if i['is_potentially_hazardous_asteroid'] == True:
            dangerous+=1
            print("NEO with ID {0} is potentially hazardous!".format(i['id']))

print("NEO that will be the closest will be {0} miles away!".format(closest))
print("Total number of potentially hazardous NEOs is {0}!".format(dangerous))
