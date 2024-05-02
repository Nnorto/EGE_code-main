from ipaddress import *

k = 0
adr = ip_address('93.138.160.0')
for mask in range(33):
    net = ip_network('93.138.164.49/' + str(mask), 0)
    nnet = net.network_address
    if nnet == adr:
        k += 1

print(k)
print("  ")

k = 0
for mask in range(0, 33):
    net = ip_network(f'93.138.164.49/{mask}', 0)
    if net.network_address == ip_address('93.138.160.0'):
        k += 1

print(k)