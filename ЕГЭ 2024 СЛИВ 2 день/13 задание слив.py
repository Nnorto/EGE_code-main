from ipaddress import *
for mask in range(32 + 1): # максимум в маске 32 единиц
    net1 = ip_network(f"115.127.30.120/{mask}", 0)
    net2 = ip_network(f"115.127.151.120/{mask}", 0)
    if net1.network_address == net2.network_address:
        print(net1.netmask)