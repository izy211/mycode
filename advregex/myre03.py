#!/usr/bin/env python3
import re

wood = "How much wood would an awoken woodchuck chuck if a woodchuck could chuck wood?"

hobbit = "In a hole in the ground there lived a hobbit. \
        Not a nasty, dirty, wet hole, filled with the ends of \
        worms and an oozy smell, nor yet a dry, bare, sandy \
        hole with nothing in it to sit down on or to eat: \
        it was a hobbit-hole, and that means comfort. It \
        had a perfectly round door like a porthole, \
        painted green, with a shiny yellow brass knob \
        in the exact middle. The door opened on to a \
        tube-shaped hall like a tunnel: a very comfortable tunnel \
        without smoke, with panelled walls, and floors tiled \
        and carpeted, provided with polished chairs..." 

search1 = re.findall(r"\swo\w+", wood)
print("Results of search 1: ", search1)

search2 = re.findall(r"o+", wood)
print("Results of search 2: ", search2)

search3 = re.findall(r"carrots", wood)
print("Results of search 3: ", search3)

search4 = re.findall(r"\sth\w+", hobbit)
print("Results of search 4: ", search4)

search5 = re.findall(r"\sth\w+", hobbit, re.IGNORECASE)
print("Results of search 5: ", search5)

