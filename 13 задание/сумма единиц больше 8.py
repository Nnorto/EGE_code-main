from ipaddress import *

net = ip_network('192.128.32.160/255.255.255.240', 0)
k = 0
for ad in net:
    ad_bin = f'{ad:b}'
    if ad_bin.count('1') > 8:
        k += 1
print(k)