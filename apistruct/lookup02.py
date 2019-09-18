#!/usr/bin/env python3
import requests

MYTOKEN = '0a169eb052f4b19ca6c1c7850f00ecdb6cec771eba49026f'
MYAPI = 'https://fonoapi.freshpixl.com/v1/getlatest'

def main():
    mybuiltapi = MYAPI + "?token=" + MYTOKEN

    brand = input("What brand of device are you searching for? ")
    brand = "&brand=" + brand

    myjson = requests.get(mybuiltapi + brand).json()

    for x in myjson:
        #print(x)
        print(x['DeviceName'])

if __name__ == '__main__':
    main()
