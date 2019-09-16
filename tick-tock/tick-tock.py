#!/usr/bin/env python

import time

def main():
    ticks = time.time()
    print("Number of ticks in epoch time: ", ticks)

    myTime = time.localtime(ticks)
    print("The local time tuple is: ", myTime)
    print("The local time tuple year is: ", myTime[0])
    print("The local time tuple month is: ", myTime[1])
    print("The local time tuple day is: ", myTime[2])
    print("The local time tuple hour is: ", myTime[3])
    print("The local time tuple minute is: ", myTime[4])
    print("The local time tuple second is: ", myTime[5])
    print("The local time tuple week is: ", myTime[6])
    print("The local time tuple year is: ", myTime[7])
    print("The local time tuple daylight savings is: ", myTime[8])

    for x in range(10):
        print('This program will end in... ', 10-x)
        time.sleep(5)

main()
