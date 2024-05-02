from ipaddress import *
net = ip_network('10.18.134.220/255.255.255.192', 0)
index = 0
for ad in net:  # бежим по адресам в сети
    index += 1
    if ad == ip_address('10.18.134.220'):  # если адрес = нашему, то заебись!
        print(index)
        break


