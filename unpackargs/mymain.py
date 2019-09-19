#!/usr/bin/env python3
from jrpg import find

EXCLUDE = ["/usr", "/home", "/var"]

def getuserinput():
    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg)? ")
    lookwhere = input("What is the path in which I should search? ")
    return (lookfor, lookwhere)

def main():
    while(True):
        print(f"Results: {find(*getuserinput(), EXCLUDE)}")
        if (input("\nPress n to quit or other to search again.").lower() == "n"):
            break

main()
