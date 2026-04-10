from ipaddress import *
for mask in range(33):
    net = ip_network(f'84.23.84.23/{mask}', 0)
    if '84.23.84.0' == str(net[0]):
        print(net.netmask)
print(255+224)




