#!/usr/bin/env python

def main():
    iplist = ['10.0.0.1', '10.0.1.1', '10.3.2.1']
    iplist2 = ['5060', '80', '22']

    print(iplist)

    iplist.append(iplist2)

    print(iplist)

main()
