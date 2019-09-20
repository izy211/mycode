#!/usr/bin/env python3
import json
import time
import sqlite3
import requests

def walmartlookup(walmarturl, mykey, upckey):
    try:
        walmarturlobj = requests.get(walmarturl + mykey + upckey)
        print(walmarturlobj)
        return walmarturlobj.json()
    except:
        return False

def trackmeplease(tracktime, trackprice):
    conn.execute("INSERT INTO PRICE (TIME,PRICE) VALUES (?,?)",(tracktime, trackprice))
    conn.commit()
    
    print("Entry added to database!")

def print_database(conn):
    cursor = conn.execute("SELECT time, price from PRICE")
    for row in cursor:
        print(f"TIME = {row[0]}")
        print(f"PRICE = {row[1]}")

def main():
    wurl = 'http://api.walmartlabs.com/v1/items?'
    wkey = 'apikey=d7hjdvye4sky5cdwmmmtf3bf'
    raw_upc = '190198511270'
    wupc = "&upc=" + raw_upc

    print(f"Walmart Query URL is: {wurl}{wkey}{wupc}")
    
    conn = sqlite3.connect('price.db')
    try:
        conn.execute('''CREATE TABLE PRICE
        (TIME   VARCHAR2 PRIMARY KEY    NOT NULL,
        PRICE   REAL    NOT NULL);''')
    except:
        pass


    decodewalmart = walmartlookup(wurl, wkey, wupc)

    if decodewalmart:
        print(f"\nWalmart Price on {time.ctime()}: ${str(decodewalmart['items'][0]['salePrice'])}")
        if input("Should we track this data within the database? y/n ").lower() == 'y':
            print(time.ctime())
            trackmeplease(time.ctime(), decodewalmart['items'][0]['salePrice'])
        else:
            print("Thanks for checking prices!")
    else:
        print("The UPC lookup failed.")

    if input("Should we output the database? y/n ").lower() == 'y':
        print_database(conn)

    conn.close()

if __name__ == "__main__":
    main()
