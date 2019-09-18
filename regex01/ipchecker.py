#!/usr/bin/env python3
import urllib.request
import re
import os
import socket

REGEX  = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
BAD_REGEX  = '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'

def get_external_ip():
    url = 'http://checkip.dyndns.org'
    requesty = urllib.request.urlopen(url).read().decode('UTF-8')
    externalIP = re.findall(REGEX, requesty)
    return externalIP

def get_internal_ip():
    ip = socket.gethostbyname(socket.gethostname())
    internalIP = re.findall(REGEX, ip)
    return internalIP

print('Your public IP address is: ' + str(get_external_ip()))
print('Your internal IP address is: ' + str(get_internal_ip()))

testIP = '192.168.1.1'
brokeIP = '192f168g1h1'

print('Using bad regex:')
print(re.findall(BAD_REGEX, testIP))
print(re.findall(BAD_REGEX, brokeIP))

print('Using escaped regex:')
print(re.findall(REGEX, testIP))
print(re.findall(REGEX, brokeIP))
