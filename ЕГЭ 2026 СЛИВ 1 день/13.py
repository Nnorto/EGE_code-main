from ipaddress import *
net = ip_network('102.162.200.51/255.255.255.0', 0)
print(net[-2]) # наиб
print(net[1]) # наим
# 102+162+200+254 = 718 наиб
# 102+162+200+1 = 465 наим