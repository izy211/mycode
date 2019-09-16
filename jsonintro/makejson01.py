#!/usr/bin/env python3

import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "specis": "Human"}]

    print(hitchhikers)

    zfile = open("galaxyguide.json", "w")
    json.dump(hitchhikers, zfile)

    zfile.close()
main()
