#!/usr/bin/env python3
import re

mytxt = open('grimm.txt')
allLines = mytxt.readlines()
mytxt.close()

#lookingfor = re.compile(r'wol[vf][es]*')
lookingfor = re.compile(r'wol(f|ves)')

for oneline in allLines:
    mymatchobj = lookingfor.search(oneline)
    if mymatchobj:
        print(mymatchobj.group(), '***', oneline, end='')
