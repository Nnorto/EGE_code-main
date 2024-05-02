from ipaddress import *
# создание ip-адреса
ad = ip_address('адрес узла')

# создание сети
net = ip_network("адрес сети/маска")
net1 = ip_network("адрес узла/маска", 0)

# получение адреса сети
s = net.network_address

# получение количества адресов
count = net.num_addresses

# получить маску
mask = net.netmask

# перебор ip-адресов сети
for ad in net:
    "и т.д"
# перебор масок
for mask in range(33):
    net = ip_network('адрес узла/' + str(mask), 0)

# переобразование ip-адреса в двоичное представление
ad = ip_address('адрес узла')
ad_2 = bin(int(ad))[2:].zfill(32)