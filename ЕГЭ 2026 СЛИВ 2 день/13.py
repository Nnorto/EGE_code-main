from ipaddress  import *
net = ip_network('102.162.200.51/255.255.255.0', 0)
print('адр сети', net[0])
print('шир сети', net[-1])