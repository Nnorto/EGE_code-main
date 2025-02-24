from ipaddress import *
net = ip_network('145.205.76.0/255.255.192.0', 0)
k = 0
for ad in net:
    ad2 = f'{ad:b}'
    # add2 = bin(int(ad))[2:].zfill(32)
    if ad2.count('1') % 2 != 0:
        k += 1
print(k)