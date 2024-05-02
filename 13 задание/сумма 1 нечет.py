from ipaddress import *

net = ip_network('192.168.32.0/255.255.254.0', 0)
k = 0
for ad in net:
    ad_bin = bin(int(ad))[2:].zfill(32)
    if ad_bin.count('1') % 2 == 1:
        k += 1
print(k)