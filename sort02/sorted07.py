#!/usr/bin/env python3

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp', 'dell']

print("Currently, the list is: ", vendors)
print('\nThe results of sorted are not permanent: ', sorted(vendors))
print('\nThe results of sorted are not permanent: ', vendors)

print('\nThe results of .sort are, and running it returns None: ', vendors.sort())
print('\nNow, the list is permanently: ', vendors)

