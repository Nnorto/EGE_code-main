from ipaddress import *

# 3адание 1
net = ip_network('227.116.246.2/255.255.224.0', 0)
print(net)

# задание 2
net_2 = ip_network('126.200.20.55/255.255.128.0', 0)
print(net_2)
