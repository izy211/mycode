#!/usr/bin/env python3
import requests

MYTOKEN = '0a169eb052f4b19ca6c1c7850f00ecdb6cec771eba49026f'
MYAPI = 'https://fonoapi.freshpixl.com/v1/getlatest'

def main():
    print(MYTOKEN)
    mybuiltapi = MYAPI + "?token=" + MYTOKEN
    print(mybuiltapi)

    myjson = requests.get(mybuiltapi).json()

    for x in myjson:
        print(x)

if __name__ == '__main__':
    main()
