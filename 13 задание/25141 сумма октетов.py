from ipaddress import *
cnt = 0
net = ip_network('46.29.170.214/255.255.128.0', 0)
for ad in net:
    octet = [int(x) for x in str(ad).split('.')]
    for i in range(len(octet)):
        if octet[i] == sum(octet) - octet[i]:
            print(ad)





