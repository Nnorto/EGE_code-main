from ipaddress import *
net = ip_network('217.216.215.101/255.255.240.0', 0)
pn = 0
for ad in net:
    if str(ad) == '217.216.215.101':
        print(pn, ad)
    pn += 1
