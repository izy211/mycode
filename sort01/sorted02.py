#!/usr/bin/env python3

iplist = ['10.8.2.1', '1.1.1.1', '255.255.255.255', '10.1.2.1', '10.2.1.2', \
        '10.2.3.2', '10.7.2.1', '192.168.23.1', '192.168.66.1', '10.42.2.1', \
        '10.11.10.2', '10.25.32.2', '10.27.21.1', '192.168.55.1']

print('Currently iplist looks like this: ', iplist)
print('\nThe results of sorted(iplist): ', sorted(iplist))
print('\nBut the original hasn\'t changed: ', iplist)

iplistkeyed = sorted(iplist, key=len)
print('\nResult of key=len sort: ', str(iplistkeyed))

bakiplistkeyed = sorted(iplist, key=len, reverse=True)
print('\nResult of reverse key=len sort: ', str(bakiplistkeyed))

dnsrecord_types = ['a', 'MX', 'AAAA', 'CNAME', 'naptr', 'ns', 'svr', 'SOA']
print('\ndnsrecord_types looks like this: ', dnsrecord_types)
print('\ndnsrecord_types sorted looks like this: ', sorted(dnsrecord_types))
print('\ndnsrecord_types sorted by key=str.lower looks like this: ', sorted(dnsrecord_types, key=str.lower))

