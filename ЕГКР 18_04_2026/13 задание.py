from ipaddress import *
net = ip_network('191.89.109.206/255.255.224.0', 0)
print(net[-2])
# 191.89.127.254