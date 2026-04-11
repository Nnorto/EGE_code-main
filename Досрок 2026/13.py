from ipaddress import *
net = ip_network('146.180.173.153/255.192.0.0', 0)
print(net[-2])
# for ad in net:
#     print(ad)

# 146.191.255.254