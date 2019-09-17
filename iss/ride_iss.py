#!/usr/bin/env python3
import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    helmet = groundctrl.read()
    
    helmetson = json.loads(helmet.decode('utf-8'))

    #print("\n\nConverted Python data: ")
    #print(helmetson)
    
    print("People in Space: {0}\n".format(helmetson['number']))
    people = helmetson['people']
    for i in range(helmetson['number']):
        print("{0} on the {1}".format(people[i]['name'], people[i]['craft']))
    for i in people:
        print("{0} on the {1}".format(i['name'], i['craft']))

main()
