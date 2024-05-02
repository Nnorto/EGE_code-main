from ipaddress import *

c = -1
net = ip_network('10.18.134.220/255.255.255.192', 0)
for ad in net:
    c += 1
    if ad == ip_address('10.18.134.220'):
        print(c)
        break
