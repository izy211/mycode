#!/usr/bin/env python3

import requests

LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=27510&date=2019-09-17&distance=25&API_KEY=A5CAD82A-4904-4979-9500-936DAC376C92'

def main():
    r = requests.get(LOOKUPAPI)

    print("Weather Forecast")
    print("----------------")

#    print(r.json())

    for x in r.json():
        print(x.get("DateForecast"))
        print("----------")
        print(x.get("Discussion"))

main()
