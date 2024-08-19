from ipaddress import *

net = ip_network('242.67.112.134/255.255.255.192', 0)
count = 0
for ad in net:
    ad2 = bin(int(ad))[2:].zfill(32)
    lev = ad2[:len(ad2)//2]
    prav = ad2[len(ad2)//2:]
    if lev.count('1') >= prav.count('1'):
        count += 1
print(count)