from ipaddress import *
net = ip_network('234.185.92.147/255.255.255.192', 0)
for ad in net.hosts():
    print(ad)