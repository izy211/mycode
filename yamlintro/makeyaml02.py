#!/usr/bin/env python3

import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "specis": "Human"}]

    print(hitchhikers)

    yamlstring = yaml.dump(hitchhikers)

    print(yamlstring)
main()
