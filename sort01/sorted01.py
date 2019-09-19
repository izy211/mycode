#!/usr/bin/env python3

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']
print("Currently the value of vendors is: ", vendors)
print("\nThe results of sorted() function on vendors: ", sorted(vendors))
print("But vendors still is: ", vendors)

sortedvendors = sorted(vendors)
print("\nThe sorted and saved vendors list is: ", str(sortedvendors))

baksortvendors = sorted(vendors, reverse=True)
print("\nThe reverse sorted and saved vendors list is: ", str(baksortvendors))

vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', 'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']
print('Our new vendorsdeux list looks like this: ', vendorsdeux)
print('Our new sorted vendorsdeux list looks like this: ', sorted(vendorsdeux))
