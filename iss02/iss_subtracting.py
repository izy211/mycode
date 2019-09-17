#!/usr/bin/env python3
import urllib.request
import json
import turtle
import time

durhamlat = 35.994034
durhamlon = -78.898621
eoss = 'http://api.open-notify.org/iss-now.json'
passiss = 'http://api.open-notify.org/iss-pass.json'

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic('iss_map.gif')
screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(durhamlon, durhamlat)
mylocation.dot(5)
mylocation.hideturtle()

passiss = passiss + '?lat={0}&lon={1}'.format(str(durhamlat), str(durhamlon))
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode('utf-8'))
    
over = result['response'][1]['risetime']
style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)

while True:
    trackiss = urllib.request.urlopen(eoss)
    ztrack = trackiss.read()
    result = json.loads(ztrack.decode('utf-8'))
    
    
    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    
    
    lon = round(float(lon))
    lat = round(float(lat))
    iss.penup()
    iss.goto(lon, lat)
    time.sleep(1)
    print("Updating position...")
turtle.mainloop()
