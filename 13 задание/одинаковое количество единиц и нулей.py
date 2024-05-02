from ipaddress import *

net = ip_network('90.65.32.0/255.255.224.0', 0)
k = 0
for ad in net:
    ad_bin = bin(int(ad))[2:].zfill(32)
    if ad_bin.count('1') == ad_bin.count('0'):
        k += 1
print(k)