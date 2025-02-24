from ipaddress import *
net = ip_network('157.180.63.114/255.255.255.248', 0)
k = 0
for ad in net:
    ad2 = f'{ad:b}'
    # add2 = bin(int(ad))[2:].zfill(32)
    if ad2.count('1') % 4 != 0:
        k += 1
print(k)

from ipaddress import *
net = ip_network('112.160.0.0/255.240.0.0', 0)
k = 0
for ad in net:
    ad2 = f'{ad:b}'
    # add2 = bin(int(ad))[2:].zfill(32)
    if ad2.count('1') % 5 == 0:
        k += 1
print(k)

from ipaddress import *
net = ip_network('187.27.234.0/255.255.248.0', 0)
k = 0
for ad in net:
    ad2 = f'{ad:b}'
    # add2 = bin(int(ad))[2:].zfill(32)
    if ad2.count('1') % 3 != 0:
        k += 1
print(k)