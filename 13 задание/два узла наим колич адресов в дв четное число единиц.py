from ipaddress import *

for mask in reversed(range(0, 33)): # чем больше маска тем меньше компов в сети может быть
    net1 = ip_network('202.3.20.24/' + str(mask), 0)
    net2 = ip_network('202.3.27.11/' + str(mask), 0)
    if net1.network_address == net2.network_address:
        count = 0
        for ad in net2:
            ad2 = bin(int(ad))[2:].zfill(32)
            if ad2.count('1') % 2 == 0:
                count += 1
        print(count)
        break





