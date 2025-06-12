from ipaddress import *
net = ip_network('45.172.106.203/255.255.252.0', 0)
for ad in net:
    print(ad)

# 45172107254