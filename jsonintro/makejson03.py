#!/usr/bin/env python3

import json

def main():

    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    print(datacenterstring)
    print(type(datacenterstring))

    datacenterdecoded = json.loads(datacenterstring)

    print("\nAfter converting to a dictionary:")

    print(type(datacenterdecoded))
    print(datacenterdecoded)

    print("\nRow 3 data: ", datacenterdecoded["row3"])

    print("Row 2 index 1: ", datacenterdecoded["row2"][1])

    with open("datacenter.json", "r") as datacenterjsonopen:
        datacenterjson = json.loads(datacenterjsonopen.read())

    print(type(datacenterjson))
    print(datacenterjson)

main()
