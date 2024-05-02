from ipaddress import *

for mask in reversed(range(33)):
    net1 = ip_network('202.3.20.24/' + str(mask), 0)
    net2 = ip_network('202.3.27.11/' + str(mask), 0)
    if net1.network_address == net2.network_address:
        print(net1.netmask)
        c = 0
        for ad in net1:
            add = bin(int(ad))[2:].zfill(32)
            if add.count('1') % 2 == 0:
                c += 1
        print(c)
        break





