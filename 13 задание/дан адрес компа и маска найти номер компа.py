from ipaddress import *
net = ip_network('206.158.124.67/255.255.224.0', 0)
index = -1
for ad in net:  # бежим по адресам в сети
    index += 1
    if ad == ip_address('206.158.124.67'):  # если адрес = нашему, то заебись!
        print(index)

setb = int(net.network_address) # setb - сеть
komp = int(ip_address('206.158.124.67'))
print(komp - setb)